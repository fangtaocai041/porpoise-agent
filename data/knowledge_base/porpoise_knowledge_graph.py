"""
江豚研究动态知识图谱 (Porpoise Knowledge Graph)
────────────────────────────────────────────────
基于图论的动态知识图谱，管理研究者/机构/论文/物种/方向间的多跳关系。

实体类型:
  - Researcher:   研究者 (姓名, 英文名, 单位, h_index, 方向)
  - Institution:  研究机构 (名称, 英文名, 类型, 国家)
  - Paper:        论文 (标题, DOI, 年份, 期刊)
  - Species:      物种 (学名, 中文名, IUCN, 分布)
  - Direction:    学科方向 (标签, 描述)

边类型:
  - WORKS_AT:      研究者 → 机构
  - AUTHORED:      研究者 → 论文
  - ABOUT:         论文 → 物种
  - CITES:         论文 → 论文
  - COLLABORATES:  机构 → 机构 (合作)
  - SPECIALIZES:   研究者 → 方向
  - BELONGS_TO:    物种 → 方向

用法:
    from data.knowledge_base.porpoise_knowledge_graph import get_graph

    g = get_graph()
    # 查询某单位的所有江豚研究者
    researchers = g.query(node_type="Researcher", property="institution", value="水生所")
    # 查找某人的合作者 (两跳邻居)
    collaborators = g.neighbors("researcher:王丁", max_depth=2, edge_type="AUTHORED")
    # 新论文入库
    g.add_paper(title="...", doi="10.xxx", year=2025, authors=["王丁", "梅志刚"], species="江豚")
"""

import json
import logging
import os
from collections import defaultdict, deque
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

logger = logging.getLogger(__name__)

# ── 实体类型 ────────────────────────────────────────────────

ENTITY_TYPES = {"Researcher", "Institution", "Paper", "Species", "Direction"}
EDGE_TYPES = {"WORKS_AT", "AUTHORED", "ABOUT", "CITES", "COLLABORATES", "SPECIALIZES", "BELONGS_TO"}


@dataclass
class Node:
    """图谱节点"""
    id: str                          # e.g. "researcher:王丁", "institution:水生所"
    type: str                        # ENTITY_TYPES 之一
    label: str                       # 显示名称
    properties: dict = field(default_factory=dict)


@dataclass
class Edge:
    """图谱边 (有向)"""
    source: str                      # 源节点 id
    target: str                      # 目标节点 id
    type: str                        # EDGE_TYPES 之一
    weight: float = 1.0
    properties: dict = field(default_factory=dict)


@dataclass
class GraphQuery:
    """查询结果"""
    nodes: list[Node]
    edges: list[Edge]
    paths: list[list[str]] = field(default_factory=list)


# ══════════════════════════════════════════════════════════════
# 图引擎
# ══════════════════════════════════════════════════════════════

class KnowledgeGraph:
    """
    动态知识图谱引擎。

    内部用邻接表存储: adjacency[node_id] = {edge_type: [target_ids]}
    支持按节点类型/属性查询、BFS 邻居、最短路径、增量更新。
    """

    def __init__(self):
        self._nodes: dict[str, Node] = {}          # node_id → Node
        self._edges: dict[str, list[Edge]] = {}    # source_id → [Edge]
        self._reverse_edges: dict[str, list[Edge]] = {}  # target_id → [Edge]
        # 索引: type → {property_name → {value → [node_id]}}
        self._index: dict[str, dict[str, dict[str, list[str]]]] = {
            et: {} for et in ENTITY_TYPES
        }
        self._version: int = 1
        self._updated_at: str = datetime.now().isoformat()
        # 自动播种初始数据 (来自知识库)
        _seed_from_knowledge_base(self)

    # ── 节点操作 ─────────────────────────────────────

    def add_node(self, id: str, type: str, label: str,
                 properties: Optional[dict] = None) -> Node:
        """添加或更新节点"""
        node = Node(id=id, type=type, label=label,
                    properties=properties or {})
        self._nodes[id] = node
        self._index_node(node)
        self._version += 1
        return node

    def get_node(self, id: str) -> Optional[Node]:
        return self._nodes.get(id)

    def remove_node(self, id: str):
        """删除节点及关联的所有边"""
        self._nodes.pop(id, None)
        self._unindex_node(self._nodes.get(id))
        self._edges.pop(id, None)
        self._reverse_edges.pop(id, None)
        # 清理其他节点指向本节点的边
        for src in list(self._edges.keys()):
            self._edges[src] = [e for e in self._edges[src] if e.target != id]
        for tgt in list(self._reverse_edges.keys()):
            self._reverse_edges[tgt] = [e for e in self._reverse_edges[tgt] if e.source != id]
        self._version += 1

    # ── 边操作 ───────────────────────────────────────

    def add_edge(self, source: str, target: str, type: str,
                 weight: float = 1.0, properties: Optional[dict] = None) -> Optional[Edge]:
        """添加边（两端节点必须已存在）"""
        if source not in self._nodes or target not in self._nodes:
            logger.warning(f"Cannot add edge {source} → {target}: node missing")
            return None
        if type not in EDGE_TYPES:
            logger.warning(f"Unknown edge type: {type}")
            return None

        edge = Edge(source=source, target=target, type=type,
                    weight=weight, properties=properties or {})
        self._edges.setdefault(source, []).append(edge)
        self._reverse_edges.setdefault(target, []).append(edge)
        self._version += 1
        return edge

    def get_edges(self, source: Optional[str] = None,
                  type: Optional[str] = None) -> list[Edge]:
        """查询边"""
        edges = []
        for src_edges in self._edges.values():
            for e in src_edges:
                if source and e.source != source:
                    continue
                if type and e.type != type:
                    continue
                edges.append(e)
        return edges

    def remove_edge(self, source: str, target: str, type: str):
        """删除指定边"""
        self._edges[source] = [e for e in self._edges.get(source, [])
                               if not (e.target == target and e.type == type)]
        self._reverse_edges[target] = [e for e in self._reverse_edges.get(target, [])
                                        if not (e.source == source and e.type == type)]
        self._version += 1

    # ── 查询 ─────────────────────────────────────────

    def query(self, node_type: str, property: str = "",
              value: Any = None) -> list[Node]:
        """
        按类型和属性查询节点。

        Args:
            node_type: ENTITY_TYPES 之一, 或 "ALL" 表示全部
            property: 属性名 (为空时返回该类型全部节点)
            value: 属性值

        Returns:
            list[Node]: 匹配的节点列表
        """
        if node_type == "ALL":
            nodes = list(self._nodes.values())
            if property and value is not None:
                return [n for n in nodes if n.properties.get(property) == value]
            return nodes

        if node_type not in ENTITY_TYPES:
            return []

        if not property:
            return [n for n in self._nodes.values() if n.type == node_type]

        idx = self._index.get(node_type, {}).get(property, {}).get(str(value), [])
        return [self._nodes[nid] for nid in idx if nid in self._nodes]

    def neighbors(self, node_id: str, max_depth: int = 2,
                  edge_type: Optional[str] = None) -> GraphQuery:
        """
        BFS 邻居查询。

        Args:
            node_id: 起始节点
            max_depth: 最大跳数
            edge_type: 边类型过滤

        Returns:
            GraphQuery: 邻居节点 + 经过的边 + 路径
        """
        visited_nodes: set[str] = set()
        visited_edges: list[Edge] = []
        paths: dict[str, list[str]] = {node_id: [node_id]}

        queue = deque([(node_id, 0)])
        visited_nodes.add(node_id)

        while queue:
            current, depth = queue.popleft()
            if depth >= max_depth:
                continue

            for edge in self._edges.get(current, []):
                if edge_type and edge.type != edge_type:
                    continue
                if edge.target not in visited_nodes:
                    visited_nodes.add(edge.target)
                    visited_edges.append(edge)
                    paths[edge.target] = paths[current] + [edge.target]
                    queue.append((edge.target, depth + 1))

            # 反向边（被引用也算邻居）
            for edge in self._reverse_edges.get(current, []):
                if edge_type and edge.type != edge_type:
                    continue
                if edge.source not in visited_nodes:
                    visited_nodes.add(edge.source)
                    visited_edges.append(edge)
                    paths[edge.source] = paths[current] + [edge.source]
                    queue.append((edge.source, depth + 1))

        return GraphQuery(
            nodes=[self._nodes[nid] for nid in visited_nodes if nid in self._nodes],
            edges=visited_edges,
            paths=list(paths.values()),
        )

    def shortest_path(self, source: str, target: str) -> list[str]:
        """BFS 最短路径"""
        if source not in self._nodes or target not in self._nodes:
            return []
        visited = {source}
        queue = deque([(source, [source])])
        while queue:
            current, path = queue.popleft()
            for edge in self._edges.get(current, []):
                if edge.target == target:
                    return path + [target]
                if edge.target not in visited:
                    visited.add(edge.target)
                    queue.append((edge.target, path + [edge.target]))
            for edge in self._reverse_edges.get(current, []):
                if edge.source == target:
                    return path + [target]
                if edge.source not in visited:
                    visited.add(edge.source)
                    queue.append((edge.source, path + [edge.source]))
        return []

    # ── 便捷方法 ─────────────────────────────────────

    def add_researcher(self, name: str, english_name: str = "",
                       institution: str = "", h_index: int = 0,
                       directions: Optional[list[str]] = None) -> Node:
        """注册研究者 + 自动关联机构和方向"""
        rid = f"researcher:{name}"
        node = self.add_node(
            id=rid, type="Researcher", label=name,
            properties={
                "name_zh": name,
                "name_en": english_name,
                "institution": institution,
                "h_index": h_index,
                "directions": directions or [],
            }
        )
        if institution:
            iid = f"institution:{institution}"
            if iid not in self._nodes:
                self.add_institution(institution)
            self.add_edge(rid, iid, "WORKS_AT")
        for d in (directions or []):
            did = f"direction:{d}"
            if did not in self._nodes:
                self.add_direction(d)
            self.add_edge(rid, did, "SPECIALIZES")
        return node

    def add_institution(self, name: str, english_name: str = "",
                        country: str = "中国") -> Node:
        return self.add_node(
            id=f"institution:{name}", type="Institution", label=name,
            properties={"name_zh": name, "name_en": english_name, "country": country},
        )

    def add_paper(self, title: str, doi: str = "", year: int = 0,
                  journal: str = "", authors: Optional[list[str]] = None,
                  species: Optional[list[str]] = None) -> Node:
        """添加论文 + 自动关联作者和物种"""
        pid = f"paper:{doi or title[:40]}"
        node = self.add_node(
            id=pid, type="Paper", label=title[:80],
            properties={"title": title, "doi": doi, "year": year, "journal": journal},
        )
        for author in (authors or []):
            aid = f"researcher:{author}"
            if aid not in self._nodes:
                self.add_researcher(author, institution="未知")
            self.add_edge(aid, pid, "AUTHORED")
        for sp in (species or []):
            sid = f"species:{sp}"
            if sid not in self._nodes:
                self.add_species(sp)
            self.add_edge(pid, sid, "ABOUT")
        return node

    def add_species(self, name: str, scientific_name: str = "",
                    iucn: str = "", distribution: str = "",
                    directions: Optional[list[str]] = None) -> Node:
        sid = f"species:{name}"
        node = self.add_node(
            id=sid, type="Species", label=name,
            properties={
                "name_zh": name, "scientific_name": scientific_name,
                "iucn": iucn, "distribution": distribution,
            },
        )
        for d in (directions or []):
            did = f"direction:{d}"
            if did not in self._nodes:
                self.add_direction(d)
            self.add_edge(sid, did, "BELONGS_TO")
        return node

    def add_direction(self, name: str, description: str = "") -> Node:
        return self.add_node(
            id=f"direction:{name}", type="Direction", label=name,
            properties={"name": name, "description": description},
        )

    # ── 索引 ─────────────────────────────────────────

    def _index_node(self, node: Node):
        """建立属性索引"""
        type_idx = self._index.setdefault(node.type, {})
        for key, value in node.properties.items():
            val_str = str(value)
            type_idx.setdefault(key, {}).setdefault(val_str, []).append(node.id)

    def _unindex_node(self, node: Optional[Node]):
        if not node:
            return
        type_idx = self._index.get(node.type, {})
        for key, value in node.properties.items():
            val_str = str(value)
            if key in type_idx and val_str in type_idx[key]:
                if node.id in type_idx[key][val_str]:
                    type_idx[key][val_str].remove(node.id)

    # ── 序列化 ─────────────────────────────────────────

    def to_dict(self) -> dict:
        """导出为可序列化字典"""
        return {
            "version": self._version,
            "updated_at": self._updated_at,
            "nodes": [(n.id, n.type, n.label, n.properties) for n in self._nodes.values()],
            "edges": [(e.source, e.target, e.type, e.weight) for es in self._edges.values() for e in es],
        }

    def save(self, path: str = ""):
        """持久化到 JSON"""
        path = path or "data/knowledge_base/graph_export.json"
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)
        logger.info(f"Knowledge graph saved: {path} ({len(self._nodes)} nodes, {sum(len(v) for v in self._edges.values())} edges)")

    def load(self, path: str = ""):
        """从 JSON 恢复"""
        path = path or "data/knowledge_base/graph_export.json"
        if not Path(path).exists():
            return
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        self._nodes.clear()
        self._edges.clear()
        self._reverse_edges.clear()
        self._index = {et: {} for et in ENTITY_TYPES}
        for nid, ntype, label, props in data["nodes"]:
            self.add_node(nid, ntype, label, props)
        for src, tgt, etype, weight in data["edges"]:
            # 重建边需要引用已有节点
            if src in self._nodes and tgt in self._nodes:
                edge = Edge(source=src, target=tgt, type=etype, weight=weight)
                self._edges.setdefault(src, []).append(edge)
                self._reverse_edges.setdefault(tgt, []).append(edge)
        self._version = data.get("version", 1)
        self._updated_at = data.get("updated_at", "")
        logger.info(f"Knowledge graph loaded: {len(self._nodes)} nodes, {sum(len(v) for v in self._edges.values())} edges")

    @property
    def stats(self) -> dict:
        """统计"""
        type_count = defaultdict(int)
        for n in self._nodes.values():
            type_count[n.type] += 1
        edge_count = defaultdict(int)
        for es in self._edges.values():
            for e in es:
                edge_count[e.type] += 1
        return {
            "total_nodes": len(self._nodes),
            "total_edges": sum(len(v) for v in self._edges.values()),
            "by_type": dict(type_count),
            "by_edge": dict(edge_count),
            "version": self._version,
            "updated_at": self._updated_at,
        }


# ── 全局实例 ────────────────────────────────────────────────

_graph: Optional[KnowledgeGraph] = None


def get_graph() -> KnowledgeGraph:
    """获取全局图谱实例 (懒加载 + 自动导入初始数据)"""
    global _graph
    if _graph is None:
        _graph = KnowledgeGraph()

        # 尝试从持久化文件恢复
        persist_path = "data/knowledge_base/graph_export.json"
        if Path(persist_path).exists():
            try:
                _graph.load(persist_path)
                return _graph
            except Exception as e:
                logger.debug(f"Graph load failed ({e}), will seed from scratch")

        # 首次运行: 从知识库导入初始数据
        _seed_from_knowledge_base(_graph)
        try:
            _graph.save(persist_path)
        except Exception:
            pass
    return _graph


def _seed_from_knowledge_base(g: KnowledgeGraph):
    """从知识库文档导入初始数据"""
    # ── 方向 ──
    directions = {
        "遗传与分子": "种群遗传学、分子标记、系统发育",
        "基因组学": "全基因组组装、比较基因组、MHC",
        "生物声学": "NBHF click、PAM、回声定位",
        "生态与种群": "分布、种群动态、栖息地利用",
        "污染物与健康": "POPs、重金属、微塑料、微生物",
        "保护管理": "IUCN评估、迁地保护、自然保护区",
        "解剖与生理": "系统解剖、听力生理、潜水生理",
        "行为与认知": "母子行为、社群结构、捕食策略",
    }
    for d, desc in directions.items():
        g.add_direction(d, desc)

    # ── 物种 ──
    species = [
        ("长江江豚", "Neophocaena asiaeorientalis asiaeorientalis", "CR", "长江中下游"),
        ("东溟江豚", "Neophocaena sunameri", "NT", "中国沿海、日本、韩国"),
        ("印太江豚", "Neophocaena phocaenoides", "VU", "印度-太平洋"),
        ("港湾鼠海豚", "Phocoena phocoena", "LC", "北大西洋/北太平洋"),
        ("加湾鼠海豚", "Phocoena sinus", "CR", "加利福尼亚湾"),
        ("白鱀豚", "Lipotes vexillifer", "CR(PE)", "长江 (原)"),
        ("中华白海豚", "Sousa chinensis", "VU", "中国东南沿海"),
    ]
    for sp, sciname, iucn, dist in species:
        g.add_species(sp, sciname, iucn, dist)

    # ── 机构 ──
    institutions = [
        ("中国科学院水生生物研究所", "IHB-CAS", "中国"),
        ("淡水渔业研究中心", "FFRC-CAFS", "中国"),
        ("南京师范大学", "NNU", "中国"),
        ("复旦大学", "Fudan", "中国"),
        ("中山大学", "SYSU", "中国"),
        ("中科院深海所", "IDSSE", "中国"),
        ("自然资源部第三海洋研究所", "TIO-MNR", "中国"),
        ("日本渔业研究教育机构", "FRA-Japan", "日本"),
        ("韩国海洋研究所", "KIOST", "韩国"),
        ("香港大学", "HKU", "中国香港"),
        ("伦敦动物学会", "ZSL", "英国"),
        ("俄罗斯科学院", "RAS", "俄罗斯"),
    ]
    for name, en, country in institutions:
        g.add_institution(name, en, country)

    # ── 研究者（按机构分组，每组内按角色优先级排序）──

    # 1. 中国科学院水生生物研究所（IHB-CAS）— PI/总负责人→研究员→副研究员→其他
    # 王丁: 总PI，40+年江豚研究，全球最高引
    # 王克雄: 研究员，生物声学组负责人
    # 郑劲松: 研究员，遗传学组负责人
    # 梅志刚: 副研究员，种群动态组负责人
    # 郝玉江: 副研究员，保护管理组负责人/白鱀豚馆负责人
    # 王智伟: 副研究员，PAM方向
    # 陈敏敏: 副研究员，遗传学方向
    # 方亮: 助理研究员，声学参数方向
    researchers = [
        # ── IHB-CAS：按关键程度排序 ──
        ("王丁", "Wang Ding", "中国科学院水生生物研究所", 38, ["保护管理", "生态与种群"]),
        ("王克雄", "Wang Kexiong", "中国科学院水生生物研究所", 24, ["生物声学"]),
        ("郑劲松", "Zheng Jinsong", "中国科学院水生生物研究所", 18, ["遗传与分子"]),
        ("梅志刚", "Mei Zhigang", "中国科学院水生生物研究所", 22, ["生态与种群", "保护管理"]),
        ("郝玉江", "Hao Yujiang", "中国科学院水生生物研究所", 18, ["保护管理"]),
        ("王智伟", "Wang Zhiwei", "中国科学院水生生物研究所", 17, ["生物声学"]),
        ("陈敏敏", "Chen Minmin", "中国科学院水生生物研究所", 12, ["遗传与分子"]),
        ("方亮", "Fang Liang", "中国科学院水生生物研究所", 10, ["生物声学"]),

        # ── FFRC-CAFS（你的课题组）：按职级排序 ──
        # 徐跑: FFRC 所长/研究员
        # 刘凯: 研究员/博导，你的导师
        # 杨彦平: 博士/助理研究员
        # 蔺丹清、张家路、应聪萍、尹登花、王银平、轩中亚、方弟安、段金荣、徐东坡、张敏莹: 成员
        ("徐跑", "Xu Pao", "淡水渔业研究中心", 16, ["保护管理"]),
        ("刘凯", "Liu Kai", "淡水渔业研究中心", 12, ["生态与种群", "保护管理"]),
        ("杨彦平", "Yang Yanping", "淡水渔业研究中心", 8, ["生态与种群"]),
        ("蔺丹清", "Lin Danqing", "淡水渔业研究中心", 5, ["生态与种群"]),
        ("张家路", "Zhang Jialu", "淡水渔业研究中心", 5, ["生态与种群"]),
        ("应聪萍", "Ying Congping", "淡水渔业研究中心", 5, ["保护管理"]),
        ("尹登花", "Yin Denghua", "淡水渔业研究中心", 5, ["保护管理"]),
        ("王银平", "Wang Yinping", "淡水渔业研究中心", 8, ["生态与种群"]),
        ("轩中亚", "Xuan Zhongya", "淡水渔业研究中心", 5, ["生态与种群"]),
        ("方弟安", "Fang Di'an", "淡水渔业研究中心", 10, ["生态与种群"]),
        ("段金荣", "Duan Jinrong", "淡水渔业研究中心", 8, ["生态与种群"]),
        ("徐东坡", "Xu Dongpo", "淡水渔业研究中心", 10, ["生态与种群"]),
        ("张敏莹", "Zhang Minying", "淡水渔业研究中心", 8, ["生态与种群"]),

        # ── 国内其他单位 ──
        ("杨光", "Yang Guang", "南京师范大学", 28, ["遗传与分子", "基因组学"]),
        ("李松海", "Li Songhai", "中科院深海所", 22, ["生物声学"]),
        ("王先艳", "Wang Xianyan", "自然资源部第三海洋研究所", 10, ["生态与种群"]),
        ("刘佳佳", "Liu Jiajia", "复旦大学", 12, ["保护管理"]),

        # ── 国际合作伙伴 ──
        ("Tomonari Akamatsu", "Akamatsu T", "日本渔业研究教育机构", 38, ["生物声学"]),
        ("Leszek Karczmarski", "Karczmarski L", "香港大学", 32, ["生态与种群"]),
        ("Samuel Turvey", "Turvey ST", "伦敦动物学会", 28, ["保护管理"]),
        ("Popov VV", "Popov VV", "俄罗斯科学院", 22, ["生物声学"]),
    ]
    for name, en, inst, h, dirs in researchers:
        g.add_researcher(name, en, inst, h, dirs)

    # ── 论文 ──
    papers = [
        ("The Yangtze finless porpoise: on an accelerating path to extinction?",
         "10.1016/j.biocon.2012.03.005", 2012, "Biological Conservation",
         ["梅志刚", "王丁"], ["长江江豚"]),
        ("Range contraction of the Yangtze finless porpoise inferred from classic Chinese poems",
         "10.1016/j.cub.2025.02.052", 2025, "Current Biology",
         ["梅志刚", "王克雄", "王丁", "刘佳佳"], ["长江江豚"]),
        ("Population genomics of finless porpoises reveal an incipient cetacean species adapted to freshwater",
         "10.1038/s41467-018-03722-x", 2018, "Nature Communications",
         ["杨光"], ["长江江豚", "东溟江豚"]),
        ("长江江豚保护进展与工作展望",
         "10.7541/2024.2024.0027", 2024, "水生生物学报",
         ["徐跑", "刘凯"], ["长江江豚"]),
        ("Diel echolocation activity of Yangtze finless porpoise",
         "10.1371/journal.pone.0104038", 2014, "PLoS ONE",
         ["王智伟"], ["长江江豚"]),
        ("长江安庆段长江江豚分布特征及其影响因子探究",
         "", 2024, "水生生物学报",
         ["刘凯", "蔺丹清"], ["长江江豚"]),
        ("Noise exposure and its effect on Yangtze finless porpoise",
         "10.1016/j.envpol.2020.114679", 2020, "Environmental Pollution",
         ["王智伟"], ["长江江豚"]),
        ("Evoked-potential audiogram of the Yangtze finless porpoise",
         "10.1121/1.3655295", 2011, "Journal of the Acoustical Society of America",
         ["Popov VV"], ["长江江豚"]),
        ("A-tag density estimation method for finless porpoise",
         "10.1121/1.3492859", 2010, "Journal of the Acoustical Society of America",
         ["Tomonari Akamatsu"], ["长江江豚", "东溟江豚"]),
    ]
    for title, doi, year, journal, authors, species in papers:
        g.add_paper(title, doi, year, journal, authors, species)

    logger.info(f"Graph seeded: {len(g._nodes)} nodes, {sum(len(v) for v in g._edges.values())} edges")

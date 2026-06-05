# Skill: search-literature

## Description
Multi-source scientific literature search specialized for cetacean/porpoise research.

## Trigger
- User mentions: search, literature, papers, review, find papers, 文献, 综述
- Research phase: Phase 1 (Literature Review)

## Input
- Required: query (str) - research question or keywords
- Optional:
  - sources (list[str]) - data sources: arxiv, pubmed, semantic_scholar, google_scholar
  - max_results (int, default 20)
  - year_from (int) - start year filter
  - year_to (int) - end year filter

## Steps
1. Decompose question into 3-5 searchable sub-questions
2. Generate Chinese + English keyword combinations
3. Search across multiple sources in parallel
4. Filter by relevance (high/medium/low) based on title+abstract
5. For high-relevance papers: extract methods, data, key findings
6. Track citation chains (references + cited by)
7. Synthesize findings and identify research gaps

## Keywords Mapping
- Jiangtun/finless porpoise/Neophocaena
- NBHF/narrow-band high-frequency/click/echolocation
- PAM/passive acoustic monitoring
- abundance/density/distribution/habitat
- conservation/threat/status/IUCN

## Decision Points
- If < 5 high-relevance papers: broaden search terms
- If > 50 results: narrow by year or add specific filters
- If conflicting findings: flag for manual review

## Output Format
```json
{
  "research_question": "...",
  "sub_questions": ["..."],
  "papers": [{
    "title": "...",
    "authors": ["..."],
    "year": 2024,
    "journal": "...",
    "doi": "...",
    "relevance": "high",
    "key_findings": ["..."],
    "methods": ["..."],
    "limitations": ["..."]
  }],
  "synthesis": "...",
  "research_gaps": ["..."]
}
```

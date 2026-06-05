"""
Porpoise Agent CLI - Command-line interface

Usage:
    porpoise chat       Interactive chat mode
    porpoise run TASK   Run a single research task
    porpoise code DIR   Code analysis mode
    porpoise doctor     Health check
"""

import argparse
import asyncio
import logging
import sys


def setup_parser() -> argparse.ArgumentParser:
    """Setup CLI argument parser"""
    parser = argparse.ArgumentParser(
        prog="porpoise",
        description="Porpoise Agent - 江豚研究智能体",
        epilog="服务于无锡渔业学院/淡水渔业研究中心 刘凯研究员课题组",
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # chat command
    chat_parser = subparsers.add_parser("chat", help="Interactive chat mode")
    chat_parser.add_argument(
        "--model", "-m",
        type=str,
        default="deepseek-chat",
        help="Model to use (deepseek-chat or deepseek-reasoner)"
    )
    
    # run command
    run_parser = subparsers.add_parser("run", help="Run a single research task")
    run_parser.add_argument(
        "task",
        type=str,
        help="Research task description"
    )
    run_parser.add_argument(
        "--model", "-m",
        type=str,
        default="deepseek-chat",
        help="Model to use"
    )
    
    # doctor command
    subparsers.add_parser("doctor", help="Health check")
    
    return parser


async def run_chat(model: str):
    """Run interactive chat mode"""
    from src.agent.loop import PorpoiseLoop
    
    print("=" * 60)
    print("  Porpoise Agent - 江豚研究智能体")
    print("  服务: 无锡渔业学院/淡水渔业研究中心")
    print("  课题组: 刘凯研究员课题组")
    print("=" * 60)
    print(f"  Model: {model}")
    print("  Type 'quit' to exit, 'help' for commands")
    print("-" * 60)
    
    loop = PorpoiseLoop(model=model)
    
    while True:
        try:
            user_input = input("\n[You] > ").strip()
            if not user_input:
                continue
            if user_input.lower() in ("quit", "exit", "q"):
                print("Goodbye!")
                break
            if user_input.lower() == "help":
                print("Commands: quit/exit/q, help, clear")
                continue
            if user_input.lower() == "clear":
                loop.conversation_log.clear()
                print("[Session cleared]")
                continue
            
            result = await loop.run(user_input)
            print(f"\n[Agent] {result['response']}")
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


async def run_task(task: str, model: str):
    """Run a single research task"""
    from src.agent.orchestrator import Orchestrator
    
    print(f"Task: {task}")
    print(f"Model: {model}")
    print("-" * 60)
    
    orchestrator = Orchestrator()
    result = await orchestrator.run(task)
    
    print(f"\nResult: {result}")
    return result


async def run_doctor():
    """Health check"""
    import os
    from src.utils.config import config
    
    print("Porpoise Agent Health Check")
    print("=" * 40)
    
    # Check Python version
    py_version = sys.version_info
    print(f"[OK] Python {py_version.major}.{py_version.minor}.{py_version.micro}")
    
    # Check API key
    api_key = config.deepseek_api_key
    if api_key and api_key != "sk-your-deepseek-api-key":
        print("[OK] DeepSeek API key configured")
    else:
        print("[WARN] DeepSeek API key not set. Edit .env file.")
    
    # Check data directory
    data_dir = config.data_dir
    if data_dir.exists():
        print(f"[OK] Data directory: {data_dir}")
    else:
        print(f"[WARN] Data directory not found: {data_dir}")
    
    # Check dependencies
    deps = ["numpy", "scipy", "pandas", "librosa", "sklearn"]
    for dep in deps:
        try:
            __import__(dep.replace("sklearn", "sklearn"))
            print(f"[OK] {dep}")
        except ImportError:
            print(f"[MISS] {dep} - install with: pip install {dep}")


def main():
    """Main CLI entry point"""
    parser = setup_parser()
    args = parser.parse_args()
    
    if args.command == "chat":
        asyncio.run(run_chat(args.model))
    elif args.command == "run":
        asyncio.run(run_task(args.task, args.model))
    elif args.command == "doctor":
        asyncio.run(run_doctor())
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

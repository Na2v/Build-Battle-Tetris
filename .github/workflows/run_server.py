"""Standalone server (optional; host menu auto-starts server)."""

import asyncio
import argparse

from src.network.server import find_free_port, run_server


def parse_args() -> argparse.Namespace:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description="Tetris battle server")
    parser.add_argument("--host", default="0.0.0.0", help="Bind address")
    parser.add_argument("--port", type=int, default=0, help="Port (0 = auto)")
    return parser.parse_args()


def main() -> None:
    args: argparse.Namespace = parse_args()
    port: int = args.port if args.port > 0 else find_free_port()
    print(f"Tetris server listening on {args.host}:{port}")
    asyncio.run(run_server(host=args.host, port=port))


if __name__ == "__main__":
    main()

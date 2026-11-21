"""Entry point for the bao package."""

from __future__ import annotations

import sys


def greet(name: str = "world") -> str:
    """Return a greeting for *name*."""
    return f"Hello, {name}!"


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    name = args[0] if args else "world"
    print(greet(name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

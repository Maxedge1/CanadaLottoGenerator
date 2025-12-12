"""Minimal CLI for the Canada Lotto Generator."""

from __future__ import annotations

import argparse
import json
from typing import List

from .generator import generate_draw
from typing import Any, Mapping


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="canada-lotto")
    p.add_argument(
        "-n", "--num-draws", type=int, default=1, help="Number of draws to generate"
    )
    p.add_argument(
        "-k", "--numbers", type=int, default=6, help="How many main numbers per draw"
    )
    p.add_argument("-r", "--range", type=int, default=49, help="Max number in the pool")
    p.add_argument(
        "--preset",
        choices=["649", "max"],
        help="Common Canadian lotto presets: 649 or max",
    )
    p.add_argument(
        "--seed", type=int, default=None, help="Deterministic seed for draws"
    )
    p.add_argument("--bonus", action="store_true", help="Also generate a bonus number")
    p.add_argument(
        "--format", choices=["text", "json"], default="text", help="Output format"
    )
    return p


def format_draw(draw: Mapping[str, Any], fmt: str = "text") -> str:
    if fmt == "json":
        return json.dumps(draw)
    numbers = " ".join(str(n) for n in draw["numbers"])
    if draw.get("bonus") is not None:
        return f"{numbers} | Bonus: {draw['bonus']}"
    return numbers


def main(argv: List[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    # Apply preset if provided
    if args.preset == "649":
        args.numbers = 6
        args.range = 49
    elif args.preset in ("max", "lotto-max"):
        args.numbers = 7
        args.range = 50

    # Validate args
    if args.numbers < 1:
        parser.error("--numbers must be >= 1")
    if args.range < args.numbers:
        parser.error("--range must be >= --numbers (or choose a preset)")

    for i in range(args.num_draws):
        draw = generate_draw(
            numbers=args.numbers, range_max=args.range, bonus=args.bonus, seed=args.seed
        )
        print(format_draw(draw, args.format))

    return 0

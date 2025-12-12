"""Lotto number generation helpers."""

from __future__ import annotations

import random
from typing import List, Optional, TypedDict


class Draw(TypedDict):
    numbers: List[int]
    bonus: Optional[int]


def generate_draw(
    numbers: int = 6,
    range_max: int = 49,
    bonus: bool = False,
    seed: Optional[int] = None,
) -> Draw:
    """Generate a lotto draw.

    Args:
        numbers: how many main numbers to generate (default 6).
        range_max: highest number in the pool (default 49).
        bonus: whether to include a bonus ball (distinct from the main numbers).

    Returns:
        A dict with keys 'numbers' (sorted list) and 'bonus' (int or None).
    """
    if numbers < 1:
        raise ValueError("numbers must be >= 1")
    if range_max < numbers:
        raise ValueError("range_max must be >= numbers")

    pool = list(range(1, range_max + 1))
    rnd = random.Random(seed) if seed is not None else random
    main = rnd.sample(pool, numbers)
    main.sort()

    bonus_ball = None
    if bonus:
        remaining = [n for n in pool if n not in main]
        if remaining:
            bonus_ball = rnd.choice(remaining)
        else:
            bonus_ball = None

    return Draw(numbers=main, bonus=bonus_ball)

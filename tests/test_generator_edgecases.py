import pytest

from canada_lotto_generator.generator import generate_draw


def test_invalid_numbers_raises():
    with pytest.raises(ValueError):
        generate_draw(numbers=0)


def test_range_smaller_than_numbers_raises():
    with pytest.raises(ValueError):
        generate_draw(numbers=5, range_max=4)


def test_bonus_when_no_remaining_is_none():
    # numbers == range_max -> no remaining for bonus
    draw = generate_draw(numbers=5, range_max=5, bonus=True)
    assert draw["bonus"] is None

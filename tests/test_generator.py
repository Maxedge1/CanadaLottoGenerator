from canada_lotto_generator.generator import generate_draw


def test_generate_default():
    draw = generate_draw()
    assert isinstance(draw, dict)
    assert set(draw.keys()) == {"numbers", "bonus"}
    assert len(draw["numbers"]) == 6
    assert draw["bonus"] is None


def test_generate_unique_and_sorted():
    draw = generate_draw(numbers=6, range_max=49)
    nums = draw["numbers"]
    assert len(set(nums)) == len(nums)
    assert nums == sorted(nums)
    for n in nums:
        assert 1 <= n <= 49


def test_generate_bonus():
    draw = generate_draw(numbers=6, range_max=49, bonus=True)
    assert draw["bonus"] is None or (draw["bonus"] not in draw["numbers"])


def test_generate_seed_is_deterministic():
    a = generate_draw(numbers=6, range_max=49, bonus=True, seed=42)
    b = generate_draw(numbers=6, range_max=49, bonus=True, seed=42)
    assert a == b


def test_generate_different_seeds():
    a = generate_draw(numbers=6, range_max=49, bonus=True, seed=1)
    b = generate_draw(numbers=6, range_max=49, bonus=True, seed=2)
    assert a != b

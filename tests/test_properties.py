from hypothesis import given
from hypothesis import strategies as st

from canada_lotto_generator.generator import generate_draw


@given(
    numbers=st.integers(min_value=1, max_value=10),
    range_max=st.integers(min_value=1, max_value=100),
)
def test_properties_numbers_in_range(numbers, range_max):
    # Only test valid combinations where range_max >= numbers
    if range_max < numbers:
        return
    draw = generate_draw(numbers=numbers, range_max=range_max)
    nums = draw["numbers"]
    assert len(nums) == numbers
    assert nums == sorted(nums)
    assert all(1 <= n <= range_max for n in nums)


@given(
    seed=st.integers(),
    numbers=st.integers(min_value=1, max_value=7),
    range_max=st.integers(min_value=1, max_value=100),
)
def test_seeded_is_deterministic(seed, numbers, range_max):
    if range_max < numbers:
        return
    a = generate_draw(numbers=numbers, range_max=range_max, seed=seed, bonus=True)
    b = generate_draw(numbers=numbers, range_max=range_max, seed=seed, bonus=True)
    assert a == b

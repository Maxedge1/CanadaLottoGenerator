## API

`generate_draw(numbers=6, range_max=49, bonus=False, seed=None)`

- `numbers` (int): how many main numbers to generate.
- `range_max` (int): highest number in the pool.
- `bonus` (bool): whether to include a bonus number.
- `seed` (int|None): deterministic seed for reproducible draws.

Returns a dict with `numbers` (sorted list[int]) and `bonus` (int|None).

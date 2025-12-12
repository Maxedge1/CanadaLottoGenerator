from canada_lotto_generator.cli import format_draw
from canada_lotto_generator.cli import main as cli_main


def test_format_text_no_bonus():
    sample = {"numbers": [1, 2, 3, 4, 5, 6], "bonus": None}
    s = format_draw(sample, fmt="text")
    assert "Bonus" not in s
    assert "1 2 3 4 5 6" in s


def test_format_text_with_bonus():
    sample = {"numbers": [1, 2, 3, 4, 5, 6], "bonus": 42}
    s = format_draw(sample, fmt="text")
    assert "Bonus: 42" in s


def test_json_output():
    sample = {"numbers": [1, 2, 3, 4, 5, 6], "bonus": None}
    s = format_draw(sample, fmt="json")
    assert '"numbers"' in s
    assert '"bonus"' in s


def test_cli_main_runs(capsys):
    # Ensure the main function can be called and prints output
    cli_main(["-n", "2", "--bonus"])
    captured = capsys.readouterr()
    assert captured.out.strip() != ""


def test_cli_preset_and_seed_captures(capsys):
    # Using the preset and a seed should be deterministic
    cli_main(["--preset", "649", "--seed", "42"])
    first = capsys.readouterr().out.strip()
    cli_main(["--preset", "649", "--seed", "42"])
    second = capsys.readouterr().out.strip()
    assert first == second


def test_cli_validation_errors():
    # Invalid number of numbers
    try:
        cli_main(["--numbers", "0"])
    except SystemExit as e:
        assert e.code != 0

    # Range smaller than numbers
    try:
        cli_main(["--numbers", "10", "--range", "5"])
    except SystemExit as e:
        assert e.code != 0

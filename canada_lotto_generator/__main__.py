"""Run the CLI when the package is executed as a module."""

from .cli import main

if __name__ == "__main__":
    raise SystemExit(main())

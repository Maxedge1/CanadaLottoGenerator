VENV ?= .venv

.PHONY: install-dev test lint format type docs build package

install-dev:
	python -m pip install --upgrade pip
	python -m pip install -e .[dev]

test:
	python -m pytest

lint:
	ruff check .

format:
	black .

type:
	mypy .

docs:
	mkdocs build

build:
	python -m build

package: build
	twine check dist/*

release:
	@echo "Bump version (patch), commit, and tag."
	python -m bump2version patch
	git push --follow-tags

release-minor:
	@echo "Bump minor version, commit, and tag."
	python -m bump2version minor
	git push --follow-tags

release-major:
	@echo "Bump major version, commit, and tag."
	python -m bump2version major
	git push --follow-tags
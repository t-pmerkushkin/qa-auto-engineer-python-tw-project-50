install:
	uv sync

build:
	uv build

pi:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check gendiff

gendiff:
	uv run --active gendiff
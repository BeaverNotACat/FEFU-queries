deps:
	python -m pip install poetry
	poetry install --only main

dev-deps: deps
	poetry install

lint:
	poetry run ruff check
	poetry run mypy app/

test:
	echo "WIP"

migrate:
	echo "WIP"

run:
	poetry run litestar run -H 0.0.0.0

run-dev:
	poetry run litestar run -d -H 0.0.0.0

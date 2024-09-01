deps:
	python -m pip install poetry
	poetry install --only main

deps-dev: deps
	poetry install

lint:
	poetry run ruff check
	poetry run mypy app/ --enable-incomplete-feature=NewGenericSyntax

format:
	poetry run ruff format app/
	poetry run black app/
	poetry run isort app/

test:
	echo "WIP"

migrate:
	echo "WIP"

run:
	poetry run litestar run -H 0.0.0.0

run-dev:
	poetry run litestar run -d -H 0.0.0.0

sources = {{ cookiecutter.project_slug }}

.PHONY: test lint unittest coverage check pre-commit clean
test: lint check unittest

lint:
	isort $(sources) tests
	black $(sources) tests
	flake8 $(sources) tests

check:
	mypy $(sources)

unittest:
	pytest

coverage:
	pytest --cov=$(sources) --cov-branch --cov-report term-missing

pre-commit:
	pre-commit run --all-files

clean:
	rm -rf .mypy_cache .pytest_cache *.egg-info .tox dist site coverage.xml .coverage

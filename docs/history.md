# v1.0
***first release with the following features:***

1. [Poetry](https://python-poetry.org/): Manage version, dependancy, build and release
2. [Mkdocs](https://www.mkdocs.org): Writting your docs in markdown style
3. Testing with [Pytest](https://pytest.org) (unittest is still supported out of the box)
4. Code coverage report and endorsed by [Codecov](https://codecov.io)
5. [Tox](https://tox.readthedocs.io): Test your code against environment matrix, lint and artifact check.
6. Format with [Black](https://github.com/psf/black) and [Isort](https://github.com/PyCQA/isort)
7. Lint code with [Flake8](https://flake8.pycqa.org) and [Flake8-docstrings](https://pypi.org/project/flake8-docstrings/)
8. Check static type with [Mypy](http://mypy-lang.org/)
9. [Pre-commit hooks](https://pre-commit.com/): Formatting/linting anytime when commit/run local tox/CI
10. [Mkdocstrings](https://mkdocstrings.github.io/): Auto API doc generation
11. Command line interface using [Click](https://click.palletsprojects.com/en/8.0.x/) (optional)
12. Continuous Integration/Deployment by [GitHub actions](https://github.com/features/actions), includes:
    - publish dev build/official release to TestPyPI/PyPI automatically when CI success
    - publish documents automatically when CI success
    - extract change log from GitHub and integrate with release notes automatically
13. Host your documentation from [GitHub Pages](https://pages.github.com) with zero-config

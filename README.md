# Cookiecutter PyPackage

Cookiecutter template for a Python package, built with popular develop tools and
conform to best practice.

[![CI Status](https://github.com/waynerv/cookiecutter-pypackage/actions/workflows/release.yml/badge.svg)](https://github.com/zillionare/cookiecutter-pypackage)
[![License](https://img.shields.io/pypi/l/ppw)](https://opensource.org/licenses/BSD-2-Clause)


## Features

This tool will create Python project with the following features:

* [Poetry](https://python-poetry.org/): Manage version, dependancy, build and release
* [Mkdocs](https://www.mkdocs.org): Writting your docs in markdown style
* Testing with [Pytest](https://pytest.org) (unittest is still supported out of the box)
* Code coverage report and endorsed by [Codecov](https://codecov.io)
* [Tox](https://tox.readthedocs.io): Test your code against environment matrix, lint and artifact check.
* Format with [Black](https://github.com/psf/black) and [Isort](https://github.com/PyCQA/isort)
* Lint code with [Flake8](https://flake8.pycqa.org) and [Flake8-docstrings](https://pypi.org/project/flake8-docstrings/)
* Check static type with [Mypy](http://mypy-lang.org/)
* [Pre-commit hooks](https://pre-commit.com/): Formatting/linting anytime when commit/run local tox/CI
* [Mkdocstrings](https://mkdocstrings.github.io/): Auto API doc generation
* Command line interface using [Click](https://click.palletsprojects.com/en/8.0.x/) (optional)
* Continuous Integration/Deployment by [GitHub actions](https://github.com/features/actions), includes:
    - publish dev build/official release to TestPyPI/PyPI automatically when CI success
    - publish documents automatically when CI success
    - extract change log from GitHub and integrate with release notes automatically
* Host your documentation from [GitHub Pages](https://pages.github.com) with zero-config

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):

```
pip install -U cookiecutter
```

Generate a Python package project:

```
cookiecutter https://github.com/waynerv/cookiecutter-pypackage.git
```

Then follow **[Tutorial](https://waynerv.github.io/cookiecutter-pypackage/tutorial/)** to finish other configurations.

# Credits

This repo is forked from [zillionare/cookiecutter-pypackage](https://github.com/zillionare/cookiecutter-pypackage/), which originally forked from [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)

# Todo

[x] add makefile
[x] resolve pre-commit fail
[x] add bump2version
[ ] add flake8 rst docstring support
[ ] a better README template
[ ] improve docs

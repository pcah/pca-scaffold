## python-clean-architecture

# pca-scaffold

![GitHub tag](https://img.shields.io/github/v/tag/pcah/pca-scaffold)
[![development status](https://img.shields.io/badge/development%20status-alpha-yellow.svg)](https://pypi.org/project/pca-scaffold/)
[![supports](https://img.shields.io/pypi/pyversions/pca-scaffold)]([tox.ini](https://pypi.org/project/pca-scaffold/))
[![CI Status](https://github.com/pcah/pca-scaffold/actions/workflows/check_code_quality.yml/badge.svg)](https://github.com/pcah/pca-scaffold/actions/workflows/check_code_quality.yml)
[![codecov](https://codecov.io/gh/pcah/pca-scaffold/branch/master/graph/badge.svg)](https://codecov.io/gh/pcah/pca-scaffold)

Scaffolding template for a python-clean-architecture package.

* Documentation: <https://pcah.github.io/pca-scaffold>
* GitHub: <https://github.com/pcah/pca-scaffold>
* PyPI: <https://pypi.org/project/pca-scaffold/>
* Free software: [BSD-3-Clause](./LICENSE)

## Features

This tool will create Python project with the following features:

* [Poetry](https://python-poetry.org/): Manage dependency, build and release
* [Mkdocs](https://www.mkdocs.org): Writing your docs in markdown style
* Testing with [Pytest](https://pytest.org) (unittest is still supported out of the box)
* Code coverage report and endorsed by [Codecov](https://codecov.io)
* [Tox](https://tox.readthedocs.io): Test your code against environment matrix, lint and artifact check
* Format with [Black](https://github.com/psf/black) and [Isort](https://github.com/PyCQA/isort)
* Lint code with [Flake8](https://flake8.pycqa.org) and [Flake8-docstrings](https://pypi.org/project/flake8-docstrings/)
* Check static type with [Mypy](http://mypy-lang.org/) (optional)
* [Pre-commit hooks](https://pre-commit.com/): Formatting/linting anytime when commit your code
* [Mkdocstrings](https://mkdocstrings.github.io/): Auto API doc generation
* Command line interface using [Click](https://click.palletsprojects.com/en/8.0.x/) (optional)
* [bump2version](https://github.com/c4urself/bump2version): Pre-configured version bumping with a single command
* Continuous Integration/Deployment by [GitHub actions](https://github.com/features/actions), includes:
  * publish dev build/official release to TestPyPI/PyPI automatically when CI success
  * publish documents automatically when CI success
  * extract changelog from CHANGELOG and integrate with release notes automatically
* Host your documentation from [GitHub Pages](https://pages.github.com) with zero-config

## Quickstart

Install the latest [Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/) if you haven't installed it yet (this requires Cookiecutter `1.4.0` or higher):

```bash
pip install -U cookiecutter
```

Generate a Python package project:

```bash
cookiecutter https://github.com/pcah/pca-scaffold.git
```

Then follow **[Tutorial](https://pcah.github.io/pca-scaffold/tutorial/)** to finish other configurations.

# Credits

* This repo is forked from [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage),
* which originally forked from [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage),
* and custom adjustments for [python-clean-architecture](https://github.com/pcah/python-clean-architecture) by [pcah](https://github.com/pcah).

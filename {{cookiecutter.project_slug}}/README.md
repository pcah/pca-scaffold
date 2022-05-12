{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}

## python-clean-architecture

# {{cookiecutter.project_name}}

{% if is_open_source %}
[![GitHub tag](https://img.shields.io/github/v/tag/{{cookiecutter.project_owner}}/{{cookiecutter.project_slug}})]({{cookiecutter.repo_url}}/tags)
[![development status](https://img.shields.io/badge/development%20status-pre--alpha-orange.svg)](https://pypi.org/project/{{cookiecutter.project_slug}}/)
[![supports](https://img.shields.io/pypi/pyversions/{{cookiecutter.project_slug}}.svg)]({{cookiecutter.repo_url}}/blob/master/pyproject.toml)
[![CI status]({{cookiecutter.repo_url}}/actions/workflows/check_code_quality.yml/badge.svg)]({{cookiecutter.repo_url}}/actions/workflows/check_code_quality.yml)
[![codecov](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/main/graphs/badge.svg)](https://codecov.io/github/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}})

{% else %}
[![Build Status]({{cookiecutter.repo_url}}/actions/workflows/check_code_quality.yml/badge.svg)]({{cookiecutter.repo_url}}/actions/workflows/check_code_quality.yml)

{% endif %}
{{cookiecutter.project_short_description}}

{% if is_open_source %}
* Documentation: <{{cookiecutter.docs_url}}>
* GitHub: <{{cookiecutter.repo_url}}>
* PyPI: <https://pypi.org/project/{{cookiecutter.project_slug}}/>
* Free software: [{{cookiecutter.open_source_license}}](./LICENSE)
{% endif %}

## Features

* [TBDL]

{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}

## python-clean-architecture

# {{ cookiecutter.project_name }}

{% if is_open_source %}
[![pypi](<https://img.shields.io/pypi/v/>{{ cookiecutter.project_slug }}.svg)](<https://pypi.org/project/>{{ cookiecutter.project_slug }}/)
[![python](<https://img.shields.io/pypi/pyversions/>{{ cookiecutter.project_slug }}.svg)](<https://pypi.org/project/>{{ cookiecutter.project_slug }}/)
[![Build Status](<https://github.com/>{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/dev.yml/badge.svg)](<https://github.com/>{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/dev.yml)
[![codecov](<https://codecov.io/gh/>{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/main/graphs/badge.svg)](<https://codecov.io/github/>{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})

{% else %}
{% endif %}

{{cookiecutter.project_short_description}}

{% if is_open_source %}

* Documentation: <{{cookiecutter.docs_url}}>
* GitHub: <{{cookiecutter.repo_url}}>
* PyPI: <https://pypi.org/project/{{ cookiecutter.project_slug }}/>
* Free software: [{{ cookiecutter.open_source_license }}](./LICENSE)
{% endif %}

## Features

* [TBDL]

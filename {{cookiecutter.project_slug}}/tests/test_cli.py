{% if cookiecutter.command_line_interface|lower == 'click' -%}
from click.testing import CliRunner

from {{ cookiecutter.package_qualified_name }} import cli


def test_command_line_interface():
    """Test the CLI"""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert '{{ cookiecutter.project_slug }}' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
{%- endif %}

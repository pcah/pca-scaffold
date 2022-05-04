"""Tests for `{{ cookiecutter.package_qualified_name }}` package."""


def test_pca_namespace():
    """Test the package is accessible through the `pca` namespace"""
    from pca.packages import {{ cookiecutter.package_name }}

    assert hasattr({{ cookiecutter.package_name }}, "VERSION")

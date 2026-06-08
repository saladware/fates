"""Configuration file for the Sphinx documentation builder."""
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "fates"
copyright = "2026, Evgeny Goryachev"  # noqa: A001
author = "Evgeny Goryachev"
release = "0.0.2"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "autoapi.extension",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

autoapi_type = "python"
autoapi_dirs = ["../src/fates/"]
autoapi_root = "apidocs"

napoleon_google_docstring = True
napoleon_numpy_docstring = False

python_use_unqualified_type_names = True
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    "imported-members",  # Позволит корректно отобразить их в fates/index.html
]


myst_enable_extensions = ["colon_fence"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]

html_show_sphinx = False

html_theme_options = {
    "source_repository": "https://github.com/saladware/fates/",
    "source_branch": "master",
    "source_directory": "docs/",
    "light_css_variables": {
        "color-brand-primary": "#A9720C",
        "color-brand-content": "#A26D0B",
    },
    "dark_css_variables": {
        "color-brand-primary": "#F1C40F",
        "color-brand-content": "#F39C12",
    },
}

html_css_files = [
    "custom.css",
]

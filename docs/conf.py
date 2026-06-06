# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "fates"
copyright = "2026, Evgeny Goryachev"  # noqa: A001
author = "Evgeny Goryachev"
release = "0.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "sphinx_copybutton"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]

html_show_sphinx = False

html_theme_options = {
    # Настройки для светлой темы
    "light_css_variables": {
        "color-brand-primary": "#E5A93C",
        "color-brand-content": "#D2911A",
    },
    "dark_css_variables": {
        "color-brand-primary": "#F1C40F",
        "color-brand-content": "#F39C12",
    },
}

html_css_files = [
    "custom.css",
]

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
import pathlib
import sys
import os

sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())
sys.path.insert(0, os.path.abspath('../../app-1/code'))
sys.path.insert(0, os.path.abspath('../../app-2/code'))
sys.path.insert(0, os.path.abspath('../../app-2/code/models'))

project = 'Test Sphinx Generator'
copyright = '2023, Sunny'
author = 'Sunny'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.githubpages',
    'sphinx.ext.extlinks',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosummary',
    'sphinx.ext.imgconverter',
    'sphinxcontrib.openapi',
    'sphinxcontrib.httpdomain',
    'sphinxcontrib.swaggerui',
    'swagger_plugin_for_sphinx',
    'sphinx_tabs.tabs',
]

templates_path = ['app-1/_templates', 'app-2/_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_logo = '_static/logo.png'
# html_logo = 'https://www.nov.com/-/media/Project/NOV/NOV-Brands/GustoMSC/Logo/GustoMS'
# pygments_style = 'stata-dark'
html_theme = 'furo'
html_theme_options = {
    "dark_mode_code_blocks": True,
}
html_static_path = ['app-1/_static', 'app-2/_static']

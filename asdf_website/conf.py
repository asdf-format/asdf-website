# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

import os
import datetime
import importlib.metadata
from pathlib import Path
import tomli

# -- Project information -----------------------------------------------------

# Get configuration information from `pyproject.toml`
with open(Path(__file__).parent.parent / "pyproject.toml", "rb") as configuration_file:
    conf = tomli.load(configuration_file)
configuration = conf["project"]

project = configuration["name"]
author = f"{configuration['authors'][0]['name']} <{configuration['authors'][0]['email']}>"
copyright = f"{datetime.datetime.now().year}, {author}"

# The full version, including alpha/beta/rc tags
release = configuration["version"]


# The short X.Y version
# TODO
version = '0.0'

# -- General configuration ---------------------------------------------------
on_rtd = 'True'

html_baseurl = "https://www.asdf-format.org"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx_copybutton",
    "sphinx_tabs.tabs",
]


intersphinx_mapping = {
    "asdf-standard": ("https://www.asdf-format.org/projects/asdf-standard/en/latest/", None),
    "asdf": ("https://asdf.readthedocs.io/en/latest/", None),
    "asdf-coordinates-schemas": ("https://www.asdf-format.org/projects/asdf-coordinates-schemas/en/latest/", None),
    "asdf-transform-schemas": ("https://www.asdf-format.org/projects/asdf-transform-schemas/en/latest/", None),
    "asdf-wcs-schemas": ("https://www.asdf-format.org/projects/asdf-wcs-schemas/en/latest/", None),
    "astropy": ("https://docs.astropy.org/en/stable", None),
    "asdf-astropy": ("https://asdf-astropy.readthedocs.io/en/latest/", None),
}

html_static_path = ["_static"]

static_dir = os.path.join(os.path.dirname(__file__), "_static")

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "monokai"

# NB Dark style pygments is furo-specific at this time
pygments_dark_style = "monokai"

# Render inheritance diagrams in SVG
graphviz_output_format = "svg"

graphviz_dot_args = [
    "-Nfontsize=10",
    "-Nfontname=Helvetica Neue, Helvetica, Arial, sans-serif",
    "-Efontsize=10",
    "-Efontname=Helvetica Neue, Helvetica, Arial, sans-serif",
    "-Gbgcolor=white",
    "-Gfontsize=10",
    "-Gfontname=Helvetica Neue, Helvetica, Arial, sans-serif",
]
# The reST default role (used for this markup: `text`) to use for all documents.
default_role = "ref"

# The default language for highlighting
highlight_language = "yaml"

# The encoding of source files.
source_encoding = "utf-8"


# -- Options for HTML output -------------------------------------------------

html_title = "ASDF Documentation"
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"

# html_theme_path = []

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {
#     "sidebar_hide_name": True,
# }

# Override default settings from sphinx_asdf / sphinx_astropy (incompatible with furo)
html_sidebars = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

static_dir = os.path.join(os.path.dirname(__file__), "_static")


# The root toctree document.
root_doc = "index"

master_doc = 'index'

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_additional_pages = {
    "index": "index.html",
}


# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/images/favicon.ico"
# html_logo = "_static/images/logo.png"

globalnavlinks = {
    "Docs": "https://www.asdf-format.org",
    "Tutorials": "https://www.asdf-format.org/en/latest/tutorials/index.html",
    "Community": "https://www.asdf-format.org/en/latest/community/index.html",
    "Installation": "https://www.asdf-format.org/en/latest/applications/index.html",
}

topbanner = ""
for text, link in globalnavlinks.items():
    topbanner += f"<a href={link}>{text}</a>"

html_theme_options = {
    "light_logo": "images/logo-light-mode.png",
    "dark_logo": "images/logo-dark-mode.png",
    "announcement": topbanner,
}

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = "%b %d, %Y"

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# If false, no module index is generated.
html_domain_indices = False

# If false, no index is generated.
html_use_index = True

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True


# html_css_files = [
#     'css/globalnav.css',
#     # 'css/custom.css',
# ]

# html_js_files = [
#     'js/custom.js',
# ]


intersphinx_disabled_reftypes = ["*"]

def setup(app):
    app.add_css_file("css/globalnav.css")

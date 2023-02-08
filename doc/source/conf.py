"""Sphinx documentation configuration file."""

from datetime import datetime
import os
from pathlib import Path
from typing import List

from sphinx.builders.latex import LaTeXBuilder

LaTeXBuilder.supported_image_types = ["image/png", "image/pdf", "image/svg+xml"]

from ansys_sphinx_theme import (
    __version__,
    ansys_favicon,
    ansys_logo_black,
)

# Project information
project = "ansys_sphinx_theme"
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = "ANSYS, Inc."
release = version = __version__
cname = os.getenv("DOCUMENTATION_CNAME", "nocname.com")

# use the default ansys logo
html_logo = ansys_logo_black
html_theme = "ansys_sphinx_theme"

html_context = {
    "github_user": "ansys",
    "github_repo": "ansys-sphinx-theme",
    "github_version": "main",
    "doc_path": "doc/source",
}

# specify the location of your github repo
html_theme_options = {
    "github_url": "https://github.com/ansys/ansys-sphinx-theme",
    "contact_mail": "pyansys.support@ansys.com",
    "additional_breadcrumbs": [
        ("Ansys Internal Developer Portal", "https://dev.docs.ansys.com"),
    ],
}

html_short_title = html_title = "Ansys Sphinx Theme"

# Sphinx extensions
extensions = [
    "numpydoc",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx_design",
]

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/dev", None),
    # kept here as an example
    # "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    # "numpy": ("https://numpy.org/devdocs", None),
    # "matplotlib": ("https://matplotlib.org/stable", None),
    # "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
    # "pyvista": ("https://docs.pyvista.org/", None),
}

# Favicon
html_favicon = ansys_favicon

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

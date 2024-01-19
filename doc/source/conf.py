"""Sphinx documentation configuration file."""

from datetime import datetime

from sphinx.builders.latex import LaTeXBuilder

LaTeXBuilder.supported_image_types = [
    "image/png",
    "image/pdf",
    "image/svg+xml",
]

from ansys_sphinx_theme import __version__, ansys_favicon, ansys_logo_black

# Project information
project = "ansys_sphinx_theme"
copyright = (
    f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
)
author = "ANSYS, Inc."
release = version = __version__

# use the default ansys logo
html_logo = ansys_logo_black
html_theme = "ansys_sphinx_theme"

html_context = {
    "github_user": "ansys",
    "github_repo": "pyansys-cheat-sheet",
    "github_version": "main",
    "doc_path": "doc/source",
}

# specify the location of your github repo
html_theme_options = {
    "github_url": "https://github.com/ansys/pyansys-cheat-sheet",
    "contact_mail": "pyansys.core@ansys.com",
    "additional_breadcrumbs": [
        ("PyAnsys", "https://docs.pyansys.com"),
    ],
    "show_prev_next": False,
    "show_breadcrumbs": True,
    "collapse_navigation": True,
    "use_edit_page_button": True,
    "icon_links": [
        {
            "name": "Support",
            "url": "https://github.com/ansys/pyansys-cheat-sheet/discussions",
            "icon": "fa fa-comment fa-fw",
        },
    ],
}

html_short_title = html_title = "PyAnsys Cheat sheets"

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
}

# Favicon
html_favicon = ansys_favicon

# The suffix(es) of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use the absolute path, like shown here.
import sys
from pathlib import Path
sys.path.insert(0, str(Path('../').resolve()))


# -- Project information -----------------------------------------------------

project = 'QGreenland'
copyright = '2021, Twila Moon, et al.'
author = 'Twila Moon, et al.'

# The full version, including alpha/beta/rc tags
release = 'v2.0.0alpha4'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx.ext.linkcode',
    'sphinx.ext.autodoc',
    # TODO: What does this do?
    # 'sphinx_autodoc_typehints',  # MUST be after 'sphinx.ext.autodoc'.
    'sphinxcontrib.autodoc_pydantic',

]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for linkcode behavior ---------------------------------------------
def linkcode_resolve(domain, info):
    # Domain could be `py`, `c`, `cpp`, `javascript`, but this is a Python
    # project.
    if domain != 'py':
        return None
    if not info['module']:
        return None

    filename = info['module'].replace('.', '/')
    return f'https://github.com/nsidc/qgreenland/blob/main/{filename}.py'


# -- Options for autodoc output ------------------------------------------------
autodoc_default_options = {
    # Document all public members by default.
    'members': None,
    'show-inheritance': True,
    # If set, autodoc will also generate document for the members not having docstrings:
    'undoc-members': True,
}

# Show the full path to the object (this is the default), e.g.:
# `qgreenland.models.config.asset.CmrAsset`
add_module_names = True

# Show the typehints in the description of each object instead of the signature.
# We found this to be more readable.
autodoc_typehints = 'description'

# TODO: Make this work. Why doesn't it work?
# autodoc_type_aliases = {
#     'AnyAsset': 'qgreenland.models.config.asset.AnyAsset',
# }

# Hide pydantic model configuration from the sphinx output.
autodoc_pydantic_model_show_config_summary = False

# Hide redundant pydantic validators summary
autodoc_pydantic_model_show_validator_summary = False

# Hide redundant field summary
autodoc_pydantic_model_show_field_summary = False

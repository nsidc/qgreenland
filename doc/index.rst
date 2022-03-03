.. QGreenland documentation master file, created by
   sphinx-quickstart on Mon Dec  6 11:34:57 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


========================
QGreenland Documentation
========================


.. raw:: latex

    \part{Introduction}


.. toctree::
    :maxdepth: 1
    :hidden:

    what_is_qgr.md
    citing.md
    acknowledgements.md


.. raw:: latex

    \part{Tutorials}


.. toctree::
    :name: Tutorials
    :caption: Tutorials
    :maxdepth: 1
    :glob:
    :hidden:

    tutorials/get-started.md
    tutorials/*


.. raw:: latex

    \part{How-to}


.. toctree::
    :name: How-to
    :caption: How-to
    :maxdepth: 1
    :hidden:

    user-how-to/index
    contributor-how-to/index


.. raw:: latex

    \part{Reference}


.. toctree::
    :name: Reference
    :caption: Reference
    :maxdepth: 1
    :glob:
    :hidden:

    reference/glossary/index
    reference/architecture/index
    reference/api/index
    reference/cli/index
    reference/*


.. raw:: latex

    \part{Discussion topics}


.. toctree::
    :name: Discussion topics
    :caption: Discussion topics
    :maxdepth: 1
    :glob:
    :hidden:

    discussion/*


.. raw:: latex

    \part{Appendix}


.. only:: builder_html

    .. include:: what_is_qgr.md
        :parser: myst_parser.sphinx_

    .. include:: citing.md
        :parser: myst_parser.sphinx_

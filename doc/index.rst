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
    tutorials/video-series-overview.md
    tutorials/*


.. raw:: latex

    \part{How-to}


.. toctree::
    :name: User_How_to
    :caption: User How-to
    :maxdepth: 1
    :glob:
    :hidden:

    user-how-to/*


.. only:: not latex

  .. toctree::
      :name: Contributor_How_to
      :caption: Contributor How-to
      :maxdepth: 1
      :glob:
      :hidden:

      contributor-how-to/*


.. raw:: latex

    \part{Reference}


.. toctree::
    :name: User_Reference
    :caption: User Reference
    :maxdepth: 1
    :hidden:

    reference/glossary/index
    reference/data-compatibility-guide.md
    reference/online-resources.md


.. only:: not latex

  .. toctree::
      :name: Contributor_Reference
      :caption: Contributor Reference
      :maxdepth: 1
      :hidden:
  
      reference/architecture/index
      reference/api/index
      reference/cli/index
      reference/style-guide.md


.. raw:: latex

    \part{Discussion topics}


.. toctree::
    :name: Discussion topics
    :caption: Discussion topics
    :maxdepth: 1
    :glob:
    :hidden:

    discussion/*


.. only:: builder_html

    .. include:: what_is_qgr.md
        :parser: myst_parser.sphinx_

    .. include:: citing.md
        :parser: myst_parser.sphinx_

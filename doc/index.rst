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


.. toctree::
    :name: User_Documentation
    :caption: User Documentation
    :hidden:

    user/tutorials/index
    user/how-to/index
    user/reference/index
    user/discussion/index


.. only:: html

    .. toctree::
        :name: Contributor_Documentation
        :caption: Contributor Documentation
        :maxdepth: 1
        :hidden:

        contributor/how-to/index
        contributor/reference/index
        contributor/discussion/index


    .. include:: what_is_qgr.md
        :parser: myst_parser.sphinx_


    .. include:: citing.md
        :parser: myst_parser.sphinx_

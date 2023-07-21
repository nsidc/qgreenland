.. _cli-reference:

=============
CLI reference
=============

The QGreenland CLI can be accessed by :code:`./scripts/cli.sh`. This will run a
CLI inside the QGreenland container, which is required for most commands. If
you prefer to run a local CLI, this is possible for commands like
:code:`provenance`, which only requires the configuration, with
:code:`./scripts/experimental/local_cli.sh`.


.. click:: qgreenland.cli:cli
    :prog: qgreenland-cli
    :nested: full

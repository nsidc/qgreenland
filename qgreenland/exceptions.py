class QgrVersionError(Exception):
    """Something went wrong trying to determine the current QGR version."""

    pass


class QgrInvalidConfigError(Exception):
    """Something went wrong with validating/parsing/interpreting the config."""

    pass


class QgrRuntimeError(Exception):
    """Something went wrong in the QGreenland runtime framework."""

    pass


class QgrSubprocessError(Exception):
    """Something went wrong running a `subprocess` command."""

    pass


class QgrQgsLayerError(Exception):
    """Something went wrong creating a QgsLayer."""

    pass

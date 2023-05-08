import click

from qgreenland.constants.paths import PACKAGE_VERSION


@click.command()
def version() -> None:
    """Print the version of this code.

    NOTE: The QGreenland output zip will be versioned with this string as well.
    """
    print(PACKAGE_VERSION)

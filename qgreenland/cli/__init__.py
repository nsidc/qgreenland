import click

from qgreenland.cli.cleanup import cleanup
from qgreenland.cli.config_migrate import config_migrate


@click.group()
def cli():
    ...


cli.add_command(config_migrate)
cli.add_command(cleanup)


if __name__ == '__main__':
    cli()

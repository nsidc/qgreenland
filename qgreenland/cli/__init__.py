import click

from qgreenland.cli.config_migrate import config_migrate
from qgreenland.cli.cleanup import cleanup 


@click.group()
def cli():
    ...


cli.add_command(config_migrate)
cli.add_command(cleanup)


if __name__ == '__main__':
    cli()

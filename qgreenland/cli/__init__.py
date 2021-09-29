import click

from qgreenland.cli.cleanup import cleanup
from qgreenland.cli.config_migrate import config_migrate
from qgreenland.cli.run import run


@click.group(context_settings={'help_option_names': ['-h', '--help']})
def cli():
    ...


cli.add_command(config_migrate)
cli.add_command(cleanup)
cli.add_command(run)


if __name__ == '__main__':
    cli()

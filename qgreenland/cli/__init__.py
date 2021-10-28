import click

from qgreenland.cli.cleanup import cleanup
from qgreenland.cli.config_template import config_template
from qgreenland.cli.fetch import fetch
from qgreenland.cli.run import run


@click.group(context_settings={'help_option_names': ['-h', '--help']})
def cli():
    ...


cli.add_command(cleanup)
cli.add_command(config_template)
cli.add_command(run)
cli.add_command(fetch)


if __name__ == '__main__':
    cli()

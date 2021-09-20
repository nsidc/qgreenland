import click

from qgreenland.cli.config_migrate import config_migrate


@click.group()
def cli():
    ...


cli.add_command(config_migrate)


if __name__ == '__main__':
    cli()

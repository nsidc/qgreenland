import click
import luigi


@click.command()
def fetch() -> None:
    """..."""
    luigi.build([...])
    raise NotImplementedError('Come back tomorrow!')

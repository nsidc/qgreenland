import click

from qgreenland.constants.paths import TEMPLATES_DIR


def _print_template(template_fn: str) -> None:
    contents = open(TEMPLATES_DIR / template_fn, 'r').read()

    # Don't print the extra newline, so the contents can be redirected without
    # change.
    print(contents[:-1])


@click.group()
def config_template():
    """Generate a template to help with creating layers or datasets."""
    ...


@config_template.command()
def dataset():
    """Generate a dataset configuration template."""
    _print_template('dataset_cfg.py')


@config_template.command()
def layer():
    """Generate a layer configuration template."""
    _print_template('layer_cfg.py')

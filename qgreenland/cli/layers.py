import json
from fnmatch import fnmatch

import click
from funcy import select

from qgreenland.util.json import MagicJSONEncoder

Format = ['ids', 'titles', 'json']


@click.command()
@click.option(
    'format',
    '--format',
    '-f',
    type=click.Choice(Format, case_sensitive=False),
    default='ids',
    show_default=True,
    help='The format in which to display the layers.',
)
@click.argument('pattern')
def layers(
    pattern: str,
    format: str,
) -> None:
    """List available layers matching PATTERN."""
    from qgreenland.util.config.config import (
        get_config,
        init_config,
    )
    init_config()
    config = get_config()

    layers = select(
        lambda i: fnmatch(i[1].id, pattern),
        config.layers,
    ).values()

    if format == 'ids':
        for layer in layers:
            print(layer.id)
    elif format == 'titles':
        for layer in layers:
            print(f'{layer.id}: {layer.title}')
    elif format == 'json':
        # TODO: This doesn't use the __json__ helper and dumps the full layer
        # config, as opposed to the filtered version that goes in the lockfile.
        # This is more useful for debugging.
        print(json.dumps(
            # Full dump:
            [layer.dict() for layer in layers],
            # Filtered dump:
            # list(layers),
            cls=MagicJSONEncoder,
            indent=2,
            sort_keys=True,
        ))

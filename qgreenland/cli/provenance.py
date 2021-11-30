import sys

import click

from qgreenland.util.config.config import (
    get_config,
    init_config,
)
from qgreenland.util.provenance import layer_provenance_text


@click.command()
@click.argument('layer_id')
def provenance(layer_id):
    init_config()
    config = get_config()

    try:
        layer_cfg = config.layers[layer_id]
    except KeyError:
        print(f'Could not find layer {layer_id}.')
        sys.exit(1)

    print(layer_provenance_text(layer_cfg))

import sys

import click

from qgreenland.util.config.config import (
    get_config,
    init_config,
)
from qgreenland.util.provenance import steps_to_provenance_text


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

    if not layer_cfg.steps:
        print(f'No steps associated with layer {layer_id}.')
        sys.exit(1)

    print(steps_to_provenance_text(layer_cfg.steps))

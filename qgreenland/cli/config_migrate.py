import click
import requests
import yaml
from funcy import lwhere

from qgreenland.util.template import load_template

def _load_yaml_from_gh(url_fp: str) -> dict:
    """Load YAML from v1 tag on GitHub."""
    BASE_URL = 'https://raw.githubusercontent.com/nsidc/qgreenland/v1.0.1'
    url = BASE_URL + url_fp
    loaded = yaml.safe_load(requests.get(url).text)

    return loaded


def _find_one(mappings, **cond):
    result = lwhere(mappings, **cond)
    if len(result) != 1:
        raise RuntimeError(
            f'Expected 1 result for ({cond}). Received: {result}',
        )

    return result[0]


@click.group()
def config_migrate():
    """Migrate v1 config (YAML) to v2 config (Python)."""
    ...


@config_migrate.command()
@click.argument('dataset_id')
def dataset(dataset_id):
    """Migrate config DATASET_ID from v1 to v2."""
    yml = _load_yaml_from_gh('/qgreenland/config/datasets.yml')
    dataset = _find_one(yml, id=dataset_id)

    template = load_template('dataset_config_v2.py.jinja')
    rendered = template.render(
        dataset=dataset,
        asset_type_map={
            'manual': 'ConfigDatasetManualAsset',
        },
    )
    print(rendered)


@config_migrate.command()
@click.argument('layer_id')
def layer(layer_id):
    """Migrate config LAYER_ID from v1 to v2."""
    yml = _load_yaml_from_gh('/qgreenland/config/layers.yml')
    layer = _find_one(yml, id=layer_id)
    raise NotImplementedError()

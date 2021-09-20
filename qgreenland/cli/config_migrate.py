import click
import requests
import yaml
from funcy import lwhere

BASE_URL = 'https://raw.githubusercontent.com/nsidc/qgreenland/v1.0.1'


def _read_yaml_from_gh(url_fp: str) -> dict:
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
    yml = _read_yaml_from_gh('/qgreenland/config/datasets.yml')

    dataset = _find_one(yml, id=dataset_id)
    breakpoint()
    print()
    ...


@config_migrate.command()
@click.argument('layer_id')
def layer(layer_id):
    """Migrate config LAYER_ID from v1 to v2."""
    raise NotImplementedError()

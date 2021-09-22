from fnmatch import fnmatch

import click
import requests
import yaml
from funcy import select

from qgreenland.util.template import load_template


def _load_yaml_from_gh(url_fp: str) -> dict:
    """Load YAML from v1 tag on GitHub."""
    base_url = 'https://raw.githubusercontent.com/nsidc/qgreenland/v1.0.1'
    url = base_url + url_fp
    loaded = yaml.safe_load(requests.get(url).text)

    return loaded


def _select(mappings, pattern):
    pred = lambda i: fnmatch(i['id'], pattern)  # noqa: E731
    results = select(pred, mappings)
    if len(results) == 0:
        raise RuntimeError(
            f'No results found for "{pattern}".',
        )

    return results


@click.group()
def config_migrate():
    """Migrate v1 config (YAML) to v2 config (Python)."""
    ...


@config_migrate.command()
@click.argument('pattern')
def dataset(pattern):
    """Migrate datasets with ids matching PATTERN from v1 to v2.

    Matching is done with Unix shell-style wildcards (see `fnmatch.fnmatch`).

    NOTE: If multiple matches are found, the ouput will need to be manually
    touched up to consolidate import statements.
    """
    yml = _load_yaml_from_gh('/qgreenland/config/datasets.yml')
    datasets = _select(yml, pattern=pattern)
    template = load_template('dataset_config_v2.py.jinja')

    for dataset in datasets:
        rendered = template.render(
            dataset=dataset,
            asset_type_map={
                'manual': 'ConfigDatasetManualAsset',
            },
        )
        print(rendered)


@config_migrate.command()
@click.argument('pattern')
def layer(pattern):
    """Migrate layers with ids matching PATTERN from v1 to v2.

    Matching is done with Unix shell-style wildcards (see `fnmatch.fnmatch`).

    NOTE: If multiple matches are found, the ouput will need to be manually
    touched up to consolidate import statements.
    """
    yml = _load_yaml_from_gh('/qgreenland/config/layers.yml')
    layers = _select(yml, pattern=pattern)
    template = load_template('layer_config_v2.py.jinja')

    for layer in layers:
        rendered = template.render(
            layer=layer,
        )
        print(rendered)

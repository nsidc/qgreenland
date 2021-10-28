from pathlib import Path
from typing import Union, cast

from qgreenland.config.datasets.hdx_hotosm import hdx_hotosm as dataset
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.models.config.asset import ConfigDatasetHttpAsset
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


def _make_hotosm_populated_places() -> ConfigLayer:
    return ConfigLayer(
        id='hotosm_populated_places',
        title='Populated places',
        description=(
            """Points representing populated places in Greenland."""
        ),
        tags=[],
        style='hotosm_populated_places_point',
        input=ConfigLayerInput(
            dataset=dataset,
            asset=dataset.assets['populated_places'],
        ),
        steps=[
            *compressed_vector(
                input_file='{input_dir}/hotosm_grl_populated_places_points_shp.zip',
                output_file='{output_dir}/hotosm_populated_places.gpkg',
                ogr2ogr_args=[
                    '-dialect', 'sqlite',
                    '-sql', (
                        '"SELECT'
                        ' osm_id,'
                        ' is_in,'
                        ' source,'
                        ' name,'
                        ' place,'
                        ' geometry,'
                        ' CAST(population AS INTEGER) as population'
                        ' FROM hotosm_grl_populated_places_points"'
                    ),
                ],
            ),
        ],
    )


_other_hotosm_layer_params: dict[str, dict[str, Union[str, None]]] = {
    'health_facilities': {
        'description': 'Points representing health facilities in Greenland.',
        'style': 'health_facility_point',
    },
    'airports': {
        'description': 'Points representing airports in Greenland.',
        'style': 'airport_point',
    },
    'seaports': {
        'description': 'Points representing seaports in Greenland.',
        'style': 'seaport_point',
    },
    'waterways': {
        'description': 'Lines representing waterways in Greenland.',
        'style': None,
    },
    'financial_services': {
        'description': 'Points representing financial services in Greenland.',
        'style': 'financial_facility_point',
    },
    'education_facilities': {
        'description': 'Points representing educational facilities in Greenland.',
        'style': 'education_facility_point',
    },
    'points_of_interest': {
        'description': 'Points of interest in Greenland.',
        'style': None,
    },
    'roads': {
        'description': 'Lines representing roads in Greenland.',
        'style': 'roads_line',
    },
    'buildings': {
        'description': 'Polygons representing buildings in Greenland.',
        'style': 'buildings_shape',
    },
}


def _make_other_hotosm_layers() -> list[ConfigLayer]:
    layers = []
    for asset_id, params in _other_hotosm_layer_params.items():
        asset = cast(ConfigDatasetHttpAsset, dataset.assets[asset_id])
        layers.append(
            ConfigLayer(
                id=f'hotosm_{asset_id}',
                title=f"{asset_id.capitalize().replace('_', ' ')}",
                description=params['description'],
                tags=[],
                style=params['style'],
                input=ConfigLayerInput(
                    dataset=dataset,
                    asset=asset,
                ),
                steps=[
                    *compressed_vector(
                        input_file=(
                            '{input_dir}/'
                            + Path(asset.urls[0]).name
                        ),
                        output_file='{output_dir}/' + f'{asset_id}.gpkg',
                    ),
                ],
            ),
        )

    return layers


def make_all_hotosm_layers() -> list[ConfigLayer]:
    layers = [_make_hotosm_populated_places()]
    layers.extend(_make_other_hotosm_layers())

    return layers


def hotosm_layers_order() -> list[str]:
    layer_order = ['hotosm_populated_places']

    for asset_id in _other_hotosm_layer_params.keys():
        layer_order.append(f'hotosm_{asset_id}')

    return layer_order


other_hotosm_layers = _make_other_hotosm_layers()

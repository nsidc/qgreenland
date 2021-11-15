from qgreenland.config.datasets.streams_outlets_basins import streams_outlets_basins as dataset  # noqa: E501
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import Layer, LayerInput


_stream_selection_ogr2ogr_args: list[str] = [
    '-dialect', 'sqlite',
    '-sql', (
        """\"SELECT * from streams
        WHERE GeometryType(geom) = 'LINESTRING' AND ST_NPoints(geom) > 1\""""
    ),
]

_layer_params: dict[str, dict[str, str]] = {
    'ice_outlets': {
        'description': (
            'Calculated locations for subglacial hydrologic basin'
            ' ice-margin-terminating outlets.'
        ),
        'input_filename': 'outlets.gpkg',
    },
    'land_outlets': {
        'description': (
            'Calculated locations for terrestrial hydrologic basin'
            ' coast-terminating outlets.'
        ),
        'input_filename': 'outlets.gpkg',
    },
    'ice_streams': {
        'description': 'Calculated subglacial hydrologic stream paths.',
        'input_filename': 'streams.gpkg',
    },
    'ice_basins': {
        'description': (
            'Calculated ice sheet hydrologic basins using regional climate'
            ' model spatial coverage.'
        ),
        'input_filename': 'basins.gpkg',
    },
    'ice_basins_filled': {
        'description': (
            'Calculated ice sheet hydrologic basins including areas classified'
            ' as land/ocean by regional climate models (filled).'
        ),
        'input_filename': 'basins_filled.gpkg',
    },
    'land_streams': {
        'description': 'Calculated terrestrial hydrologic stream paths.',
        'input_filename': 'streams.gpkg',
    },
    'land_basins': {
        'description': (
            'Calculated terrestrial hydrologic basins using regional climate'
            ' model spatial coverage.'
        ),
        'input_filename': 'basins.gpkg',
    },
    'land_basins_filled': {
        'description': (
            'Calculated terrestrial hydrologic basins including areas classified'
            ' as ice/ocean by regional climate models (filled).'
        ),
        'input_filename': 'basins_filled.gpkg',
    },
}

layers = [
    Layer(
        id=layer_id,
        title=layer_id.replace('_', ' ').capitalize(),
        description=(
            """Calculated locations for subglacial hydrologic basin
            ice-margin-terminating outlets."""
        ),
        tags=[],
        style=layer_id.replace('_filled', ''),
        input=LayerInput(
            dataset=dataset,
            asset=dataset.assets[layer_id],
        ),
        steps=[
            *ogr2ogr(
                input_file='{input_dir}/' + params['input_filename'],
                output_file='{output_dir}/' + f'{layer_id}.gpkg',
                ogr2ogr_args=(
                    _stream_selection_ogr2ogr_args if 'streams' in layer_id else []
                ),
            ),
        ],
    )
    for layer_id, params in _layer_params.items()
]


ORDERED_LAYER_IDS = list(_layer_params.keys())

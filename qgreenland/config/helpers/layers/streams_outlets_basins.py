from qgreenland.config.datasets.streams_outlets_basins import streams_outlets_basins as dataset
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


_stream_selection_ogr2ogr_args = (
    '-dialect', 'sqlite',
    '-sql', (
        """\"SELECT * from streams
        WHERE GeometryType(geom) = 'LINESTRING' AND ST_NPoints(geom) > 1\""""
    )
)

_layer_params = {
    'ice_outlets': {
        'description': (
            'Calculated locations for subglacial hydrologic basin'
            ' ice-margin-terminating outlets.'
        ),
        'ogr2ogr_args': (),
        'input_filename': 'outlets.gpkg',
    },
    'land_outlets': {
        'description': (
            'Calculated locations for terrestrial hydrologic basin'
            ' coast-terminating outlets.'
        ),
        'ogr2ogr_args': (),
        'input_filename': 'outlets.gpkg',
    },
    'ice_streams': {
        'description': 'Calculated subglacial hydrologic stream paths.',
        'ogr2ogr_args': _stream_selection_ogr2ogr_args,
        'input_filename': 'streams.gpkg',
    },
    'ice_basins': {
        'description': (
            'Calculated ice sheet hydrologic basins using regional climate'
            ' model spatial coverage.'
        ),
        'ogr2ogr_args': (),
        'input_filename': 'basins.gpkg',
    },
    'ice_basins_filled': {
        'description': (
            'Calculated ice sheet hydrologic basins including areas classified'
            ' as land/ocean by regional climate models (filled).'
        ),
        'ogr2ogr_args': (),
        'input_filename': 'basins_filled.gpkg',
    },
    'land_streams': {
        'description': 'Calculated terrestrial hydrologic stream paths.',
        'ogr2ogr_args': _stream_selection_ogr2ogr_args,
        'input_filename': 'streams.gpkg',
    },
    'land_basins': {
        'description': (
            'Calculated terrestrial hydrologic basins using regional climate'
            ' model spatial coverage.'
        ),
        'ogr2ogr_args': (),
        'input_filename': 'basins.gpkg',
    },
    'land_basins_filled': {
        'description': (
            'Calculated terrestrial hydrologic basins including areas classified'
            ' as ice/ocean by regional climate models (filled).'
        ),
        'ogr2ogr_args': (),
        'input_filename': 'basins_filled.gpkg',
    },
}

layers = [
    ConfigLayer(
        id=layer_id,
        title=layer_id.replace('_', ' ').capitalize(),
        description=(
            """Calculated locations for subglacial hydrologic basin
            ice-margin-terminating outlets."""
        ),
        tags=[],
        style=layer_id.replace('_filled', ''),
        input=ConfigLayerInput(
            dataset=dataset,
            asset=dataset.assets[layer_id],
        ),
        steps=[
            *ogr2ogr(
                input_file='{input_dir}/' + params['input_filename'],
                output_file='{output_dir}/' + f'{layer_id}.gpkg',
                ogr2ogr_args=params['ogr2ogr_args'],
            ),
        ],
    )
    for layer_id, params in _layer_params.items()
]


ORDERED_LAYER_IDS = list(_layer_params.keys())

from qgreenland.config.datasets.promice import (
    gc_net_promice_stations as dataset,
)
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep

promice_layer_params = {
    'promice_research_stations': {
        'title': 'PROMICE automated weather stations',
        'description': (
            """Locations and details of PROMICE automated weather stations."""
        ),
        'asset_id': 'promice',
    },
    'promice_research_stations_former': {
        'title': 'Former PROMICE automated weather stations',
        'description': (
            """Locations and details of inactive PROMICE automated weather
            stations."""
        ),
        'asset_id': 'promice_former',
    },
    'gc_net_research_stations': {
        'title': 'GC-NET automated weather stations',
        'description': (
            """Location and details of GC-NET automated weather stations."""
        ),
        'asset_id': 'gc_net',
    },
}


layers = [
    ConfigLayer(
        id=id,
        title=params['title'],
        description=params['description'],
        tags=[],
        # style='labeled_point',
        input=ConfigLayerInput(
            dataset=dataset,
            asset=dataset.assets[params['asset_id']],
        ),
        steps=[
            *ogr2ogr(
                # This CSV data is tab-delimeted, but ogr2ogr can
                # auto-detect that.
                input_file='{input_dir}/*.csv',
                output_file='{output_dir}/final.gpkg',
                ogr2ogr_args=(
                    '-s_srs', 'EPSG:4326',
                    '-oo', 'X_POSSIBLE_NAMES=lon',
                    '-oo', 'Y_POSSIBLE_NAMES=lat',
                ),
            )
        ],
    )

    for id, params in promice_layer_params.items()
]

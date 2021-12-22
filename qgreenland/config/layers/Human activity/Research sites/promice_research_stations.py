from qgreenland.config.datasets.promice_stations import (
    gc_net_promice_stations as dataset,
)
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import Layer, LayerInput

promice_layer_params = {
    'promice_research_stations': {
        'title': 'PROMICE automated weather stations',
        'description': (
            """Locations and details of PROMICE automated weather stations."""
        ),
        'asset_id': 'promice',
        'table_name': 'PROMICE_info_from_GPS_data_2017-2018',
    },
    'promice_research_stations_former': {
        'title': 'Former PROMICE automated weather stations',
        'description': (
            """Locations and details of inactive PROMICE automated weather
            stations."""
        ),
        'asset_id': 'promice_former',
        'table_name': 'PROMICE_info_from_GPS_data_2017-2018_former_sites',
    },
    'gc_net_research_stations': {
        'title': 'GC-NET automated weather stations',
        'description': (
            """Location and details of GC-NET automated weather stations."""
        ),
        'asset_id': 'gc_net',
        'table_name': 'GCN%20info%20ca.2000',
    },
}


layers = [
    Layer(
        id=id,
        title=params['title'],
        description=params['description'],
        tags=[],
        style='labeled_point',
        input=LayerInput(
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
                    '-sql', fr'"SELECT *, name as label from \"{params["table_name"]}\""',
                ),
            ),
        ],
    )

    for id, params in promice_layer_params.items()
]

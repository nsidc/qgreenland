from qgreenland.config.datasets.glacier_terminus import glacier_terminus as dataset
from qgreenland.config.helpers.layers.glacier_terminus import LAYER_YEARS
from qgreenland.config.helpers.layers.glacier_terminus import id_str
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


layers = [
    ConfigLayer(
        id=id_str(start=START, end=END),
        title=f'Glacier termini {START} to {END}',
        description=f'Glacier terminus during the {START}-{END} winter season.',
        tags=[],
        input=ConfigLayerInput(
            dataset=dataset,
            asset=dataset.assets[f'{START}_{END}'],
        ),
        steps=[
            *ogr2ogr(
                input_file='{input_dir}/termini_*.shp',
                output_file='{output_dir}/boundary.gpkg',
            ),
        ],
    )
    for (START, END) in LAYER_YEARS
]

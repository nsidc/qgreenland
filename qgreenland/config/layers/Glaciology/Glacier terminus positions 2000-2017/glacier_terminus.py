from qgreenland.config.datasets.glacier_terminus import glacier_terminus as dataset
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.config.helpers.layers.glacier_terminus import LAYER_YEARS
from qgreenland.config.helpers.layers.glacier_terminus import id_str
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


layers = [
    ConfigLayer(
        id=id_str(start=START, end=END),
        title=f'Glacier termini {START} to {END}',
        description=f'Glacier terminus during interval {START} to {END}.',
        tags=[],
        input=ConfigLayerInput(
            dataset=dataset,
            asset=dataset.assets[f'{START}_{END}'],
        ),
        steps=[
            *ogr2ogr(
                input_file='{input_dir}/glacier_terminus.' + str(START) + '_' + str(END),
                output_file='{output_dir}/boundary.gpkg',
            ),
        ],

    )
    for (START, END) in LAYER_YEARS
]
from qgreenland.config.datasets.glacier_terminus import glacier_terminus as dataset
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


START = 2005
END = 2017

LAYER_YEARS = [
    (2000, 2001),
    *[
        (START, START + 1)
        for year in range(2005, 2017 + 1)
    ],
]

layers = [
    ConfigLayer(
        id=f'glacier_terminus_{START}_{END}',
        title=f'Glacier termini {START} to {END}',
        description='',
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

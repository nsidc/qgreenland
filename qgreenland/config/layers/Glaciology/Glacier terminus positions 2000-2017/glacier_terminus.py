from qgreenland.config.datasets.glacier_terminus import datasets as dataset
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


LAYER_YEARS = [
    (2000, 2001),
    *[
        (start_year, start_year+1)
        for year in range(2005, 2017+1)
    ],
] 

layers = [
    ConfigLayer(
        id = f'glacier_terminus_{start_year}_{end_year}',
        title  = f'Glacier termini {start_year} to {end_year}',
        description = '',
        tags = [],
        input=ConfigLayerInput(
            dataset=dataset,
            asset=dataset.assets[f'{start_year}_{end_year}'],
        ),
        steps=[
            *ogr2ogr(
                input_file='{input_dir}/glacier_terminus.' + start_year + '_' + end_year,
                output_file='{output_dir}/boundary.gpkg',
            ),
        ],

    )
    for (start_year, end_year) in LAYER_YEARS
]

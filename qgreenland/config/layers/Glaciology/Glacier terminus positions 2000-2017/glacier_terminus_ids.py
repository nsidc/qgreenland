from qgreenland.config.datasets.glacier_terminus import datasets as dataset
from qgreenland.config.helpers.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


glacier_terminus_glacier_ids = ConfigLayer(
    id='glacier_terminus_glacier_ids',
    title='Glacier IDs',
    description=(
        """"""
    ),
    tags=[],
    style='glacier_ids',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['glacier_ids'],
    ),
    steps=[
        *ogr2ogr(
                input_file='{input_dir}/glacier_terminus.glacier_ids,
                output_file='{output_dir}/boundary.gpkg',
            ),
    ],
)
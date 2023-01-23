from qgreenland.config.datasets.glacier_terminus import glacier_terminus as dataset
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import Layer, LayerInput

glacier_terminus_glacier_ids = Layer(
    id="glacier_terminus_glacier_ids",
    title="Glacier IDs",
    description="Glacier location for termini with matching ID.",
    tags=[],
    style="glacier_ids",
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets["glacier_ids"],
    ),
    steps=[
        *ogr2ogr(
            input_file="{input_dir}/GlacierIDs_v02.0.shp",
            output_file="{output_dir}/boundary.gpkg",
        ),
    ],
)

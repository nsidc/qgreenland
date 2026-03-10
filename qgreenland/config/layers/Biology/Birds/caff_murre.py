from qgreenland.config.datasets.caff import caff_murre_colonies as dataset
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.models.config.layer import Layer, LayerInput

murre_layer = Layer(
    id="caff_murre_colonies",
    title="Murre colonies",
    description=("""Point locations of thick-billed and common Murre colonies."""),
    tags=[],
    style="caff_murre_colonies",
    inputs=[
        LayerInput(
            dataset=dataset,
            asset=dataset.assets["only"],
        )
    ],
    steps=[
        *compressed_vector(
            input_file="{input_dir}/MurreColonies.zip",
            output_file="{output_dir}/final.gpkg",
            vector_filename=("MurreColonies.shp"),
        ),
    ],
)

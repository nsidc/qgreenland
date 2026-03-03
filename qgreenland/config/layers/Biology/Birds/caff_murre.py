from qgreenland.config.datasets.caff import caff_murre_colonies as dataset
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.models.config.layer import Layer, LayerInput


murre_layer = Layer(
    id="caff_murre_colonies",
    title='Murre colonies 2010',
    description=(
        f"""Point locations of Murre colonies as surveyed in
        2010."""
    ),
    tags=[],
    # TODO: come back to this.
    # style=f"murre_colonies",
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets["only"],
    ),
    steps=[
        *compressed_vector(
            input_file="{input_dir}/MurreColonies.zip",
            output_file="{output_dir}/final.gpkg",
            vector_filename=(
                'MurreColonies.shp'
            ),
        ),
    ],
)

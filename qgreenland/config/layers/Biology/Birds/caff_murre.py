from qgreenland.config.datasets.caff import caff_murre_colonies as dataset
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.models.config.layer import Layer, LayerInput

murre_layers = {
    "common_murre": {
        "name": "Common Murre",
    },
    "thickbilled_murre": {
        "name": "Thickbilled Murre",
    },
}

layers = [
    Layer(
        id=f"caff_{key}_colonies",
        title=f'{params["name"]} colonies 2010',
        description=(
            f"""Point locations of {params['name']} colonies as surveyed in
            2010."""
        ),
        tags=[],
        style=f"{key}_colonies",
        input=LayerInput(
            dataset=dataset,
            asset=dataset.assets["only"],
        ),
        steps=[
            *compressed_vector(
                input_file="{input_dir}/Murres_distribution.zip",
                output_file="{output_dir}/final.gpkg",
                vector_filename=(
                    f'Distribution_{params["name"].replace(" ", "_")}_Colonies.shp'
                ),
            ),
        ],
    )
    for key, params in murre_layers.items()
]

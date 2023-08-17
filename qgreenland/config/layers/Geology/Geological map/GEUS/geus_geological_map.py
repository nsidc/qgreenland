from qgreenland.config.datasets.online import geus_geological_map as dataset
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.config.helpers.steps.decompress import decompress_step
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput

LAYER_PARAMS = {
    "g500_rivers_arc": {
        "description": ("""TBD."""),
    },
    "g500_geology_trends": {
        "description": ("""TBD."""),
    },
    "g500_contours_arc": {
        "description": ("""TBD."""),
    },
    "g500_geology_arcs": {
        "description": ("""TBD."""),
    },
    "g500_geology_polygon": {
        "description": ("""TBD."""),
    },
}


def make_layer(*, layer_id: str, layer_params: dict) -> Layer:
    return Layer(
        id=layer_id,
        # TODO: better title.
        title=layer_id,
        description=layer_params["description"],
        tags=[],
        style=layer_id,
        input=LayerInput(
            dataset=dataset,
            asset=dataset.assets["offline"],
        ),
        steps=[
            # The dataset comes as a zipfile
            decompress_step(
                input_file="{input_dir}/Map.zip",
            ),
            # The zipfile contains an Esri map package (`.mpkx`), which is a
            # 7zipped archive containing a file geodatabase (`.gdb`) with vector
            # layers we are interested in.
            *compressed_vector(
                input_file="{input_dir}/G500_version_2023.mpkx",
                output_file="{output_dir}/" + f"{layer_id}.gpkg",
                boundary_filepath=project.boundaries["background"].filepath,
                decompress_step_kwargs={
                    "decompress_contents_mask": "p20/g500_2023_pro.gdb/*",
                    "decompress_type": "7z",
                },
                vector_filename=f"p20/g500_2023_pro.gdb {layer_id}",
            ),
        ],
    )


# TODO: settings for layer order.
layers = [
    make_layer(layer_id=layer_id, layer_params=layer_params)
    for layer_id, layer_params in LAYER_PARAMS.items()
]

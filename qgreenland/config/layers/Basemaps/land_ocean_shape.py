from qgreenland.config.datasets.land_ocean_shape import land_shape as dataset_land
from qgreenland.config.datasets.land_ocean_shape import ocean_shape as dataset_ocean
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.models.config.layer import Layer, LayerInput


layer_params = {
    'land': dataset_land,
    'ocean': dataset_ocean,
}


def make_land_ocean_layer(layer_id: str) -> Layer:
    return Layer(
        id=layer_id,
        title=layer_id.capitalize(),
        description=(
            f"""Polygons representing the {layer_id}."""
        ),
        tags=[],
        style=layer_id,
        input=LayerInput(
            dataset=layer_params[layer_id],
            asset=layer_params[layer_id].assets['only'],
        ),
        steps=[
            *compressed_vector(
                input_file='{input_dir}/' + f'ne_10m_{layer_id}.zip',
                output_file='{output_dir}/final.gpkg',
            ),
        ],
    )


layers = [
    make_land_ocean_layer(layer_id)
    for layer_id in layer_params.keys()
]

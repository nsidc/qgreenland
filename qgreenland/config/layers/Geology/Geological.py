from qgreenland.config.datasets.geological_map import geological_map as dataset_geo_map
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


layer_params = {
    'greenland_ice': dataset_geo_map,
    'bathymetry': dataset_geo_map,
    'greenland_onshore': dataset_geo_map,
    'greenland_onshore_pattern': dataset_geo_map,
    'greenland_onshore_planar': dataset_geo_map,
}


def make_geo_layer(layer_id:str) -> ConfigLayer:
    return ConfigLayer(
        id=layer_id,
        title=layer_id.capitalize(),
        description=(
            """ """
        ),
        tags=[],
        # TODO: export stylesheet
        # style='ice_isopachs',
        input=ConfigLayerInput(
            dataset=layer_params[layer_id],
            asset=layer_params[layer_id].assets['only'],
        ),
        steps=[
            *compressed_vector(
                input_file='{input_dir}/as_2159.zip',
                decompress_step_kwargs={
                    'decompress_contents_mask': f'data/shape/*/{layer_id}.*',
                },
                output_file='{output_dir}/final.gpkg',
                vector_filename=f'data/shape/*/{layer_id}.shp',
            ),
        ],
    )


layers = [
    make_geo_layer(layer_id)
    for layer_id in layer_params.keys()
]

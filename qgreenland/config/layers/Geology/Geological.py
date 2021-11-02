from qgreenland.config.datasets.greenland_ice import greenland_ice as dataset_greenland_ice
from qgreenland.config.datasets.bathymetry import bathymetry as dataset_bathymetry
from qgreenland.config.datasets.greenland_onshore import greenland_onshore as dataset_onshore
from qgreenland.config.datasets.greenland_onshore_pattern import greenland_onshore_pattern as dataset_onshore_pattern
from qgreenland.config.datasets.greenland_onshore_planar import greenland_onshore_planar as dataset_onshore_planar
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


layer_params = {
    'greenland_ice': dataset_greenland_ice,
    'bathymetry': dataset_bathymetry,
    'greenland_onshore': dataset_onshore,
    'greenland_onshore_pattern': dataset_onshore_pattern,
    'greenland_onshore_planar': dataset_onshore_planar,
}


def make_geo_layer(layer_id:str) -> ConfigLayer:
    return ConfigLayer(
        id=layer_id,
        title=str(layer_id).capitalize(),
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

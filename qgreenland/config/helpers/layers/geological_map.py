from qgreenland.config.datasets.geological_map import geological_map as dataset
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


LAYER_PARAMS = {
    'onshore_planar_geological_map': {
        'title': 'Faults',
        'description': (
            """Onshore faults for the landmass and islands of Greenland."""
        ),
        'style': 'onshore_planar_geological_map',
        'input_filepath': 'data/shape/geology/Greenland_onshore_planar',
        'fn_mask': 'Greenland_onshore_Planar.*',
    },
    'onshore_geological_map': {
        'title': 'Rock types',
        'description': (
            """Geological unit polygon features for the onshore landmass and
            islands of Greenland."""
        ),
        'style': 'geological_map_polygons',
        'input_filepath': 'data/shape/geology/Greenland_onshore',
        'fn_mask': 'Greenland_onshore.*',
    },
    'greenland_ice': {
        'title': 'Ice thickness contours',
        'description': (
            """This linear feature class contains onshore ice isopachs for the landmass of Greenland.
        The isopochs illustrate the variation in ice thickness
        with a contour interval of 250 metres."""
        ),
        'style': 'greenland_ice',
        'input_filepath': 'data/shape/base/Greenland_ice',
        'fn_mask': 'Greenland_ice.*',
    },
}


def make_layer(*, layer_id: str, layer_params: dict) -> ConfigLayer:
    return ConfigLayer(
        id=layer_id,
        title=layer_params['title'],
        description=layer_params['description'],
        tags=[],
        style=layer_params['style'],
        input=ConfigLayerInput(
            dataset=dataset,
            asset=dataset.assets['only'],
        ),
        steps=[
            *compressed_vector(
                input_file='{input_dir}/as_2159.zip',
                output_file='{output_dir}/final.gpkg',
                boundary_filepath=project.boundaries['background'].filepath,
                decompress_step_kwargs={
                    'decompress_contents_mask':
                        layer_params['input_filepath'] + '.*',
                },
                vector_filename=layer_params['input_filepath'] + '.shp',
            ),
        ],
    )

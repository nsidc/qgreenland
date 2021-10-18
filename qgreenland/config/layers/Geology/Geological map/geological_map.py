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
        'fn_mask': 'Greenland_onshore_Planar.*',
    },
    'onshore_geological_map': {
        'title': 'Rock types',
        'description': (
            """Geological unit polygon features for the onshore landmass and
            islands of Greenland."""
        ),
        'style': 'geological_map_polygons',
        'fn_mask': 'Greenland_onshore.*',
    },
}

layers = [
    ConfigLayer(
        id=key,
        title=params['title'],
        description=params['description'],
        tags=[],
        style=params['style'],
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
                        f'data/shape/geology/{params["fn_mask"]}',
                },
                vector_filename='data/shape/geology/*.shp',
            ),
        ],
    )
    for key, params in LAYER_PARAMS.items()
]

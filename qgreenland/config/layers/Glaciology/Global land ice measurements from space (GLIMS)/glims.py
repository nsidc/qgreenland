from qgreenland.config.datasets.glims import glims as dataset
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


LAYER_PARAMS = {
    'points': {
        'hint': 'locations',
        'description': (
            """Points representing GLIMS glaciers and locations of interest."""
        ),
    },
    'polygons': {
        'hint': 'outlines',
        'description': (
            """Polygons represent GLIMS features, typically glacier outlines, but
            also including regions of glacial lakes, debris cover, rocks within the
            glacier (nunataks), and other polygonal features."""
        ),
    },
}

layers = [
    ConfigLayer(
        id=f'glims_{key}',
        title=f'Peripherical glacier/feature {params["hint"]}',
        description=params['description'],
        tags=[],
        input=ConfigLayerInput(
            dataset=dataset,
            asset=dataset.assets['only'],
        ),
        steps=[
            *compressed_vector(
                input_file='{input_dir}/*.zip',
                output_file='{output_dir}/final.gpkg',
                boundary_filepath=project.boundaries['data'].filepath,
                decompress_step_kwargs={
                    'decompress_contents_mask': \
                        f'glims_download_82381/*_{key}.*',
                },
                vector_filename='glims_download_82381/*.shp',
            ),
        ],
    )
    for key, params in LAYER_PARAMS.items()
]

from qgreenland.config.datasets.undersea_features import (
    undersea_features as dataset,
)
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


# Note: source zipfile for undersea features data also has 'multipoint'
# shapefile that only contains data outside of the project extent.
LAYER_PARAMS = {
    'point': {
        'title': 'Point locations',
        'description': (
            """Points representing undersea features."""
        ),
        'style': 'Undersea_Points',
        'extra_ogr2ogr_args': [],
    },
    'multilinestring': {
        'title': 'Linear features',
        'description': (
            """Lines representing undersea features."""
        ),
        'style': 'Undersea_Linear',
        'extra_ogr2ogr_args': [],
    },
    'multipolygon': {
        'title': 'Shapes',
        'description': (
            """Polygons representing undersea features."""
        ),
        'style': 'Undersea_Shapes',
        # Prevent polygon from being turned in to a linestring during clip:
        'extra_ogr2ogr_args': ['-nlt', 'POLYGON'],
    },
}


layers = [
    ConfigLayer(
        id=f'undersea_features_{key}',
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
                input_file='{input_dir}/features.zip',
                output_file='{output_dir}/final.gpkg',
                boundary_filepath=project.boundaries['background'].filepath,
                decompress_step_kwargs={
                    'decompress_contents_mask':
                        f'features/features-{key}.*',
                },
                vector_filename=f'features/features-{key}.shp',
                ogr2ogr_args=(
                    *params['extra_ogr2ogr_args'],
                    '-sql', (
                        f"""'SELECT *, name as label
                        FROM "features-{key}"'"""
                    ),
                ),
            ),
        ],
    )
    for key, params in LAYER_PARAMS.items()
]

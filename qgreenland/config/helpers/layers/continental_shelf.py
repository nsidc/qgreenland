from qgreenland.config.datasets.continental_shelf import continental_shelf as dataset
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.config.project import project
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.models.config.layer import Layer, LayerInput


LAYER_PARAMS = {
    'north_points': {
        'title': 'Continental shelf points (north)',
        'description': (
            """Northern continental shelf of Greenland."""
        ),
        'layer_id': 'north_points',
    },
    'north_lines': {
        'title': 'Continental shelf lines (north)',
        'description': (
            """Northern continental shelf of Greenland."""
        ),
        'layer_id': 'north_lines',
    },
    'north_polygons': {
        'title': 'Continental shelf poloygons (north)',
        'description': (
            """Northern continental shelf of Greenland."""
        ),
        'layer_id': 'north_polygons',
    },
    'northeast_points': {
        'title': 'Continental shelf (northeast)',
        'description': (
            """Northeastern continental shelf of Greenland."""
        ),
        'layer_id': 'northeast_points',
    },
    'northeast_lines': {
        'title': 'Continental shelf (northeast)',
        'description': (
            """Northeastern continental shelf of Greenland."""
        ),
        'layer_id': 'northeast_lines',
    },
    'northeast_polygons': {
        'title': 'Continental shelf (northeast)',
        'description': (
            """Northeastern continental shelf of Greenland."""
        ),
        'layer_id': 'northeast_polygons',
    },
    'south_points': {
        'title': 'Continental shelf (south)',
        'description': (
            """Southern continental shelf of Greenland."""
        ),
        'layer_id': 'south_points',
    },
    'south_lines': {
        'title': 'Continental shelf (south)',
        'description': (
            """Southern continental shelf of Greenland."""
        ),
        'layer_id': 'south_lines',
    },
    'south_polygons': {
        'title': 'Continental shelf (south)',
        'description': (
            """Southern continental shelf of Greenland."""
        ),
        'layer_id': 'south_polygons',
    },
}


def make_layers() -> list[Layer]:
    return [
        Layer(
            id=key,
            title=params['title'],
            description=params['description'],
            tags=[],
            input=LayerInput(
                dataset=dataset,
                asset=dataset.assets[params['layer_id']],
            ),
            steps=[
                *compressed_vector(
                    input_file='{input_dir}/*.shp',
                    output_file='{output_dir}/final.gpkg',
                ),
                *ogr2ogr(
                    input_file='{input_dir}/*.shp',
                    output_file='{output_dir}/final.gpkg',
                    boundary_filepath=project.boundaries['background'].filepath,
                ),
            ],
        ) for key, params in LAYER_PARAMS.items()
    ]

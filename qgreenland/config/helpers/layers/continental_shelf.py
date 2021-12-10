from qgreenland.config.datasets.continental_shelf import continental_shelf as dataset
from qgreenland.config.helpers.steps.ogr2ogr import STANDARD_OGR2OGR_ARGS
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep


LAYER_PARAMS = {
    'north_points': {
        'title': 'North (points)',
        'description': (
            """Northern continental shelf of Greenland."""
        ),
    },
    'north_lines': {
        'title': 'North (lines)',
        'description': (
            """Northern continental shelf of Greenland."""
        ),
    },
    'north_polygons': {
        'title': 'North (poloygons)',
        'description': (
            """Northern continental shelf of Greenland."""
        ),
    },
    'northeast_points': {
        'title': 'Northeast (points)',
        'description': (
            """Northeastern continental shelf of Greenland."""
        ),
    },
    'northeast_lines': {
        'title': 'Northeast (lines)',
        'description': (
            """Northeastern continental shelf of Greenland."""
        ),
    },
    'northeast_polygons': {
        'title': 'Northeast (polygons)',
        'description': (
            """Northeastern continental shelf of Greenland."""
        ),
    },
    'south_points': {
        'title': 'South (points)',
        'description': (
            """Southern continental shelf of Greenland."""
        ),
    },
    'south_lines': {
        'title': 'South (lines)',
        'description': (
            """Southern continental shelf of Greenland."""
        ),
    },
    'south_polygons': {
        'title': 'South (polygons)',
        'description': (
            """Southern continental shelf of Greenland."""
        ),
    },
}


def make_layers() -> list[Layer]:
    return [
        Layer(
            id=f'continental_shelf_{key}',
            title=params['title'],
            description=params['description'],
            tags=[],
            input=LayerInput(
                dataset=dataset,
                asset=dataset.assets[key],
            ),
            steps=[
                CommandStep(
                    args=[
                        'unzip',
                        '{input_dir}/*.zip',
                        '-d',
                        '{output_dir}',
                    ],
                ),
                CommandStep(
                    args=[
                        'ogr2ogr',
                        *STANDARD_OGR2OGR_ARGS,
                        '-makevalid',
                        '{output_dir}/final.gpkg',
                        '{input_dir}/*.shp',
                    ],
                ),
            ],
        ) for key, params in LAYER_PARAMS.items()
    ]

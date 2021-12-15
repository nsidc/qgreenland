from qgreenland.config.datasets.continental_shelf import continental_shelf as dataset
from qgreenland.config.helpers.steps.ogr2ogr import STANDARD_OGR2OGR_ARGS
from qgreenland.config.helpers.steps.decompress import decompress_step
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep


LAYER_PARAMS = {
    'north_points': {
        'title': 'North (points)',
        'description': (
            """Points representing the boundary of the Northern extended continental shelf
            of Greenland."""
        ),
    },
    'north_lines': {
        'title': 'North (lines)',
        'description': (
            """Lines representing the boundary of the Northern extended continental shelf of
            Greenland."""
        ),
    },
    'north_polygons': {
        'title': 'North (poloygons)',
        'description': (
            """Polygons representing the area between the Greenland Exclusive
            Economic Zone and the Northern Continental Shelf."""
        ),
    },
    'northeast_points': {
        'title': 'Northeast (points)',
        'description': (
            """Points representing the boundary of the Northeastern extended continental shelf
            of Greenland."""
        ),
    },
    'northeast_lines': {
        'title': 'Northeast (lines)',
        'description': (
            """Lines representing the boundary of the Northeastern extended continental shelf
            of Greenland."""
        ),
    },
    'northeast_polygons': {
        'title': 'Northeast (polygons)',
        'description': (
            """Polygons representing the area between the Greenland Exclusive
            Economic Zone and the Northeastern Continental Shelf."""
        ),
    },
    'south_points': {
        'title': 'South (points)',
        'description': (
            """Points representing the boundary of the Southern extended continental shelf
            of Greenland."""
        ),
    },
    'south_lines': {
        'title': 'South (lines)',
        'description': (
            """Lines representing the boundary of the Southern extended continental shelf of
            Greenland."""
        ),
    },
    'south_polygons': {
        'title': 'South (polygons)',
        'description': (
            """Polygons representing the area between the Greenland Exclusive
            Economic Zone and the Southern Continental Shelf."""
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
                decompress_step(
                    input_file='{input_dir}/*.zip',
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

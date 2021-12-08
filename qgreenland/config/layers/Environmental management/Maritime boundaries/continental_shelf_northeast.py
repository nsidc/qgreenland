from qgreenland.config.datasets.continental_shelf_northeast import (
    northeast_lines as lines_dataset,
    northeast_points as points_dataset,
    northeast_polygons as polygons_dataset,
)
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput


LINE_FILE = 'Greenland_North_Lines.shp'
POINT_FILE = 'Greenland_North_Points.shp'
POLYGON_FILE = 'Greenland_North_Polygons.shp'
LAYER_PARAMS = {
    'continental_shelf_northeast_line': {
        'title': 'Northeast (polyline)',
        'description': (
            """ """
        ),
        'input_filename': LINE_FILE,
        'layer_name': 'Northeast (polyline)',
        'dataset': lines_dataset,
    },
    'continental_shelf_northeast_point': {
        'title': 'Northeast (point)',
        'description': (
            """ """
        ),
        'input_filename': POINT_FILE,
        'layer_name': 'Northeast (point)',
        'dataset': points_dataset,
    },
    'continental_shelf_northeast_polygon': {
        'title': 'Northeast (polygon)',
        'description': (
            """ """
        ),
        'input_filename': POLYGON_FILE,
        'layer_name': 'Northeast (polygon)',
        'dataset': polygons_dataset,
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
                dataset=params['dataset'],
                asset=params['dataset'].assets['only'],
            ),
            steps=[
                *ogr2ogr(
                    input_file='{input_dir}/' + params['input_filename'],
                    output_file='{output_dir}/final.gpkg',
                    boundary_filepath=project.boundaries['background'].filepath,
                    ogr2ogr_args=[
                        '-where',
                        f'"\"layer\" = \'{params["layer_name"]}\'"',
                    ],
                ),
            ],
        )
        for key, params in LAYER_PARAMS.items()
    ]

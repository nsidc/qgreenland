from qgreenland.config.datasets.continental_shelf import (
    continental_shelf as dataset,
)
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput


POLYLINE_FILE = 'Greenland_South_Lines.shp'
POINT_FILE = 'Greenland_South_Points.shp'
POLYGON_FILE = 'Greenland_South_Polygons.shp'
LAYER_PARAMS = {
    'continental_shelf_south_line': {
        'title': 'South (polyline)',
        'description': (
            """ """
        ),
        'input_filename': POLYLINE_FILE,
        'layer_name': 'South (polyline)',
    },
    'continental_shelf_south_point': {
        'title': 'South (point)',
        'description': (
            """ """
        ),
        'input_filename': POINT_FILE,
        'layer_name': 'South (point)',
    },
    'continental_shelf_south_polygon': {
        'title': 'South (polygon)',
        'description': (
            """ """
        ),
        'input_filename': POLYGON_FILE,
        'layer_name': 'South (polygon)',
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
                asset=dataset.assets['only'],
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
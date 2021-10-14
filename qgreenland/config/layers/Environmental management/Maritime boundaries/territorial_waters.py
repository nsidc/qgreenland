from qgreenland.config.datasets.greenland_territorial_waters import (
    greenland_territorial_waters as dataset,
)
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


POLYLINE_FILE = 'GreenlandTerritory_Baseline_3NM_12NM_EEZ_polylines.shp'
POLYGON_FILE = 'GreenlandTerritory_Baseline_3NM_12NM_EEZ_polygons.shp'
LAYER_PARAMS = {
    'exclusive_economic_zone': {
        'title': 'Exclusive economic zone (polyline)',
        'description': (
            """Exclusive Economic Zone of Greenland based on Executive Order on the
            Exclusive Economic Zone at Greenland. BEK no. 1020 of 20/10/2004.
            Foreign Ministry of Denmark."""
        ),
        'input_filename': POLYLINE_FILE,
        'layer_name': 'Boundary_EEZ',
    },
    'baseline': {
        'title': 'Baseline (polyline)',
        'description': (
            """The territorial sea baseline is shown in accordance to Executive
            Order no 1004 dated 15.10.2004."""
        ),
        'input_filename': POLYLINE_FILE,
        'layer_name': 'Boundary_baseline',
    },
    '3nm_polyline': {
        'title': '3NM (polyline)',
        'description': (
            """Reference to Inatsisartut Act no. 15 of 18 June 2017 on protection of
            the marine environment, paragraph 4, 2. NM = nautical mile."""
        ),
        'input_filename': POLYLINE_FILE,
        'layer_name': 'Boundary_3NM',
    },
    '12nm_polyline': {
        'title': '12NM (polyline)',
        'description': (
            """Fishery limit. Regarding the fishery limit, reference is made to
            Greenland Home Rule Parliament Act no 18 dated 31.10.1996, paragraph 7,
            2. NM = nautical mile."""
        ),
        'input_filename': POLYLINE_FILE,
        'layer_name': 'Boundary_12NM',
    },
    '3nm_polygon': {
        'title': '3NM (polygon)',
        'description': (
            """Reference to Inatsisartut Act no. 15 of 18 June 2017 on protection of
            the marine environment, paragraph 4, 2. NM = nautical mile."""
        ),
        'input_filename': POLYGON_FILE,
        'layer_name': 'Boundary_3NM_area',
    },
    'fishzone_boundary': {
        'title': 'Fishing zone (polygon)',
        'description': (
            """Fishery limit. Regarding the fishery limit, reference is made to
            Greenland Home Rule Parliament Act no 18 dated 31.10.1996"""
        ),
        'input_filename': POLYGON_FILE,
        'layer_name': 'Boundary_fishzone',
    },
}


layers = [
    ConfigLayer(
        id=key,
        title=params['title'],
        description=params['description'],
        tags=[],
        input=ConfigLayerInput(
            dataset=dataset,
            asset=dataset.assets['only'],
        ),
        steps=[
            *ogr2ogr(
                input_file='{input_dir}/' + params['input_filename'],
                output_file='{output_dir}/final.gpkg',
                boundary_filepath=project.boundaries['boundary'].filepath,
                ogr2ogr_args=(
                    '-where',
                    f'"\"layer\" = \'{params["layer_name"]}\'"',
                ),
            ),
        ],
    )
    for key, params in LAYER_PARAMS.items()
]

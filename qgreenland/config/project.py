from qgreenland.config.constants import PROJECT_CRS
from qgreenland.constants import ASSETS_DIR, PROJECT_DIR
from qgreenland.models.config.project import ConfigProject

project = ConfigProject(
    crs=PROJECT_CRS,
    boundaries={
        'background': {
            'filepath': '{assets_dir}/latitude_shape_40_degrees.geojson',
        },
        'data': {
            'filepath': '{assets_dir}/greenland_rectangle.geojson',
        },
    },
)

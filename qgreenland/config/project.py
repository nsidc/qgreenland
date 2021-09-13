from qgreenland.config.constants import PROJECT_CRS
from qgreenland.constants import ASSETS_DIR, PROJECT_DIR
from qgreenland.models.config.project import ConfigProject

project = ConfigProject(
    crs=PROJECT_CRS,
    boundaries={
        'background': {
            'filepath': (
                ASSETS_DIR / 'latitude_shape_40_degrees.geojson'
            ).relative_to(PROJECT_DIR),
        },
        'data': {
            'filepath': (
                ASSETS_DIR / 'greenland_rectangle.geojson'
            ).relative_to(PROJECT_DIR),
        },
    },
)

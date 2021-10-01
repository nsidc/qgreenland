from qgreenland.config.constants import PROJECT_CRS
from qgreenland.constants import ASSETS_DIR
from qgreenland.models.config.project import ConfigProject

project = ConfigProject(
    crs=PROJECT_CRS,
    boundaries={
        'background': {
            'filepath': f'{ASSETS_DIR}/latitude_shape_40_degrees.geojson',  # noqa: FS003
        },
        'data': {
            'filepath': f'{ASSETS_DIR}/greenland_rectangle.geojson',  # noqa: FS003
        },
    },
)

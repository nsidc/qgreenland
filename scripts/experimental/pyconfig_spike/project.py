from scripts.experimental.pyconfig_spike.config_constants import PROJECT_CRS
from qgreenland.models.config.project import ConfigBoundariesInfo, ConfigProject
from qgreenland.constants import ASSETS_DIR

project = ConfigProject(
    crs=PROJECT_CRS,
    boundaries={
        'background': {'fp': ASSETS_DIR / 'latitude_shape_40_degrees.geojson'},
        'data': {'fp': ASSETS_DIR / 'greenland_rectangle.geojson'}
    }
)

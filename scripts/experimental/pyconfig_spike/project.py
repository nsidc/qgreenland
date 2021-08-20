from qgreenland.models.config.project import ConfigBoundariesInfo, ConfigProject
from qgreenland.constants import ASSETS_DIR

project = ConfigProject(
    crs='EPSG:3413',
    boundaries={
        'background': {'fp': ASSETS_DIR / 'latitude_shape_40_degrees.geojson'}
    }
)

print(project.json(indent=4))

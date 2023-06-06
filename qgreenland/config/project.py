from qgreenland.config.constants import PROJECT_CRS
from qgreenland.models.config.project import Project

project = Project(
    crs=PROJECT_CRS,
    boundaries={
        "background": {
            "filepath": "{assets_dir}/latitude_shape_40_degrees.geojson",
        },
        "data": {
            "filepath": "{assets_dir}/greenland_rectangle.geojson",
        },
    },
)

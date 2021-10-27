from qgreenland.config.datasets.soil_types import soil_types as dataset
from qgreenland.config.helpers.steps.decompress import decompress_step
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


soil_types = ConfigLayer(
    id='soil_types',
    title='Soil characteristics',
    description=(
        """Polygons representing dominant soil characteristics with percentage
        polygon area for each soil type. Data coverage limited to Greenland."""
    ),
    tags=[],
    style='soil_types',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        decompress_step(
            decompress_type='gzip',
            input_file='{input_dir}/*.gz',
        ),
        *ogr2ogr(
            input_file='{input_dir}/ggd602_soils_greenland.shp',
            output_file='{output_dir}/soil_types.gpkg',
            boundary_filepath=project.boundaries['data'].filepath,
            ogr2ogr_args=(
                '-s_srs',
                '"+proj=laea +a=6370997.00 +b=6370997.00 +lat_0=90 +lon_0=180 +x_0=0 +y_0=0"',
            ),
        ),
    ],
)

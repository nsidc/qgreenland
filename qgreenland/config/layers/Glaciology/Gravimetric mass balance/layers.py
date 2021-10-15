from qgreenland.config.datasets.esa_cci_gravimetric_mass_balance import esa_cci_gravimetric_mass_balance_dtu as dataset
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


esa_cci_gravimetric_mass_balance_dtu_2005 = ConfigLayer(
    id='esa_cci_gravimetric_mass_balance_dtu_2005',
    title='Mass balance trend 2003-2007',
    description=(
        """Trend derived from the period 2003-01-01 to 2007-12-31 via gravity
        measurements. Data is on a ~50 km resolution grid (displayed as
        points)."""
    ),
    tags=[],
    style='gmb_dtu_space',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        *ogr2ogr(
            input_file='{input_dir}/QGREENLAND_GEOPACKAGES/points_2003-01-01_2007-12-31.gpkg',
            output_file='{output_dir}/points_2003-01-01_2007-12-31.gpkg',
            boundary_filepath=project.boundaries['data'].filepath,
        ),
    ],
)

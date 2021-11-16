from qgreenland.config.datasets.arctic_dem import arctic_dem as dataset
from qgreenland.config.helpers.steps.build_overviews import build_overviews
from qgreenland.config.helpers.steps.compress_raster import compress_raster
from qgreenland.config.helpers.steps.gdal_edit import gdal_edit
from qgreenland.config.helpers.steps.warp import warp
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep


arctic_dem = Layer(
    id='arctic_dem',
    title='Arctic DEM (100m)',
    description=(
        """Surface elevation in meters using hillshade symbology."""
    ),
    tags=[],
    style='arctic_dem',
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets['100m'],
    ),
    steps=[
        *warp(
            input_file='{input_dir}/arcticdem_mosaic_100m_v3.0.tif',
            output_file='{output_dir}/arctic_dem.tif',
            cut_file=project.boundaries['data'].filepath,
        ),
        CommandStep(
            args=[
                'gdal_calc.py',
                '--calc', '"A * 100.0"',
                '--NoDataValue', '-9999',
                '--type', 'Int32',
                '-A', '{input_dir}/arctic_dem.tif',
                '--outfile', '{output_dir}/arctic_dem_scaled.tif',
            ],
        ),
        *gdal_edit(
            input_file='{input_dir}/arctic_dem_scaled.tif',
            output_file='{output_dir}/arctic_dem.tif',
            gdal_edit_args=[
                '-scale', '0.01',
            ],
        ),
        *compress_raster(
            input_file='{input_dir}/arctic_dem.tif',
            output_file='{output_dir}/arctic_dem.tif',
        ),
        *build_overviews(
            input_file='{input_dir}/arctic_dem.tif',
            output_file='{output_dir}/arctic_dem.tif',
        ),
    ],
)

from qgreenland.config.datasets.bathymetric_chart import bathymetric_chart as dataset
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


bathymetric_chart = ConfigLayer(
    id='bathymetric_chart',
    title='Bathymetric chart of the Arctic Ocean (400m)',
    description=(
        """Bathymetric elevation in meters. Elevations can be assumed to be
        relative to mean sea level. However, in some shallow water areas, the
        grids include data from sources having a vertical datum other than mean
        sea level."""
    ),
    tags=[],
    style='ibcao_bathymetry',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        *warp_and_cut(
            input_file='NETCDF:{input_dir}/IBCAO_v4_400m_ice.nc:z',
            output_file='{output_dir}/bathymetric_chart.tif',
            reproject_args=(
                '-s_srs', '"+proj=stere +lat_0=90 +lat_ts=75 +datum=WGS84"',
                '-dstnodata', '-9999',
                '-tr', '400', '400',
            ),
            cut_file=project.boundaries['background'].filepath,
        ),
    ],
)

from qgreenland.config.datasets.bathymetric_chart import bathymetric_chart as dataset
from qgreenland.config.helpers.steps.build_overviews import build_overviews
from qgreenland.config.helpers.layers.geological_map import make_layers
from qgreenland.config.helpers.steps.warp import warp
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput


LAYER_PARAMS = {
    'bathymetric_raster': {
        'title': 'Raster (400m)',
        'description': (
            """Bathymetric elevation in meters. Elevations can be assumed to be
        relative to mean sea level. However, in some shallow water areas, the
        grids include data from sources having a vertical datum other than mean
        sea level."""
        ),
        'style': 'ibcao_bathymetry',
        'dataset': dataset,
        'fn_mask': 'bathymetry.*',
    },
}

layers = [
    ConfigLayer(
        id=key,
        title=params['title'],
        description=params['description'],
        tags=[],
        style=params['style'],
        input=ConfigLayerInput(
            dataset=params['dataset'],
            asset=dataset.assets['only'],
        ),
        steps=[
            *warp(
                input_file='NETCDF:{input_dir}/IBCAO_v4_400m_ice.nc:z',
                output_file='{output_dir}/bathymetric_chart.tif',
                warp_args=(
                    '-s_srs', '"+proj=stere +lat_0=90 +lat_ts=75 +datum=WGS84"',
                    '-dstnodata', '-9999',
                    '-tr', '400', '400',
                ),
                cut_file=project.boundaries['background'].filepath,
            ),
            *build_overviews(
                input_file='{input_dir}/bathymetric_chart.tif',
                output_file='{output_dir}/bathymetric_chart.tif',
            ),
        ],    
    )
    for key, params in LAYER_PARAMS.items()
    #geological_layers = make_layers()
]
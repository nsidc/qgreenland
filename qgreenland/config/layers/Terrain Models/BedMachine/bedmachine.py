from qgreenland.config.datasets import bedmachine
from qgreenland.config.helpers.steps.build_overviews import build_overviews
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput

bedmachine_fn = 'BedMachineGreenland-2021-04-20.nc'


bed_datasets = {
    'thickness': {
        'title': 'Ice thickness',
        'description': (
            """Ice thickness in meters. Mass conservation source data provided
            by Mathieu Morlighem."""
        ),
    },
    'surface': {
        'title': 'Surface elevation',
        'description': (
            """Surface elevation in meters. Source is GIMP DEM v2.1
            (http://bprc.osu.edu/GDG/gimpdem.php)"""
        ),
    },
    'bed': {
        'title': 'Bedrock elevation',
        'description': 'Bedrock elevation in meters.',
    },
    'errbed': {
        'title': 'Bedrock elevation/ice thickness error',
        'description': (
            """Error estimate for Greenland bed elevation and ice thickness in
            meters."""
        ),
    },
}

layers = [
    ConfigLayer(
        id=f'bedmachine_{key}',
        title=f'{params["title"]} (150m)',
        description=params['description'],
        tags=['terrain_model'],
        style=f'bedmachine_{key}',
        input=ConfigLayerInput(
            dataset=bedmachine.bedmachine,
            asset=bedmachine.bedmachine.assets['only'],
        ),
        steps=[
            *warp_and_cut(
                input_file='NETCDF:{input_dir}/' + f'{bedmachine_fn}:{key}',
                output_file='{output_dir}/warped_and_cut.tif',
                cut_file='{assets_dir}/greenland_rectangle.geojson',
            ),
            *build_overviews(
                input_file='{input_dir}/warped_and_cut.tif',
                output_file='{output_dir}/overviews.tif',
            ),
        ],
    )
    for key, params in bed_datasets.items()
]

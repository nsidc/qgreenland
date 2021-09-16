from qgreenland.config.datasets import bedmachine
from qgreenland.config.helpers.steps.build_overviews import build_overviews
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput

bedmachine_fn = 'BedMachineGreenland-2021-04-20.nc'


layers = [
    ConfigLayer(
        id='bedmachine_thickness',
        title='Ice thickness (150m)',
        description="""
Ice thickness in meters. Mass conservation source data provided by Mathieu
Morlighem.""",
        tags=['terrain_model'],
        show=False,
        style='bedmachine_thickness',
        in_package=True,
        input=ConfigLayerInput(
            dataset=bedmachine.bedmachine,
            asset=bedmachine.bedmachine.assets['only'],
        ),
        steps=[
            *warp_and_cut(
                input_file='NETCDF:{input_dir}/' + f'{bedmachine_fn}:thickness',
                output_file='{output_dir}/warped_and_cut.tif',
                cut_file='{assets_dir}/greenland_rectangle.geojson',
            ),
            *build_overviews(
                input_file='{input_dir}/warped_and_cut.tif',
                output_file='{output_dir}/overviews.tif',
            ),
        ],
    ),
]

# TODO: Finish bedmachine!
"""
- &bedmachine
  id: bedmachine_thickness
  title: 'Ice thickness (150m)'
  description: >-
    Ice thickness in meters. Mass conservation source data provided by Mathieu
    Morlighem.
  hierarchy: ['Terrain models', 'BedMachine']
  show: False
  style: 'bedmachine_thickness'
  in_package: True
  input:
    dataset: bedmachine
    asset: only
  steps:
    - type: 'template'
      template_name: 'extract_nc_dataset'
      kwargs:
        # TODO: All templates have input and output files. Promote to top-level
        # step key?
        input_file: '{input_dir}/BedMachineGreenland-2017-09-20.nc'
        output_file: '{output_dir}/thickness.tif'
        variable: 'thickness'

    # TODO: re-use warp_and_cut template with conditonal args.
    - type: 'command'
      args:
        - 'gdalwarp'
        - '-t_srs'
        - 'EPSG:3413'
        - '{input_dir}/thickness.tif'
        - '{output_dir}/warped.tif'
    - type: 'command'
      args:
        - 'gdalwarp'
        - '-cutline'
        - '{assets_dir}/greenland_rectangle.geojson'
        - '-crop_to_cutline'
        - '-co'  # creationOptions=['COMPRESS=DEFLATE']
        - 'COMPRESS=DEFLATE'
        - '{input_dir}/warped.tif'  # <--- Input
        - '{output_dir}/warped_and_cut.tif'  # <--- Output

    - type: 'template'
      template_name: 'build_overviews'
      kwargs:
        input_file: '{input_dir}/warped_and_cut.tif'
        output_file: '{output_dir}/overviews.tif'


# - <<: *bedmachine
#   id: bedmachine_surface
#   title: 'Surface elevation (150m)'
#   description: >-
#       Surface elevation in meters. Source is GIMP DEM v2.1
#       (http://bprc.osu.edu/GDG/gimpdem.php)
#   style: 'bedmachine_surface'
#   # extract_nc_dataset_kwargs:
#   #   extract_dataset: 'surface'
#
# - <<: *bedmachine
#   id: bedmachine_bed
#   title: 'Bedrock elevation (150m)'
#   description: >-
#     Bedrock elevation in meters.
#   style: 'bedmachine_bed'
#   # extract_nc_dataset_kwargs:
#   #   extract_dataset: 'bed'
#
# - <<: *bedmachine
#   id: bedmachine_errbed
#   title: 'Bedrock elevation/ice thickness error (150m)'
#   description: >-
#     Error estimate for Greenland bed elevation and ice thickness in meters.
#   style: 'bedmachine_errbed'
#   # extract_nc_dataset_kwargs:
#   #   extract_dataset: 'errbed'
"""
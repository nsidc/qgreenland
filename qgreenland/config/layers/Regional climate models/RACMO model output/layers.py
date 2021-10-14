from qgreenland.config.datasets.racmo import racmo_qgreenland_jan2021 as dataset
from qgreenland.config.helpers.steps.build_overviews import build_overviews
from qgreenland.config.helpers.steps.decompress import decompress_step
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.helpers.steps.zipped_vector import zipped_vector
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


racmo_wind_vectors = ConfigLayer(
    id='racmo_wind_vectors',
    title='Annual mean wind vectors 1958-2019 (5km)',
    description=(
        """Averaged annual mean wind direction in meters per second from
        RACMO2.3p2 for the period 1958-2019."""
    ),
    tags=[],
    style='racmo_wind_vectors',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        *zipped_vector(
            input_file='{input_dir}/RACMO_QGreenland_Jan2021.zip',
            output_file='{output_dir}/racmo_wind_vectors.gpkg',
            vector_filename='wind_vector_points.gpkg',
            decompress_step_kwargs={
                'decompress_contents_mask': 'wind_vector_points.gpkg',
            },
        ),
    ],
)

racmo_wind_speed = ConfigLayer(
    id='racmo_wind_speed',
    title='Annual mean wind speed 1958-2019 (5km)',
    description=(
        """Averaged annual mean wind speed in meters per second from RACMO2.3p2
        for the period 1958-2019."""
    ),
    tags=[],
    style='racmo_wind_speed',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        decompress_step(
            input_file='{input_dir}/RACMO_QGreenland_Jan2021.zip',
            decompress_contents_mask='magnitudes.nc',
        ),
        *warp_and_cut(
            input_file='{input_dir}/magnitudes.nc',
            output_file='{output_dir}/racmo_wind_speed.tif',
            cut_file=project.boundaries['data'].filepath,
        ),
    ],
)

racmo_precip = ConfigLayer(
    id='racmo_precip',
    title='Total precipitation 1958-2019 (1km)',
    description=(
        """Averaged annual total precipitation in milimeters of water equivilent
        (mm w.e.) from RACMO2.3p2 for the period 1958-2019 covering the whole
        ice sheet and peripheral ice caps."""
    ),
    tags=[],
    style='racmo_precip',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        # - unzip (needs data file AND Icemask_Topo_Iceclasses_lon_lat_average_1km_GrIS.nc
        # TODO: make this return a list of one step like e.g., build_overviews?
        decompress_step(
            input_file='{input_dir}/RACMO_QGreenland_Jan2021.zip',
            decompress_contents_mask=(
                'precip.1958-2019.BN_RACMO2.3p2_FGRN055_1km.YY-mean.nc'
                ' Icemask_Topo_Iceclasses_lon_lat_average_1km_GrIS.nc'
            ),
        ),
        # Apply the promice mask. The `Promicemask` values are 3 = Greenland ice
        # sheet; 2,1 = Greenland peripheral ice caps; 0 = Ocean. This step masks
        # out the ocean as 'nodata'.
        ConfigLayerCommandStep(
            args=[
                'gdal_calc.py',
                '--calc="numpy.where((B != 0), A, -9999)"',
                '--NoDataValue=-9999',
                '--outfile={output_dir}/precip.tif',
                '-A', '{input_dir}/precip.1958-2019.BN_RACMO2.3p2_FGRN055_1km.YY-mean.nc',
                '-B', 'NETCDF:{input_dir}/Icemask_Topo_Iceclasses_lon_lat_average_1km_GrIS.nc:Promicemask',
            ],
        ),
        # TODO: create a helper for gdal_edit.
        ConfigLayerCommandStep(
            args=[
                'cp', '{input_dir}/precip.tif', '{output_dir}/edited.tif',
                '&&',
                'gdal_edit.py',
                '-a_srs', project.crs,
                '{output_dir}/edited.tif',
            ],
        ),
        *build_overviews(
            input_file='{input_dir}/edited.tif',
            output_file='{output_dir}/racmo_precip.tif',
        ),
    ],
)

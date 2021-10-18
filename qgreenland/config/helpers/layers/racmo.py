from qgreenland.config.datasets.racmo import racmo_qgreenland_jan2021 as dataset
from qgreenland.config.helpers.steps.build_overviews import build_overviews
from qgreenland.config.helpers.steps.compressed_vector import compressed_vector
from qgreenland.config.helpers.steps.decompress import decompress_step
from qgreenland.config.helpers.steps.gdal_edit import gdal_edit
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.project import project
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


def _make_racmo_wind_vectors() -> ConfigLayer:
    return ConfigLayer(
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
            *compressed_vector(
                input_file='{input_dir}/RACMO_QGreenland_Jan2021.zip',
                output_file='{output_dir}/racmo_wind_vectors.gpkg',
                vector_filename='wind_vector_points.gpkg',
                decompress_step_kwargs={
                    'decompress_contents_mask': 'wind_vector_points.gpkg',
                },
            ),
        ],
    )


def _make_racmo_wind_speed() -> ConfigLayer:
    return ConfigLayer(
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


# Params for racmo rasters that need to be masked via the Promicemask.
_masked_racmo_raster_params = {
    'racmo_precip': {
        'title': 'Total precipitation 1958-2019 (1km)',
        'description': (
            """Averaged annual total precipitation in milimeters of water equivilent
            (mm w.e.) from RACMO2.3p2 for the period 1958-2019 covering the whole
            ice sheet and peripheral ice caps."""
        ),
    },
    'racmo_snowfall': {
        'title': 'Snowfall 1958-2019 (1km)',
        'description': (
            """Averaged annual snowfall in milimeters of water equivilent (mm w.e.) from
            RACMO2.3p2 for the period 1958-2019 covering the whole ice sheet and
            peripheral ice caps."""
        ),
    },
    'racmo_snowmelt': {
        'title': 'Snowmelt 1958-2019 (1km)',
        'description': (
            """Averaged annual snowmelt in milimeters of water equivilent (mm w.e.) from
            RACMO2.3p2 for the period 1958-2019 covering the whole ice sheet and
            peripheral ice caps."""
        ),
    },
    'racmo_runoff': {
        'title': 'Runoff 1958-2019 (1km)',
        'description': (
            """Averaged annual runoff in milimeters of water equivilent (mm w.e.) from
            RACMO2.3p2 for the period 1958-2019 covering the whole ice sheet and
            peripheral ice caps."""
        ),
    },
    'racmo_subl': {
        'title': 'Sublimation 1958-2019 (1km)',
        'description': (
            """Averaged annual sublimation in milimeters of water equivilent (mm w.e.)
            from RACMO2.3p2 for the period 1958-2019 covering the whole ice sheet and
            peripheral ice caps."""
        ),
    },
    'racmo_sndiv': {
        'title': 'Snow drift erosion 1958-2019 (1km)',
        'description': (
            """Averaged annual snow drift erosion in milimeters of water equivilent (mm
            w.e.) from RACMO2.3p2 for the period 1958-2019 covering the whole ice
            sheet and peripheral ice caps."""
        ),
    },
    'racmo_t2m': {
        'title': 'Annual mean temperature at 2m 1958-2019 (1km)',
        'description': (
            """Averaged annual mean temperature at 2m in degrees Kelvin from RACMO2.3p2
            for the period 1958-2019."""
        ),
    },
}


RACMO_LAYER_ORDER = list(_masked_racmo_raster_params.keys())


def _make_masked_racmo_layer(
        *,
        layer_id: str,
        title: str,
        description: str,
        style: str,
        input_filename: str,
        decompress_contents_mask: str,
        variable: str,
        nodata: int = -9999,
        gdal_edit_args=(),
) -> ConfigLayer:
    return ConfigLayer(
        id=layer_id,
        title=title,
        description=description,
        tags=[],
        style=style,
        input=ConfigLayerInput(
            dataset=dataset,
            asset=dataset.assets['only'],
        ),
        steps=[
            decompress_step(
                input_file='{input_dir}/RACMO_QGreenland_Jan2021.zip',
                decompress_contents_mask=decompress_contents_mask,
            ),
            # Apply the promice mask. The `Promicemask` values are 3 = Greenland ice
            # sheet; 2,1 = Greenland peripheral ice caps; 0 = Ocean. This step masks
            # out the ocean as 'nodata'.
            ConfigLayerCommandStep(
                args=[
                    'gdal_calc.py',
                    f'--calc="numpy.where((B != 0), A, {nodata})"',
                    f'--NoDataValue={nodata}',
                    '--outfile={output_dir}/' + f'{variable}.tif',
                    '-A', 'NETCDF:{input_dir}/' + f'{input_filename}:{variable}',
                    '-B', (
                        'NETCDF:{input_dir}/'
                        'Icemask_Topo_Iceclasses_lon_lat_average_1km_GrIS.nc:Promicemask'
                    ),
                ],
            ),
            *gdal_edit(
                input_file='{input_dir}/' + f'{variable}.tif',
                output_file='{output_dir}/edited.tif',
                gdal_edit_args=[
                    '-a_srs', project.crs,
                    *gdal_edit_args,
                ],
            ),
            *build_overviews(
                input_file='{input_dir}/edited.tif',
                output_file='{output_dir}/' + f'racmo_{variable}.tif',
            ),
        ],
    )


def _make_masked_racmo_layers() -> list[ConfigLayer]:
    layers = []
    for layer_id, params in _masked_racmo_raster_params.items():
        variable = layer_id.split('_')[1]
        input_filename = f'{variable}.1958-2019.BN_RACMO2.3p2_FGRN055_1km.YY-mean.nc'
        layers.append(
            _make_masked_racmo_layer(
                layer_id=layer_id,
                title=params['title'],
                description=params['description'],
                style=layer_id,
                decompress_contents_mask=(
                    input_filename
                    + ' Icemask_Topo_Iceclasses_lon_lat_average_1km_GrIS.nc'
                ),
                input_filename=input_filename,
                variable=variable,
            ),
        )

    return layers


def make_racmo_layers() -> list[ConfigLayer]:
    wind_vectors = _make_racmo_wind_vectors()
    wind_speed = _make_racmo_wind_speed()
    layers = [wind_vectors, wind_speed]
    layers.extend(
        _make_masked_racmo_layers(),
    )

    return layers


RACMO_ULLR = '-639456.0 -655096.0 856544.0 -3355096.0'


def make_racmo_supplemental_layers() -> list[ConfigLayer]:
    layers = []

    _racmo_mask_layer_params = {
        'racmo_promicemask': {
            'title': 'PROMICE mask (1km)',
            'description': (
                """Mask of categorized Greenland ice. 3 = Greenland ice sheet; 2,1 = Greenland
                peripheral ice caps; 0 = Ocean."""
            ),
            'extract_filename': 'Icemask_Topo_Iceclasses_lon_lat_average_1km_GrIS.nc',
            'variable': 'Promicemask',
        },
        'racmo_grounded_ice': {
            'title': 'Grounded ice mask (1km)',
            'description': 'Mask of grounded ice. 1 = grounded.',
            'extract_filename': 'Icemask_Topo_Iceclasses_lon_lat_average_1km_Aug2020.nc',
            'variable': 'grounded_ice',
        },
    }

    for layer_id, params in _racmo_mask_layer_params.items():
        layers.append(
            ConfigLayer(
                id=layer_id,
                title=params['title'],
                description=params['description'],
                tags=[],
                style='racmo_promicemask',
                input=ConfigLayerInput(
                    dataset=dataset,
                    asset=dataset.assets['only'],
                ),
                steps=[
                    decompress_step(
                        input_file='{input_dir}/RACMO_QGreenland_Jan2021.zip',
                        decompress_contents_mask=params['extract_filename'],
                    ),
                    ConfigLayerCommandStep(
                        args=[
                            'gdal_translate',
                            '-a_srs', project.crs,
                            '-a_ullr', RACMO_ULLR,
                            ('NETCDF:{input_dir}/'
                             + f"{params['extract_filename']}:{params['variable']}"),
                            '{output_dir}/' + f"{params['variable']}.tif",
                        ],
                    ),
                    *build_overviews(
                        input_file='{input_dir}/' + f"{params['variable']}.tif",
                        output_file='{output_dir}/' + f'{layer_id}.tif',
                    ),
                ],
            ),
        )

    racmo_topography = _make_masked_racmo_layer(
        layer_id='racmo_topography',
        title='Ice surface topography (1km)',
        description=(
            """Ice sheet surface elevation in meters upscaled from the Greenland Mapping
            Project (GIMP) Digital Elevation Model."""
        ),
        style='racmo_topography',
        decompress_contents_mask='Icemask_Topo_Iceclasses_lon_lat_average_1km_GrIS.nc',
        input_filename='Icemask_Topo_Iceclasses_lon_lat_average_1km_GrIS.nc',
        variable='Topography',
        gdal_edit_args=[
            '-a_ullr', RACMO_ULLR,
        ],
    )

    layers.append(racmo_topography)

    return layers


RACMO_SUPPLEMENTAL_LAYER_ORDER = [
    'racmo_promicemask',
    'racmo_grounded_ice',
    'racmo_topography',
]

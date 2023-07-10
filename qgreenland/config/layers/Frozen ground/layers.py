from qgreenland.config.datasets.circumpolar_active_layer_monitoring import (
    circumpolar_layer_monitoring,
)
from qgreenland.config.datasets.pangaea_ground_temperature import (
    pangaea_ground_temperature as dataset,
)
from qgreenland.config.helpers.steps.compress_and_add_overviews import (
    compress_and_add_overviews,
)
from qgreenland.config.helpers.steps.decompress import decompress_step
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput

_layer_params = {
    "ground_temperature": {
        "title": "Ground temperature 2000-2016 (10km)",
        "description": "Average mean annual ground temperature in degrees Celsius.",
        "style": "ground_temperature",
        "variable": "MAGT",
    },
    "ground_temperature_sd": {
        "title": "Ground temperature standard deviation (10km)",
        "description": (
            """Standard deviation of the average mean annual ground temperature
            in degrees Celsius."""
        ),
        "style": "ground_temperature_std",
        "variable": "SD",
    },
    "permafrost_probability": {
        "title": "Permafrost probability (10km)",
        "description": (
            """Permafrost probability (fraction values from 0 to 1) assigned to
            each grid cell with mean annual ground temperature (MAGT) < 0°C."""
        ),
        "style": "permafrost_probability",
        "variable": "PerProb",
    },
}


pangaea_layers = [
    Layer(
        id=layer_id,
        title=params["title"],
        description=params["description"],
        tags=[],
        style=params["style"],
        input=LayerInput(
            dataset=dataset,
            asset=dataset.assets["10km"],
        ),
        steps=[
            *warp_and_cut(
                input_file=(
                    "NETCDF:{input_dir}/UiO_PEX_5.0_20181127_2000_2016_10km.nc:"
                    + params["variable"]
                ),
                output_file="{output_dir}/" + f"{layer_id}.tif",
                reproject_args=[
                    # Webpage for this data
                    # (https://doi.pangaea.de/10.1594/PANGAEA.888600) notes All
                    # files are provided in Arctic Polar Stereographic projection
                    # (EPSG:3995 WGS 84)
                    "-s_srs",
                    "EPSG:3995",
                    "-tr",
                    "10000",
                    "10000",
                    # This dataset does not contain CF-compliant fields or
                    # geotransform array. Set
                    # `GDAL_NETCDF_IGNORE_XY_AXIS_NAME_CHECKS` to `true` to use
                    # the provided `x` and `y` dims as coordinate values so that
                    # gdal can compute the transform on its own. See
                    # https://github.com/OSGeo/gdal/issues/4075
                    "--config",
                    "GDAL_NETCDF_IGNORE_XY_AXIS_NAME_CHECKS",
                    "true",
                ],
                cut_file=project.boundaries["data"].filepath,
            ),
            *compress_and_add_overviews(
                input_file="{input_dir}/" + f"{layer_id}.tif",
                output_file="{output_dir}/" + f"{layer_id}.tif",
                dtype_is_float=True,
            ),
        ],
    )
    for layer_id, params in _layer_params.items()
]


calm_layer = Layer(
    id="calm_network_sites",
    title="CALM network sites",
    description="""TODO...""",
    tags=[],
    style=None,
    input=LayerInput(
        dataset=circumpolar_layer_monitoring,
        asset=circumpolar_layer_monitoring.assets["only"],
    ),
    steps=[
        decompress_step(
            input_file="{input_dir}/CALM_Sites_wData.7z", decompress_type="7z"
        ),
        *ogr2ogr(
            input_file="{input_dir}/CALM_SitesData.shp",
            output_file="{output_dir}/calm_sites_data.gpkg",
            # Some features fall outside of our project CRS so an error is
            # raised without `skipfailures`.
            ogr2ogr_args=("-skipfailures",),
        ),
    ],
)

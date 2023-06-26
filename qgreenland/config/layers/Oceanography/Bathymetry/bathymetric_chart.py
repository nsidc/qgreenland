from qgreenland.config.datasets.bathymetric_chart import bathymetric_chart as dataset
from qgreenland.config.datasets.bathymetric_chart import gebco_bathymetric_chart
from qgreenland.config.helpers.layers.geological_map import make_layer
from qgreenland.config.helpers.steps.compress_and_add_overviews import (
    compress_and_add_overviews,
)
from qgreenland.config.helpers.steps.decompress import decompress_step
from qgreenland.config.helpers.steps.warp import warp
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput

bathymetric_raster_params = {
    "id": "bathymetric_raster",
    "title": "Depth (400m)",
    "description": (
        """Bathymetric elevation in meters.

        Elevations can be assumed to be relative to mean sea level. However,
        note that there may be differences in the vertical datum (the basis for
        elevations) for some older data from which this bathymetry dataset was
        derived."""
    ),
    "style": "ibcao_bathymetry",
    "dataset": dataset,
    "fn_mask": "bathymetry.*",
}

bathymetric_contours_params = {
    "id": "bathymetric_contours",
    "title": "Depth contours",
    "description": (
        """This dataset includes linear features that represent
         bathymetric contours recorded in metres,
        derived from the International Bathymetric Chart of the Arctic Ocean."""
    ),
    "style": "bathymetry",
    "input_filepath": "data/shape/base/bathymetry",
    "fn_mask": "bathymetry.*",
}


bathymetric_raster = Layer(
    id=bathymetric_raster_params["id"],
    title=bathymetric_raster_params["title"],
    description=bathymetric_raster_params["description"],
    tags=[],
    style=bathymetric_raster_params["style"],
    input=LayerInput(
        dataset=bathymetric_raster_params["dataset"],
        asset=dataset.assets["only"],
    ),
    steps=[
        *warp(
            input_file="NETCDF:{input_dir}/IBCAO_v4_2_400m_ice.nc:z",
            output_file="{output_dir}/bathymetric_chart.tif",
            warp_args=(
                "-s_srs",
                '"+proj=stere +lat_0=90 +lat_ts=75 +datum=WGS84"',
                "-dstnodata",
                "-9999",
                "-tr",
                "400",
                "400",
                # This dataset does not contain CF-compliant fields or
                # geotransform array. Set
                # `GDAL_NETCDF_IGNORE_XY_AXIS_NAME_CHECKS` to `true` to use
                # the provided `x` and `y` dims as coordinate values so that
                # gdal can compute the transform on its own. See
                # https://github.com/OSGeo/gdal/issues/4075
                "--config",
                "GDAL_NETCDF_IGNORE_XY_AXIS_NAME_CHECKS",
                "true",
            ),
            cut_file=project.boundaries["background"].filepath,
        ),
        *compress_and_add_overviews(
            input_file="{input_dir}/bathymetric_chart.tif",
            output_file="{output_dir}/bathymetric_chart.tif",
            dtype_is_float=True,
        ),
    ],
)


_background_boundary = project.boundaries["background"]
_background_bbox = _background_boundary.bbox
gebco_bathymetric_raster = Layer(
    id="gebco_bathymetric_raster",
    title="GEBCO depth",
    description=bathymetric_raster_params["description"],
    tags=[],
    style=bathymetric_raster_params["style"],
    input=LayerInput(
        dataset=gebco_bathymetric_chart,
        asset=gebco_bathymetric_chart.assets["only"],
    ),
    steps=[
        decompress_step(input_file="{input_dir}/gebco_2023.zip"),
        *warp_and_cut(
            input_file="NETCDF:{input_dir}/GEBCO_2023.nc:elevation",
            output_file="{output_dir}/bathymetric_chart.tif",
            reproject_args=(
                "-te",
                f"{_background_bbox.min_x} {_background_bbox.min_y} {_background_bbox.max_x} {_background_bbox.max_y}",
                "-dstnodata",
                "-9999",
                "-tr",
                "400",
                "400",
            ),
            cut_file=project.boundaries["background"].filepath,
        ),
        *compress_and_add_overviews(
            input_file="{input_dir}/bathymetric_chart.tif",
            output_file="{output_dir}/bathymetric_chart.tif",
            dtype_is_float=False,
        ),
    ],
)


bathymetric_contours = make_layer(
    layer_id=bathymetric_contours_params["id"],
    layer_params=bathymetric_contours_params,
)

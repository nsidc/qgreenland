from qgreenland.config.datasets.bathymetric_chart import gebco_bathymetric_chart
from qgreenland.config.helpers.steps.compress_and_add_overviews import (
    compress_and_add_overviews,
)
from qgreenland.config.helpers.steps.decompress import decompress_step
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep

_background_boundary = project.boundaries["background"]
_background_bbox = _background_boundary.bbox
gebco_bathymetric_raster = Layer(
    id="gebco_bathymetric_raster",
    title="Depth (400m)",
    description=(
        """Bathymetric elevation in meters.

        Negative values represent bathymetric depths and positive values are
        topographic heights.

        Elevations can be assumed to be relative to mean sea level. However, in
        some shallow water areas, the grids include data from sources having a
        vertical datum other than mean sea level. We are working to understand
        how best to fully assimilate these data."""
    ),
    tags=[],
    style="gebco_bathymetry",
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

gebco_bathymetric_contours = Layer(
    id="gebco_bathymetric_contours",
    title="Depth contours",
    description=(
        """Bathymetric elevation contours in meters.

        Contour interval is 100m and was derived from the "Depth (400m)" layer.

        Elevations can be assumed to be relative to mean sea level. However, in
        some shallow water areas, the grids include data from sources having a
        vertical datum other than mean sea level. We are working to understand
        how best to fully assimilate these data."""
    ),
    tags=[],
    style="bathymetry",
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
                "-tr",
                "400",
                "400",
            ),
            cut_file=project.boundaries["background"].filepath,
        ),
        CommandStep(
            args=[
                "gdal_calc.py",
                '--calc="where(A < 0, absolute(A), nan)"',
                "--A_band=1",
                "-A",
                "{input_dir}/bathymetric_chart.tif",
                "--outfile={output_dir}/positive_depths.tif",
            ],
        ),
        CommandStep(
            args=[
                "gdal_contour",
                "-a",
                "DEPTH",
                "-i",
                "500",
                "-nln",
                "bathymetry",
                "{input_dir}/positive_depths.tif",
                "{output_dir}/bathymetric_chart.gpkg",
            ],
        ),
    ],
)

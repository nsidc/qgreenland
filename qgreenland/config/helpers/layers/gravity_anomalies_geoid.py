from qgreenland.config.datasets.geoid import geoid
from qgreenland.config.datasets.gravity_anomalies import gravity_anomalies
from qgreenland.config.helpers.steps.compress_and_add_overviews import (
    compress_and_add_overviews,
)
from qgreenland.config.helpers.steps.decompress import decompress_step
from qgreenland.config.helpers.steps.warp_and_cut import warp_and_cut
from qgreenland.config.project import project
from qgreenland.models.config.dataset import Dataset
from qgreenland.models.config.layer import Layer, LayerInput


def _make_layer(
    *,
    layer_id: str,
    title: str,
    description: str,
    style: str,
    filename: str,
    dataset: Dataset,
) -> Layer:
    return Layer(
        id=layer_id,
        title=title,
        description=description,
        packaging_tags=["core"],
        style=style,
        input=LayerInput(
            dataset=dataset,
            asset=dataset.assets["only"],
        ),
        steps=[
            decompress_step(
                input_file="{input_dir}/archive.zip",
                decompress_contents_mask=filename,
            ),
            *warp_and_cut(
                input_file="{input_dir}/" + filename,
                output_file="{output_dir}/" + filename,
                reproject_args=[
                    # The source nodata value is 1.70141e+38. This value is not
                    # correctly set in the overviews (added in the step below),
                    # so override it here as -9999. See
                    # https://github.com/OSGeo/gdal/issues/8187.
                    "-dstnodata",
                    "-9999",
                    # Source data is 0.02x-0.02 degrees resolution. Rene noted in
                    # his email to QGreenland on 2021-01-22 that the geoid and
                    # gravity anomaly grids are 2km resolution.
                    "-tr",
                    "2000",
                    "2000",
                ],
                cut_file=project.boundaries["data"].filepath,
            ),
            *compress_and_add_overviews(
                input_file="{input_dir}/" + filename,
                output_file="{output_dir}/" + filename,
                dtype_is_float=True,
            ),
        ],
    )


_gravity_anomaly_layer_params = {
    "bouguer_gravity_anomaly": {
        "title": "Bouguer gravity anomaly (2km)",
        "filename": "bouguer_gravity_anomaly.tif",
    },
    "faye_gravity_anomaly": {
        "title": "Faye (free-air) gravity anomaly (2km)",
        "filename": "faye_gravity_anomaly.tif",
    },
}


def make_gravity_anomaly_layers() -> list[Layer]:
    return [
        _make_layer(
            layer_id=layer_id,
            title=params["title"],
            description="Gravity anomalies in miligals (mGal).",
            style="gravity_anomaly",
            filename=params["filename"],
            dataset=gravity_anomalies,
        )
        for layer_id, params in _gravity_anomaly_layer_params.items()
    ]


def make_geoid_layer() -> Layer:
    return _make_layer(
        layer_id="geoid",
        title="Geoid model (2km)",
        description="Official gravimetric geoid model for Greenland in meters.",
        style="geoid",
        filename="ggeoid16.tif",
        dataset=geoid,
    )

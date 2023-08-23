from qgreenland.config.datasets.grimp import grimp_annual_ice_velocity as annual_dataset
from qgreenland.config.helpers.steps.compress_and_add_overviews import (
    compress_and_add_overviews,
)
from qgreenland.config.helpers.steps.gdal_edit import gdal_edit
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep


def make_layer(
    *, variable: str, layer_id: str, style: str, title: str, description: str
) -> Layer:
    return Layer(
        id=layer_id,
        title=title,
        description=description,
        style=style,
        input=LayerInput(
            dataset=annual_dataset,
            asset=annual_dataset.assets["only"],
        ),
        steps=[
            # Round data to the nearest cm and convert to integer to save disk
            # space.
            CommandStep(
                args=[
                    "gdal_calc.py",
                    "--calc",
                    '"round(A * 100.0)"',
                    "--NoDataValue",
                    "-9999",
                    "--type",
                    "Int32",
                    "-A",
                    "{input_dir}/" + f"*{variable}*.tif",
                    "--outfile",
                    "{output_dir}/scaled.tif",
                ],
            ),
            # The `scale` metadata lets tools like QGIS know that the integers
            # should be interpreted as floating point data (e.g,. a value of
            # `12345` is displayed as 123.45)
            *gdal_edit(
                input_file="{input_dir}/scaled.tif",
                output_file="{output_dir}/edited.tif",
                gdal_edit_args=[
                    "-scale",
                    "0.01",
                ],
            ),
            *compress_and_add_overviews(
                input_file="{input_dir}/edited.tif",
                output_file="{output_dir}/compressed_with_overviews.tif",
                dtype_is_float=False,
            ),
        ],
    )


_description_common = """
Annual mosaics are produced from data with resolutions varying from a few
hundred meters to 1.5km. The 2021 annual mosaic includes data collected between
2020-12-01 and 2021-11-30.

Note that these data have been rounded to the nearest centimeter for QGreenland
to save disk space. Please see the original data source for the un-modified and
additional data:

* x and y component velocity error estimates (ex, ey).
* A temporal offset parameter (dT) that reports the difference in days between
  the date of each velocity estimate and the midpoint date of the corresponding
  measurement period.
* Shapefile that indicates the source of the image pairs (SAR or Landsat 8) used
  to produce the mosaic.
"""


_layer_params = {
    "vv": {
        "description": "Ice sheet velocity magnitude (vv) in meters per year for 2021."
        + _description_common,
        "style": "grimp_velocity_magnitude",
        "title": "Annual ice sheet velocity magnitude 2021 (200m)",
    },
    "vx": {
        "description": "Ice sheet velocity x component (vy) in meters per year for 2021."
        + _description_common,
        "style": "grimp_velocity_component",
        "title": "Annual ice sheet velocity x component 2021 (200m)",
    },
    "vy": {
        "description": "Ice sheet velocity y component (vy) in meters per year for 2021."
        + _description_common,
        "style": "grimp_velocity_component",
        "title": "Annual ice sheet velocity y component 2021 (200m)",
    },
}

annual_grimp_layers = [
    make_layer(
        variable=variable,
        layer_id=f"grimp_annual_{variable}_2021",
        style=layer_params["style"],
        description=layer_params["description"],
        title=layer_params["title"],
    )
    for variable, layer_params in _layer_params.items()
]

grimp_vector_layer = Layer(
    id="grimp_annual_vectors_2021",
    title="Annual ice sheet velocity vectors 2021 (1.5km)",
    description=(
        """Vector representation of ice sheet velocity in meters per year for 2021."""
    ),
    style="grimp_vectors",
    input=LayerInput(
        dataset=annual_dataset,
        asset=annual_dataset.assets["only"],
    ),
    steps=[
        # Now merge the variables into a 3-band .tif file.
        CommandStep(
            args=[
                "gdal_merge.py",
                "-a_nodata",
                "-2e+09",
                "-separate",
                "-o",
                "{output_dir}/merged.tif",
                "{input_dir}/*vx*.tif",
                "{input_dir}/*vy*.tif",
            ],
        ),
        # Downsample to 1.5km
        CommandStep(
            args=[
                "gdalwarp",
                "-tr",
                "1500 1500",
                "{input_dir}/merged.tif",
                "{output_dir}/downsampled.tif",
            ],
        ),
        # Next, convert the .tif into a csv file. This converts the raster into
        # a format readable by `ogr2ogr`, used in the next step.
        CommandStep(
            args=[
                "gdal2xyz.py",
                "-skipnodata",
                "-csv",
                "-allbands",
                "{input_dir}/downsampled.tif",
                "{output_dir}/as_xyz.xyz",
                "&&",
                'echo "x,y,vx,vy" > {output_dir}/data_with_header.csv',
                "&&",
                "cat {output_dir}/as_xyz.xyz >> {output_dir}/data_with_header.csv",
            ],
        ),
        # Finally, convert to gpkg.
        *ogr2ogr(
            input_file="CSV:{input_dir}/data_with_header.csv",
            output_file="{output_dir}/vectors.gpkg",
            ogr2ogr_args=(
                "-oo",
                "X_POSSIBLE_NAMES=x",
                "-oo",
                "Y_POSSIBLE_NAMES=y",
                "-s_srs",
                "EPSG:3413",
                "-oo",
                "KEEP_GEOM_COLUMNS=NO",
                "-oo",
                "AUTODETECT_TYPE=YES",
            ),
        ),
    ],
)

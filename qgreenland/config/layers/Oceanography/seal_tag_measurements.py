from qgreenland.config.datasets.seal_tag_water_measurements import dataset
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import Layer, LayerInput

layer = Layer(
    id="seal_tag_measurements",
    title="Seal tag water measurements",
    description=(
        """Locaitons of seal tag measurements with temperature and salinity in coastal Greenland from 2010-08-31 to 2012-05-14."""
    ),
    tags=[],
    in_package=True,
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets["only"],
    ),
    steps=[
        *ogr2ogr(
            input_file="{input_dir}/*.csv",
            output_file="{output_dir}/final.gpkg",
            ogr2ogr_args=(
                "-s_srs",
                "EPSG:4326",
                "-oo",
                "X_POSSIBLE_NAMES=Longitude",
                "-oo",
                "Y_POSSIBLE_NAMES=Latitude",
            ),
        ),
    ],
)

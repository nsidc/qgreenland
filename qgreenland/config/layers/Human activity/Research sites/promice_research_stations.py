from qgreenland.config.datasets.promice_stations import (
    gc_net_promice_stations as dataset,
)
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import Layer, LayerInput

layer = Layer(
    id="promice_gc_net_stations",
    title="PROMICE and GC-Net automated weather stations",
    description="""Automated weather station locations for the PROMICE,
        GC-Net, Glaciobasis (GEM), and other programs.

        Station locations, installation (if necessary, decommission) date,
        location type (tundra, ice sheet, local glacier), station type (one or
        two levels of measurements) are available as attributes.""",
    tags=[],
    style="labeled_point",
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets["only"],
    ),
    steps=[
        *ogr2ogr(
            # This CSV data is tab-delimeted, but ogr2ogr can
            # auto-detect that.
            input_file="{input_dir}/*.csv",
            output_file="{output_dir}/final.gpkg",
            ogr2ogr_args=(
                "-s_srs",
                "EPSG:4326",
                "-oo",
                "X_POSSIBLE_NAMES=lon_installation",
                "-oo",
                "Y_POSSIBLE_NAMES=lat_installation",
                "-sql",
                r'"SELECT *, stid as label from \"AWS_metadata\""',
            ),
        ),
    ],
)

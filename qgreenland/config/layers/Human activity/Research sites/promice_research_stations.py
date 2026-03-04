from qgreenland.config.datasets.promice_stations import (
    gc_net_promice_stations as dataset,
)
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import Layer, LayerInput

layer = Layer(
    id="promice_gc_net_stations",
    title="PROMICE and GC-Net automated weather stations",
    description="""Automated weather station sites for the PROMICE,
        GC-Net, Glaciobasis (GEM), and other programs.

        Station locations, installation (if necessary, decommission) date,
        location type (tundra, ice sheet, local glacier) are available as
        attributes.""",
    tags=[],
    style="labeled_point",
    inputs=[
        LayerInput(
            dataset=dataset,
            asset=dataset.assets["only"],
        )
    ],
    steps=[
        *ogr2ogr(
            input_file="{input_dir}/*.csv",
            output_file="{output_dir}/final.gpkg",
            ogr2ogr_args=(
                "-s_srs",
                "EPSG:4326",
                "-oo",
                "X_POSSIBLE_NAMES=longitude_installation",
                "-oo",
                "Y_POSSIBLE_NAMES=latitude_installation",
                "-sql",
                r'"SELECT *, site_id as label from \"AWS_sites_metadata\""',
            ),
        ),
    ],
)

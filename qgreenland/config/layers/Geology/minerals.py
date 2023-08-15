from qgreenland.config.datasets.geus_mineral_occurrences import (
    geus_mineral_occurrences as dataset,
)
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import Layer, LayerInput

mineral_occurrences_layer = Layer(
    id="mineral_occurrences",
    title="Mineral occurrences",
    description=(
        """Points representing the location of mineral occurrences in Greenland.

        Points are categorized by commodity group using color. Labels indicate
        the main commodity of each occurence.
        """
    ),
    tags=[],
    style="mineral_occurrences",
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets["only"],
    ),
    steps=[
        *ogr2ogr(
            input_file="{input_dir}/geus_mineral_occurrences.gpkg",
            output_file="{output_dir}/geus_mineral_occurrences_reprojected.gpkg",
        ),
    ],
)

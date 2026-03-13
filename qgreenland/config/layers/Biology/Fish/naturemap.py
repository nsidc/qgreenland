from qgreenland.config.datasets.naturemap import (
    naturemap_important_wildlife_areas as dataset,
)
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import Layer, LayerInput

atlantic_salmon_in_kapisillit = Layer(
    id="atlantic_salmon_in_kapisillit",
    title="Atlantic salmon in Kapisillit",
    description=(
        """Polygons representing Atlantic salmon areas in Kapisillit.

        The only known spawning stock of Atlantic salmon in Greenland is found
        in the Kapisillit River in the head of Nuup Kangerlua fjord, West
        Greenland. The stock is genetically isolated and unique in Greenland."""
    ),
    tags=[],
    in_package=True,
    style="protected_area_polygon",
    inputs=[
        LayerInput(
            dataset=dataset,
            asset=dataset.assets["atlantic_salmon_in_kapisillit"],
        )
    ],
    steps=[
        *ogr2ogr(
            input_file="{input_dir}/*.gpkg",
            output_file="{output_dir}/final.gpkg",
        ),
    ],
)

from qgreenland.config.datasets.naturemap import (
    naturemap_important_wildlife_areas as dataset,
)
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import Layer, LayerInput

atlantic_salmon_in_kapisillit = Layer(
    id="important_areas_red_listed_plant_taxa",
    title="Important areas red listed plant taxa",
    description=(
        """Polygons representing red-listed plant taxa of Greenland.

        Red listed species are those assessed to be Regionally Extinct [RE,
        Regionalt uddød], Critically Endangered [CR, Kritisk truet], Endangered
        [EN, Truet), Vulnerable [VU, Sårbar], Near Threatened [NT, Næsten truet)
        and Data Deficient [DD, Utilstrækkelige data].

        The layer depicts dissolved buffer zones of 4 km around occurrences of red
        listed plant taxa.

        For more information, see:
        https://natur.gl/wp-content/uploads/2024/04/Important-areas-for-red-listed-plant-taxa.pdf.
        """
    ),
    tags=[],
    in_package=True,
    style="protected_area_polygon",
    inputs=[
        LayerInput(
            dataset=dataset,
            asset=dataset.assets["important_areas_red_listed_plant_taxa"],
        )
    ],
    steps=[
        *ogr2ogr(
            input_file="{input_dir}/*.gpkg",
            output_file="{output_dir}/final.gpkg",
        ),
    ],
)

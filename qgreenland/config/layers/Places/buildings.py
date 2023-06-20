from qgreenland.config.datasets.asiaq_nunagis import asiaq_nunagis
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput

buildings = Layer(
    id="buildings",
    title="Buildings",
    style="buildings_shape",
    description="""Polygons representing buildings in Greenland.

    The attribute containing building use is called ‘Info’ and is provided in Danish.""",
    tags=["places"],
    input=LayerInput(
        dataset=asiaq_nunagis,
        asset=asiaq_nunagis.assets["buildings"],
    ),
    steps=[
        *ogr2ogr(
            input_file="{input_dir}/fetched.geojson",
            output_file="{output_dir}/final.gpkg",
            boundary_filepath=project.boundaries["data"].filepath,
        ),
    ],
)

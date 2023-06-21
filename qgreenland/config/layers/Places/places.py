from qgreenland.config.datasets.asiaq_nunagis import asiaq_nunagis
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput

cities = Layer(
    id="cities",
    title="Cities",
    # style=None,
    description="""Lines representing roads in Greenland.""",
    tags=["places"],
    input=LayerInput(
        dataset=asiaq_nunagis,
        asset=asiaq_nunagis.assets["cities"],
    ),
    steps=[
        *ogr2ogr(
            input_file="{input_dir}/fetched.geojson",
            output_file="{output_dir}/final.gpkg",
            boundary_filepath=project.boundaries["data"].filepath,
        ),
    ],
)

settlements = Layer(
    id="settlements",
    title="Settlements",
    # style=None,
    description="""Lines representing roads in Greenland.""",
    tags=["places"],
    input=LayerInput(
        dataset=asiaq_nunagis,
        asset=asiaq_nunagis.assets["settlements"],
    ),
    steps=[
        *ogr2ogr(
            input_file="{input_dir}/fetched.geojson",
            output_file="{output_dir}/final.gpkg",
            boundary_filepath=project.boundaries["data"].filepath,
        ),
    ],
)

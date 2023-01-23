from qgreenland.config.datasets.seismograph_stations import (
    seismograph_stations as dataset,
)
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput

seismograph_stations = Layer(
    id="seismograph_stations",
    title="Seismograph stations",
    description=("""Location and details of Greenland seismograph stations."""),
    tags=[],
    style="seismograph_stations",
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets["only"],
    ),
    steps=[
        *ogr2ogr(
            input_file="{input_dir}/stations.kmz",
            output_file="{output_dir}/ogr2ogr.gpkg",
            boundary_filepath=project.boundaries["data"].filepath,
        ),
    ],
)

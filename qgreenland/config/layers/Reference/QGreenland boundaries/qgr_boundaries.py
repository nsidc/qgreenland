from qgreenland.config.datasets.boundaries import qgr_bounds as dataset
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.models.config.layer import Layer, LayerInput


qgr_boundary_data = Layer(
    id='qgr_boundary_data',
    title='Greenland-focused boundary',
    description=(
        """Polygon representing the tight boundary for QGreenland
        data/imagery."""
    ),
    tags=[],
    style='transparent_shape',
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets['data'],
    ),
    steps=[
        *ogr2ogr(
            input_file='{input_dir}/greenland_rectangle.geojson',
            output_file='{output_dir}/boundary.gpkg',
        ),
    ],
)

qgr_boundary_background = Layer(
    id='qgr_boundary_background',
    title='Background boundary',
    description=(
        """Polygon representing the full boundary of QGreenland background
        data/imagery."""
    ),
    tags=[],
    show=True,
    style='transparent_shape',
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets['background'],
    ),
    steps=[
        *ogr2ogr(
            input_file='{input_dir}/latitude_shape_40_degrees.geojson',
            output_file='{output_dir}/boundary.gpkg',
        ),
    ],
)

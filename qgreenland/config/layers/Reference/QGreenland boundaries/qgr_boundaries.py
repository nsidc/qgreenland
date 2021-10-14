from qgreenland.config.datasets.boundaries import qgr_bounds as dataset
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr 
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
from qgreenland.models.config.step import ConfigLayerCommandStep


def _ogr2ogr_step(input_fn: str) -> list[ConfigLayerCommandStep]:
    return ogr2ogr(
        input_file='{input_dir}/' + input_fn,
        output_file='{output_dir}/boundary.gpkg',
    )


qgr_boundary_data = ConfigLayer(
    id='qgr_boundary_data',
    title='Greenland-focused boundary',
    description=(
        """Polygon representing the tight boundary for QGreenland
        data/imagery."""
    ),
    tags=[],
    style='transparent_shape',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['data'],
    ),
    steps=[
        *_ogr2ogr_step('greenland_rectangle.geojson'),
    ],
)

qgr_boundary_background = ConfigLayer(
    id='qgr_boundary_background',
    title='Background boundary',
    description=(
        """Polygon representing the full boundary of QGreenland background
        data/imagery."""
    ),
    tags=[],
    show=True,
    style='transparent_shape',
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['background'],
    ),
    steps=[
        *_ogr2ogr_step('latitude_shape_40_degrees.geojson'),
    ],
)

# TODO: `from qgreenland.helpers.? import ?` if needed
# TODO: `from qgreenland.config.project import project` if needed
# TODO: Replace `?` below with the correct package/module/object to import
from qgreenland.config.datasets.? import ? as dataset
from qgreenland.models.config.layer import ConfigLayer, ConfigLayerInput
# TODO: Import the correct step type for steps populated below


exclusive_economic_zone = ConfigLayer(
    id='exclusive_economic_zone',
    title='Exclusive economic zone (polyline)',
    description=(
        """Exclusive Economic Zone of Greenland based on Executive Order on the
        Exclusive Economic Zone at Greenland. BEK no. 1020 of 20/10/2004.
        Foreign Ministry of Denmark."""
    ),
    tags=[],
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        # TODO: Populate steps
    ],
)

baseline = ConfigLayer(
    id='baseline',
    title='Baseline (polyline)',
    description=(
        """The territorial sea baseline is shown in accordance to Executive
        Order no 1004 dated 15.10.2004."""
    ),
    tags=[],
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[],
)

3nm_polyline = ConfigLayer(
    id='3nm_polyline',
    title='3NM (polyline)',
    description=(
        """Reference to Inatsisartut Act no. 15 of 18 June 2017 on protection of
        the marine environment, paragraph 4, 2. NM = nautical mile."""
    ),
    tags=[],
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[
        # TODO: Populate steps
    ],
)

12nm_polyline = ConfigLayer(
    id='12nm_polyline',
    title='12NM (polyline)',
    description=(
        """Fishery limit. Regarding the fishery limit, reference is made to
        Greenland Home Rule Parliament Act no 18 dated 31.10.1996, paragraph 7,
        2. NM = nautical mile."""
    ),
    tags=[],
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[],
)

3nm_polygon = ConfigLayer(
    id='3nm_polygon',
    title='3NM (polygon)',
    description=(
        """Reference to Inatsisartut Act no. 15 of 18 June 2017 on protection of
        the marine environment, paragraph 4, 2. NM = nautical mile."""
    ),
    tags=[],
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[],
)

fishzone_boundary = ConfigLayer(
    id='fishzone_boundary',
    title='Fishing zone (polygon)',
    description=(
        """Fishery limit. Regarding the fishery limit, reference is made to
        Greenland Home Rule Parliament Act no 18 dated 31.10.1996"""
    ),
    tags=[],
    input=ConfigLayerInput(
        dataset=dataset,
        asset=dataset.assets['only'],
    ),
    steps=[],
)

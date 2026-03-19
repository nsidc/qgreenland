import pytest

from qgreenland.models.config.asset import HttpAsset, OnlineAsset
from qgreenland.models.config.dataset import Dataset
from qgreenland.models.config.layer import Layer, LayerInput, VectorLayerReferenceInput
from qgreenland.models.config.layer_group import LayerGroupSettings, RootGroupSettings
from qgreenland.test.constants import (
    MOCK_COMPILE_PACKAGE_DIR,
    MOCK_RELEASE_LAYERS_DIR,
    TEST_CONFIG_DIR,
)
from qgreenland.util.config import config
from qgreenland.util.qgis.project import QgsApplicationContext
from qgreenland.util.tree import LayerGroupNode, LayerNode

_mock_metadata = {
    "title": "Example Dataset",
    "abstract": "Example abstract.",
    "citation": {
        "text": "NSIDC 2020",
        "url": "https://nsidc.org",
    },
}
_mock_asset_id = "only"

_mock_online_asset_cfg = {
    "id": _mock_asset_id,
    "provider": "wms",
    "url": "crs=EPSG:4326&format=image/png&layers=continents&styles&url=https://demo.mapserver.org/cgi-bin/wms",  # noqa
}
MockOnlineLayerConfig = Layer(
    id="example_online",
    title="Example online",
    description="Example layer description.",
    tags=["foo", "bar", "baz"],
    in_package=True,
    inputs=[
        LayerInput(
            dataset=Dataset(
                id="baz",
                assets=[OnlineAsset(**_mock_online_asset_cfg)],
                metadata=_mock_metadata,
            ),
            asset=OnlineAsset(**_mock_online_asset_cfg),
        ),
    ],
)

_mock_http_asset_cfg = {
    "id": _mock_asset_id,
    "urls": ["https://foo.bar.com/data.zip"],
}
mock_raster_layer_cfg = {
    "id": "example_raster",
    "title": "Example raster",
    "description": "Example layer description.",
    "tags": ["foo", "bar", "baz"],
    "in_package": True,
    "inputs": [
        {
            "dataset": {
                "id": "example_dataset",
                "assets": [HttpAsset(**_mock_http_asset_cfg)],
                "metadata": _mock_metadata,
            },
            "asset": HttpAsset(**_mock_http_asset_cfg),
        }
    ],
    "steps": [
        {
            "type": "command",
            "args": ["foo", "bar"],
        },
    ],
}
MockRasterLayerConfig = Layer(**mock_raster_layer_cfg)


def _layer_node(cfg: Layer) -> LayerGroupNode:
    node = LayerGroupNode(
        "layers",
        settings=RootGroupSettings(),
    )

    for node_name in ["Group", "Subgroup"]:
        node = LayerGroupNode(
            node_name,
            settings=LayerGroupSettings(),
            parent=node,
        )

    return LayerNode(cfg.id, layer_cfg=cfg, parent=node)


@pytest.fixture
def online_layer_cfg():
    """Return an example online layer."""
    return MockOnlineLayerConfig


@pytest.fixture
def layer_cfgs():
    """Return a list of example layers."""
    _layer_ids = [
        "bedmachine_error",
        "bedmachine_thickness",
        "background",
        "lat_0_25_deg",
        "lon_0_5_deg",
        "lon_5_deg",
    ]
    return [
        Layer(
            **{
                **mock_raster_layer_cfg,
                "id": s,
                "title": "Foo",
                "description": "Bar.",
            }
        )
        for s in _layer_ids
    ]


@pytest.fixture
def raster_layer_cfg():
    """Return an example local raster layer."""
    return MockRasterLayerConfig


@pytest.fixture()
def full_cfg(monkeypatch):
    """Initialize and return test config."""
    config.init_config(config_dir=TEST_CONFIG_DIR)
    compiled_config = config.get_config()

    monkeypatch.setattr(
        "qgreenland.util.layer.RELEASE_LAYERS_DIR", MOCK_RELEASE_LAYERS_DIR
    )
    monkeypatch.setattr(
        "qgreenland.util.layer.COMPILE_PACKAGE_DIR", MOCK_COMPILE_PACKAGE_DIR
    )

    yield compiled_config

    config.init_config()


@pytest.fixture(scope="session")
def setup_teardown_qgis_app():
    """Set up and teardown a QgsApplication instance ONCE.

    The QgsApplication must be setup and torn town once (`scope='session'`) and
    only once. Attempting to setup and teardown more than once will result in
    segmentation faults.
    """
    with QgsApplicationContext():
        yield


@pytest.fixture
def online_layer_node(online_layer_cfg):
    return _layer_node(online_layer_cfg)


@pytest.fixture
def raster_layer_node(raster_layer_cfg):
    return _layer_node(raster_layer_cfg)


ref_layer_id = "example_vector"
mock_dataset = Dataset(
    id=f"{ref_layer_id}_dataset",
    assets=[
        HttpAsset(
            id="dataset_http",
            urls=["https://example.com/get/1"],
        ),
    ],
    metadata=_mock_metadata,
)

MockVectorLayerConfig = Layer(
    id=ref_layer_id,
    title="Vector layer used by a VRT",
    description="Example layer description.",
    tags=["foo", "bar", "baz"],
    inputs=[
        LayerInput(
            dataset=mock_dataset,
            asset=mock_dataset.assets["dataset_http"],
        ),
    ],
)

MockVectorVrtLayerConfig = Layer(
    id="example_vector_vrt",
    title="Vector VRT layer referencing vector_example",
    description="Example layer description.",
    tags=["foo", "bar", "baz"],
    inputs=[
        VectorLayerReferenceInput(
            layer_id=ref_layer_id,
            sql="SELECT * FROM foo as subset limit 1",
        ),
    ],
)


@pytest.fixture
def vector_vrt_layer_cfg():
    return MockVectorVrtLayerConfig


@pytest.fixture
def vector_layer_cfg():
    return MockVectorLayerConfig

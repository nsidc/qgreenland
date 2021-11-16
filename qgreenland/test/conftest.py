import pytest

from qgreenland.models.config.asset import (
    HttpAsset,
    OnlineAsset,
)
from qgreenland.models.config.layer import Layer
from qgreenland.models.config.layer_group import (
    LayerGroupSettings,
    RootGroupSettings,
)
from qgreenland.test.constants import (
    TEST_CONFIG_DIR,
)
from qgreenland.util.config.compile import compile_cfg
from qgreenland.util.qgis.project import QgsApplicationContext
from qgreenland.util.tree import (
    LayerGroupNode,
    LayerNode,
)

_mock_metadata = {
    'title': 'Example Dataset',
    'abstract': 'Example abstract.',
    'citation': {
        'text': 'NSIDC 2020',
        'url': 'https://nsidc.org',
    },
}
_mock_asset_id = 'only'

_mock_online_asset_cfg = {
    'id': _mock_asset_id,
    'provider': 'wms',
    'url': 'crs=EPSG:4326&format=image/png&layers=continents&styles&url=https://demo.mapserver.org/cgi-bin/wms'  # noqa
}
mock_online_layer_cfg = {
    'id': 'example_online',
    'title': 'Example online',
    'description': 'Example layer description.',
    'tags': ['foo', 'bar', 'baz'],
    'in_package': True,
    'input': {
        'dataset': {
            'id': 'baz',
            'assets': [OnlineAsset(**_mock_online_asset_cfg)],
            'metadata': _mock_metadata,
        },
        'asset': OnlineAsset(**_mock_online_asset_cfg),
    },
}
MockOnlineLayerConfig = Layer(**mock_online_layer_cfg)

_mock_http_asset_cfg = {
    'id': _mock_asset_id,
    'urls': ['https://foo.bar.com/data.zip'],
}
mock_raster_layer_cfg = {
    'id': 'example_raster',
    'title': 'Example raster',
    'description': 'Example layer description.',
    'tags': ['foo', 'bar', 'baz'],
    'in_package': True,
    'input': {
        'dataset': {
            'id': 'example_dataset',
            'assets': [HttpAsset(**_mock_http_asset_cfg)],
            'metadata': _mock_metadata,
        },
        'asset': HttpAsset(**_mock_http_asset_cfg),
    },
    'steps': [
        {
            'type': 'command',
            'args': ['foo', 'bar'],
        },
    ],
}
MockRasterLayerConfig = Layer(**mock_raster_layer_cfg)


def _layer_node(cfg: Layer) -> LayerGroupNode:
    node = LayerGroupNode(
        'layers',
        settings=RootGroupSettings(),
    )

    for node_name in ['Group', 'Subgroup']:
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
        'bedmachine_error',
        'bedmachine_thickness',
        'background',
        'lat_0_25_deg',
        'lon_0_5_deg',
        'lon_5_deg',
    ]
    return [
        Layer(**{
            **mock_raster_layer_cfg,  # type: ignore[arg-type]
            'id': s,
            'title': 'Foo',
            'description': 'Bar.',
        }) for s in _layer_ids
    ]


@pytest.fixture
def raster_layer_cfg():
    """Return an example local raster layer."""
    return MockRasterLayerConfig


@pytest.fixture
def full_cfg():
    """Return an example config."""
    return compile_cfg(TEST_CONFIG_DIR)


@pytest.fixture(scope='session')
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

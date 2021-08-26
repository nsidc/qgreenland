import pytest

from qgreenland.models.config.layer import ConfigLayer
from qgreenland.models.config.layer_group import (
    LayerGroupSettings,
    RootGroupSettings,
)
from qgreenland.test.constants import TEST_CONFIG_DIR
from qgreenland.util.qgis.project import QgsApplicationContext
from qgreenland.util.tree import (
    LayerGroupNode,
    LayerNode,
)

_mock_metadata = {
    'title': 'Example Dataset',
    'abstract': 'Example abstract',
    'citation': {
        'text': 'NSIDC 2020',
        'url': 'https://nsidc.org',
    },
}
_mock_asset_id = 'only'

_mock_online_asset_cfg = {
    'type': 'online',
    'id': _mock_asset_id,
    'provider': 'wms',
    'url': 'crs=EPSG:4326&format=image/png&layers=continents&styles&url=https://demo.mapserver.org/cgi-bin/wms'  # noqa
}
mock_online_layer_cfg = ConfigLayer(**{
    'id': 'example_online',
    'title': 'Example online',
    'description': 'Example layer description',
    'in_package': True,
    'input': {
        'dataset': {
            'id': 'baz',
            'assets': {_mock_asset_id: _mock_online_asset_cfg},
            'metadata': _mock_metadata,
        },
        'asset': _mock_online_asset_cfg,
    },
})

_mock_http_asset_cfg = {
    'type': 'http',
    'id': _mock_asset_id,
    'urls': ['https://foo.bar.com/data.zip'],
}
mock_raster_layer_cfg = ConfigLayer(**{
    'id': 'example_raster',
    'title': 'Example raster',
    'description': 'Example layer description',
    'in_package': True,
    'input': {
        'dataset': {
            'id': 'example_dataset',
            'assets': {_mock_asset_id: _mock_http_asset_cfg},
            'metadata': _mock_metadata,
        },
        'asset': _mock_http_asset_cfg,
    },
    'steps': [
        {
            'type': 'command',
            'args': ['foo', 'bar'],
        },
    ],
})


def _layer_node(cfg: ConfigLayer) -> LayerGroupNode:
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
    return mock_online_layer_cfg


@pytest.fixture
def raster_layer_cfg():
    """Return an example local raster layer."""
    return mock_raster_layer_cfg


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


@pytest.fixture
def mock_layer_config_contents():
    ordered_dir_path = TEST_CONFIG_DIR / 'Group' / 'Subgroup'
    return list(ordered_dir_path.iterdir())


@pytest.fixture
def mock_layer_config_contents_unordered():
    unordered_dir_path = TEST_CONFIG_DIR / 'Group' / 'Subgroup without settings'
    return list(unordered_dir_path.iterdir())

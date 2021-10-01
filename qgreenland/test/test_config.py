import pytest

from qgreenland.util.config.config import (
    get_config,
    init_config,
)

# TODO: Fixture?
init_config()


def test_get_layer_config_all():
    config = get_config()
    layer_config = config.layers

    # There are at least 2 layers.
    assert len(layer_config.keys()) >= 2


def test_get_layer_config_one():
    config = get_config()
    # If the layer does not exist, an exception will be raised and pytest will
    # appropriately fail.
    assert config.layers['background']


# TODO: Remove all tests that act on a real config. The vision for the future is
# to fully divorce the framework from the config.  All tests below this line can
# be done on a mock config. All tests above this line can be deleted.

def test_immutable_model():
    config = get_config()
    # Immutable models raise a TypeError on item assignment with a message like:
    # `TypeError: "ConfigLayer" is immutable and does not support item
    # assignment`
    with pytest.raises(TypeError):
        config.layers['background'].description = 'override'


def test_layer_indexes():
    config = get_config()
    for key, layer in config.layers.items():
        assert key == layer.id


def test_dataset_and_asset_indexes():
    config = get_config()
    for dataset_key, dataset in config.datasets.items():
        assert dataset_key == dataset.id

        for asset_key, asset in dataset.assets.items():
            assert asset_key == asset.id

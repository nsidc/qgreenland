import pytest

from qgreenland.util.config.config import CONFIG


def test_get_layer_config_all():
    layer_config = CONFIG.layers

    # There are at least 2 layers.
    assert len(layer_config.keys()) >= 2


def test_get_layer_config_one():
    # If the layer does not exist, an exception will be raised and pytest will
    # appropriately fail.
    assert CONFIG.layers['background']


def test_immutable_model():
    # Immutable models raise a TypeError on item assignment with a message like:
    # `TypeError: "ConfigLayer" is immutable and does not support item
    # assignment`
    with pytest.raises(TypeError):
        CONFIG.layers['background'].description = 'override'


def test_layer_indexes():
    for key, layer in CONFIG.layers.items():
        assert key == layer.id


def test_dataset_and_asset_indexes():
    for dataset_key, dataset in CONFIG.datasets.items():
        assert dataset_key == dataset.id

        for asset_key, asset in dataset.assets.items():
            assert asset_key == asset.id

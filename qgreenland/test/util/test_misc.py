from qgreenland.util import misc


def test_get_layer_config_all():
    layer_config = misc.get_layer_config()

    # There are at least 2 layers.
    assert len(layer_config.keys()) >= 2


def test_get_layer_config_one():
    # If the layer does not exist, an exception will be raised and pytest will
    # appropriately fail.
    misc.get_layer_config('coastlines')

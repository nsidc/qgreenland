import json

from compile import JSONNET_DICT, THIS_DIR


def test_jsonnet():
    old_config = json.load(open(THIS_DIR / 'old_config.json', 'r'))

    expected_layer_config = old_config['layers']['background']
    expected_layer_config.pop('steps')

    expected_config = {
        'layers': {'background': expected_layer_config},
        'datasets': {
            'background': old_config['datasets']['background']
        }
    }

    assert expected_config == JSONNET_DICT

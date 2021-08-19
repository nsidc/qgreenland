import json
from pathlib import Path

import _jsonnet


THIS_DIR = Path(__file__).parent
NEW_CFG_DIR = THIS_DIR / 'new_cfg'
NEW_CFG = NEW_CFG_DIR / 'one_layer.jsonnet'

COMPILED_JSON = _jsonnet.evaluate_file(str(NEW_CFG))

JSONNET_DICT = json.loads(COMPILED_JSON)


if __name__ == '__main__':
    print(COMPILED_JSON)

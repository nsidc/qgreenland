import json
from pathlib import Path

import _jsonnet

THIS_DIR = Path(__file__).parent

COMPILED_JSON = _jsonnet.evaluate_file(str(THIS_DIR /'one_layer.jsonnet'))

JSONNET_DICT = json.loads(COMPILED_JSON)


if __name__ == '__main__':
    print(COMPILED_JSON)

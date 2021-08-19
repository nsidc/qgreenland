from pathlib import Path

import _jsonnet

THIS_DIR = Path(__file__).parent

print(_jsonnet.evaluate_file(str(THIS_DIR /'one_layer.jsonnet')))

import json
from pathlib import Path


THIS_DIR = Path(__file__).parent
NEW_CFG_DIR = THIS_DIR / 'new_cfg'
NEW_CFG = NEW_CFG_DIR / 'one_layer.cue'

COMPILED_JSON = subprocess.run('cue', 'eval', NEW_CFG)
COMPILED_DICT = json.loads(COMPILED_JSON)


if __name__ == '__main__':
    print(COMPILED_JSON)

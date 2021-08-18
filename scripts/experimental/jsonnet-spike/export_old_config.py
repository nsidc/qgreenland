# NOTE: Execute from a directory sibling or child to the `qgreenland` package
# ... or modify the PYTHONPATH
import json

from qgreenland.config import CONFIG

print(
    json.dumps(json.loads(CONFIG.json()), indent=2)
)

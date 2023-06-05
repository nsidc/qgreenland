import json
from pathlib import Path


class MagicJSONEncoder(json.JSONEncoder):
    """Call __json__ method of object for JSON serialization.

    Also handle Paths.
    """

    def default(self, o):
        if isinstance(o, Path):
            # Not sure why Paths don't serialize out-of-the-box!
            # https://github.com/samuelcolvin/pydantic/issues/473
            return str(o)
        if hasattr(o, "__json__") and callable(o.__json__):
            return o.__json__()
        return super().default(o)

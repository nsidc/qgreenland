from invoke import Collection

from qgreenland.util.config.config import init_config

from . import config
from . import test


# Initialize config for the full invoke context to avoid multiple inits in one
# `inv` call. `inv` is the entrypoint in that case.
init_config()

ns = Collection()
ns.add_collection(config)
ns.add_collection(test)

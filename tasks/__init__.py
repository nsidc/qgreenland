from invoke import Collection

from . import config
from . import test

ns = Collection()
ns.add_collection(config)
ns.add_collection(test)

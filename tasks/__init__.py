from invoke import Collection

from . import config, docs
from . import test

ns = Collection()
ns.add_collection(config)
ns.add_collection(docs)
ns.add_collection(test)

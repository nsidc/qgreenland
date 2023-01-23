from invoke import Collection

from . import config, docs, env
from . import format as _format
from . import test

ns = Collection()
ns.add_collection(config)
ns.add_collection(docs)
ns.add_collection(env)
ns.add_collection(test)
ns.add_collection(_format)

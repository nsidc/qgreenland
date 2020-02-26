from invoke import Collection

from . import test
from . import version

ns = Collection()
ns.add_collection(test)
ns.add_collection(version)

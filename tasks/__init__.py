from invoke import Collection

from . import test
from . import run

ns = Collection()
ns.add_collection(test)
ns.add_collection(run)

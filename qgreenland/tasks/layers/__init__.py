from qgreenland.tasks.layers.arctic_dem import ArcticDEM
from qgreenland.tasks.layers.bedmachine import BedMachineDataset
from qgreenland.tasks.layers.coastlines import Coastlines
from qgreenland.tasks.layers.glacier_terminus import GlacierTerminus
from qgreenland.tasks.layers.velocity_mosaic import VelocityMosaic

INGEST_TASKS = {
    'arctic_dem': ArcticDEM,
    'bedmachine': BedMachineDataset,
    'coastlines': Coastlines,
    'glacier_terminus': GlacierTerminus,
    'velocity_mosaic': VelocityMosaic
}

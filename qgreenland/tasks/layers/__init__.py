from qgreenland.tasks.layers.arctic_dem import ArcticDEM
from qgreenland.tasks.layers.bedmachine import BedMachineDataset
from qgreenland.tasks.layers.glacier_terminus import GlacierTerminus
from qgreenland.tasks.layers.velocity_mosaic import VelocityMosaic
from qgreenland.tasks.layers.zipped_shapefile import ZippedShapefile

INGEST_TASKS = {
    'arctic_dem': ArcticDEM,
    'bedmachine': BedMachineDataset,
    'glacier_terminus': GlacierTerminus,
    'velocity_mosaic': VelocityMosaic,
    'zipped_shapefile': ZippedShapefile
}

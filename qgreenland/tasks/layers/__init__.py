from qgreenland.tasks.layers.arctic_dem import ArcticDEM
from qgreenland.tasks.layers.arctic_vegetation import ArcticVegetation
from qgreenland.tasks.layers.background_image import BackgroundImage
from qgreenland.tasks.layers.bedmachine import BedMachineDataset
from qgreenland.tasks.layers.glacier_terminus import GlacierTerminus
from qgreenland.tasks.layers.ice_thickness_change import IceThicknessChange
from qgreenland.tasks.layers.permaice import Permaice
from qgreenland.tasks.layers.rarred_shapefile import RarredShapefile
from qgreenland.tasks.layers.velocity_mosaic import VelocityMosaic
from qgreenland.tasks.layers.zipped_shapefile import ZippedShapefile

INGEST_TASKS = {
    'arctic_dem': ArcticDEM,
    'arctic_vegetation': ArcticVegetation,
    'background_image': BackgroundImage,
    'bedmachine': BedMachineDataset,
    'glacier_terminus': GlacierTerminus,
    'ice_thickness_change': IceThicknessChange,
    'permaice': Permaice,
    'rarred_shapefile': RarredShapefile,
    'velocity_mosaic': VelocityMosaic,
    'zipped_shapefile': ZippedShapefile
}

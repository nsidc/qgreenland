from qgreenland.tasks.layers.arctic_vegetation import ArcticVegetation
from qgreenland.tasks.layers.background_image import BackgroundImage
from qgreenland.tasks.layers.bedmachine import BedMachineDataset
from qgreenland.tasks.layers.glacier_terminus import GlacierTerminus
from qgreenland.tasks.layers.gzipped_shapefile_parts import GzippedShapefileParts
from qgreenland.tasks.layers.ice_thickness_change import IceThicknessChange
from qgreenland.tasks.layers.permaice import Permaice
from qgreenland.tasks.layers.rarred_shapefile import RarredShapefile
from qgreenland.tasks.layers.raster import Raster
from qgreenland.tasks.layers.utm_zones import UtmZones
from qgreenland.tasks.layers.velocity_mosaic import VelocityMosaic
from qgreenland.tasks.layers.zipped_shapefile import ZippedShapefile
from qgreenland.tasks.layers.arctic_circle import ArcticCircle

INGEST_TASKS = {
    'arctic_vegetation': ArcticVegetation,
    'background_image': BackgroundImage,
    'bedmachine': BedMachineDataset,
    'glacier_terminus': GlacierTerminus,
    'gzipped_shapefile_parts': GzippedShapefileParts,
    'ice_thickness_change': IceThicknessChange,
    'permaice': Permaice,
    'rarred_shapefile': RarredShapefile,
    'raster': Raster,
    'utm_zones': UtmZones,
    'velocity_mosaic': VelocityMosaic,
    'zipped_shapefile': ZippedShapefile,
    'arctic_circle': ArcticCircle,
}

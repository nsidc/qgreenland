from qgreenland.tasks.layers.arctic_vegetation import ArcticVegetation
from qgreenland.tasks.layers.background_image import BackgroundImage
from qgreenland.tasks.layers.basal_thermal_state import BasalThermalState
from qgreenland.tasks.layers.bedmachine import BedMachineDataset
from qgreenland.tasks.layers.glacier_terminus import GlacierTerminus
from qgreenland.tasks.layers.gzipped_vector_parts import GzippedVectorParts
from qgreenland.tasks.layers.ice_thickness_change import IceThicknessChange
from qgreenland.tasks.layers.local_vector import LocalVector
from qgreenland.tasks.layers.netcdf_raster import NetCdfRaster
from qgreenland.tasks.layers.online_vector import OnlineVector
from qgreenland.tasks.layers.permaice import Permaice
from qgreenland.tasks.layers.rarred_vector import RarredVector
from qgreenland.tasks.layers.raster import Raster
from qgreenland.tasks.layers.raster_calc import RasterCalc
from qgreenland.tasks.layers.utm_zones import UtmZones
from qgreenland.tasks.layers.zipped_netcdf import ZippedNetCdf
from qgreenland.tasks.layers.zipped_vector import ZippedVector

INGEST_TASKS = {
    'arctic_vegetation': ArcticVegetation,
    'background_image': BackgroundImage,
    'basal_thermal_state': BasalThermalState,
    'bedmachine': BedMachineDataset,
    'glacier_terminus': GlacierTerminus,
    'gzipped_vector_parts': GzippedVectorParts,
    'ice_thickness_change': IceThicknessChange,
    'local_vector': LocalVector,
    'netcdf_raster': NetCdfRaster,
    'online_vector': OnlineVector,
    'permaice': Permaice,
    'rarred_vector': RarredVector,
    'raster': Raster,
    'raster_calc': RasterCalc,
    'utm_zones': UtmZones,
    'zipped_netcdf': ZippedNetCdf,
    'zipped_vector': ZippedVector,
}

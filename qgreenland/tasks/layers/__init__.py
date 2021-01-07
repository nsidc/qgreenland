from qgreenland.tasks.layers.arctic_dem import ArcticDEM
from qgreenland.tasks.layers.arctic_vegetation import ArcticVegetation
from qgreenland.tasks.layers.background_image import BackgroundImage
from qgreenland.tasks.layers.basal_thermal_state import BasalThermalState
from qgreenland.tasks.layers.bedmachine import BedMachineDataset
from qgreenland.tasks.layers.delimited_text_vector import DelimitedTextVector
from qgreenland.tasks.layers.dms_gtk_topo import DmsGtkTopo
from qgreenland.tasks.layers.glacier_terminus import GlacierTerminus
from qgreenland.tasks.layers.gzipped_vector_parts import GzippedVectorParts
from qgreenland.tasks.layers.ice_thickness_change import IceThicknessChange
from qgreenland.tasks.layers.local_vector import LocalVector
from qgreenland.tasks.layers.local_zipped_netcdf_raster import LocalZippedNetCdfRaster
from qgreenland.tasks.layers.local_zipped_vector import LocalZippedVector
from qgreenland.tasks.layers.netcdf_raster import NetCdfRaster
from qgreenland.tasks.layers.ogr_remote_vector import OgrRemoteVector
from qgreenland.tasks.layers.online_vector import OnlineVector
from qgreenland.tasks.layers.racmo import Racmo
from qgreenland.tasks.layers.rarred_vector import RarredVector
from qgreenland.tasks.layers.raster import Raster
from qgreenland.tasks.layers.raster_calc import RasterCalc
from qgreenland.tasks.layers.sea_ice_age import SeaIceAge
from qgreenland.tasks.layers.surface_elevation_change import CCISurfaceElevationChange
from qgreenland.tasks.layers.velocity_mosaic import VelocityMosaic
from qgreenland.tasks.layers.zipped_netcdf import ZippedNetCdf
from qgreenland.tasks.layers.zipped_vector import ZippedVector

# TODO: Automatically generate this list from some Python metadata?
INGEST_TASKS = {
    'arctic_dem': ArcticDEM,
    'arctic_vegetation': ArcticVegetation,
    'background_image': BackgroundImage,
    'basal_thermal_state': BasalThermalState,
    'bedmachine': BedMachineDataset,
    'dms_gtk_topo': DmsGtkTopo,
    'delimited_text_points_vector': DelimitedTextVector,
    'glacier_terminus': GlacierTerminus,
    'gzipped_vector_parts': GzippedVectorParts,
    'ice_thickness_change': IceThicknessChange,
    'local_vector': LocalVector,
    'local_zipped_vector': LocalZippedVector,
    'local_zipped_netcdf_raster': LocalZippedNetCdfRaster,
    'netcdf_raster': NetCdfRaster,
    'ogr_remote_vector': OgrRemoteVector,
    'online_vector': OnlineVector,
    'racmo': Racmo,
    'rarred_vector': RarredVector,
    'raster': Raster,
    'raster_calc': RasterCalc,
    'sea_ice_age': SeaIceAge,
    'cci_surface_elevation_change': CCISurfaceElevationChange,
    'velocity_mosaic': VelocityMosaic,
    'zipped_netcdf': ZippedNetCdf,
    'zipped_vector': ZippedVector,
}

from qgreenland.models.config.asset import CmrAsset
from qgreenland.models.config.dataset import Dataset

grimp_annual_ice_velocity = Dataset(
    id="grimp_annual_ice_velocity",
    assets=[
        # GL_vel_mosaic_Annual_01Dec20_30Nov21_{variable}_v04.0.tif
        CmrAsset(
            id="only",
            granule_ur="SC:NSIDC-0725.004:243900064",
            collection_concept_id="C2386646586-NSIDC_ECS",
        ),
    ],
    metadata={
        "title": "MEaSUREs Greenland Annual Ice Sheet Velocity Mosaics from SAR and Landsat, Version 4",
        "abstract": """
This data set, part of the NASA Making Earth System Data Records for Use in
Research Environments (MEaSUREs) program, contains annual ice velocity mosaics
for the Greenland Ice Sheet derived from Synthetic Aperture Radar (SAR) data
obtained by the German Space Agency's TerraSAR-X/TanDEM-X (TSX/TDX) and the
European Space Agency's Copernicus Sentinel-1A and -1B satellites, and from the
US Geological Survey's Landsat 8 optical imagery for years 2015 to 2021. See
Greenland Ice Mapping Project (GrIMP) website for related data:
http://nsidc.org/data/measures/gimp.
""",
        "citation": {
            "text": """
Joughin, I. (2022). MEaSUREs Greenland Annual Ice Sheet Velocity Mosaics from
SAR and Landsat, Version 4 [Data Set]. Boulder, Colorado USA. NASA National Snow
and Ice Data Center Distributed Active Archive
Center. https://doi.org/10.5067/RS8GFZ848ZU9. {{date_accessed}}
""",
            "url": "https://doi.org/10.5067/RS8GFZ848ZU9",
        },
    },
)

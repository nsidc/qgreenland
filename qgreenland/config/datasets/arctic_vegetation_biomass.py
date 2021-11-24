from qgreenland.models.config.asset import CmrAsset
from qgreenland.models.config.dataset import Dataset


arctic_vegetation_biomass_2010 = Dataset(
    id='arctic_vegetation_biomass_2010',
    assets=[
        CmrAsset(
            id='only',
            granule_ur='Arctic_Vegetation_Maps.aga_circumpolar_avhrr_biomass_2010.tif',
            collection_concept_id='C2170968604-ORNL_CLOUD',
        ),
    ],
    metadata={
        'title': 'Circumpolar Arctic Vegetation, Geobotanical, Physiographic Maps, 1982-2003',
        'abstract': (
            """The broader data set provides the spatial distributions of
            vegetation types, geobotanical characteristics, and physiographic
            features for the circumpolar Arctic tundra biome for the period
            1982-2003. Specific attributes include dominant vegetation,
            bioclimate subzones, floristic subprovinces, landscape types, lake
            coverage, Arctic treeline, elevation, and substrate chemistry data.
            Vegetation indices, trends, and biomass estimate products for the
            circumpolar Arctic through 2010 are also provided. QGreenland
            displays the 2010 vegetation biomass in kilograms per square meter.
            Users can look to the source information for additional data."""
        ),
        'citation': {
            'text': (
                """Walker, D.A., and M.K. Raynolds. 2018. Circumpolar Arctic
                Vegetation, Geobotanical, Physiographic Maps, 1982-2003. ORNL
                DAAC, Oak Ridge, Tennessee, USA.
                https://doi.org/10.3334/ORNLDAAC/1323"""
            ),
            'url': 'https://doi.org/10.3334/ORNLDAAC/1323',
        },
    },
)

from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset


streams_outlets_basins = Dataset(
    id='streams_outlets_basins',
    assets=[
        HttpAsset(
            id='ice_basins',
            urls=[
                'https://dataverse01.geus.dk/api/access/datafile/283?gbrecs=true',
            ],
        ),
        HttpAsset(
            id='land_basins',
            urls=[
                'https://dataverse01.geus.dk/api/access/datafile/286?gbrecs=true',
            ],
        ),
        HttpAsset(
            id='ice_basins_filled',
            urls=[
                'https://dataverse01.geus.dk/api/access/datafile/278?gbrecs=true',
            ],
        ),
        HttpAsset(
            id='land_basins_filled',
            urls=[
                'https://dataverse01.geus.dk/api/access/datafile/279?gbrecs=true',
            ],
        ),
        HttpAsset(
            id='ice_outlets',
            urls=[
                'https://dataverse01.geus.dk/api/access/datafile/276?gbrecs=true',
            ],
        ),
        HttpAsset(
            id='land_outlets',
            urls=[
                'https://dataverse01.geus.dk/api/access/datafile/285?gbrecs=true',
            ],
        ),
        HttpAsset(
            id='ice_streams',
            urls=[
                'https://dataverse01.geus.dk/api/access/datafile/277?gbrecs=true',
            ],
        ),
        HttpAsset(
            id='land_streams',
            urls=[
                'https://dataverse01.geus.dk/api/access/datafile/275?gbrecs=true',
            ],
        ),
    ],
    metadata={
        'title': 'Streams, Outlets, and Basins [k=1.0]',
        'abstract': (
            """Greenland land and ice sheet streams, outlets, and basins.
            Routing assumes k = 1.0 for subglacial routing algorithm. Further
            details from citation publication: The static products (streams,
            outlets, and basins) are derived from an ice sheet surface digital
            elevation model (DEM), an ice sheet bed DEM, an ice sheet mask, the
            land surface DEM, and an ocean mask. For the surface DEM, we use
            ArcticDEM v7 100 m (Porter et al., 2018). Subglacial routing uses
            ArcticDEM and ice thickness from BedMachine v3 (Morlighem et al.,
            2017a,b). Both DEMs are referenced to the WGS84 ellipsoid. For the
            ice mask we use the Programme for Monitoring of the Greenland Ice
            Sheet (PROMICE) ice extent (Citterio and Ahlstrøm, 2013). For the
            ocean mask we use the Making Earth System Data Records for Use in
            Research Environments (MEaSUREs) Greenland Ice Mapping Project
            (GIMP) Land Ice and Ocean Classification Mask, Version 1 (Howat,
            2017b; Howat et al., 2014). Full references available in linked
            publication."""
        ),
        'citation': {
            'text': (
                """Mankoff, Ken, 2020, "Streams, Outlets, and Basins [k=1.0]",
                https://doi.org/10.22008/FK2/XKQVL7, GEUS, V1,
                UNF:6:SweJ3D918I+g+OYxdPDa4g== [fileUNF] """
            ),
            'url': 'https://doi.org/10.22008/FK2/XKQVL7',
        },
    },
)

from qgreenland.models.config.asset import ConfigDatasetHttpAsset
from qgreenland.models.config.dataset import ConfigDataset


bathymetry = ConfigDataset(
    id='bathymetry',
    assets=[
        ConfigDatasetHttpAsset(
            id='only',
            urls=[
                'https://ftp.maps.canada.ca/pub/nrcan_rncan/publications/STPublications_PublicationsST/287/287868/as_2159.zip',
            ],
        ),
    ],
    metadata={
        'title': " ",
        'abstract': (
            """This dataset includes linear features that represent bathymetric contours recorded in metres, 
            derived from the International Bathymetric Chart of the Arctic Ocean (IBCAO, 2003) and locally modified by T. 
            Brent GSC/NRCan. The data has been modified in some areas to avoid registration errors with the hydrology 
            (Hydrology_arc and Hydrology_poly)."""
        ),
        'citation': {
            'text': (
                """Harrison, J.C., St-Onge, M.R., Petrov, O.V., Strelnikov,
                S.I., Lopatin, B.G., Wilson, F.H., Tella, S., Paul, D., Lynds,
                T., Shokalsky, S.P., Hults, C.K., Bergman, S., Jepsen, H.F., and
                Solli, A., 2011. Geological map of the Arctic / Carte gologique
                de l'Arctique; Geological Survey of Canada, Map 2159A, scale 1:5
                000 000."""
            ),
            'url': 'https://doi.org/10.4095/287868',
        },
    },
)

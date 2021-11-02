from qgreenland.models.config.asset import ConfigDatasetHttpAsset
from qgreenland.models.config.dataset import ConfigDataset


greenland_onshore_planar = ConfigDataset(
    id='greenland_onshore_planar',
    assets=[
        ConfigDatasetHttpAsset(
            id='only',
            urls=[
                'https://ftp.maps.canada.ca/pub/nrcan_rncan/publications/STPublications_PublicationsST/287/287868/as_2159.zip',
            ],
        ),
    ],
    metadata={
        'title': "Onshore faults for the landmass of Greenland",
        'abstract': (
            """This dataset contains onshore faults for the landmass and islands of Greenland."""
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

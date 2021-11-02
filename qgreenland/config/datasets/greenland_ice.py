from qgreenland.models.config.asset import ConfigDatasetHttpAsset
from qgreenland.models.config.dataset import ConfigDataset


greenland_ice = ConfigDataset(
    id='greenland_ice',
    assets=[
        ConfigDatasetHttpAsset(
            id='only',
            urls=[
                'https://ftp.maps.canada.ca/pub/nrcan_rncan/publications/STPublications_PublicationsST/287/287868/as_2159.zip',
            ],
        ),
    ],
    metadata={
        'title': "Onshore ice isopachs for the landmass of Greenland",
        'abstract': (
            """This linear feature class contains onshore ice isopachs for the landmass of Greenland. 
            The isopochs illustrate the variation in ice thickness with a contour interval of 250 metres. 
            The data set was provided by the Geological Survey of Denmark and Greenland."""
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

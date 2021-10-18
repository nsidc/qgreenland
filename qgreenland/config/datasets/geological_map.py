from qgreenland.models.config.asset import ConfigDatasetHttpAsset
from qgreenland.models.config.dataset import ConfigDataset


geological_map = ConfigDataset(
    id='geological_map',
    assets=[
        ConfigDatasetHttpAsset(
            id='only',
            urls=[
                'https://ftp.maps.canada.ca/pub/nrcan_rncan/publications/STPublications_PublicationsST/287/287868/as_2159.zip',
            ],
        ),
    ],
    metadata={
        'title': "Geological map of the Arctic / Carte gologique de l'Arctique",
        'abstract': (
            """As part of the International Polar Year (IPY) 2007-08 and 2008-09
            activities, and related objectives of the Commission for the
            Geological Map of the World (CGMW), nations of the circumpolar
            Arctic have co-operated to produce a new bedrock geology map and
            related digital map database at a scale of 1:5 000 000. The map,
            released in north polar stereographic projection using the World
            Geodetic System (WGS) 84 datum, includes complete geological and
            physiographic coverage of all onshore and offshore bedrock areas
            north of latitude 60 degrees north."""
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

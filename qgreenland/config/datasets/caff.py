from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

caff_murre_colonies = Dataset(
    id="caff_murre_colonies",
    assets=[
        HttpAsset(
            id="only",
            urls=[
                "https://geo.abds.is/geonetwork/srv/api/records/8942d6b5-6060-412b-b696-0aa583965317/attachments/MurreColonies.zip",
            ],
        ),
    ],
    metadata={
        "title": "Murres as indicators of a changing Arctic.",
        "abstract": (
            """The two species of murres, thick-billed Uria lomvia and common
            U. aalge, both have circumpolar distributions, breeding in Arctic,
            sub-Arctic and temperate seas from alifornia and N Spain to N
            Greenland, high Arctic Canada, Svalbard, Franz Josef Land and Novaya
            Zemlya."""
        ),
        "citation": {
            "text": (
                """Conservation of Arctic Flora and Fauna, CAFF 2013 - Akureyri
                . Arctic Biodiversity Assessment. Status and Trends in Arctic
                biodiversity. - Birds(Chapter 4) page 163."""
            ),
            "url": "https://geo.abds.is/geonetwork/srv/eng/catalog.search#/metadata/8942d6b5-6060-412b-b696-0aa583965317",
        },
    },
)

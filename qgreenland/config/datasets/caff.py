from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

caff_murre_colonies = Dataset(
    id="caff_murre_colonies",
    assets=[
        HttpAsset(
            id="only",
            urls=[
                "https://abds.is/index.php/publications/the-distribution-of-thick-billed-and-common-murre-colonies-in-the-north/download",
            ],
        ),
    ],
    metadata={
        "title": "The distribution of thick-billed and common murre colonies in the North.",
        "abstract": (
            """Murres are among the most abundant seabirds in the Northern
            Hemisphere with a population in excess of ten million adults. No
            obvious global trend has been identified but the majority of
            regional populations have shown declines over the past three
            decades. While they are currently abundant, climate change is
            projected to pose problems to murres in the future, especially for
            the more northern species, the thick-billed murre, which is strongly
            associated with sea ice. Other threats include fisheries
            interactions, over-exploitation, contaminants, and oil spills, the
            latter becoming more important if climate change expands shipping
            and hydrocarbon development in the Arctic."""
        ),
        "citation": {
            "text": (
                """Arctic Biodiversity Trends 2010 – Selected indicators of
                change. CAFF International Secretariat, Akureyri, Iceland.May
                2010."""
            ),
            "url": "https://abds.is/index.php/publications/species/the-distribution-of-thick-billed-and-common-murre-colonies-in-the-north",
        },
    },
)

from qgreenland.models.config.asset import ConfigDatasetHttpAsset
from qgreenland.models.config.dataset import ConfigDataset


caff_murre_colonies = ConfigDataset(
    id='caff_murre_colonies',
    assets=[
        ConfigDatasetHttpAsset(
            id='only',
            urls=[
                'https://abds.is/index.php/publications/the-distribution-of-thick-billed-and-common-murre-colonies-in-the-north/download',
            ],
        ),
    ],
    metadata={
        'title': 'The distribution of thick-billed and common murre colonies in the North.',
        'abstract': (
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
        'citation': {
            'text': (
                """Arctic Biodiversity Trends 2010 – Selected indicators of
                change. CAFF International Secretariat, Akureyri, Iceland.May
                2010."""
            ),
            'url': 'https://abds.is/index.php/publications/species/the-distribution-of-thick-billed-and-common-murre-colonies-in-the-north',
        },
    },
)

caff_char = ConfigDataset(
    id='caff_char',
    assets=[
        ConfigDatasetHttpAsset(
            id='only',
            urls=[
                'http://geo.abds.is/geonetwork/srv/api/records/4dc7f9b6-b553-445a-a8a3-a0ece574e8ce/attachments/Arctic_Char_2010.zip',
            ],
        ),
    ],
    metadata={
        'title': 'Circumpolar distribution of arctic char species complex Salvelinus alpinus, and related species',
        'abstract': (
            """Circumpolar distribution of Arctic Char species complex
            Salvelinus alpinus, and related species.  Arctic Biodiversity
            Assessment, Chapter 6: Fishes: http://www.caff.is/assessment-series/
            10-arctic-biodiversity-assessment/211-arctic-biodiversity-assessment
            -2013-chapter-6-fishes"""
        ),
        'citation': {
            'text': (
                """Conservation of Arctic Flora and Fauna (CAFF www.caff.is)
                working group of the Arctic Council"""
            ),
            'url': 'http://geo.abds.is/geonetwork/srv/eng/catalog.search#/metadata/4dc7f9b6-b553-445a-a8a3-a0ece574e8ce',
        },
    },
)

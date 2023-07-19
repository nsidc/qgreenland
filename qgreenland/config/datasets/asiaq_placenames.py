from qgreenland.models.config.asset import ManualAsset
from qgreenland.models.config.dataset import Dataset

asiaq_private_placenames = Dataset(
    id="asiaq_private_placenames",
    assets=[
        ManualAsset(
            id="only",
            access_instructions="""Provided by Eva Mätzler via email as a zipped
collection of data '20201112_Oqaasileriffik_place-name register.zip'. See
scripts/private-archive-preprocess/eva_placenames/README.md (at QGreenland
GitHub: https://github.com/nsidc/qgreenland) for preprocessing steps.""",
        ),
    ],
    metadata={
        "title": "Place names",
        "abstract": """Place names as provided by Asiaq Greenland Survey,
December 2020. Translation for data fields provided by Arnaq B. Johansen,
Greenland Project Manager in Collection of Place Names (January 2021).""",
        "citation": {
            "text": "Place names, Asiaq Greenland Survey, December 2020",
            "url": "",
        },
    },
)

from qgreenland.models.config.asset import ConfigDatasetManualAsset
from qgreenland.models.config.dataset import ConfigDataset


asiaq_private_placenames = ConfigDataset(
    id='asiaq_private_placenames',
    assets=[
        ConfigDatasetManualAsset(
            id='only',
            access_instructions="""Provided by Eva Mätzler via email as a zipped
collection of data '20201112_Oqaasileriffik_place-name register.zip'. See
scripts/private-archive-preprocess/eva_placenames/README.md (at QGreenland
GitHub: https://github.com/nsidc/qgreenland) for preprocessing steps.""",
        ),
    ],
    metadata={
        'title': 'Place names',
        'abstract': """Place names as provided by Asiaq Greenland Survey,
December 2020. Translation for data fields provided by Arnaq B. Johansen,
Greenland Project Manager in Collection of Place Names (January 2021).

QGreenland Team - Noted Data Issues

* East Greenland: Ikkatteq (correctly spelled ‘Ikateq’) is an abandoned airstrip
and is not populated.

* Near Ittoqqortoormiit: Uunartoq and Ittaajimmiit are both abandoned.

* Westcoast of Greenland, near Paamiut: Ivittuut is abandoned, Narsalik
was abandoned in 1997.

* South Greenland: Qaqortoq is placed twice - two dots next to each other.

* Near Qaanaaq: Qeqertarsuaq and Moriusaq are abandoned.

* Near Upernavik: Tussaaq is an abandoned settlement.

* Near Uummannaq: Illorsuit and Nuugaatsiaq are two recently abandoned
settlements (2017) due a massive landslide and subsequent tsunami.

* Kangerlussuaq (west coast): Is not indicated on the map.

* West: Aasiaat is placed twice - two dots next to each other.""",
        'citation': {
            'text': 'Place names, Asiaq Greenland Survey, December 2020',
            'url': '',
        },
    },
)

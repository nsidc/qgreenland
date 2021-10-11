from qgreenland.models.config.asset import ConfigDatasetOgrRemoteAsset
from qgreenland.models.config.dataset import ConfigDataset


nunagis_pop2019_municipalities = ConfigDataset(
    id='nunagis_pop2019_municipalities',
    assets=[
        ConfigDatasetOgrRemoteAsset(
            id='only',
            query_url='https://kort.nunagis.gl/server/rest/services/Hosted/POP2019_Municipalities/FeatureServer/0/query/?f=json&where=true&outFields=*&orderByFields=pop_municipality_2019_objectid+ASC',
        ),
    ],
    metadata={
        'title': 'Municipalities with Population',
        'abstract': (
            """Greenland municipality boundaries. Data includes information on
            2019 municipality population and the municipality population as a
            percent of total Greenland population."""
        ),
        'citation': {
            'text': (
                """NunaGIS (2020). Municipalities by population numbers in 2019,
                Greenland. Web:
                  https://kort.nunagis.gl/portal/home/item.html?id=b70a43b814e84
                78c9514208548ca5f61.
                Date accessed: {{date_accessed}}."""
            ),
            'url': 'https://kort.nunagis.gl/portal/home/item.html?id=b70a43b814e8478c9514208548ca5f61',
        },
    },
)

from qgreenland.models.config.asset import ConfigDatasetOgrRemoteAsset
from qgreenland.models.config.dataset import ConfigDataset


nunagis_protected_areas = ConfigDataset(
    id='nunagis_protected_areas',
    assets=[
        ConfigDatasetOgrRemoteAsset(
            id='only',
            query_url='https://kort.nunagis.gl/server/rest/services/Hosted/Bird_important_areas/FeatureServer/0/query?f=json&where=true&outFields=*&orderByFields=fid0+ASC',
        ),
    ],
    metadata={
        'title': 'NunaGIS data server protected area data',
        'abstract': (
            """The NunaGIS data server provides a range of datasets on animal
            areas of importance and protected areas. These data are used to
            populate the following QGreenland data layers: Walrus Protected
            Areas, Goose Protected Areas, Caribou Calving Areas, Beluga Areas,
            Bird Protected Areas, Thickbilled Murre Breeding Colony 5km Zones,
            Seabird Breeding Colonies, Eider Protected Areas, Murre Group 1 km
            Zones, Musk Oxen Calving Areas, Narwhal Areas, and Polar Bear
            Breeding Areas."""
        ),
        'citation': {
            'text': (
                """NunaGIS (2020). Date accessed: {{date_accessed}}."""
            ),
            'url': 'https://kort.nunagis.gl/server/rest/services/Hosted',
        },
    },
)

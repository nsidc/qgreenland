from qgreenland.models.config.asset import ConfigDatasetRepositoryAsset
from qgreenland.models.config.dataset import ConfigDataset


gem_research_stations = ConfigDataset(
    id='gem_research_stations',
    assets=[
        ConfigDatasetRepositoryAsset(
            id='only',
            filepath='{assets_dir}/gem_research_stations.geojson',
        ),
    ],
    metadata={
        'title': 'Greenland Ecosystem Monitoring - Location and Description of Research Stations',
        'abstract': (
            """Greenland Ecosystem Monitoring (GEM) is an integrated monitoring
            and long-term research programme on ecosystems and climate change
            effects and feedbacks in the Arctic. Since 1995 the programme has
            established a coherent and integrated understanding of the
            functioning of ecosystems in a highly variable climate, which is
            based upon a comprehensive, long-term inter-disciplinary data
            collection carried out by Danish and Greenlandic monitoring and
            research institutions.

            The GEM Programme puts around 75 scientists in the field annually to
            collect data on ecosystem and climate change in Greenland. The data
            base currently covers data from monitoring programmes from
            Zackenberg (1995-), Kobbefjord at Nuuk (2007-) and Disko (2017-).
            The well over 1000 parameters are freely available via the GEM
            Database and used by GEM participants and external scientists to
            produce scientific papers, scientific assessments, advisory reports,
            etc.

            Full station descriptions were manually added by QGreenland from the
            'Station Link' associated with each feature."""
        ),
        'citation': {
            'text': (
                """Roemer, Jonas K. (2020). Greenland Ecosystem Monitoring -
                Location and Description of Research Stations (Version 1.0).
                Zenodo. http://doi.org/10.5281/zenodo.3991670"""
            ),
            'url': 'http://doi.org/10.5281/zenodo.3991670',
        },
    },
)

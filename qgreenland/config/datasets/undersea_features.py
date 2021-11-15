from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset


undersea_features = Dataset(
    id='undersea_features',
    assets=[
        HttpAsset(
            id='only',
            urls=[
                'https://www.ngdc.noaa.gov/gazetteer/feature/export?aoi=POLYGON%28%28-162.82882+39.14360%2C+120.79574+45.17504%2C+-1.80233+31.69553%2C+-68.42289+32.69612%2C+-162.82882+39.14360%29%29&name=&featureType=&proposerId=&discovererId=&meeting=&status=&format=shapefile',
            ],
        ),
    ],
    metadata={
        'title': 'IHO-IOC GEBCO Gazetteer of Undersea Feature Names',
        'abstract': (
            """The General Bathymetric Chart of the Oceans (GEBCO) Sub-Committee
            on Undersea Feature Names (SCUFN) maintains and makes available a
            digital gazetteer of the names, generic feature type, and geographic
            position of features on the seafloor. The gazetteer is available to
            view and download (http://www.ngdc.noaa.gov/gazetteer/) via a web
            map application, hosted by the International Hydrographic
            Organization Data Centre for Digital Bathymetry (IHO DCDB)
            co-located with the US National Centers for Environmental
            Information (NCEI)."""
        ),
        'citation': {
            'text': (
                """IHO-IOC GEBCO Gazetteer of Undersea Feature Names,
                www.gebco.net"""
            ),
            'url': 'https://www.gebco.net/data_and_products/undersea_feature_names/',
        },
    },
)

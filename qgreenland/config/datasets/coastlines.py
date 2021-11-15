from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset


bas_coastlines = Dataset(
    id='bas_coastlines',
    assets=[
        HttpAsset(
            id='only',
            urls=[
                'https://ramadda.data.bas.ac.uk/repository/entry/get/Greenland_coast.zip?entryid=synth:8cecde06-8474-4b58-a9cb-b820fa4c9429:L0dyZWVubGFuZF9jb2FzdC56aXA=',
            ],
        ),
    ],
    metadata={
        'title': (
            'The coastline of Kalaallit Nunaat/ Greenland available as a shapefile'
            ' and geopackage, covering the main land and islands, with glacier'
            ' fronts updated as of 2017.'
        ),
        'abstract': (
            """A coastline of Kalaallit Nunaat/ Greenland covering all land and
            islands, produced in 2017 for the BAS map 'Greenland and the
            European Arctic'. The dataset was produced by extracting the land
            mask from the Greenland BedMachine dataset and manually editing
            anomalous data. Some missing islands were added and glacier fronts
            were updated using 2017 satellite imagery. The dataset can be used
            for cartography, analysis and as a mask, amongst other uses. At very
            large scales, the data will appear angular due to the nature of
            being extracted from a raster with 150 m cell size, but the dataset
            should be suitable for use at most scales and can be edited by the
            user to exclude very small islands if required. The projection of
            the dataset is WGS 84 NSIDC Sea Ice Polar Stereographic North, EPSG
            3413. The dataset does not promise to cover every island and
            coastlines were digitised using the data creator's interpretation of
            the landforms from the images."""
        ),
        'citation': {
            'text': (
                """Gerrish, L. (2020). The coastline of Kalaallit Nunaat/
                Greenland available as a shapefile and geopackage, covering the
                main land and islands, with glacier fronts updated as of 2017.
                (Version 1.0) [Data set]. UK Polar Data Centre, Natural
                Environment Research Council, UK Research & Innovation."""
            ),
            'url': 'https://doi.org/10.5285/8cecde06-8474-4b58-a9cb-b820fa4c9429',
        },
    },
)

coastlines = Dataset(
    id='coastlines',
    assets=[
        HttpAsset(
            id='only',
            urls=[
                'https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/physical/ne_10m_coastline.zip',
            ],
        ),
    ],
    metadata={
        'title': 'Natural Earth Coastlines (10m)',
        'abstract': (
            """Natural Earth Coastlines (Public Domain)."""
        ),
        'citation': {
            'text': (
                """Made with Natural Earth"""
            ),
            'url': 'https://github.com/nvkelso/natural-earth-vector/blob/master/LICENSE.md',
        },
    },
)

from qgreenland.models.config.asset import (
    CommandAsset,
    HttpAsset,
)
from qgreenland.models.config.dataset import Dataset


nunagis_pop2019_municipalities = Dataset(
    id='nunagis_pop2019_municipalities',
    assets=[
        CommandAsset(
            id='only',
            args=[
                'ogr2ogr',
                '-oo', 'FEATURE_SERVER_PAGING=YES',
                '{output_dir}/fetched.geojson',
                'https://kort.nunagis.gl/server/rest/services/Hosted/POP2019_Municipalities/FeatureServer/0/query/?f=json&where=true&outFields=*&orderByFields=pop_municipality_2019_objectid+ASC',
            ],
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

ne_states_provinces = Dataset(
    id='ne_states_provinces',
    assets=[
        HttpAsset(
            id='only',
            urls=[
                'https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_admin_1_states_provinces.zip',
            ],
        ),
    ],
    metadata={
        'title': 'Admin 1 – States, Provinces',
        'abstract': (
            """Internal, first-order administrative boundaries and polygons for
            all but a few tiny countries. Includes name attributes (including
            diacritical marks), name variants, and some statistical codes (FIPS,
            ISO, HASC)."""
        ),
        'citation': {
            'text': (
                """Made with Natural Earth"""
            ),
            'url': 'https://github.com/nvkelso/natural-earth-vector/blob/master/LICENSE.md',
        },
    },
)

ne_countries = Dataset(
    id='ne_countries',
    assets=[
        HttpAsset(
            id='only',
            urls=[
                'https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_admin_0_countries.zip',
            ],
        ),
    ],
    metadata={
        'title': 'Admin 0 – Countries',
        'abstract': (
            """Countries distinguish between metropolitan (homeland) and
            independent and semi-independent portions of sovereign states. If
            you want to see the dependent overseas regions broken out (like in
            ISO codes, see France for example), use map units instead.

            Each country is coded with a world region that roughly follows the
            United Nations setup.

            Countries are coded with standard ISO and FIPS codes. French INSEE
            codes are also included.

            Includes some thematic data from the United Nations, U.S. Central
            Intelligence Agency, and elsewhere."""
        ),
        'citation': {
            'text': (
                """Made with Natural Earth"""
            ),
            'url': 'https://github.com/nvkelso/natural-earth-vector/blob/master/LICENSE.md',
        },
    },
)

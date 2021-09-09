from qgreenland.models.config.asset import ConfigDatasetOnlineAsset
from qgreenland.models.config.dataset import ConfigDataset


image_mosaic = ConfigDataset(
    id='image_mosaic',
    assets=[
        ConfigDatasetOnlineAsset(
            id='2019',
            provider='gdal',
            url=(
                '/vsicurl/http://its-live-data.jpl.nasa.gov.s3.amazonaws.com/'
                'rgb_mosaics/GRE2/Greenlandmedian_Aug_2019.vrt'
            ),
        ),
        ConfigDatasetOnlineAsset(
            id='2015',
            provider='gdal',
            url=(
                '/vsicurl/http://its-live-data.jpl.nasa.gov.s3.amazonaws.com/'
                'rgb_mosaics/GRE2/Greenlandmedian_Aug_2019.vrt'
            ),
        ),
    ],
    # TODO: Switch to class instantiation. Makes it easier to differentiate keys
    # from values in this big wall-of-string.
    metadata={
        'title': 'Sentinel-2 Imagery Mosaics',
        # Editability matters most, so we use """triple-quote strings""".
        'abstract': """
Abstract for reference publication: Each summer, surface melting of the
margin of the Greenland Ice Sheet exposes a distinctive visible
stratigraphy that is related to past variability in subaerial dust
deposition across the accumulation zone and subsequent ice flow toward
the margin. Here we map this surface stratigraphy along the northern
margin of the ice sheet using mosaicked Sentinel-2 multispectral
satellite imagery from the end of the 2019 melt season and
finer-resolution WorldView-2/3 imagery for smaller regions of interest.
We trace three distinct transitions in apparent dust concentration and
the top of a darker basal layer. The three dust transitions have been
identified previously as representing late-Pleistocene climatic
transitions, allowing us to develop a coarse margin chronostratigraphy
for northern Greenland. Substantial folding of late-Pleistocene
stratigraphy is observed but uncommon. The oldest conformal
surface-exposed ice in northern Greenland is likely located adjacent to
Warming Land and may be up to ~55 thousand years old. Basal ice is
commonly exposed hundreds of metres from the ice margin and may
indicate a widespread frozen basal thermal state. We conclude that the
ice margin across northern Greenland offers multiple opportunities to
recover paleoclimatically distinct ice relative to previously studied
regions in southwestern Greenland.

QGreenland displays 2015 and 2019 Sentinel-2 mosaics as online-only
access layers.""",
        'citation': {
            'text': """
MacGregor JA, Fahnestock MA, Colgan WT, Larsen NK, Kjeldsen KK, Welker
JM (2020). The age of surface-exposed ice along the northern margin of
the Greenland Ice Sheet. Journal of Glaciology 66(258), 667–684.
https://doi.org/10.1017/jog.2020.62""",
            'url': 'https://doi.org/10.1017/jog.2020.62',
        },
    },
)

sea_ice_index = ConfigDataset(
    id='sea_ice_index',
    assets=[
        ConfigDatasetOnlineAsset(
            id='monthly_polyline_n',
            provider='gdal',
            # Whitespace matters most, so we use implicit string concatenation
            url=(
                "pagingEnabled='true' preferCoordinatesForWfsT11='false'"
                " restrictToRequestBBOX='1' srsname='EPSG:3413'"
                " typename='NSIDC:g02135_polyline_n'"
                " url='https://nsidc.org/api/mapservices/NSIDC/wfs'"
                " url='https://nsidc.org/api/mapservices/NSIDC/wfs?version=1.1.0'"
                " version='auto'"
            ),
        ),
    ],
    metadata={
        'title': 'Sea Ice Index, Version 3',
        'abstract': """
The Sea Ice Index provides a quick look at Arctic- and Antarctic-wide
changes in sea ice. It is a source for consistent, up-to-date sea ice
extent and concentration images, in PNG format, and data values, in
GeoTIFF and ASCII text files, from November 1978 to the present. Sea Ice
Index images also depict trends and anomalies in ice cover calculated
using a 30-year reference period of 1981 through 2010.

The images and data are produced in a consistent way that makes the
Index time-series appropriate for use when looking at long-term trends
in sea ice cover. Both monthly and daily products are
available. However, monthly products are better to use for long-term
trend analysis because errors in the daily product tend to be averaged
out in the monthly product and because day-to-day variations are often
the result of short-term weather.""",
        'citation': {
            'text': """
Fetterer, F., K. Knowles, W. N. Meier, M. Savoie, and
A. K. Windnagel. 2017, updated daily. Sea Ice Index, Version 3. Boulder,
Colorado USA. NSIDC: National Snow and Ice Data Center. doi:
https://doi.org/10.7265/N5K072F8. 2020-08-06.""",
            'url': 'https://nsidc.org/data/g02135',
        },
    },
)

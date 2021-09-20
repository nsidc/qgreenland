from qgreenland.models.config.asset import ConfigDatasetManualAsset
from qgreenland.models.config.dataset import ConfigDataset


supraglacial_lakes = ConfigDataset(
    id='esa_cci_supraglacial_lakes',
    assets=[
        ConfigDatasetManualAsset(
            id='only',
            access_instructions=inspect.cleandoc(
                """Dataset can be found on the European Space Agency (ESA)
                Climate Change Initiative (CCI) products website
                (http://products.esa-icesheets-cci.org). Data are free to
                download after simple registration requiring `first.last` name
                and `affiliation`. No password is required."""
            ),
        ),
    ],
    metadata={
        'title': """ESA Greenland Ice Sheet CCI, Supraglacial Lakes from
Sentinel-2""",
        'abstract': """Supraglacial Lake vectors for select areas of interest
(AOI) on the Greenland Ice Sheet produced using Sentinel-2.

Version 1.1 includes:

AOI:
*Sermeq Kujalleq (Jakobshavn Isbræ)

Time-period:
*2019/05/01-2019/10/01

For general background information see
http://esa-icesheets-greenland-cci.org""",
        'citation': {
            'text': """Data are produced by Penelope How, Alexandra Messerli,
and Eva Mätzler (Department of Remote Sensing, Asiaq Greenland Survey)""",
            'url': (
                'http://products.esa-icesheets-cci.org/products/details/'
                'greenland_sgl_s2_20190501_20191001_jakobshavn_v1_1.zip/'
            ),
        },
    },
)

surface_elevation_change = ConfigDataset(
    id='esa_cci_surface_elevation_change',
    assets=[
        ConfigDatasetManualAsset(
            id='only',
            access_instructions="""Dataset can be found on the European Space
Agency (ESA) Climate Change Initiative (CCI) products website
(http://products.esa-icesheets-cci.org). Data are free to download after simple
registration requiring `first.last` name and `affiliation`. No password is
required.

Once the `cci_sec_2020.tar.gz` file is downloaded, use the supplied
`scripts/esa_cci_surface_elevation_change/preprocess.sh` script to uncompress
the data.""",
        ),
    ],
    metadata={
        'title': """1992-2020 Greenland surface elevation change from ERS-1,
ERS-2, ENVISAT, Cryosat-2, and Sentinel-3 data, at 5-years means""",
        'abstract': """Data are based on the European Space Agency's Ku-band
radar satellite level-2 data products.  Given the longer time span of operation
of the satellites, the data are provided at a five-year mean.

The algorithms used to derive the product are explained in detail in Simonsen
and Sørensen (2017), and Sørensen et al. (2018). The approach used here is the
most optimal combination of the XO-, TR-, and PF-algorithm; the data are
corrected for both backscatter and leading-edge width, and solved at 1 km grid
resolution and averaged in the post-processing to 5 km grid resolution by
ordinary kriging.

Reference:
Simonsen, S. B., and Sørensen, L. S.  (2017) ‘Implications of changing
scattering properties on Greenland ice sheet volume change from Cryosat-2
altimetry’, Remote Sensing of Environment.  Elsevier Inc., 190, pp.  207–216.
DOI: 10.1016/j.rse.2016.12.012.

Sørensen, L. S., Simonsen, S.  B., Forsberg, R., Khvorostovsky, K., Meister, R.,
and Engdahl, M. E.  (2018) '25 years of elevation changes of the Greenland Ice
Sheet from ERS, Envisat, and CryoSat-2 radar altimetry', Earth and Planetary
Science Letters, 495, pp. 234-241 DOI: 10.1016/j.epsl.2018.05.015""",
        'citation': {
            'text': """ESA. (2020) 1992-2020 Greenland SEC from ERS-1, ERS-2,
ENVISAT, Cryosat-2, and Sentinel-3 data, at 5-year means. Greenland Ice Sheet
CCI Products.""",
            'url': (
                'http://products.esa-icesheets-cci.org/products/details/'
                'cci_sec_2020.tar.gz/'
            ),
        },
    },
)

ice_sheet_velocity = ConfigDataset(...)

gravimetric_mass_balance_dtu = ConfigDataset(...)

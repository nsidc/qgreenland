from qgreenland.models.config.asset import HttpAsset, ManualAsset
from qgreenland.models.config.dataset import Dataset

esa_cci_supraglacial_lakes = Dataset(
    id="esa_cci_supraglacial_lakes",
    assets=[
        ManualAsset(
            id="only",
            access_instructions=(
                """Dataset can be found on the European Space Agency (ESA)
                Climate Change Initiative (CCI) products website
                (http://products.esa-icesheets-cci.org). Data are free to
                download after simple registration requiring `first.last` name
                and `affiliation`. No password is required."""
            ),
        ),
    ],
    metadata={
        "title": "ESA Greenland Ice Sheet CCI, Supraglacial Lakes from Sentinel-2",
        "abstract": (
            """Supraglacial Lake vectors for select areas of interest (AOI) on
            the Greenland Ice Sheet produced using Sentinel-2.

            Version 1.1 includes.
            AOI:
            * Sermeq Kujalleq (Jakobshavn Isbræ)

            Time-period:
            * 2019/05/01-2019/10/01

            For general background information see
            http://esa-icesheets-greenland-cci.org."""
        ),
        "citation": {
            "text": (
                """Data are produced by Penelope How, Alexandra Messerli, and
                Eva Mätzler (Department of Remote Sensing, Asiaq Greenland
                Survey)"""
            ),
            "url": "http://products.esa-icesheets-cci.org/products/details/greenland_sgl_s2_20190501_20191001_jakobshavn_v1_1.zip/",
        },
    },
)


esa_cci_surface_elevation_change = Dataset(
    id="esa_cci_surface_elevation_change",
    assets=[
        ManualAsset(
            id="only",
            access_instructions=(
                """Dataset can be found on the European Space Agency (ESA)
                Climate Change Initiative (CCI) products website
                (http://products.esa-icesheets-cci.org). Data are free to
                download after simple registration requiring `first.last` name
                and `affiliation`. No password is required."""
            ),
        ),
    ],
    metadata={
        "title": (
            "1992-2021 Greenland elevation change from multiple altimetric mission"
        ),
        "abstract": (
            """The 2021 CCI Surface Elevation Change (SEC) release contains two
            data sets and the release product contains two different types of
            data files:
            I) png plots of the surface elevation changes and errors.
            II) NetCDF files containing the surface elevation changes and
            their associated errors:

            The two datasets are as follows:
            1) The Long time series of 5-year mean SEC from ESAs Ku-band
            radar satellite level-2 data products. This data continues the
            times-series of previous releases, and this current release is
            data version 3.0. Data are based on ESAs Ku-band radar satellite
            level-2 data products.
            Given the longer time span of operation of the satellites, the
            data are provided at a five-year mean. The algorithms used to
            derive the product are explained in detail in Simonsen and
            Sørensen (2017), and Sørensen et al. (2018). The approach used
            here is the most optimal combination of the XO-, TR-, and
            PF-algorithm; the data are corrected for both backscatter and
            leading-edge width, and solved at 1 km grid resolution, and
            averaged in the post-processing to 5 km grid resolution by
            ordinary kriging.

            2) An experimental 2-year SEC dataset from ICESat-2. This
            release contains the first version of this product (vers
            1.0). The data are provided at a two-year mean. The TR
            algorithms presented in Sørensen et al. (2018) are used to
            derive the product, and 1 km grid resolution, and averaged in
            the post-processing to 5 km grid resolution by ordinary kriging.

            Reference:
            Simonsen, S. B., and Sørensen, L. S. (2017) ‘Implications of
            changing scattering properties on Greenland ice sheet volume
            change from Cryosat-2 altimetry’, Remote Sensing of
            Environment. Elsevier Inc., 190, pp. 207–216. DOI:
            10.1016/j.rse.2016.12.012.

            Sørensen, L. S., Simonsen, S. B., Forsberg, R., Khvorostovsky,
            K., Meister, R., and Engdahl, M. E. (2018) '25 years of
            elevation changes of the Greenland Ice Sheet from ERS, Envisat,
            and CryoSat-2 radar altimetry', Earth and Planetary Science
            Letters, 495, pp. 234-241 DOI: 10.1016/j.epsl.2018.05.015."""
        ),
        "citation": {
            "text": (
                """ESA. (2021) 1992-2021 Greenland elevation change from
                multiple altimetric mission.  Greenland Ice Sheet CCI
                Products."""
            ),
            "url": "http://products.esa-icesheets-cci.org/products/download/cci_sec_2021.zip",
        },
    },
)


esa_cci_ice_sheet_velocity_20191214_20200131 = Dataset(
    id="esa_cci_ice_sheet_velocity_20191214_20200131",
    assets=[
        ManualAsset(
            id="only",
            access_instructions=(
                """Dataset can be found on the European Space Agency (ESA)
                Climate Change Initiative (CCI) products website
                (http://products.esa-icesheets-cci.org). Data are free to
                download after simple registration requiring `first.last` name
                and `affiliation`. No password is required."""
            ),
        ),
    ],
    metadata={
        "title": "Greenland Ice Sheet Velocity 2019/20 from SENTINEL-1 winter campaign from 2019/12/14 to 2020/01/31.",
        "abstract": (
            """Greenland Ice Sheet Velocity - Winter Campaign 2019/2020: 250m
            gridded velocity map, generated applying coherent and incoherent
            offset tracking using SENTINEL-1 data acquired between 2019-12-14
            and 2020-01-31.

            This data set is part of the ESA Greenland Ice sheet CCI project.
            The original source data file includes all measurements and
            annotation. It provides components of the ice velocity, along with
            maps showing the horizontal magnitude, valid pixel count and
            uncertainty (based on the std.) within a NetCDF file. The ice
            velocity map is provided on a polar stereographic grid (EPSG 3413)
            with 250m grid spacing. The horizontal velocity is provided in true
            meters per day, towards Easting (x) and Northing (y) direction of
            the grid. The vertical displacement is derived from a digital
            elevation model.

            The product was generated by ENVEO."""
        ),
        "citation": {
            "text": (
                """Greenland Ice Sheet velocity map from Sentinel-1, winter
                campaign 2019/2020 [version 1.3]"""
            ),
            "url": "http://products.esa-icesheets-cci.org/products/details/greenland_iv_250m_s1_20191214_20200131_v1_3.zip/",
        },
    },
)


esa_cci_gravimetric_mass_balance_dtu = Dataset(
    id="esa_cci_gravimetric_mass_balance_dtu",
    assets=[
        ManualAsset(
            id="only",
            access_instructions=(
                """Dataset can be found on the European Space Agency (ESA)
                Climate Change Initiative (CCI) products website
                (http://products.esa-icesheets-cci.org). Data are free to
                download after simple registration requiring `first.last` name
                and `affiliation`. No password is required.

                Once the `greenland_gravimetric_mass_balance_rl06_dtuspace_v2_0-
                170820.zip` file is downloaded, use `unzip` to extract the data.
                Next, the supplied `scripts/esa_cci_gravimetric_mass_balance_dtu
                /gmb_dtu_nc_to_gpkg.py` script is run to convert the netcdf data
                into shapefiles that can easily ingested via the `LocalVector`
                layer task."""
            ),
        ),
    ],
    metadata={
        "title": "GMB products for the Greenland Ice Sheet from GRACE satellite gravimetry (CSR RL06) by DTU Space.",
        "abstract": (
            """From citation publication: During the last decade, the GRACE
            mission has provided valuable data for determining the mass changes
            ofthe Greenland and Antarctic ice sheets. Yet, discrepancies still
            exist in the published mass balance results, and comprehensive
            analyses on the sources of errors and discrepancies are lacking.
            Here, we present monthly mass changes together with trends derived
            from GRACE data at basin scalefor both the Greenland and Antarctic
            ice sheets, and we assess the variability and errors for each of the
            possible sources of discrepancies, and we do this in an
            unprecedented systematic way, taking into account mass inference
            methods, datasets and background models. We find a very good
            agreement between the monthly mass change results derived from two
            independent methods, which represents a cross validation. For the
            monthly solutions, we find that most of the scatter is caused by the
            use of the two different data sets rather than the two different
            methods applied. Besides the well-known GIA trend uncertainty, we
            find that the geocenter motion and the recent dealiasing corrections
            significantly impact the trends, with contributions of+13.2 Gt
            yr−1and−20 Gt yr−1, respectively, for Antarctica, which is more
            affected by these than Greenland. We show differences between the
            use of release RL04 and the new RL05 and confirma lower noise
            content in the new release. The overall scatter of the solutions
            well exceeds the uncertainties propagated from the data errors and
            the leakage (as done in the past); hence we calculate new sound
            total errors for the monthly solutions and the trends. We find that
            the scatter in the monthly solutions caused by applying different
            estimates of geocenter motion time series(degree-1 corrections) is
            significant – contributing with up to 40% of the total error."""
        ),
        "citation": {
            "text": (
                """Barletta, V. R., Sørensen, L. S., and Forsberg, R.: Scatter
                of mass changes estimates at basin scale for Greenland and
                Antarctica, The Cryosphere, 7, 1411-1432,
                doi:10.5194/tc-7-1411-2013, 2013."""
            ),
            "url": "http://products.esa-icesheets-cci.org/products/details/greenland_gravimetric_mass_balance_rl06_dtuspace_v2_0-170820.zip/",
        },
    },
)

esa_cci_marginal_lakes = Dataset(
    id="esa_cci_marginal_lakes",
    assets=[
        HttpAsset(
            id="only",
            urls=[
                "https://dap.ceda.ac.uk/neodc/esacci/glaciers/data/IIML/Greenland/v1/2017/20170101-ESACCI-L3S_GLACIERS-IML-MERGED-fv1.zip?download=1",
            ],
        ),
    ],
    metadata={
        "title": (
            """ESA Glaciers Climate Change Initiative (Glaciers_cci): 2017
            inventory of ice marginal lakes in Greenland (IIML), v1"""
        ),
        "abstract": (
            """The IIML is a comprehensive record of all identified ice marginal
            lakes across the terrestrial margin of Greenland, detected using
            remote sensing techniques. The detected lakes are presented as
            polygon vector features in shapefile format, with coordinates
            provided in the WGS 1984 UTM Zone 24N projected coordinate
            system. Ice marginal lakes were identified using three independent
            remote sensing methods: 1) multi-temporal backscatter classification
            from Sentinel-1 synthetic aperture radar imagery; 2) multi-spectral
            indices classification from Sentinel-2 optical imagery; and 3) sink
            detection from the ArcticDEM (v3). All data were compiled and
            filtered in a semi-automated approach, using a modified version of
            the MEaSUREs GIMP ice mask
            (https://nsidc.org/data/NSIDC-0714/versions/1) to clip the dataset
            to within 1 km of the ice margin. Each detected lake was then
            verified manually. The IIML was collected to better understand the
            impact of ice marginal lake change on the future sea level budget
            and the terrestrial and marine landscapes of Greenland, such as its
            ecosystems and human activities.

            The IIML is a complete inventory of Greenland, with no absent data."""
        ),
        "citation": {
            "text": (
                """Wiesmann, A.; Santoro, M.; Caduff, R.; How, P.; Messerli, A.;
                Mätzler, E.; Langley, K.; Høegh Bojesen, M.; Paul, F.; Kääb,
                A.M. (2021): ESA Glaciers Climate Change Initiative
                (Glaciers_cci): 2017 inventory of ice marginal lakes in
                Greenland (IIML), v1. Centre for Environmental Data Analysis, 19
                February
                2021. doi:10.5285/7ea7540135f441369716ef867d217519.
                http://dx.doi.org/10.5285/7ea7540135f441369716ef867d217519"""
            ),
            "url": "http://dx.doi.org/10.5285/7ea7540135f441369716ef867d217519",
        },
    },
)

from qgreenland.models.config.asset import ConfigDatasetManualAsset
from qgreenland.models.config.dataset import ConfigDataset


esa_cci_gravimetric_mass_balance_dtu = ConfigDataset(
    id='esa_cci_gravimetric_mass_balance_dtu',
    assets=[
        ConfigDatasetManualAsset(
            id='only',
            access_instructions=(
                """Dataset can be found on the European Space Agency (ESA)
                Climate Change Initiative (CCI) products website
                (http://products.esa-icesheets-cci.org). Data are free to
                download after simple registration requiring `first.last` name
                and `affiliation`. No password is required.

                Once the `greenland_gravimetric_mass_balance_rl06_dtuspace_v2_0-
                170820.zip` file is downloaded, use `unzip` to extract the data.
                Next, the supplied `scripts/esa_cci_gravimetric_mass_balance_dtu
                /gmb_dtu_nc_to_shp.py` script is run to convert the netcdf data
                into shapefiles that can easily ingested via the `LocalVector`
                layer task."""
            ),
        ),
    ],
    metadata={
        'title': 'GMB products for the Greenland Ice Sheet from GRACE satellite gravimetry (CSR RL06) by DTU Space.',
        'abstract': (
            """From citation publication: During the last decade, the GRACE
            mission has provided valuable data for determining the mass changes
            ofthe Greenland and Antarctic ice sheets.  Yet, discrepancies still
            exist in the published mass balance results, and comprehensive
            analyses on the sources of errors and discrepancies are lacking.
            Here, we present monthly mass changes together with trends derived
            from GRACE data at basin scalefor both the Greenland and Antarctic
            ice sheets, and we assess the variability and errors for each of the
            possible sources of discrepancies, and we do this in an
            unprecedented systematic way, taking into account mass inference
            methods, datasets and background models.  We find a very good
            agreement between the monthly mass change results derived from two
            independent methods, which represents a cross validation.  For the
            monthly solutions, we find that most of the scatter is caused by the
            use of the two different data sets rather than the two different
            methods applied. Besides the well-known GIA trend uncertainty, we
            find that the geocenter motion and the recent dealiasing corrections
            significantly impact the trends, with contributions of+13.2 Gt
            yr−1and−20 Gt yr−1, respectively, for Antarctica, which is more
            affected by these than Greenland.  We show differences between the
            use of release RL04 and the new RL05 and confirma lower noise
            content in the new release. The overall scatter of the solutions
            well exceeds the uncertainties propagated from the data errors and
            the leakage (as done in the past); hence we calculate new sound
            total errors for the monthly solutions and the trends. We find that
            the scatter in the monthly solutions caused by applying different
            estimates of geocenter motion time series(degree-1 corrections) is
            significant – contributing with up to 40% of the total error."""
        ),
        'citation': {
            'text': (
                """Barletta, V. R., Sørensen, L. S., and Forsberg, R.: Scatter
                of mass changes estimates at basin scale for Greenland and
                Antarctica, The Cryosphere, 7, 1411-1432,
                doi:10.5194/tc-7-1411-2013, 2013."""
            ),
            'url': 'http://products.esa-icesheets-cci.org/products/details/greenland_gravimetric_mass_balance_rl06_dtuspace_v2_0-170820.zip/',
        },
    },
)

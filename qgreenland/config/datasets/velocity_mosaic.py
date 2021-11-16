from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset


velocity_mosaic = Dataset(
    id='velocity_mosaic',
    assets=[
        HttpAsset(
            id='only',
            urls=[
                'http://its-live-data.jpl.nasa.gov.s3.amazonaws.com/velocity_mosaic/landsat/v00.0/static/GRE_G0120_0000.nc',
            ],
        ),
    ],
    metadata={
        'title': 'Regional Glacier and Ice Sheet Surface Velocities',
        'abstract': (
            """The Inter-mission Time Series of Land Ice Velocity and Elevation
            (ITS_LIVE) project facilitates ice sheet, ice shelf and glacier
            research by providing a globally comprehensive and temporally dense
            multi-sensor record of land ice velocity and elevation with low
            latency."""
        ),
        'citation': {
            'text': (
                """Velocity data generated using auto-RIFT (Gardner et al.,
                2018) and provided by the NASA MEaSUREs ITS_LIVE project
                (Gardner et al., 2019).

                Gardner, A. S., M. A. Fahnestock, and T. A. Scambos, 2019
                [Accessed on {{date_accessed}}]: ITS_LIVE Regional Glacier and
                Ice Sheet Surface Velocities. Data archived at National Snow and
                Ice Data Center; doi:10.5067/6II6VW8LLWJ7.

                Gardner, A. S., G. Moholdt, T. Scambos, M. Fahnstock, S.
                Ligtenberg, M. van den Broeke, and J. Nilsson, 2018: Increased
                West Antarctic and unchanged East Antarctic ice discharge over
                the last 7 years, Cryosphere, 12(2): 521–547,
                doi:10.5194/tc-12-521-2018."""
            ),
            'url': 'https://its-live.jpl.nasa.gov/#documentation',
        },
    },
)

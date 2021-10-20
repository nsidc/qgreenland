from qgreenland.models.config.asset import ConfigDatasetManualAsset
from qgreenland.models.config.dataset import ConfigDataset


gravity_anomalies = ConfigDataset(
    id='gravity_anomalies',
    assets=[
        ConfigDatasetManualAsset(
            id='only',
            access_instructions=(
                """These data were obtained from Rene Forsberg of DTU Space as a
                private data transfer on 2021-01-22."""
            ),
        ),
    ],
    metadata={
        'title': 'Geoid model and gravity anomalies for Greenland',
        'abstract': (
            """The Bouguer anomaly grid of Greenland have been derived from a
            rigorous least-squares collocation downward continuation process of
            terrain-corrected data, from the same data used to derive the geoid.
            The Bouguer anomalies are derived for a density of 2.67 g/cm3 over
            for rock density, and 0.92 g/cm3 for ice thickness. No Bouguer
            correction have been applied for marine areas, so offshore and data
            are free-air anomalies. The gravity reference system is GRS80, based
            on fundamental absolute gravity network.

            The gravity Faye (free-air) anomaly grid has been restored from the
            Bouguer anomaly grid by the normal gravity gradient of 0.1119
            mGal/m, without terrain corrections, based on the underlying DEM of
            land and glaciers/ice sheet."""
        ),
        'citation': {
            'text': (
                """Forsberg R., Jensen T. (2015) New Geoid of Greenland: A Case
                Study of Terrain and Ice Effects, GOCE and Use of Local Sea
                Level Data. In: Jin S., Barzaghi R. (eds) IGFS 2014. Int.
                Association of Geodesy Symposia, vol 144.  Springer,
                https://doi.org/10.1007/1345_2015_50."""
            ),
            'url': 'https://doi.org/10.1007/1345_2015_50',
        },
    },
)

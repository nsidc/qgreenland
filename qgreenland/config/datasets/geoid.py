from qgreenland.models.config.asset import ManualAsset
from qgreenland.models.config.dataset import Dataset


geoid = Dataset(
    id='geoid',
    assets=[
        ManualAsset(
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
            """GGeoid16 is the currently official gravimetric geoid model for
            Greenland, covering the area 58-85°N and 77-7°W with a grid
            resolution of 0.02° x 0.05° (approx. 2 km). It is based on a large
            set of land, marine, airborne and satellite gravity measurements, as
            well as digital terrain models for land and thickness of the inland
            ice.

            The geoid has been shifted from the global WGS84 computation system,
            to match the mean sea level at Nuuk. The GGeoid16 model is based on
            a previous preliminary model GGeoid14, with some changes in methods,
            new improved GOCE satellite data (Release 5), new aircraft-based
            gravity data from NASA OMG (Oceans Melting Greenland) project, as
            well as new gravity data from satellite altimetry (DTU13). The geoid
            determination is performed in the framework of a remove-restore
            procedure, using the DTU-Space GRAVSOFT package. The used global
            gravity model is EIGEN-6C4 up to degree and order 360, while the
            residual terrain correction is computed from a 500 m resolution land
            and ice thickness terrain model in Greenland.

            A downward continuation and gridding of all gravity field data to
            the terrain surface is performed by block least squares collocation,
            and then residual quasi-geoid heights are derived by Stokes'
            integration through spherical Fast Fourier Transform. After
            restoring the terrain effect and the reference global gravity field,
            quasi geoid heights are finally converted to geoid heights. The
            resulting GGeoid16 model is used to define the GVR2016 vertical
            reference system in Greenland. The accuracy of GGEOID16 is highly
            dependent on the underlying gravity coverage and is estimated to be
            5-10 cm in areas of good gravity coverage."""
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

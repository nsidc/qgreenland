from qgreenland.models.config.asset import ManualAsset
from qgreenland.models.config.dataset import Dataset


greenland_territorial_waters = Dataset(
    id='greenland_territorial_waters',
    assets=[
        ManualAsset(
            id='only',
            access_instructions=(
                """Dataset provided by Karl Zinglersen of the Greenland
                Institude for Natural Resources via a private one-time FTP
                transfer on Nov. 30, 2020. This dataset is not expected to be
                publicily archived outside of QGreenland."""
            ),
        ),
    ],
    metadata={
        'title': 'Greenland Territorial Waters',
        'abstract': (
            """Datasets provided by the Greenland Institute for Natural
            Resources (from Karl Zinglersen) via a private one-time FTP transfer
            on November 30, 2020. These data are not expected to be publicly
            archived outside of QGreenland."""
        ),
        'citation': {
            'text': (
                """Vector data from the Danish Geodata Agency. Attributes
                processed by Karl Brix Zinglersen, Greenland Institute of
                Natural Resources (2020)."""
            ),
            'url': '',
        },
    },
)

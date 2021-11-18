from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset


icesheet_height_and_thickness_change = Dataset(
    id='icesheet_height_and_thickness_change',
    assets=[
        HttpAsset(
            id='only',
            urls=[
                'https://digital.lib.washington.edu/researchworks/bitstream/handle/1773/45388/ICESat1_ICESat2_mass_change.zip',
            ],
        ),
    ],
    metadata={
        'title': 'Ice-sheet height and thickness changes from ICESat to ICESat-2',
        'abstract': (
            """These data represent ice-column thickness-change-rate estimates
            based on data from NASA's ICESat and ICESat-2 satellites. These data
            aided the first estimates of ice-sheet mass change from these two
            missions, spanning the 16 years from 2003 to 2019, taking advantage
            of the high vertical and horizontal resolution of the two
            satellites' laser altimeters."""
        ),
        'citation': {
            'text': (
                """Smith, Ben; Fricker, Helen; Gardner, Alex; Medley, Brooke;
                Nilsson, Johan; Paolo, Fernando; Holschuh, Nicholas; Adusumilli,
                Susheel; Brunt, Kelly; Csatho, Bea; Harbeck, Kaitlin; Markus,
                Thorsten; Neumann, Thomas; Siegfried, Matthew; Zwally, H. Jay;
                NASA grant numbers: NNX15AE15G, NNX15AC80G, NNX16AM01G,
                NNX17AI03G. NASA Cryospheric Sciences and MEaSUREs programs.
                http://hdl.handle.net/1773/45388. 2020."""
            ),
            'url': 'http://hdl.handle.net/1773/45388',
        },
    },
)

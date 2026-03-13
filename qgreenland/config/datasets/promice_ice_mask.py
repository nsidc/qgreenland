from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

# The name of the `dataset` variable doesn't matter here.
dataset = Dataset(
    id="promice_2022_ice_mask",
    assets=[
        HttpAsset(
            id="06_promice_2022_icemask_nunatak_polygon",
            urls=["https://dataverse.geus.dk/api/access/datafile/96892?gbrecs=true"],
        ),
        HttpAsset(
            id="13_promice_2022_icemask_raster_150m_v3",
            urls=["https://dataverse.geus.dk/api/access/datafile/97124?gbrecs=true"],
        ),
    ],
    metadata={
        "title": "PROMICE-2022 Ice Mask",
        "abstract": (
            """The PROMICE-2022 Ice Mask is a high-resolution outline of the
            contiguous ice masses of the Greenland Ice Sheet. The dataset is
            derived from a true-colour, multi-band mosaic of Sentinel-2
            satellite images at 10 m resolution, compiled using the SentinelHub
            Cloud Processing API. The mosaic was generated using the most recent
            valid pixels from August 2022, ensuring high temporal and geometric
            accuracy.

            Manual editing and mapping was conducted at a scale of around
            1:25,000, after which quality assessment was performed independently
            of the mapping operator, before finally being merged into one
            coherent dataset. The manual mapping process is further supported by
            data from the Danish Agency for Climate Data (KDS), including
            mosaics of Sentinel-2 and SPOT 6/7 imagery, as well as recent vector
            data from topographical mapping.

            Associated paper:

            Luetzenburg G. et al. (2026) PROMICE-2022 Ice Mask: A
            High-Resolution Outline of the Greenland Ice Sheet from August
            2022. Earth Syst. Sci. Data, 18,
            411–427. https://doi.org/10.5194/essd-18-411-2026."""
        ),
        "citation": {
            "text": (
                """Luetzenburg, Gregor; Korsgaard, Niels J.; Deichmann, Anna K.;
                Socher, Tobias; Gleie, Karin; Scharffenberger, Thomas; Fahrner,
                Dominik; Nielsen, Eva B.; How, Penelope; Bjørk, Anders A.;
                Kjeldsen, Kristian K.; Ahlstrøm, Andreas P.; Fausto, Robert S.,
                2025, "PROMICE-2022 Ice Mask",
                https://doi.org/10.22008/FK2/O8CLRE, GEUS Dataverse, V3"""
            ),
            "url": "https://doi.org/10.22008/FK2/O8CLRE",
        },
    },
)

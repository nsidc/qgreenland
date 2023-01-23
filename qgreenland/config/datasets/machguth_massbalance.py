from qgreenland.models.config.asset import ManualAsset
from qgreenland.models.config.dataset import Dataset

machguth_etal_massbalance_obs_locations = Dataset(
    id="machguth_etal_massbalance_obs_locations",
    assets=[
        ManualAsset(
            id="only",
            access_instructions=(
                """Accessed the Greenland Mass Balance database on Dec. 12, 2020
                from PROMICE (https://promice.org/PromiceDataPortal/api/download
                /1198f862-4afa-4862-952f-acd9129d790d/greenland_SMB_database_v20
                20/greenland_SMB_database_v2020.xlsx)

                See:
                `scripts/private-archive-preprocess/machguth_etal_massbalan
                ce_obs_locations/README.md` for preprocessing steps."""
            ),
        ),
    ],
    metadata={
        "title": "Greenland surface mass-balance observations from the ice-sheet ablation area and local glaciers",
        "abstract": (
            """These are historical surface mass balance measurement locations
            from Greenland Ice Sheet ablation area and surrounding local
            glaciers. There are approximately 3000 unique measurements from 46
            sites. The earliest measurements are from 1892. Each measurement is
            accompanied with position and date information, as well as quality
            and source flags. Users can look to the citation URL for additional
            data."""
        ),
        "citation": {
            "text": (
                """Machgruth, H. et al (2016). Greenland surface mass-balance
                observations from the ice-sheet ablation area and local
                glaciers. Journal of Glaciology, 62(235), 861-887.
                doi:10.1017/jog.2016.75"""
            ),
            "url": "https://www.doi.org/10.1017/jog.2016.75",
        },
    },
)

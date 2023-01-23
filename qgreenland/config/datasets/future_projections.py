from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

future_icesheet_coverage = Dataset(
    id="future_icesheet_coverage",
    assets=[
        HttpAsset(
            id="rcp_26",
            urls=[
                "https://arcticdata.io/metacat/d1/mn/v2/object/urn%3Auuid%3A61ff2294-4734-46ba-a0b0-845d69298131",
            ],
        ),
        HttpAsset(
            id="rcp_45",
            urls=[
                "https://arcticdata.io/metacat/d1/mn/v2/object/urn%3Auuid%3Aed2d7235-2193-4ba3-a98f-f09d871199a1",
            ],
        ),
        HttpAsset(
            id="rcp_85",
            urls=[
                "https://arcticdata.io/metacat/d1/mn/v2/object/urn%3Auuid%3Aecec7b68-a544-4575-8731-47d60b73215f",
            ],
        ),
    ],
    metadata={
        "title": "Contribution of the Greenland Ice Sheet to sea-level over the next millennium using Large Ensemble Simulations, spatial time series, 2008-3007.",
        "abstract": (
            """Citation publication abstract: The Greenland Ice Sheet holds
            around 7.2 meters of sea-level equivalent. In recent decades rising
            atmosphere and ocean temperatures have led to an acceleration in
            mass loss, adding an average of about 0.5 millimeters per year to
            global mean sea-level between 1991 and 2015. Current ice margin
            recession in Greenland is led by the retreat of outlet glaciers, the
            large rivers of ice ending in narrow fjords that drain the ice sheet
            interior. Recent progress in measuring ice thickness is enabling
            models to reproduce the complex flow patterns found in outlet
            glaciers, a key step towards realistic projections. Here we pair an
            outlet glacier resolving ice sheet model with a comprehensive
            uncertainty quantification to estimate Greenland's contribution to
            sea-level over the next millennium under different climate forcings.
            We find that Greenland could contribute 5-33 centimeters to
            sea-level by 2100 and 11-155 centimeters by 2200, with discharge
            from outlet glaciers contributing 6-45% of the total mass loss. Our
            analysis shows that uncertainties in projecting mass loss are
            dominated by uncertainties in climate scenarios and surface
            processes, followed by ice dynamics, whereas uncertainties in ocean
            conditions play a minor role, particularly in the long term. We
            project that Greenland will very likely become ice-free within a
            millennium without significant reductions in greenhouse gas
            emissions.

            This dataset compilation contains the simulations for the manuscript
            "Contribution of the Greenland Ice Sheet to sea-level over the next
            millennium" prepared with the Parallel Ice Sheet Model (PISM).

            This dataset provides the likelihood of a pixel being ice covered at
            the year 3007 for the RCPs (Representative Concentration Pathways)
            2.6, 4.5, and 8.5 for LES (Large Ensemble Simulations)."""
        ),
        "citation": {
            "text": (
                """Andy Aschwanden. 2019. Contribution of the Greenland Ice
                Sheet to sea-level over the next millennium using Large Ensemble
                Simulations, spatial time series, 2008-3007. Arctic Data Center.
                doi:10.18739/A29G5GD39."""
            ),
            "url": "https://doi.org/10.18739/A29G5GD39",
        },
    },
)

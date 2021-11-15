from qgreenland.models.config.asset import ManualAsset
from qgreenland.models.config.dataset import Dataset


macferrin_etal_firn_ice_layer_thicknesses = Dataset(
    id='macferrin_etal_firn_ice_layer_thicknesses',
    assets=[
        ManualAsset(
            id='only',
            access_instructions=(
                """Available via the publication website, and contained in the
                Source Data Fig. 2 file."""
            ),
        ),
    ],
    metadata={
        'title': 'Rapid expansion of Greenland’s low-permeability ice slabs',
        'abstract': (
            """Citation publication abstract: In recent decades, meltwater
            runoff has accelerated to become the dominant mechanism for mass
            loss in the Greenland ice sheet. In Greenland’s high-elevation
            interior, porous snow and firn accumulate; these can absorb surface
            meltwater and inhibit runoff, but this buffering effect is limited
            if enough water refreezes near the surface to restrict percolation.
            However, the influence of refreezing on runoff from Greenland
            remains largely unquantified. Here we use firn cores, radar
            observations and regional climate models to show that recent
            increases in meltwater have resulted in the formation of
            metres-thick, low-permeability ‘ice slabs’ that have expanded the
            Greenland ice sheet’s total runoff area by 26 ± 3 per cent since
            2001. Although runoff from the top of ice slabs has added less than
            one millimetre to global sea-level rise so far, this contribution
            will grow substantially as ice slabs expand inland in a warming
            climate. Runoff over ice slabs is set to contribute 7 to 33
            millimetres and 17 to 74 millimetres to global sea-level rise by
            2100 under moderate- and high-emissions scenarios,
            respectively—approximately double the estimated runoff from
            Greenland’s high-elevation interior, as predicted by surface mass
            balance models without ice slabs. Ice slabs will have an important
            role in enhancing surface meltwater feedback processes,
            fundamentally altering the ice sheet’s present and future
            hydrology."""
        ),
        'citation': {
            'text': (
                """MacFerrin, M., Machguth, H., As, D.v. et al. Rapid expansion
                of Greenland’s low-permeability ice slabs. Nature 573, 403–407
                (2019). https://doi.org/10.1038/s41586-019-1550-3"""
            ),
            'url': 'https://doi.org/10.1038/s41586-019-1550-3',
        },
    },
)

from qgreenland.models.config.asset import CmrAsset
from qgreenland.models.config.dataset import Dataset


basal_thermal_state = Dataset(
    id='basal_thermal_state',
    assets=[
        CmrAsset(
            id='only',
            granule_ur='SC:RDBTS4.001:114194114',
            collection_concept_id='C1397417110-NSIDC_ECS',
        ),
    ],
    metadata={
        'title': 'Likely Basal Thermal State of the Greenland Ice Sheet',
        'abstract': (
            """The Likely Basal Thermal State of the Greenland Ice Sheet product
            at the National Snow and Ice Data Center contains key datasets that
            show how the likely basal thermal state was inferred from existing
            airborne and satellite datasets and recent methods, and provides a
            synthesis mask of the likely basal thermal state over the Greenland
            Ice Sheet (MacGregor et al. 2016), which is displayed in QGreenland.

            MacGregor, J.A., M.A. Fahnestock, G.A. Catania, A. Aschwanden, G.D.
            Clow, W.T. Colgan, S.P. Gogineni, M. Morlighem, S.M.J. Nowicki,
            J.D. Paden, S.F. Price and H. Seroussi. 2016. A synthesis of the
            basal thermal state of the Greenland Ice Sheet, Journal of
            Geophysical Research Earth Surface, 121:1328–1350,
            doi:10.1002/2015JF003808."""
        ),
        'citation': {
            'text': (
                """MacGregor, J. A., M. Fahnestock, G. Catania, J. Paden, P.
                Gogineni, M. Morlighem, W. Colgan, S. M. Nowicki, G. Clow, A.
                Aschwanden, S. F. Price, and H. Seroussi. 2017. Likely Basal
                Thermal State of the Greenland Ice Sheet, Version 1. Boulder,
                Colorado USA. NASA National Snow and Ice Data Center Distributed
                Active Archive Center. doi:
                https://doi.org/10.5067/R4MWDWWUWQF9."""
            ),
            'url': 'https://nsidc.org/data/rdbts4/versions/1',
        },
    },
)

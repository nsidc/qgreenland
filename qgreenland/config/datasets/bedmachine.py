from qgreenland.models.config.dataset import (
    ConfigDataset,
    ConfigDatasetCmrAsset,
)


bedmachine = ConfigDataset(
    id='bedmachine',
    assets=[
        ConfigDatasetCmrAsset(
            id='only',
            granule_ur='SC:IDBMG4.003:160281892',
            collection_concept_id='C1584255847-NSIDC_ECS',
        ),
    ],
    metadata={
        'title': 'IceBridge BedMachine Greenland, Version 3',
        'abstract': """
This data set contains a bed topography/bathymetry map of Greenland based on
mass conservation, multi-beam data, and other techniques. It also includes
surface elevation and ice thickness data, as well as an ice/ocean/land mask.
""",
        'citation': {
            'text': """
Morlighem, M. et al. 2017, updated 2018. IceBridge BedMachine Greenland, Version
3. [Indicate subset used]. Boulder, Colorado USA. NASA National Snow and Ice
Data Center Distributed Active Archive Center. doi:
https://doi.org/10.5067/2CIX82HUV88Y. 2020/02/07.
""",
            'url': 'https://doi.org/10.5067/2CIX82HUV88Y',
        },
    },
)

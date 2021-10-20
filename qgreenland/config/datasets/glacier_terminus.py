from qgreenland.models.config.asset import ConfigDatasetCmrAsset
from qgreenland.models.config.dataset import ConfigDataset


glacier_terminus = ConfigDataset(
    id='glacier_terminus',
    assets=[
        ConfigDatasetCmrAsset(
            id='glacier_ids',
            granule_ur='SC:NSIDC-0642.001:125854253',
            collection_concept_id='C1413880084-NSIDC_ECS',
        ),
        ConfigDatasetCmrAsset(
            id='2000_2001',
            granule_ur='SC:NSIDC-0642.001:125860172',
            collection_concept_id='C1413880084-NSIDC_ECS',
        ),
        ConfigDatasetCmrAsset(
            id='2005_2006',
            granule_ur='SC:NSIDC-0642.001:125860185',
            collection_concept_id='C1413880084-NSIDC_ECS',
        ),
        ConfigDatasetCmrAsset(
            id='2006_2007',
            granule_ur='SC:NSIDC-0642.001:125860176',
            collection_concept_id='C1413880084-NSIDC_ECS',
        ),
        ConfigDatasetCmrAsset(
            id='2007_2008',
            granule_ur='SC:NSIDC-0642.001:125860183',
            collection_concept_id='C1413880084-NSIDC_ECS',
        ),
        ConfigDatasetCmrAsset(
            id='2008_2009',
            granule_ur='SC:NSIDC-0642.001:125860171',
            collection_concept_id='C1413880084-NSIDC_ECS',
        ),
        ConfigDatasetCmrAsset(
            id='2012_2013',
            granule_ur='SC:NSIDC-0642.001:125860173',
            collection_concept_id='C1413880084-NSIDC_ECS',
        ),
        ConfigDatasetCmrAsset(
            id='2014_2015',
            granule_ur='SC:NSIDC-0642.001:125860177',
            collection_concept_id='C1413880084-NSIDC_ECS',
        ),
        ConfigDatasetCmrAsset(
            id='2015_2016',
            granule_ur='SC:NSIDC-0642.001:125860175',
            collection_concept_id='C1413880084-NSIDC_ECS',
        ),
        ConfigDatasetCmrAsset(
            id='2016_2017',
            granule_ur='SC:NSIDC-0642.001:125860184',
            collection_concept_id='C1413880084-NSIDC_ECS',
        ),
    ],
    metadata={
        'title': 'MEaSUREs Annual Greenland Outlet Glacier Terminus Positions from SAR Mosaics, Version 1',
        'abstract': (
            """This data set, part of the NASA Making Earth System Data Records
            for Use in Research Environments (MEaSUREs) program, provides
            Greenland outlet glacier terminus positions created from MEaSUREs
            Synthetic Aperture Radar (SAR) mosaics and Landsat 8 OLI imagery."""
        ),
        'citation': {
            'text': (
                """Joughin, I., T. Moon, J. Joughin, and T. Black. 2015, 2017.
                MEaSUREs Annual Greenland Outlet Glacier Terminus Positions from
                SAR Mosaics, Version 1. [Indicate subset used]. Boulder,
                Colorado USA. NASA National Snow and Ice Data Center Distributed
                Active Archive Center. doi:
                https://doi.org/10.5067/DC0MLBOCL3EL. 2020/02/12."""
            ),
            'url': 'https://doi.org/10.5067/DC0MLBOCL3EL',
        },
    },
)

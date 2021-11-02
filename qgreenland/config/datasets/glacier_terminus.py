from qgreenland.models.config.asset import ConfigDatasetCmrAsset
from qgreenland.models.config.dataset import ConfigDataset


glacier_terminus = ConfigDataset(
    id='glacier_terminus',
    assets=[
        ConfigDatasetCmrAsset(
            id='glacier_ids',
            granule_ur='SC:NSIDC-0642.002:227146975',
            collection_concept_id='C2139015179-NSIDC_ECS',
        ),
        ConfigDatasetCmrAsset(
            id='2000_2001',
            granule_ur='SC:NSIDC-0642.002:227146979',
            collection_concept_id='C2139015179-NSIDC_ECS',
        ),
        ConfigDatasetCmrAsset(
            id='2005_2006',
            granule_ur='SC:NSIDC-0642.002:227146973',
            collection_concept_id='C2139015179-NSIDC_ECS',
        ),
        ConfigDatasetCmrAsset(
            id='2006_2007',
            granule_ur='SC:NSIDC-0642.002:227146977',
            collection_concept_id='C2139015179-NSIDC_ECS',
        ),
        ConfigDatasetCmrAsset(
            id='2007_2008',
            granule_ur='SC:NSIDC-0642.002:227146974',
            collection_concept_id='C2139015179-NSIDC_ECS',
        ),
        ConfigDatasetCmrAsset(
            id='2008_2009',
            granule_ur='SC:NSIDC-0642.002:227146982',
            collection_concept_id='C2139015179-NSIDC_ECS',
        ),
        ConfigDatasetCmrAsset(
            id='2012_2013',
            granule_ur='SC:NSIDC-0642.002:227146972',
            collection_concept_id='C2139015179-NSIDC_ECS',
        ),
        ConfigDatasetCmrAsset(
            id='2014_2015',
            granule_ur='SC:NSIDC-0642.002:227146970',
            collection_concept_id='C2139015179-NSIDC_ECS',
        ),
        ConfigDatasetCmrAsset(
            id='2015_2016',
            granule_ur='SC:NSIDC-0642.002:227146978',
            collection_concept_id='C2139015179-NSIDC_ECS',
        ),
        ConfigDatasetCmrAsset(
            id='2016_2017',
            granule_ur='SC:NSIDC-0642.002:227146971',
            collection_concept_id='C2139015179-NSIDC_ECS',
        ),
        ConfigDatasetCmrAsset(
            id='2017_2018',
            granule_ur='SC:NSIDC-0642.002:227146980',
            collection_concept_id='C2139015179-NSIDC_ECS',
        ),
        ConfigDatasetCmrAsset(
            id='2018_2019',
            granule_ur='SC:NSIDC-0642.002:227146976',
            collection_concept_id='C2139015179-NSIDC_ECS',
        ),
        ConfigDatasetCmrAsset(
            id='2019_2020',
            granule_ur='SC:NSIDC-0642.002:227146981',
            collection_concept_id='C2139015179-NSIDC_ECS',
        ),
        ConfigDatasetCmrAsset(
            id='2020_2021',
            granule_ur='SC:NSIDC-0642.002:227146983',
            collection_concept_id='C2139015179-NSIDC_ECS',
        ),
    ],
    metadata={
        'title': 'MEaSUREs Annual Greenland Outlet Glacier Terminus Positions from SAR Mosaics, Version 2',
        'abstract': (
            """This data set, part of the NASA Making Earth System Data Records
            for Use in Research Environments (MEaSUREs) program, provides
            digitized terminus positions for 239 Greenland outlet glaciers
            during 13 winter seasons. Terminus positions were determined from
            MEaSUREs mosaics of Sentinel-1 and RADARSAT-1 synthetic aperture
            radar data, with gaps filled using Landsat-7 and -8 panchromatic
            imagery."""
        ),
        'citation': {
            'text': (
                """Joughin, I., T. Moon, J. Joughin, and
                T. Black. 2021. MEaSUREs Annual Greenland Outlet Glacier
                Terminus Positions from SAR Mosaics, Version 2. [Indicate subset
                used]. Boulder, Colorado USA. NASA National Snow and Ice Data
                Center Distributed Active Archive Center. doi:
                https://doi.org/10.5067/ESFWE11AVFKW. 2021/11/02."""
            ),
            'url': 'https://doi.org/10.5067/ESFWE11AVFKW',
        },
    },
)

from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

naturemap_important_wildlife_areas = Dataset(
    id="naturemap_areas_important_to_wildlife",
    assets=[
        HttpAsset(
            id="barnacle_goose_colony",
            urls=[
                "https://services-eu1.arcgis.com/0uK40YtWoUkQMlYW/arcgis/rest/services/Areas_Important_to_Wildlife_data/FeatureServer/replicafilescache/Areas_Important_to_Wildlife_data_4850145148347302144.gpkg",
            ],
        ),
        HttpAsset(
            id="goose_moulting_and_breeding_areas",
            urls=[
                "https://services-eu1.arcgis.com/0uK40YtWoUkQMlYW/arcgis/rest/services/Areas_Important_to_Wildlife_data/FeatureServer/replicafilescache/Areas_Important_to_Wildlife_data_-7430306519656547148.gpkg",
            ],
        ),
        # Associated report for seabird colony layers: https://dce.au.dk/fileadmin/dce.au.dk/Udgivelser/Notater_2022/N2022_78UK.pdf
        HttpAsset(
            id="seabird_colony_non_disturbance_zone_200m",
            urls=[
                "https://services-eu1.arcgis.com/0uK40YtWoUkQMlYW/arcgis/rest/services/Areas_Important_to_Wildlife_data/FeatureServer/replicafilescache/Areas_Important_to_Wildlife_data_-8920941852164200711.gpkg",
            ],
        ),
        HttpAsset(
            id="seabird_colony_non_disturbance_zone_1000m",
            urls=[
                "https://services-eu1.arcgis.com/0uK40YtWoUkQMlYW/arcgis/rest/services/Areas_Important_to_Wildlife_data/FeatureServer/replicafilescache/Areas_Important_to_Wildlife_data_-3249479950042144519.gpkg",
            ],
        ),
        HttpAsset(
            id="seabird_colony_no_drone_zone_100m",
            urls=[
                "https://services-eu1.arcgis.com/0uK40YtWoUkQMlYW/arcgis/rest/services/Areas_Important_to_Wildlife_data/FeatureServer/replicafilescache/Areas_Important_to_Wildlife_data_4938399169145340864.gpkg",
            ],
        ),
        HttpAsset(
            id="seabird_colony_no_fly_zone_500m",
            urls=[
                "https://services-eu1.arcgis.com/0uK40YtWoUkQMlYW/arcgis/rest/services/Areas_Important_to_Wildlife_data/FeatureServer/replicafilescache/Areas_Important_to_Wildlife_data_-2585139062866919292.gpkg",
            ],
        ),
        HttpAsset(
            id="seabird_colony_no_fly_zone_3000m",
            urls=[
                "https://services-eu1.arcgis.com/0uK40YtWoUkQMlYW/arcgis/rest/services/Areas_Important_to_Wildlife_data/FeatureServer/replicafilescache/Areas_Important_to_Wildlife_data_-739616273938683767.gpkg",
            ],
        ),
        HttpAsset(
            id="salt_or_saline_lake_100m_zone",
            urls=[
                "https://services-eu1.arcgis.com/0uK40YtWoUkQMlYW/arcgis/rest/services/Areas_Important_to_Wildlife_data/FeatureServer/replicafilescache/Areas_Important_to_Wildlife_data_6736240752857920611.gpkg",
            ],
        ),
        HttpAsset(
            id="national_park",
            urls=[
                "https://services-eu1.arcgis.com/0uK40YtWoUkQMlYW/arcgis/rest/services/Areas_Important_to_Wildlife_data/FeatureServer/replicafilescache/Areas_Important_to_Wildlife_data_-5248120251132702708.gpkg",
            ],
        ),
        HttpAsset(
            id="biological_important_areas_in_the_national_park",
            urls=[
                "https://services-eu1.arcgis.com/0uK40YtWoUkQMlYW/arcgis/rest/services/Areas_Important_to_Wildlife_data/FeatureServer/replicafilescache/Areas_Important_to_Wildlife_data_-8747728574225365759.gpkg",
            ],
        ),
        HttpAsset(
            id="nature_protection_area",
            urls=[
                "https://services-eu1.arcgis.com/0uK40YtWoUkQMlYW/arcgis/rest/services/Areas_Important_to_Wildlife_data/FeatureServer/replicafilescache/Areas_Important_to_Wildlife_data_8290516231831615511.gpkg",
            ],
        ),
    ],
    metadata={
        "title": "Areas important to wildlife",
        "abstract": (
            """NatureMap is a web map hub site of The Environmental Agency for
            Mineral Resource Activities (EAMRA), Government of Greenland. The
            site contains geospatial data and background reports on environment
            and nature relevant for environmentally sound planning and
            regulation of mineral resource and hydrocarbon exploration and
            exploitation activities in Greenland. The purpose of the site is to
            make data and information available to both authorities, mineral
            resource companies, and the public.

            Layers from the database Important Areas to Wildlife maintained by
            Greenland Institute of Natural Resources and DCE Aarhus University
            for the Environmental Agency for Mineral Resources Activities of the
            Government of Greenland to the support of case handling and information
            considering the Mineral Resources Act.

            NatureMap is managed by The Greenland Institute of Natural Resources
            (GINR) with support from DCE – Danish Centre for Environment and
            Energy, Aarhus University. On behalf of EAMRA, DCE and GINR run a
            datacenter with environmental data and samples relevant for planning
            and regulating mineral resources and hydrocarbon activities in
            Greenland, and NatureMap forms part of that collaboration."""
        ),
        "citation": {
            "text": (
                """NatureMap, 2025. Areas important to wildlife. {{date_accessed}}"""
            ),
            "url": "https://naturemap-nature.hub.arcgis.com/maps/nature::areas-important-to-wildlife-data/about",
        },
    },
)

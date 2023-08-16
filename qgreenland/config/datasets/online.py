from qgreenland.models.config.asset import OnlineAsset
from qgreenland.models.config.dataset import Dataset, DatasetMetadata

gibs = Dataset(
    id="gibs",
    assets=[
        OnlineAsset(
            id="only",
            provider="wms",
            url="contextualWMSLegend=0&crs=EPSG:3413&dpiMode=7&featureCount=10&format=image/png&layers=BlueMarble_ShadedRelief_Bathymetry&styles&url=https://gibs.earthdata.nasa.gov/wms/epsg3413/best/wms.cgi?VERSION%3D1.3.0",
        ),
    ],
    metadata=DatasetMetadata(
        title="Global Imagery Browse Services (GIBS)",
        abstract=(
            """NASA GIBS provides full-resolution visual representations of NASA
            Earth science data in a free, open, and interoperable
            manner. Through responsive and highly available web services, it
            enables interactive exploration of data to support a wide range of
            applications including scientific research, applied sciences,
            natural hazard monitoring, and outreach."""
        ),
        citation={
            "text": (
                """We acknowledge the use of imagery provided by services from
                NASA's Global Imagery Browse Services (GIBS), part of NASA's
                Earth Observing System Data and Information System (EOSDIS)."""
            ),
            "url": "https://www.earthdata.nasa.gov/eosdis/science-system-description/eosdis-components/gibs",
        },
    ),
)

# TODO: combine SDFI topo and satellite photos into one dataset with multiple
# assets? Better citation for these two?
sdfi_topo_map = Dataset(
    id="sdfi_topo_map",
    assets=[
        OnlineAsset(
            id="only",
            provider="wms",
            url="contextualWMSLegend=0&crs=EPSG:3183&dpiMode=7&featureCount=10&format=image/png&layers=gl_aabent_land&styles&url=https://api.dataforsyningen.dk/wms/gl_aabent_land?token%3D363159825b13ad4543a99cde905d1adc",
        ),
    ],
    metadata=DatasetMetadata(
        title="Open Country Greenland",
        abstract=(
            """Data and information provided by the Danish Board for Data Supply and Infrastructure (SDFI). 
            
            The web service consists of vector data covering the entire
            ice-free area. Vector data is supplemented with place names, curves,
            elevations and hillshade, as well as other relevant data, obtained
            from external data owners.

            Open Country Greenland can be used to plan a stay in the open
            country, thus helping, for example, hunters, anglers and tourists
            who need to hike and find their way around the landscape.

            Emergency services, police and defense, which have to carry out
            emergency operations and rescue operations in the open country, are
            also expected to be able to find good use of the service.

            Errors have been found in the height model for some steep mountain
            peaks in Greenland (more than 100 m). SDFI are investigating the
            extent and possibilities of correcting the errors. If you have
            questions or notice an error, please send an email to
            support@sdfi.dk.

            Web service wms/gl_aabent_land has been prepared on the basis
            of data from the Agency for Data Supply and Infrastructure and
            the following other institutions: Asiaq, the Geodata Agency,
            Landsplan, Nukissiorfiit, Oqaasileriffik and Tusass.

            NOTE: https://dataforsyningen.dk includes other datasets of
            Greenland that may be of interest to users of QGreenland. To access these datasets, account registration is
            required. Additionally, the website is in Danish and does not
            include an English translation. Google Translate can be used to
            provide such a translation.
            
            Greenlandic and Danish versions of the map legend can be downloaded from the Citation URL"""
        ),
        citation={
            "text": (
                """Open Country Greenland (web service wms/gl_aabent_land), Data Supply and Infrastructure Agency, Denmark, https://dataforsyningen.dk/data/4771."""
            ),
            "url": "https://dataforsyningen.dk/data/4771",
        },
    ),
)

sdfi_satellite_orthophotos = Dataset(
    id="sdfi_satellite_photo",
    assets=[
        OnlineAsset(
            id="only",
            provider="wms",
            url="contextualWMSLegend=0&crs=EPSG:32624&dpiMode=7&featureCount=10&format=image/jpeg&layers=ortofoto&styles&url=https://api.dataforsyningen.dk/wms/gl_satellitfoto?token%3D363159825b13ad4543a99cde905d1adc",
        ),
    ],
    metadata=DatasetMetadata(
        title="Satellite Photo Greenland",
        abstract=(
            """Data and information provided by the Danish Board for Data Supply and Infrastructure (SDFI).
            
            The web service consists of orthophotos from several satellite
                and aerial sources, recorded in different time periods and degrees
                of resolution, from 10m pixels to 0.2m pixels. The photos are
                supplemented in the web service by e.g. elevations (elevations and
                curves), place names and grid.

                Web service wms/gl_satellitfoto has been prepared on the
                basis of data from the Data Supply and Infrastructure Agency and the following
                other institutions: Asiaq, the Geodata Agency, Landsplan, Nukissiorfiit,
                Oqaasileriffik and Tusass

                NOTE: https://dataforsyningen.dk includes other datasets of
                Greenland that may be of interest to users of QGreenland.
                To access these datasets, account registration is
                required. Additionally, the website is in Danish and does not
                include an English translation. Google Translate can be used to
                provide such a translation."""
        ),
        citation={
            "text": (
                """Satellite Photo Greenland (web service wms/gl_satellitfoto), Data Supply and Infrastructure Agency, Denmark, https://dataforsyningen.dk/data/4783."""
            ),
            "url": "https://dataforsyningen.dk/data/4783",
        },
    ),
)

image_mosaic = Dataset(
    id="image_mosaic",
    assets=[
        OnlineAsset(
            id="2019",
            provider="gdal",
            url=(
                "/vsicurl/http://its-live-data.jpl.nasa.gov.s3.amazonaws.com/"
                "rgb_mosaics/GRE2/Greenlandmedian_Aug_2019.vrt"
            ),
        ),
        OnlineAsset(
            id="2015",
            provider="gdal",
            url=(
                "/vsicurl/http://its-live-data.jpl.nasa.gov.s3.amazonaws.com/"
                "rgb_mosaics/GRE/GRE_L8_Aug_2015_on_S3.vrt"
            ),
        ),
    ],
    # TODO: Switch to class instantiation. Makes it easier to differentiate keys
    # from values in this big wall-of-string.
    metadata={
        "title": "Sentinel-2 Imagery Mosaics",
        # Editability matters most, so we use """triple-quote strings""".
        "abstract": (
            """Abstract for reference publication: Each summer, surface melting
            of the margin of the Greenland Ice Sheet exposes a distinctive
            visible stratigraphy that is related to past variability in
            subaerial dust deposition across the accumulation zone and
            subsequent ice flow toward the margin. Here we map this surface
            stratigraphy along the northern margin of the ice sheet using
            mosaicked Sentinel-2 multispectral satellite imagery from the end of
            the 2019 melt season and finer-resolution WorldView-2/3 imagery for
            smaller regions of interest.  We trace three distinct transitions in
            apparent dust concentration and the top of a darker basal layer. The
            three dust transitions have been identified previously as
            representing late-Pleistocene climatic transitions, allowing us to
            develop a coarse margin chronostratigraphy for northern Greenland.
            Substantial folding of late-Pleistocene stratigraphy is observed but
            uncommon. The oldest conformal surface-exposed ice in northern
            Greenland is likely located adjacent to Warming Land and may be up
            to ~55 thousand years old. Basal ice is commonly exposed hundreds of
            metres from the ice margin and may indicate a widespread frozen
            basal thermal state. We conclude that the ice margin across northern
            Greenland offers multiple opportunities to recover paleoclimatically
            distinct ice relative to previously studied regions in southwestern
            Greenland.

            QGreenland displays 2015 and 2019 Sentinel-2 mosaics as online-only
            access layers."""
        ),
        "citation": {
            "text": (
                """MacGregor JA, Fahnestock MA, Colgan WT, Larsen NK, Kjeldsen
                KK, Welker JM (2020). The age of surface-exposed ice along the
                northern margin of the Greenland Ice Sheet. Journal of
                Glaciology 66(258), 667–684.

                https://doi.org/10.1017/jog.2020.62"""
            ),
            "url": "https://doi.org/10.1017/jog.2020.62",
        },
    },
)

geus_geological_map = Dataset(
    id="geus_geological_map",
    assets=[
        OnlineAsset(
            id="only",
            provider="wms",
            url="contextualWMSLegend=0&crs=EPSG:32624&dpiMode=7&featureCount=10&format=image/png&layers=Greenland_Geological_map_500k&styles=default&tileMatrixSet=default028mm&url=https://data.geus.dk/arcgis/rest/services/Greenland/Geological_map_500k/MapServer/WMTS/1.0.0/WMTSCapabilities.xml",
        ),
    ],
    metadata=DatasetMetadata(
        title="Geological Map of Greenland 1:500 000",
        abstract=(
            """This map is provided as a web service from the Geological Survey of Denmark and Greenland (GEUS)
            
            The new official geological map of Greenland in scale 1:500 000
            is based on 14 digitized map sheets covering all of Greenland with
            ammendments in specific areas. The original digital map was released
            on the GEUS Greenland Portal in 2012 (Pedersen et al. 2013). The constant
            increase in knowledge calls for pertinent revisions of the map in
            order to keep it up to date. Over the past decade a growing number
            of new scientific publications have changed the understanding of the
            geology in some areas of Greenland. With the release of the present
            map version, the following geographical areas have undergone
            revisions:

            1. The Palaeogene North Atlantic Igneous Province of West Greenland
               (Pedersen et al. 2017; 2018; Larsen J. G. & Larsen L. M. 2022).
            2. Mesozoic rocks in eastern Peary Land in North Greenland (Bjerager
               et al. 2019).
            3. The Kilen area in North Greenland, based on the latest 1:100 000
               geological map and recommended visualisation of the 1:500 000
               geology as outlined by Svennevig (2018a,b).
            4. Mesozoic rocks of North East Greenland, from Jameson Land to
               Store Koldewey (Clemmensen et al. 2020; Bjerager et al. 2020; Surlyk
               et al. 2021; Andrews et al. 2021).
            5. Neoproterozoic rocks of the Eleonore Bay Supergroup on Kuhn Ø
               (Tirsgaard & Sønderholm 1997).
            6. South East Greenland between 62° and 67° N, where new updated
               geology was presented under the SEGMENT project (Kolb et al. 2016).

            The new map has undergone extensive quality control including a
            complete harmonisation of all lineaments and structure points, which
            was not previously implemented. The map legend can be downloaded from the Citation URL."""
        ),
        citation={
            "text": (
                """Kokfelt, Thomas Find; Willerslev, Eva; Bjerager, Morten;
                Heijboer, Tjerk; Keulen, Nynke; Larsen, Lotte Melchior;
                Pedersen, Christian Brogaard; Pedersen, Mikael; Svennevig,
                Kristian; Sønderholm, Martin; Walentin, Katja Tandrup; Weng,
                Willy Lehmann, 2023, "Seamless digital 1:500 000 scale
                geological map of Greenland, version 2.0",
                GEUS GeoNetwork catalogue."""
            ),
            "url": "https://data.geus.dk/geonetwork/srv/eng/catalog.search#/metadata/0343a36d-34d4-4305-89dc-4aea8461095d?lang=en",
        },
    ),
)

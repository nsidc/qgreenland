from qgreenland.models.config.asset import OnlineAsset
from qgreenland.models.config.dataset import Dataset, DatasetMetadata

# TODO: combine SDFI topo and satellite photos into one dataset with multiple
# assets? Better citation for these two?
# TODO: note about how to access data/directing users to the
# https://dataforsyningen.dk site to find additional data with their own
# accounts.
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
            """The web service consists of vector data covering the entire
            ice-free area. Vector data is supplemented with place names, curves,
            elevations and hillshade, as well as other relevant data, obtained
            from external data owners.

            Open Country Greenland can be used to plan a stay in the open
            country, thus helping, for example, hunters, anglers and tourists
            who need to hike and find their way around the landscape.

            Emergency services, police and defence, which have to carry out
            emergency operations and rescue operations in the open country, are
            also expected to be able to find good use of the service.

            Errors have been found in the height model for some steep mountain
            peaks in Greenland (more than 100 m). We are investigating the
            extent and possibilities of correcting the errors. If you have
            questions or notice an error, please send an email to
            support@sdfi.dk."""
        ),
        citation={
            "text": (
                """Web service wms/gl_aabent_land has been prepared on the basis
                  of data from the Agency for Data Supply and Infrastructure and
                  the following other institutions: Asiaq, the Geodata Agency,
                  Landsplan, Nukissiorfiit, Oqaasileriffik and Tusass"""
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
            """The web service consists of orthophotos from several satellite
            and aerial sources; recorded in different time periods and degrees
            of resolution; from 10m pixels to 0.2m pixels. The photos are
            supplemented in the web service by e.g. elevations (elevations and
            curves), place names and grid."""
        ),
        citation={
            "text": (
                """Web service wms/gl_satellitfoto has been prepared on the
                basis of data from the Data Supply and Infrastructure Agency and the following
                other institutions: Asiaq, the Geodata Agency, Landsplan, Nukissiorfiit,
                Oqaasileriffik and Tusass"""
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

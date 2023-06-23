from qgreenland.config.helpers.assets.ogr_remote import ogr_remote_asset
from qgreenland.models.config.dataset import Dataset

asiaq_nunagis = Dataset(
    id="asiaq_nunagis",
    assets=[
        ogr_remote_asset(
            asset_id="buildings",
            output_file="{output_dir}/fetched.geojson",
            url="https://kort.nunagis.gl/refserver/rest/services/Kortportal/Kortportal_TekniskGrundkort/MapServer/82/query/?f=json&where=OBJECTID+is+not+null&outFields=*&orderByFields=OBJECTID+ASC",
        ),
        # "VEJMIDTE" means "MIDDLE OF THE ROAD" according to Google Translate
        ogr_remote_asset(
            asset_id="roads",
            output_file="{output_dir}/fetched.geojson",
            url="https://kort.nunagis.gl/refserver/rest/services/Kortportal/Kortportal_TekniskGrundkort/MapServer/38/query/?f=json&where=OBJECTID+is+not+null&outFields=*&orderByFields=OBJECTID+ASC",
        ),
    ],
    metadata={
        "title": "Asiaq Map Portal",
        "abstract": (
            """ASIAQ Greenland Survey undertakes surveys and research projects,
            based on non-living physical data from the environment in
            Greenland. Our data are derived from; mapping of cities and
            non-urban areas, measuring of water resources, climate monitoring,
            soil testing, surveying and stakeouts at construction projects. All
            these, provides a unique knowledge of the arctic climate, soil
            conditions, water resources and topography of Greenland, which makes
            possible for the Greenlandic society, partners, and costumers to
            plan and exploit the physical environment and resources.

            Asiaq is 100% owned by the Greenlandic Government and had surveyed
            all around in Greenland for more than 60 years.

            Data were retreived from the NunaGIS data server, which provides
            data for the the Asiaq Map Portal
            (https://kort.nunagis.gl/refserver/rest/services/Kortportal/). To
            learn more about NunaGIS, see: https://nunagis-asiaq.hub.arcgis.com/.
            """
        ),
        "citation": {
            "text": (
                """ASIAQ Greenland Survey (2023). Date accessed: {{date_accessed}}."""
            ),
            "url": "https://www.asiaq-greenlandsurvey.gl/",
        },
    },
)

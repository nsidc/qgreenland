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
        "title": "Asiaq Map Portal Techincal Basemap",
        "abstract": (
            """The NunaGIS data server provides data for the the Asiaq Map
            Portal Technical Basemap, which includes a variety of datasets."""
        ),
        "citation": {
            "text": ("""NunaGIS (2023). Date accessed: {{date_accessed}}."""),
            "url": "https://kort.nunagis.gl/refserver/rest/services/Kortportal/Kortportal_TekniskGrundkort/MapServer",
        },
    },
)

# flake8: noqa E501
"""Generate a sample layer manifest file.

Describes how to find a layer's files relative to the manifest, how to represent
the layer in a browsing interface, and tags for locating layers in a browsing
interface."""
import json


manifest = {
    # version of this file.
    'version': 'v0.1.0',
    'layers': [
        {
            # This id key indicates that the layer assets live under
            # https://nsidc.org/qgreenland/layers/nunagis_bird_protected_areas/
            'id': 'nunagis_bird_protected_areas',
            'assets': [
                'nunagis_bird_protected_areas.gpkg',  # https://nsidc.org/qgreenland/layers/nunagis_bird_protected_areas/nunagis_bird_protected_areas.gpkg
                'nunagis_bird_protected_areas.qml',  # https://nsidc.org/qgreenland/layers/nunagis_bird_protected_areas/nunagis_bird_protected_areas.qml
            ],

            'title': 'Bird protected areas',
            'description': 'Polygons representing protected areas for birds.',

            # The group hierarchy. This indicates that the layer should be
            # categorized under `Biology/Birds/` in the QGIS layer panel.
            'hierarchy': ['Biology', 'Birds'],

            # Used for search or tag-based browsing.
            'tags': ['Birds', 'Nests', 'Protected areas', 'Restricted areas'],

            'layer_details': """Polygons representing areas protected for birds.

<h2>Original Data Source</h2>
NunaGIS data server protected area data

The NunaGIS data server provides a range of datasets on animal areas of
importance and protected areas. These data are used to populate the following
QGreenland data layers: Walrus Protected Areas, Goose Protected Areas, Caribou
Calving Areas, Beluga Areas, Bird Protected Areas, Thickbilled Murre Breeding
Colony 5km Zones, Seabird Breeding Colonies, Eider Protected Areas, Murre Group
1 km Zones, Musk Oxen Calving Areas, Narwhal Areas, and Polar Bear Breeding
Areas.

<h2>Citation</h2>
<a href="https://kort.nunagis.gl/server/rest/services/Hosted">NunaGIS (2020).
Date accessed: 2021-01-26.</a>

<h2>Provenance</h2>
<ul>
<li><pre>gdalwarp ... v3.1.2</pre></li>
<li><pre>gdaltranslate ... v3.1.2</pre></li>
<li>...</li>
</ul>
""",
        },
    ],
}


if __name__ == '__main__':
    print(json.dumps(manifest, indent=2))

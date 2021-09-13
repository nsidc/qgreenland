# flake8: noqa E501
"""Generate a sample layer manifest file.

Describes how to find a layer's files relative to the manifest, how to represent
the layer in a browsing interface, and tags for locating layers in a browsing
interface."""
import json


manifest = {
    # Version of this file's specification.
    'version': 'v0.1.0',
    # Version of QGreenland used to generate this manifest
    'qgr_version': 'v2.0.0',

    'layers': [
        {
            # This id key indicates that the layer assets live under
            # https://nsidc.org/qgreenland/layers/nunagis_bird_protected_areas/
            'id': 'nunagis_bird_protected_areas',

            'title': 'Bird protected areas',
            'description': 'Polygons representing protected areas for birds.',

            # The group hierarchy. This indicates that the layer should be
            # categorized under `Biology/Birds/` in the QGIS layer panel.
            'hierarchy': ['Biology', 'Birds'],

            # Used for search or tag-based browsing.
            'tags': ['Birds', 'Nests', 'Protected areas', 'Restricted areas'],

            'assets': [
                {
                    # https://nsidc.org/qgreenland/layers/nunagis_bird_protected_areas/nunagis_bird_protected_areas.gpkg
                    'file': 'nunagis_bird_protected_areas.gpkg',
                    'type': 'data',
                    'checksum': 'd568078f6ef14df085c2d84e2eff573e',
                    'size_bytes': 184320,
                },
                {
                    # https://nsidc.org/qgreenland/layers/nunagis_bird_protected_areas/nunagis_bird_protected_areas.qml
                    'file': 'nunagis_bird_protected_areas.qml',
                    'type': 'style',
                    'checksum': 'b7c14ec6110fa820ca6b65f5aec85911',
                    'size_bytes': 1521,
                },
                {
                    'file': 'nunagis_bird_protected_areas.xml',
                    'type': 'ancillary',
                    'checksum': 'e491b6919b9a77a9fe98a8e574214abf',
                    'size_bytes': 2091,
                },
            ],

            # Shown in the preview window as well as the layer metadata tab
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

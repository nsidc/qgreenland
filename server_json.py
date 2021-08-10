import json


manifest = {
    # version of this file.
    'version': 'v0.1.0',
    'layers': [
        {
            # This id key indicates that the layer assets live under
            # https://example.com/foo/
            'id': 'foo',
            'assets': [
                'foo.tif',  # https://example.com/foo/foo.tif
                'foo.tif.xml',  # https://example.com/foo/foo.tif.xml
                'foo.qml',  # https://example.com/foo/foo.qml
            ],
            'title': 'Foo',
            'description': 'Foo is a very cool raster layer',
            # The group hierarchy. This indicates that the layer should be
            # categorized under `Biology/Birds/` in the QGIS layer panel.
            'hierarchy': ['Biology', 'Birds'],
            # Used for search or tag-based browsing.
            'tags': ['Birds', 'Nests', 'Protected areas'],

            # Do we want structure, or write out one big string of HTML to
            # express structure?
            'preview_panel': {
                'Layer metadata': 'Dataset metadata text and markup.',
                'provenance': '',
                'FooBar': '<>'
            },


            # Here's some ideas about provenance.  Probably won't be included
            # here in this manifest file though.
            'provenance': [
                {
                    'operation': 'executable',
                    'executable_version': 'v3.1.2',
                    'executed': 'gdalwarp -t_srs "EPSG:3413" {input_file} {output_file}'
                },
                {
                    'operation': 'qgr_python_function',
                    'qgr_version': 'v2.0.0alpha1',
                    'executed': 'qgreenland.some.module:func(arg1, arg2, kwarg1=kwarg1)',
                },
            ],
        },
    ]
    
}


if __name__ == '__main__':
    print(json.dumps(manifest))

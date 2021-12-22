import csv
import json
import tempfile
from pathlib import Path
from unittest.mock import patch

from qgreenland.test.constants import (
    MOCK_COMPILE_PACKAGE_DIR,
    MOCK_RELEASE_LAYERS_DIR,
)
from qgreenland.util.config.export import (
    export_config_csv,
    export_config_manifest,
)


@patch(
    'qgreenland.util.layer.RELEASE_LAYERS_DIR',
    new=MOCK_RELEASE_LAYERS_DIR,
)
def test_export_config_manifest(full_cfg):
    common = {
        'description': 'Example layer description.',
        # TODO: Generate this with imported function? This should be tested
        # by itself elsewhere, so there's no need to test the expected output
        # here too.
        'layer_details': """Example layer description.

=== Original Data Source ===
Example Dataset

Example abstract.

Citation:
NSIDC 2020

Citation URL:
https://nsidc.org""",
        'tags': ['foo', 'bar', 'baz'],
        'hierarchy': ['Group', 'Subgroup'],
    }
    with tempfile.NamedTemporaryFile('r') as tf:
        export_config_manifest(
            full_cfg,
            output_path=Path(tf.name),
        )

        actual = json.load(tf)

    assert type(actual['qgr_version']) is str
    assert len(actual['qgr_version']) >= 6
    del actual['qgr_version']

    # For now, do not include online layers in the layer manifest. The
    # `QGreenland Custom` QGIS Plugin does not currently support online
    # layers. Once online layers are supported in the plugin, this commented out
    # `online_asset` can be re-added:
    # online_asset = {
    #     'type': 'online',
    #     **full_cfg.layers['example_online'].input.asset.dict(
    #         include={'provider', 'url'},
    #     ),
    # }
    expected = {
        'version': 'v0.1.0',
        'layers': [
            # {
            #     'id': 'example_online',
            #     'title': 'Example online',
            #     'assets': [online_asset],
            #     **common,
            # },
            {
                'id': 'example_raster',
                'title': 'Example raster',
                'assets': [
                    {
                        'checksum': 'a9a103f208179726038fa7178747a0a1',
                        'file': 'example.tif',
                        'size_bytes': 287,
                        'type': 'data',
                    },
                    {
                        'checksum': '22b427acc6e4ebf57052115fdd5ac450',
                        'file': 'example.tif.aux.xml',
                        'size_bytes': 332,
                        'type': 'ancillary',
                    },
                ],
                **common,
            },
        ],
    }

    assert actual == expected


@patch(
    'qgreenland.util.layer.COMPILE_PACKAGE_DIR',
    new=MOCK_COMPILE_PACKAGE_DIR,
)
def test_export_config_csv(full_cfg):
    common = {
        'Data Source Abstract': 'Example abstract.',
        'Data Source Citation': 'NSIDC 2020',
        'Data Source Citation URL': 'https://nsidc.org',
        'Data Source Title': 'Example Dataset',
        'Group': 'Group',
        'Layer Description': 'Example layer description.',
        'Layer Size': '0 Bytes',
        'Layer Size Bytes': '0',
        'Subgroup': 'Subgroup',
    }
    with tempfile.NamedTemporaryFile('r') as tf:
        export_config_csv(
            full_cfg,
            output_path=Path(tf.name),
        )

        actual = list(csv.DictReader(tf))

    expected = [
        {
            **common,
            'Layer Title': 'Example online',
            'Vector or Raster': 'Online',
        },
        {
            **common,
            'Layer Title': 'Example raster',
            'Vector or Raster': 'Raster',
            'Layer Size': '619 Bytes',
            'Layer Size Bytes': '619',
        },
    ]

    assert actual == expected

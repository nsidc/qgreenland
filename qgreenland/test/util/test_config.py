import csv
import tempfile
from pathlib import Path
from unittest.mock import patch

from qgreenland.test.constants import MockTaskType
from qgreenland.util.config import (
    export_config_csv,
    export_config_manifest,
)


@patch(
    'qgreenland.util.misc.TaskType',
    new=MockTaskType,
)
def test_export_config_manifest(full_cfg):
    with tempfile.NamedTemporaryFile('r') as tf:
        export_config_manifest(
            full_cfg,
            output_path=Path(tf.name),
        )

    assert False


@patch(
    'qgreenland.util.misc.TaskType',
    new=MockTaskType,
)
def test_export_config_csv(full_cfg):
    common = {
        'Data Source Abstract': 'Example abstract',
        'Data Source Citation': 'NSIDC 2020',
        'Data Source Citation URL': 'https://nsidc.org',
        'Data Source Title': 'Example Dataset',
        'Group': 'Group',
        'Layer Description': 'Example layer description',
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

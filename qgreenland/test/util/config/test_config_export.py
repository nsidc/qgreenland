import csv
import tempfile
from pathlib import Path
from unittest.mock import patch

from qgreenland.test.constants import MOCK_COMPILE_PACKAGE_DIR
from qgreenland.util.config.export import export_config_csv


@patch(
    "qgreenland.util.layer.COMPILE_PACKAGE_DIR",
    new=MOCK_COMPILE_PACKAGE_DIR,
)
def test_export_config_csv(full_cfg):
    common = {
        "Data Source Abstract": "Example abstract.",
        "Data Source Citation": "NSIDC 2020",
        "Data Source Citation URL": "https://nsidc.org",
        "Data Source Title": "Example Dataset",
        "Group": "Group",
        "Layer Description": "Example layer description.",
        "Layer Size": "0 Bytes",
        "Layer Size Bytes": "0",
        "Subgroup": "Subgroup",
    }
    with tempfile.NamedTemporaryFile("r") as tf:
        export_config_csv(
            full_cfg,
            output_path=Path(tf.name),
        )

        actual = list(csv.DictReader(tf))

    expected = [
        {
            **common,
            "Layer Title": "Example online",
            "Vector or Raster": "Raster",
            "Internet Required?": "False",
        },
        {
            **common,
            "Layer Title": "Example raster",
            "Vector or Raster": "Raster",
            "Layer Size": "619 Bytes",
            "Layer Size Bytes": "619",
            "Internet Required?": "True",
        },
    ]

    assert actual == expected

from decimal import Decimal

from qgreenland.config.datasets.future_projections import (
    future_icesheet_coverage as dataset,
)
from qgreenland.config.helpers.steps.compress_and_add_overviews import compress_and_add_overviews
from qgreenland.config.helpers.steps.warp import warp
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput


LAYER_RCPS = (
    26,
    45,
    85,
)

layers = [
    Layer(
        id=f'future_ice_sheet_coverage_rcp_{rcp}',
        title=(
            f'Future ice sheet coverage for RCP {Decimal(rcp) / 10} scenario'
            ' for the year 3007 (1.8km)'
        ),
        description=(
            """Fraction of a grid cell covered by ice (grounded or floating) in
            the year 3007. Values less than or equal to 16% are masked."""
        ),
        tags=[],
        style='future_ice_sheet_coverage',
        input=LayerInput(
            dataset=dataset,
            asset=dataset.assets[f'rcp_{rcp}'],
        ),
        steps=[
            *warp(
                input_file=(
                    'NETCDF:{input_dir}/'
                    f'percent_gris_g1800m_v3a_rcp_{rcp}_0_1000.nc:sftgif'
                ),
                output_file='{output_dir}/extracted.tif',
                warp_args=(
                    '-srcnodata', '0',
                    '-tr', '1800', '1800',
                ),
                cut_file=project.boundaries['data'].filepath,
            ),
            *compress_and_add_overviews(
                input_file='{input_dir}/extracted.tif',
                output_file='{output_dir}/final.tif',
                dtype_is_float=True,
            ),
        ],
    ) for rcp in LAYER_RCPS
]

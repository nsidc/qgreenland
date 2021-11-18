import datetime as dt
from typing import Generator

from qgreenland.config.datasets.esa_cci import esa_cci_gravimetric_mass_balance_dtu as dataset
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput


# TODO: consider pulling this information from the source files themselves?
# Could look in the private repo location for list of files and parse start/end
# dates...
_gravimetric_mass_balance_date_ranges = (
    (dt.date(2003, 1, 1), dt.date(2007, 12, 31)),
    (dt.date(2004, 1, 1), dt.date(2008, 12, 31)),
    (dt.date(2005, 1, 1), dt.date(2009, 12, 31)),
    (dt.date(2006, 1, 1), dt.date(2010, 12, 31)),
    (dt.date(2007, 1, 1), dt.date(2011, 12, 31)),
    (dt.date(2008, 1, 1), dt.date(2012, 12, 31)),
    (dt.date(2009, 1, 1), dt.date(2013, 12, 31)),
    (dt.date(2010, 1, 1), dt.date(2014, 11, 30)),
    (dt.date(2011, 2, 1), dt.date(2015, 12, 31)),
    (dt.date(2012, 1, 1), dt.date(2016, 12, 31)),
    (dt.date(2013, 1, 1), dt.date(2017, 7, 1)),
    (dt.date(2014, 1, 1), dt.date(2018, 12, 31)),
    (dt.date(2015, 1, 1), dt.date(2019, 12, 31)),
)


def _make_layers() -> Generator[Layer, None, None]:
    for start_date, end_date in _gravimetric_mass_balance_date_ranges:
        start_year = start_date.year
        end_year = end_date.year

        yield Layer(
            id=f'esa_cci_gravimetric_mass_balance_dtu_{start_year}_{end_year}',
            title=f'Mass balance trend {start_year}-{end_year}',
            description=(
                f"""Trend derived from the period {start_year}-01-01 to {end_year}-12-31 via gravity
                measurements. Data is on a ~50 km resolution grid (displayed as
                points)."""
            ),
            tags=[],
            style='gmb_dtu_space',
            input=LayerInput(
                dataset=dataset,
                asset=dataset.assets['only'],
            ),
            steps=[
                *ogr2ogr(
                    input_file=(
                        '{input_dir}/QGREENLAND_GEOPACKAGES/'
                        f'points_{start_date:%Y-%m-%d}_{end_date:%Y-%m-%d}.gpkg'
                    ),
                    output_file=(
                        '{output_dir}/'
                        f'points_{start_date:%Y-%m-%d}_{end_date:%Y-%m-%d}.gpkg'
                    ),
                    boundary_filepath=project.boundaries['data'].filepath,
                ),
            ],
        )


layers = list(_make_layers())

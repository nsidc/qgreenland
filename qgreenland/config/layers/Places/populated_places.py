import qgreenland.config.datasets.political_boundaries as political_boundaries
from qgreenland.config.datasets.asiaq_nunagis import asiaq_nunagis
from qgreenland.config.datasets.statbank import statbank
from qgreenland.config.helpers.layers.populated_places import process_populated_places
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import PythonStep

populated_places = Layer(
    id="populated_places",
    title="Populated places",
    style="populated_places",
    description=(
        """Points representing populated places in Greenland.

QGreenland Team - Noted Data Issues:

* West coast of Greenland, near Paamiut: Ivittuut is abandoned.

* East Greenland: Ikkatteq is an abandoned airstrip and is not populated.

* Near Ittoqqortoormiit: Uunartoq is abandoned.

* Near Qaanaaq: Qeqertarsuaq and Moriusaq are abandoned.

* Near Upernavik: Tussaaq is abandoned.

* Near Uummannaq: Illorsuit and Nuugaatsiaq are two recently abandoned
  settlements (2017) due a massive landslide and subsequent tsunami."""
    ),
    tags=["places"],
    inputs=[
        # This layer provides points represented populated places (geojson).
        LayerInput(
            dataset=asiaq_nunagis,
            asset=asiaq_nunagis.assets["populated_places"],
        ),
        # This input provides population values for 1977-2026 (csv)
        LayerInput(
            dataset=statbank,
            asset=statbank.assets["localities_population"],
        ),
        # This input provides numbers of international passengers (csv)
        LayerInput(
            dataset=statbank,
            asset=statbank.assets["international_passengers"],
        ),
        # This input provides a multipolygon of municipalities and gives us the
        # municipality name for each populated place. (gpkg)
        LayerInput(
            dataset=political_boundaries.nunagis_pop2019_municipalities,
            asset=political_boundaries.nunagis_pop2019_municipalities.assets["only"],
        ),
    ],
    steps=[
        PythonStep(
            function=process_populated_places,
        ),
    ],
)

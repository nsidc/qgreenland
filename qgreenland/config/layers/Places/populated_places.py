from qgreenland.config.datasets.asiaq_nunagis import asiaq_nunagis
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput
from qgreenland.models.config.step import CommandStep

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
    input=LayerInput(
        dataset=asiaq_nunagis,
        asset=asiaq_nunagis.assets["populated_places"],
    ),
    steps=[
        CommandStep(
            args=[
                "ogrmerge.py",
                "-single",
                "-o",
                "{output_dir}/populated_places.gpkg",
                "{input_dir}/*geojson",
            ],
        ),
        *ogr2ogr(
            input_file="{input_dir}/populated_places.gpkg",
            output_file="{output_dir}/final.gpkg",
            boundary_filepath=project.boundaries["data"].filepath,
            ogr2ogr_args=(
                "-nln",
                "populated_places",
                "-dialect",
                "sqlite",
                "-sql",
                "\"SELECT geom, Ny_grønlandsk as 'New Greenlandic', Ny_grønlandsk as 'label', Gammel_grønlandsk as 'Old Greenlandic', Dansk as Danish, Alternativt_stednavn  as 'Alternative placename', Indbyggertal_2016 as 'Population 2016' FROM merged\"",
            ),
        ),
    ],
)

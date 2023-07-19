from qgreenland.config.datasets.asiaq_placenames import asiaq_private_placenames
from qgreenland.config.helpers.steps.ogr2ogr import ogr2ogr
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput

points_of_interest = Layer(
    id="points_of_interest",
    title="Points of interest",
    description="Points representing named points of interest in Greenland.",
    tags=["places"],
    style="labeled_point",
    input=LayerInput(
        dataset=asiaq_private_placenames,
        asset=asiaq_private_placenames.assets["only"],
    ),
    steps=[
        *ogr2ogr(
            input_file="{input_dir}/translations_joined.gpkg",
            output_file="{output_dir}/final.gpkg",
            boundary_filepath=project.boundaries["data"].filepath,
            ogr2ogr_args=(
                "-sql",
                (
                    '\'SELECT *, "English explanation of Object designation"'
                    ' || ":" || "New Greenlandic" as label'
                    " FROM translations_joined"
                    ' WHERE "Object designation" NOT IN ("BY", "BYGD")\''
                ),
            ),
        ),
    ],
)

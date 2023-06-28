from qgreenland.config.datasets.circumpolar_arctic_vegetation_map import (
    circumpolar_arctic_vegetation_map as dataset,
)
from qgreenland.config.helpers.steps.compress_and_add_overviews import (
    compress_and_add_overviews,
)
from qgreenland.config.helpers.steps.decompress import decompress_step
from qgreenland.config.helpers.steps.warp import warp
from qgreenland.config.project import project
from qgreenland.models.config.layer import Layer, LayerInput

circumpolar_arctic_vegetation_map_layer = Layer(
    id="circumpolar_arctic_vegetation_map",
    title="Vegetation classification map (1km)",
    description=(
        """Arctic vegetation classification raster.

            Individual raster values are mapped to vegetation types as follows:

            'Raster Code': 'Vegetation Unit' - 'Short Description'
            1: B1 - Cryptogam, herb barren
            2: B2a - Cryptogam, barren complex
            3: B3 - Non-carbonate mountain complex
            4: B4 - Carbonate mountain complex
            5: B2b - Cryptogam, barren, dwarf-shrub complex
            21: G1 - Graminoid, forb, cryptogam tundra
            22: G2 - Graminoid, prostrate dwarf-shrub, forb, moss tundra
            23: G3 - Non-tussock sedge, dwarf-shrub, moss tundra
            24: G4 - Tussock-sedge, dwarf-shrub, moss tundra
            31: P1 - Prostrate dwarf-shrub, herb, lichen tundra
            32: P2 - Prostrate/hemi-prostrate dwarf-shrub, lichen tundra
            33: S1 - Erect dwarf-shrub, moss tundra
            34: S2 - Low-shrub, moss tundra
            41: W1 - Sedge/grass, moss wetland complex
            42: W2 - Sedge, moss, dwarf-shrub wetland complex
            43: W3 - Sedge, moss, low-shrub wetland complex
            91: FW - Fresh water
            92: SW - Saline water
            93: GL - Glacier
            99: NA - Non-Arctic

             Environmental and climatic conditions are
            extreme, with a short growing season and low summer temperatures. The
            region support plants such as dwarf shrubs, herbs, lichens and mosses,
            which grow close to the ground. As one moves southward (outward from
            map's center in all directions), the amount of warmth available for
            plant growth increases considerably, allowing the size, abundance, and
            variety of plants to increase as well. Climate and other environmental
            controls, such as landscape, topography, soil chemistry, soil moisture,
            and the available plants that historically colonized an area, also
            influence the distribution of plant communities.

            For more information, visit:
            https://www.geobotany.uaf.edu/cavm/abstract.php."""
    ),
    tags=[],
    style="arctic_vegetation",
    input=LayerInput(
        dataset=dataset,
        asset=dataset.assets["only"],
    ),
    steps=[
        decompress_step(
            input_file="{input_dir}/Raster\\ CAVM\\ GIS\\ data.zip",
        ),
        *warp(
            input_file="{input_dir}/raster_cavm_v1.tif",
            output_file="{output_dir}/warped.tif",
            cut_file=project.boundaries["background"].filepath,
            warp_args=(
                "-tr",
                "1000",
                "1000",
            ),
        ),
        *compress_and_add_overviews(
            input_file="{input_dir}/warped.tif",
            output_file="{output_dir}/compressed.tif",
            dtype_is_float=False,
        ),
    ],
)

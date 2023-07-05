from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

circumpolar_arctic_vegetation_map = Dataset(
    id="circumpolar_arctic_vegetation_map",
    assets=[
        HttpAsset(
            id="only",
            urls=[
                (
                    "https://data.mendeley.com/public-files/datasets/c4xj5rv6kv/files/5223c414-234a-498c-ae08-3100cb38510f/file_downloaded"
                ),
            ],
        ),
    ],
    metadata={
        "title": "Raster Circumpolar Arctic Vegetation Map",
        "abstract": (
            """Land cover maps are the basic data layer required for
            understanding and modeling ecological patterns and processes. The
            Circumpolar Arctic Vegetation Map (CAVM), produced in 2003, has been
            widely used as a base map for studies in the arctic tundra
            biome. However, the relatively coarse resolution and vector format
            of the map were not compatible with many other data sets. We present
            a new version of the CAVM, building on the strengths of the original
            map, while providing a finer spatial resolution, raster format, and
            improved mapping. The Raster CAVM uses the legend, extent and
            projection of the original CAVM. The legend has 16 vegetation types,
            glacier, saline water, freshwater, and non-arctic land. The Raster
            CAVM divides the original rock-water-vegetation complex map unit
            that mapped the Canadian Shield into two map units, distinguishing
            between areas with lichen- and shrub-dominated vegetation. In
            contrast to the original hand-drawn CAVM, the new map is based on
            unsupervised classifications of seventeen geographic/floristic
            sub-sections of the Arctic, using AVHRR and MODIS data (reflectance
            and NDVI) and elevation data. The units resulting from the
            classification were modeled to the CAVM types using a wide variety
            of ancillary data. The map was reviewed by experts familiar with
            their particular region, including many of the original authors of
            the CAVM from Canada, Greenland (Denmark), Iceland, Norway
            (including Svalbard), Russia, and the U.S. The analysis presented
            here summarizes the area, geographical distribution, elevation,
            summer temperatures, and NDVI of the map units. The greater spatial
            resolution of the Raster CAVM allowed more detailed mapping of
            water-bodies and mountainous areas. It portrays coastal-inland
            gradients, and better reflects the heterogeneity of vegetation type
            distribution than the original CAVM. Accuracy assessment of random
            1-km pixels interpreted from 6 Landsat scenes showed an average of
            70 % accuracy, up from 39 % for the original CAVM. The distribution
            of shrub-dominated types changed the most, with more prostrate shrub
            tundra mapped in mountainous areas, and less low shrub tundra in
            lowland areas. This improved mapping is important for quantifying
            existing and potential changes to land cover, a key environmental
            indicator for modeling and monitoring ecosystems.

            Related Publication:

            Martha K. Raynolds, Donald A. Walker, Andrew Balser, Christian Bay,
            Mitch Campbell, Mikhail M. Cherosov, Fred J.A. Daniëls, Pernille
            Bronken Eidesen, Ksenia A. Ermokhina, Gerald V. Frost, Birgit
            Jedrzejek, M. Torre Jorgenson, Blair E. Kennedy, Sergei S. Kholod,
            Igor A. Lavrinenko, Olga V. Lavrinenko, Borgþór Magnússon, Nadezhda
            V. Matveyeva, Sigmar Metúsalemsson, Lennart Nilsen, Ian Olthof, Igor
            N. Pospelov, Elena B. Pospelova, Darren Pouliot, Vladimir Razzhivin,
            Gabriela Schaepman-Strub, Jozef Šibík, Mikhail Yu. Telyatnikov,
            Elena Troeva, A raster version of the Circumpolar Arctic Vegetation
            Map (CAVM), Remote Sensing of Environment, Volume 232, 2019, 111297,
            ISSN 0034-4257,
            https://doi.org/10.1016/j.rse.2019.111297. (https://www.sciencedirect.com/science/article/pii/S0034425719303165).
            """
        ),
        "citation": {
            "text": (
                """Raynolds, Martha; Walker, Donald (2022), 'Raster Circumpolar
                Arctic Vegetation Map', Mendeley Data, V2, doi:
                10.17632/c4xj5rv6kv.2"""
            ),
            "url": "https://data.mendeley.com/datasets/c4xj5rv6kv/2",
        },
    },
)

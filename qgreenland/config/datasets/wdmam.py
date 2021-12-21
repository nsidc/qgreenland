from qgreenland.models.config.asset import CommandAsset
from qgreenland.models.config.dataset import Dataset


wdmam = Dataset(
    id='wdmam',
    assets=[
        CommandAsset(
            id='only',
            args=[
                'wget',
                'http://wdmam.org/file/wdmam.asc',
                '-O', '{output_dir}/full_wdmam.xyz',
            ],
        ),
    ],
    metadata={
        'title': 'World Digital Magnetic Anomaly Map',
        'abstract': (
            """The WDMAM (World Digital Magnetic Anomaly Map) is an
            international scientific project under the auspices of IAGA
            (International Association of Geomagnetism and Aeronomy) and CGMW
            (Commission for the Geological Map of the World), aiming to compile
            and make available magnetic anomalies caused by the Earth
            lithosphere, on continental and oceanic areas, in a comprehensive
            way, all over the World.

            The project started in 2003 and resulted in a first version of the
            map (Korhonen et al., 2007). A call for candidates initiated in 2010
            led to the building of a new map which, after evaluation and
            correction, was released at the IUGG General Assembly of Prag in
            June 2015 as WDMAM version 2.0. This web site aims to distribute
            freely and as widely as possible a provisional version of the map
            (in jpeg format), the full grid (in ASCII format) or parts of the
            grid (in ASCII or GMT grd formats) to interested scientists and the
            general public. A printed version of the map will be released by
            CGMW in a very near future. A paper describing the building of the
            map will be published soon (Lesur et al., 2016, in press)."""
        ),
        'citation': {
            'text': (
                """Dyment, J., Lesur, V., Hamoudi, M., Choi, Y., Thebault, E.,
                Catalan, M., the WDMAM Task Force*, the WDMAM Evaluators**, and
                the WDMAM Data Providers**, World Digital Magnetic Anomaly Map
                version 2.0, map available at http://www.wdmam.org."""
            ),
            'url': 'http://www.wdmam.org',
        },
    },
)

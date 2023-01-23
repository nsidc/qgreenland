from qgreenland.models.config.asset import HttpAsset
from qgreenland.models.config.dataset import Dataset

monthly_albedo = Dataset(
    id="monthly_albedo",
    assets=[
        HttpAsset(
            id="2018_07",
            urls=[
                "https://dataverse01.geus.dk/api/access/datafile/:persistentId?persistentId=doi:10.22008/FK2/URJ2VK/XXQUSC"
            ],
        ),
        HttpAsset(
            id="2019_07",
            urls=[
                "https://dataverse01.geus.dk/api/access/datafile/:persistentId?persistentId=doi:10.22008/FK2/URJ2VK/6YZNSZ"
            ],
        ),
    ],
    metadata={
        "title": "SICE 1 km broadband albedo monthly averages and visualisations",
        "abstract": (
            """We present a simplified atmospheric correction algorithm for
            snow/ice albedo retrievals using single view satellite
            measurements. The validation of the technique is performed using
            Ocean and Land Colour Instrument (OLCI) on board Copernicus
            Sentinel-3 satellite and ground spectral or broadband albedo
            measurements from locations on the Greenland ice sheet and in the
            French Alps. Through comparison with independent ground
            observations, the technique is shown to perform accurately in a
            range of conditions from a 2100 m elevation mid-latitude location in
            the French Alps to a network of 15 locations across a 2390 m
            elevation range in seven regions across the Greenland ice
            sheet. Retrieved broadband albedo is accurate within 5% over a wide
            (0.5) broadband albedo range of the (N = 4155) Greenland
            observations and with no apparent bias."""
        ),
        "citation": {
            "text": (
                """Kokhanovsky A, Box JE, Vandecrux B, Mankoff KD, Lamare M,
                Smirnov A and Kern M (2020) The Determination of Snow Albedo
                from Satellite Measurements Using Fast Atmospheric Correction
                Technique. Remote Sensing 12(2), 234 doi: 10.3390/rs12020234
                https://www.mdpi.com/2072-4292/12/2/234"""
            ),
            "url": "doi.org/10.22008/FK2/URJ2VK",
        },
    },
)

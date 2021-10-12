from qgreenland.models.config.asset import ConfigDatasetHttpAsset
from qgreenland.models.config.dataset import ConfigDataset


hdx_hotosm = ConfigDataset(
    id='hdx_hotosm',
    assets=[
        ConfigDatasetHttpAsset(
            id='roads',
            urls=[
                'http://export.hotosm.org/downloads/72e59bb5-7886-4627-b207-ed1e3ea8a42a/hotosm_grl_roads_lines_shp.zip',
            ],
        ),
        ConfigDatasetHttpAsset(
            id='airports',
            urls=[
                'http://export.hotosm.org/downloads/72e59bb5-7886-4627-b207-ed1e3ea8a42a/hotosm_grl_airports_points_shp.zip',
            ],
        ),
        ConfigDatasetHttpAsset(
            id='seaports',
            urls=[
                'http://export.hotosm.org/downloads/72e59bb5-7886-4627-b207-ed1e3ea8a42a/hotosm_grl_sea_ports_points_shp.zip',
            ],
        ),
        ConfigDatasetHttpAsset(
            id='waterways',
            urls=[
                'http://export.hotosm.org/downloads/72e59bb5-7886-4627-b207-ed1e3ea8a42a/hotosm_grl_waterways_lines_shp.zip',
            ],
        ),
        ConfigDatasetHttpAsset(
            id='buildings',
            urls=[
                'http://export.hotosm.org/downloads/72e59bb5-7886-4627-b207-ed1e3ea8a42a/hotosm_grl_buildings_polygons_shp.zip',
            ],
        ),
        ConfigDatasetHttpAsset(
            id='financial_services',
            urls=[
                'http://export.hotosm.org/downloads/72e59bb5-7886-4627-b207-ed1e3ea8a42a/hotosm_grl_financial_services_points_shp.zip',
            ],
        ),
        ConfigDatasetHttpAsset(
            id='education_facilities',
            urls=[
                'http://export.hotosm.org/downloads/72e59bb5-7886-4627-b207-ed1e3ea8a42a/hotosm_grl_education_facilities_points_shp.zip',
            ],
        ),
        ConfigDatasetHttpAsset(
            id='health_facilities',
            urls=[
                'http://export.hotosm.org/downloads/72e59bb5-7886-4627-b207-ed1e3ea8a42a/hotosm_grl_health_facilities_points_shp.zip',
            ],
        ),
        ConfigDatasetHttpAsset(
            id='populated_places',
            urls=[
                'http://export.hotosm.org/downloads/72e59bb5-7886-4627-b207-ed1e3ea8a42a/hotosm_grl_populated_places_points_shp.zip',
            ],
        ),
        ConfigDatasetHttpAsset(
            id='points_of_interest',
            urls=[
                'http://export.hotosm.org/downloads/72e59bb5-7886-4627-b207-ed1e3ea8a42a/hotosm_grl_points_of_interest_points_shp.zip',
            ],
        ),
    ],
    metadata={
        'title': 'Humanitarian OpenStreetMap Team',
        'abstract': (
            """Humanitarian OpenStreetMap Team (HOT) is an international team
            dedicated to humanitarian action and community development through
            open mapping. HOT works together to provide map data which
            revolutionises disaster management, reduces risks, and contributes
            to achievement of the Sustainable Development Goals.


            Full HOT License information:

            Copyright (c) 2015-2020, Humanitarian OpenStreetMap Team All rights
            reserved.  Redistribution and use in source and binary forms, with
            or without modification, are permitted provided that the following
            conditions are met:

            Redistributions of source code must retain the above copyright
            notice, this list of conditions and the following disclaimer.
            Redistributions in binary form must reproduce the above copyright
            notice, this list of conditions and the following disclaimer in the
            documentation and/or other materials provided with the distribution.
            Neither the name of copyright holder nor the names of its
            contributors may be used to endorse or promote products derived from
            this software without specific prior written permission.  THIS
            SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
            IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
            LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
            FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
            COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
            INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
            BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
            LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
            CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
            LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
            ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
            POSSIBILITY OF SUCH DAMAGE.

            QGreenland Team: Noted Data Issues

            Layer: Populated places
            * Near Ittoqqortoormiit: Uunarteq and Itterajivit are abandoned
            settlements.
            * East Greenland: Pupik does not exist.
            * South Greenland: Uunartoq is a hot spring and is not populated
            * Kangilinnguit: abandoned Danish naval station.
            * Near Sisimiut: ‘skilift’ is not a populated settlement, it is a
            skiing area.
            * Nivâq near Aasiaat is an abandoned settlement.
            * Ataa just north of ilulissat is abandoned.
            * Qullissat, on Disko Island, appears twice, and is an abandoned
            settlement.
            * Near Uummannaq: Appat, Qernertuarssuit
            * North from Upernavik: Saattoq, Sarfaq, Kuuk, Aqqaalissiorfik,
            Itissaalik, Ikermiut, Illulik
            * North from Qaanaaq: Annoatok is a small, unpopulated hunting
            station.

            Layer: Health facilities

            There is some sort of a health clinic in all populated Greenland
            settlements and towns. Health clinics are larger and more
            sophisticated in towns. We note that health clinics exist in:

            * Qaanaaq
            * Siorapaluk
            * Savissivik
            * Kullorsuaq
            * Nuussuaq
            * Tasiusaq
            * Nutaarmiut
            * Innarsuit
            * Naajaat
            * Aappilatoq
            * Kangersuatsiaq
            * Upernavik Kujalleq
            * Qaarsut
            * Saattut
            * Niaqornat
            * Saaqqaq
            * Qeqertaq
            * Qasigiannguit
            * Ikamiut
            * Akunnaaq
            * Kitsissuarsuit
            * Attu
            * Niaqornaarsuk
            * Ikerasaarsuk
            * Ignniarfik
            * Kangerlussuaq
            * Maniitsoq
            * Atammik
            * Napasoq
            * Kangaamiut
            * Kapisillit
            * Qeqertarsuatsiaat
            * All settlements in the south of Greenland + Narsaq, Nanortalik,
            Narsaq.
            * Tasiilaq and five settlements around Tasiilaq
            * Ittoqqortoormiit

            Layer: Airports

            QGreenland Team notes that there are helistops in all settlements
            and other towns. We also note that there are airports for
            fixed-winged aircrafts in the following towns:

            * Qaanaaq
            * Upernavik
            * Qaarsut
            * Ilulissat
            * Aasiaat
            * Kangerlussuaq
            * Maniitsoq
            * Nuuk
            * Nerlerit Inaat
            * Paamiut
            * Pituffik (Thule Airbase)
            * Sisimiut
            * Narsarsuaq
            * Kulusuk

            Layer: Seaports

            Note that all Greenland towns and settlements are located by the
            sea. Hence ALL settlements and towns have a harbour or seaport.

            Layer: Financial services

            Basic banking for withdrawing money is available in all settlements
            and towns.

            Layer: Educational facilities

            This layer is quite incomplete. There is a school in every town and
            settlement in Greenland. Note that Nuuk includes six schools,
            Sisimiut two schools, and Ilulissat two schools."""
        ),
        'citation': {
            'text': (
                """Humanitarian OpenStreetMap Team (2020). Web:
                https://export.hotosm.org/en/v3/. Date accessed:
                {{date_accessed}}."""
            ),
            'url': 'https://www.hotosm.org/',
        },
    },
)

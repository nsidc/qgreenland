# ruff: noqa: C901


def prepare_places(*, input_dir: str):
    from pathlib import Path

    import geopandas as gpd
    import pandas as pd

    input_dir_path = Path(input_dir)

    # Read data
    municipalities = gpd.read_file(input_dir_path / "fetched.geojson")
    settlements = gpd.read_file(input_dir_path / "settlements.geojson")
    towns = gpd.read_file(input_dir_path / "towns.geojson")

    # Add identifier to towns and settlemetns
    towns["category"] = "town"
    settlements["category"] = "settlement"

    # Combine sttlements and towns
    places = pd.concat([towns, settlements])
    # Rename columns from Danish to English
    places = places.rename(
        columns={
            "Ny_grønlandsk": "New Greenlandic",
            "Gammel_grønlandsk": "Old Greenlandic",
            "Dansk": "Danish",
            "Alternativt_stednavn": "Alternative placename",
        }
    )
    # Add label column for labeling in QGIS
    places["label"] = places["New Greenlandic"]

    # Spatially join to municipalities in order to get the municipality name
    places = places.sjoin(
        municipalities[["geometry", "pop_municipality_2019_municip"]],
        predicate="intersects",
    )
    places = places.rename(columns={"pop_municipality_2019_municip": "municipality"})
    # Drop unneccessary columns
    places = places.drop(columns=["OBJECTID", "index_right"])

    # Create an integer ID column to uniquely identify each place for later joins.
    places["id"] = range(len(places))

    # Ensure places geometries are in the QGreenland EPSG
    places.to_crs("EPSG:3413")

    return places


def prepare_pop_table(*, input_dir: str, places):
    """Prepare the `pop` table for populated places layer."""
    import datetime as dt
    import re
    from pathlib import Path

    import geopandas as gpd

    pop = gpd.read_file(Path(input_dir) / "BEXSTD.csv")

    pop_locality_map = {}
    pop_locality_re = re.compile(
        r"(?P<locality>[\w ]+?)\s*(?:\((?P<category>\w+)(?:\s+in\s+(?P<municipality>\w+))?\))?\s*$"
    )
    for locality_str in set(pop.locality):
        # For now, Ignore population numbers that have an undisclosed location for a
        # given district.
        # TOOD: consider adding these to the district town?
        if "Uoplyst" in locality_str:
            continue

        # Ingore "Ikerasaarsuk" for now. There are two entries for this in the statbank stats:
        # Ikerasaarsuk (KAN)(settlement)
        # Ikerasaarsuk (UPE)
        # In the places database, we have one entry, "Ikerasaarsuk" in Kommune
        # Qeqertalik. It is not clear which one (if either) of the statbank
        # entries match.
        if "Ikerasaarsuk" in locality_str:
            continue

        match = pop_locality_re.match(locality_str)
        if not match:
            raise RuntimeError(f"Encountered unexpected locality: {locality_str}")

        locality = match.group("locality").strip()
        locality_cat = match.group("category")
        # Note: This may be None
        municipality = match.group("municipality")

        matching_places = places[places.label.str.lower() == locality.lower()]

        if municipality:
            matching_places = matching_places[
                matching_places.municipality.str.lower().str.contains(
                    municipality.lower()
                )
            ]

        # make an exception for Nerlerit Inaat (Airport), which we will consider
        # a settlement. This is how it is identified in the places database.
        if locality_str == "Nerlerit Inaat (Airport)":
            locality_cat = "settlement"

        if locality_cat:
            matching_places = matching_places[
                matching_places.category.str.lower() == locality_cat.lower()
            ]

        if len(matching_places) != 1:
            print(f"found no place match for {locality_str}")
        elif len(matching_places) == 1:
            pop_locality_map[locality_str] = int(matching_places.id.values[0])

    # create/update pop dataframe with ref to place_id.
    pop["place_id"] = pop["locality"].map(pop_locality_map)

    # rename col
    pop = pop.rename(columns={"Population in Localities January 1st": "population"})

    # Cast population as int
    pop["population"] = pop["population"].astype(int)

    # create start/end date columns for use with QGIS temporal controller.
    pop["start_date"] = pop["time"].apply(
        lambda year_str: dt.date(int(year_str) - 1, 1, 1)
    )
    pop["end_date"] = pop["time"].apply(
        lambda year_str: dt.date(int(year_str) - 1, 12, 31)
    )
    pop = pop.drop(columns=["time"])

    return pop


def _start_and_end_date_cols_for_monthly_data(df):
    import calendar
    import datetime as dt

    # Create start and end date fields. "time" is the year as a str. "month" is
    # the given name (e.g., "January").
    df["start_date"] = df.apply(
        lambda row: dt.date(
            int(row["time"]), list(calendar.month_name).index(row["month"]), 1
        ),
        axis=1,
    )
    df["end_date"] = df.apply(
        lambda row: dt.date(
            int(row["time"]),
            # Convert month name to integer month number
            list(calendar.month_name).index(row["month"]),
            # Get the last day of this month.
            calendar.monthrange(
                int(row["time"]),
                list(calendar.month_name).index(row["month"]),
            )[1],
        ),
        axis=1,
    )

    # Drop now-unnecessary time & month cols.
    df = df.drop(columns=["time", "month"])

    return df


def prepare_international_passengers(*, input_dir: str, places):
    """Prepare data for the 'international_passengers' table."""
    from pathlib import Path

    import geopandas as gpd

    int_passengers = gpd.read_file(Path(input_dir) / "TUXUPAX.csv")

    # filter out "total" numbers
    int_passengers = int_passengers[int_passengers["month"] != "Total"]

    # Add start/end date cols
    int_passengers = _start_and_end_date_cols_for_monthly_data(int_passengers)

    # Rename passengers col
    int_passengers = int_passengers.rename(
        columns={"Number of international passengers": "passengers"},
    )

    # Drop null passenger records and convert to int
    int_passengers = int_passengers[int_passengers["passengers"] != "-"]
    int_passengers["passengers"] = int_passengers["passengers"].astype(int)

    # Create mapping between places and int passengers
    int_airports = set(int_passengers["airport"])
    locality_map = {}
    for int_airport in int_airports:
        matches = places[places["label"].str.lower() == int_airport.lower()]
        assert len(matches) == 1
        locality_map[int_airport] = int(matches.id.values[0])

    int_passengers["place_id"] = int_passengers["airport"].map(locality_map)

    return int_passengers


def prepare_cruise_passengers(*, input_dir: str, places):
    from pathlib import Path

    import geopandas as gpd

    cruise_passengers = gpd.read_file(Path(input_dir) / "TUXKRH.csv")
    # filter out "total" numbers
    cruise_passengers = cruise_passengers[cruise_passengers["month"] != "Total"]

    # Add start/end date cols
    cruise_passengers = _start_and_end_date_cols_for_monthly_data(cruise_passengers)

    # Rename passengers col
    cruise_passengers = cruise_passengers.rename(
        columns={"Number of cruise passengers for each harbour": "passengers"},
    )

    # Drop null passenger records and convert to int
    cruise_passengers = cruise_passengers[cruise_passengers["passengers"] != "-"]
    cruise_passengers["passengers"] = cruise_passengers["passengers"].astype(int)

    # Create mapping between places and cruise passengers
    int_airports = set(cruise_passengers["port"])
    locality_map = {}
    for int_airport in int_airports:
        matches = places[(places["label"].str.lower() == int_airport.lower())]
        if len(matches) > 1:
            # Duplicates for Aappilattoq, Qeqertarsuaq, Tasiusaq can be filtered
            # out by removing those with a population of 0 - these were
            # abandoned.
            matches = matches[matches["Indbyggertal_2016"] > 0]
            assert len(matches) == 1
        locality_map[int_airport] = int(matches.id.values[0])

    cruise_passengers["place_id"] = cruise_passengers["port"].map(locality_map)

    return cruise_passengers


def prepare_fishing_vessels(*, input_dir: str, places):
    import datetime as dt
    from pathlib import Path

    import geopandas as gpd

    fishing_vessels = gpd.read_file(Path(input_dir) / "FIXFLEET.csv")

    # Filter out null records ("-")
    fishing_vessels = fishing_vessels[fishing_vessels["Number of vessels"] != "-"]

    # rename columns
    fishing_vessels = fishing_vessels.rename(
        columns={
            "Number of vessels": "number_of_vessels",
            "Vessel": "vessel_type",
        }
    )

    # Cast `number_of_vessels` to int
    fishing_vessels["number_of_vessels"] = fishing_vessels["number_of_vessels"].astype(
        int
    )

    # Create start/end date fields
    fishing_vessels["start_date"] = fishing_vessels["Time"].apply(
        lambda year_str: dt.date(int(year_str) - 1, 1, 1)
    )
    fishing_vessels["end_date"] = fishing_vessels["Time"].apply(
        lambda year_str: dt.date(int(year_str) - 1, 12, 31)
    )
    fishing_vessels = fishing_vessels.drop(columns=["Time"])

    # Map fishing vessel districts to towns in places database.
    districts = set(fishing_vessels["District"])
    district_place_mapping = {}
    for district in districts:
        # Slight spelling difference (one vs two `a`) in this district name vs
        # in places db.
        if district == "Kangatsiaq":
            district_matcher = "Kangaatsiaq"
        elif district == "Ittoqqormiit":
            district_matcher = "Ittoqqortoormiit"
        else:
            district_matcher = district

        matches = places[
            (places["label"].str.lower() == district_matcher.lower())
            # Filter for towns, which are the seat of each district and should match
            # the District name given in the fishing vessels data.
            & (places["category"] == "town")
        ]

        district_place_mapping[district] = int(matches["id"].values[0])

    fishing_vessels["place_id"] = fishing_vessels["District"].map(
        district_place_mapping
    )

    return fishing_vessels


def prepare_total_fish_shellfish_landings(*, input_dir: str, places):
    from pathlib import Path

    import geopandas as gpd

    fs_landings = gpd.read_file(Path(input_dir) / "FIX012.csv")

    # Add start/end date cols
    fs_landings = _start_and_end_date_cols_for_monthly_data(fs_landings)

    # Rename count col
    fs_landings = fs_landings.rename(
        columns={
            "Total landings of fish and shellfish": "landings_fish_and_shellfish_tonnes",
        }
    )
    # Ensure count is cast as int
    fs_landings["landings_fish_and_shellfish_tonnes"] = fs_landings[
        "landings_fish_and_shellfish_tonnes"
    ].astype(int)

    # Drop unnecessary enhed (units) col
    fs_landings = fs_landings.drop(columns=["enhed"])

    # Setup place mapping
    districts = set(fs_landings["district"])
    district_place_mapping = {}
    for district in districts:
        matches = places[
            (places["label"].str.lower() == district.lower())
            # Filter for towns, which are the seat of each district and should match
            # the District name given in the fishing vessels data.
            & (places["category"] == "town")
        ]
        assert len(matches) == 1
        district_place_mapping[district] = int(matches.id.values[0])

    fs_landings["place_id"] = fs_landings["district"].map(district_place_mapping)

    return fs_landings


def process_populated_places(*, input_dir: str, output_dir: str):
    """Combine populated places data with statistics from statbank.

    This function combines towns and settlements layers from NunaGIS into one
    geopackage and adds ancillary tables to the geopackage.

    * `pop`: population statistics
    * `international_passengers`: number of international passengers
    * `cruise_passengers`: Number of cruise passengers for each harbour
    """
    import sqlite3
    from pathlib import Path

    places = prepare_places(input_dir=input_dir)

    pop = prepare_pop_table(input_dir=input_dir, places=places)

    int_passengers = prepare_international_passengers(
        input_dir=input_dir, places=places
    )

    cruise_passengers = prepare_cruise_passengers(input_dir=input_dir, places=places)

    fishing_vessels = prepare_fishing_vessels(input_dir=input_dir, places=places)

    fs_landings = prepare_total_fish_shellfish_landings(
        input_dir=input_dir, places=places
    )

    # postprocess places to remove some columns we no longer need
    # ("Indbyggertal_2016" - the population in 2016 - is used by
    # `prepare_cruise_passengers`).
    places = places.drop(columns=["Grundkort", "Indbyggertal_2016"])

    # Write places as a gpkg
    output_dir_path = Path(output_dir)
    output_fp = output_dir_path / "places.gpkg"
    places.to_file(output_fp, driver="gpkg")

    # Update the gpkg with ancillary tables
    with sqlite3.connect(output_fp) as conn:
        pop.to_sql(
            "pop",
            conn,
        )

        int_passengers.to_sql(
            "international_passengers",
            conn,
        )

        cruise_passengers.to_sql(
            "cruise_passengers",
            conn,
        )

        fishing_vessels.to_sql(
            "fishing_vessels",
            conn,
        )

        fs_landings.to_sql(
            "total_fish_shellfish_landings",
            conn,
        )

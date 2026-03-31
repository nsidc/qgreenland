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


def prepare_international_passengers(*, input_dir: str, places):
    """Prepare data for the 'international_passengers' table."""
    import calendar
    import datetime as dt
    from pathlib import Path

    import geopandas as gpd

    int_passengers = gpd.read_file(Path(input_dir) / "TUXUPAX.csv")

    # filter out "total" numbers
    int_passengers = int_passengers[int_passengers["month"] != "Total"]

    # Create start and end date fields. "time" is the year as a str. "month" is
    # the given name (e.g., "January").
    int_passengers["start_date"] = int_passengers.apply(
        lambda row: dt.date(
            int(row["time"]), list(calendar.month_name).index(row["month"]), 1
        ),
        axis=1,
    )
    int_passengers["end_date"] = int_passengers.apply(
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
    int_passengers = int_passengers.drop(columns=["time", "month"])

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


def process_populated_places(*, input_dir: str, output_dir: str):
    """Combine populated places data with statistics from statbank.

    This function combines towns and settlements layers from NunaGIS into one
    geopackage and adds ancillary tables to the geopackage.

    * `pop`: population statistics
    * `international_passengers`: number of international passengers
    """
    import sqlite3
    from pathlib import Path

    places = prepare_places(input_dir=input_dir)

    pop = prepare_pop_table(input_dir=input_dir, places=places)

    int_passengers = prepare_international_passengers(
        input_dir=input_dir, places=places
    )

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

# ruff: noqa: C901


def process_populated_places(*, input_dir: str, output_dir: str):
    """Combine populated places data with population statistics.

    This function combines towns and settlements layers from NunaGIS into one
    geopackage and adds a "pop" table to the geopackage with population
    statistics from statistics Greenland.
    """
    import datetime as dt
    import re
    import sqlite3
    from pathlib import Path

    import geopandas as gpd
    import pandas as pd

    input_dir_path = Path(input_dir)
    output_dir_path = Path(output_dir)

    # Read data
    pop = gpd.read_file(input_dir_path / "BEXSTD.csv")
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

    pop_locality_map = {}
    # pop_locality_re = re.compile(r"(?P<locality>\w+) \((?P<type>\w+)( in (?P<municipality>\w+))?\)")
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

    # create start/end date columns for use with QGIS temporal controller.
    pop["start_date"] = pop["time"].apply(
        lambda year_str: dt.date(int(year_str) - 1, 1, 1)
    )
    pop["end_date"] = pop["time"].apply(
        lambda year_str: dt.date(int(year_str) - 1, 12, 31)
    )
    pop = pop.drop(columns=["time"])

    # Ensure places geometries are in the QGreenland EPSG
    places.to_crs("EPSG:3413")

    # Write places as a gpkg
    output_fp = output_dir_path / "places.gpkg"
    places.to_file(output_fp, driver="gpkg")

    # Update the gpkg with the pop table.
    with sqlite3.connect(output_fp) as conn:
        pop.to_sql(
            "pop",
            conn,
        )

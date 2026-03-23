def init_process(*, input_dir: str, output_dir: str):
    from pathlib import Path

    import geopandas as gpd
    import pandas as pd

    input_dir_path = Path(input_dir)
    output_dir_path = Path(output_dir)

    # Read data
    gpd.read_file(input_dir_path / "BEXSTD.csv")
    municipalities = gpd.read_file(input_dir_path / "fetched.geojson")
    settlements = gpd.read_file(input_dir_path / "settlements.geojson")
    towns = gpd.read_file(input_dir_path / "towns.geojson")

    # Combine sttlements and towns
    places = pd.concat([settlements, towns])
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

    places.to_crs("EPSG:3413")
    places.to_file(output_dir_path / "places.gpkg", driver="gpkg")

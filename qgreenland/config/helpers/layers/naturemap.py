layers_cfg = {
    "barnacle_goose_colony": {
        "title": "Barnacle goose colonies",
        "description": (
            """Shows the position of breeding colonies for barnacle goose from
               2000. Note that unrecorded important goose areas might exist,
               particularly in remote areas."""
        ),
        # Convert from polygon to point. The layer natively uses polygons to
        # represent points, but these are not easily scalable for visualization
        # purposes.
        "ogr2ogr_args": (
            "-sql",
            '"SELECT ST_CENTROID(SHAPE) as geom, * FROM Barnacle_goose_colony"',
            "-nlt",
            "POINT",
            "-nln",
            "barnacle_goose_colony",
        ),
        "style": "barnacle_goose_colonies",
    },
    "goose_moulting_and_breeding_areas": {
        "title": "Goose moulting and breeding areas",
        "description": ("""Polygons representing goose moulting and breeding areas."""),
        "ogr2ogr_args": (),
        "style": "protected_area_polygon",
    },
    "seabird_colony_non_disturbance_zone_200m": {
        "title": "Seabird colony non-disturbance zone 200m",
        "description": (
            """Polygons representing 200-meter non-disturbance zones for seabird colonies."""
        ),
        "ogr2ogr_args": (),
        "style": "protected_area_polygon",
    },
    "seabird_colony_non_disturbance_zone_1000m": {
        "title": "Seabird colony non-disturbance zone 1000m",
        "description": (
            """Polygons representing 1000-meter non-disturbance zones for seabird colonies."""
        ),
        "ogr2ogr_args": (),
        "style": "protected_area_polygon",
    },
    "seabird_colony_no_drone_zone_100m": {
        "title": "Seabird colony no-drone zone 100m",
        "description": (
            """Polygons representing 100-meter no-drone zones for seabird colonies."""
        ),
        "ogr2ogr_args": (),
        "style": "protected_area_polygon",
    },
    "seabird_colony_no_fly_zone_500m": {
        "title": "Seabird colony no-fly zone 500m",
        "description": (
            """Polygons representing 500-meter no-fly zones for seabird colonies."""
        ),
        "ogr2ogr_args": (),
        "style": "protected_area_polygon",
    },
    "seabird_colony_no_fly_zone_3000m": {
        "title": "Seabird colony no-fly zone 3000m",
        "description": (
            """Polygons representing areas where 3000-meter no-fly zones for seabird colonies."""
        ),
        "ogr2ogr_args": (),
        "style": "protected_area_polygon",
    },
}

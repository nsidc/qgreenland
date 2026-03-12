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
}

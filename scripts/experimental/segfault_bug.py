"""Reproduce a segfault on creating a QGIS Layer object.

Creating an SSCCE for this has been elusive. Check out
https://github.com/nsidc/sscce-qgis-conda-segfault for the latest progress.
TODO: Open an issue against conda-forge/qgis-feedstock (?) with SSCCE.
"""
import os
import subprocess

import qgis.core as qgc


def _get_prefix_path():
    qgis_path = (
        subprocess.run(
            ["which", "qgis"],
            stdout=subprocess.PIPE,
        )
        .stdout.decode("utf-8")
        .strip("\n")
    )

    qgis_prefix_path = os.path.abspath(os.path.join(qgis_path, "..", ".."))

    return qgis_prefix_path


def _init_qgis():
    qgs = qgc.QgsApplication([], False)
    qgs.initQgis()
    qgc.QgsApplication.setPrefixPath(_get_prefix_path(), True)


def trigger_with_vector():
    vector_path = "/tmp/populated_places.gpkg"
    result = qgc.QgsVectorLayer(
        vector_path,
        "vectorlayer",
        "ogr",
    )

    return result


def trigger_with_raster():
    raster_path = "/tmp/overviews.tif"
    result = qgc.QgsRasterLayer(
        raster_path,
        "overviews",
        "gdal",
    )

    return result


if __name__ == "__main__":
    _init_qgis()

    raster_result = trigger_with_raster()
    vector_result = trigger_with_vector()

    print(raster_result)
    print(vector_result)

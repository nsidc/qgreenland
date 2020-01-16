import glob
import os
import shutil
import tempfile
import zipfile

from shapely.geometry import Polygon
import geopandas
import requests
import yaml


CONFIG_FILE = 'layers.yml'
THIS_DIR = os.path.dirname(os.path.realpath(__file__))
LAYER_BASE_DIR = os.path.abspath(os.path.join(THIS_DIR, '../qgis-data/qgreenland/'))
REQUEST_TIMEOUT = 3


def read_config(config_file):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)


def get_layer_dir(layer_config):
    # NOTE: a single layer may have many files associated with it. Put it in its own dir.
    return os.path.join(LAYER_BASE_DIR, layer_config['layer_group'], layer_config['short_name'])


def reproject_shapefile(shp_dir, layer_config):
    shp_file = glob.glob(os.path.join(shp_dir, '*.shp'))
    if len(shp_file) != 1:
        raise RuntimeError('Unexpected number of .shp files in {shp_dir}')
    shp_file = shp_file[0]

    gdf = geopandas.read_file(shp_file)
    gdf = gdf.to_crs(epsg=3411)

    out_subdir = os.path.join(shp_dir, 'reprojected')
    os.mkdir(out_subdir)

    reprojected_shpfile = os.path.join(out_subdir, f"{layer_config['short_name']}.shp")
    gdf.to_file(reprojected_shpfile, driver='ESRI Shapefile')

    return out_subdir


def unzip(zipped_file):
    with zipfile.ZipFile(zipped_file) as zfile:
        zfile.extractall(path=os.path.dirname(zipped_file))


def subset(input_gdf):
    # l, d, r, u
    bounds = {'xmin': -3850000.000, 'ymin': -5350000.0,
              'xmax': 3750000.0, 'ymax': 5850000.000}

    points = [
        (bounds['xmin'], bounds['ymax']),
        (bounds['xmax'], bounds['ymax']),
        (bounds['xmax'], bounds['ymin']),
        (bounds['xmin'], bounds['ymin']),
        (bounds['xmin'], bounds['ymax']),
    ]

    gs = geopandas.GeoSeries([Polygon(points)])

    geopandas.overlay(input_gdf, gs, how='intersection')


def get_layer_data(layer_config):
    os.makedirs(layer_dir, exist_ok=True)
    response = requests.get(layer_config['source']['url'], timeout=REQUEST_TIMEOUT)

    with tempfile.TemporaryDirectory() as tdir:
        # TODO support other file formats other than zip.
        temp_file = os.path.join(tdir, 'data.zip')
        with open(temp_file, 'wb') as f:
            f.write(response.content)

            unzip(temp_file)
            os.remove(temp_file)

            reprojected_dir = reproject_shapefile(tdir, layer_config)

            layer_group_dir = os.path.join(LAYER_BASE_DIR, layer_config['layer_group'])
            os.makedirs(layer_group_dir, exist_ok=True)

            # Remove the output dir if it already exists (overwrite).
            output_dir = os.path.join(layer_group_dir, layer_config['short_name'])
            if os.path.isdir(output_dir):
                shutil.rmtree(output_dir)

            shutil.move(reprojected_dir, output_dir)


if __name__ == '__main__':
    if not os.path.isdir(LAYER_BASE_DIR):
        os.mkdir(LAYER_BASE_DIR)

    config = read_config(CONFIG_FILE)

    for key, layer in config.items():
        layer_dir = get_layer_dir(layer)
        get_layer_data(layer)

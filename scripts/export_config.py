"""Exports layer configuration as a CSV file."""

# Hack to import from qgreenland
import os, sys
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)
sys.path.insert(0, PARENT_DIR)

import csv

from qgreenland.constants import CONFIG

if __name__ == '__main__':
    report = [{
        'Group': layer['group_path'].split('/', 1)[0], 
        'Subgroup': (layer['group_path'].split('/', 1)[1]
                     if '/' in layer['group_path'] else ''),
        'Layer Title': layer['title'], 
        'Layer Description': layer.get('description', ''),
        'Vector or Raster': layer['data_type'],
        'Data Source Title': layer['dataset']['metadata']['title'],
        'Data Source Abstract': layer['dataset']['metadata']['abstract'],
        'Data Source Citation': layer['dataset']['metadata']['citation']['text'],
        'Data Source Citation URL': layer['dataset']['metadata']['citation']['url'],
    } for _, layer in CONFIG['layers'].items()]

    with open('layers.csv', 'w') as ofile:
        dict_writer = csv.DictWriter(ofile, report[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(report)
        print(f'Exported: {os.path.abspath(ofile.name)}')

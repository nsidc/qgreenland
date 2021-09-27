"""
Script to assist cleaning up old datasets from the input cache.

Dumb hack for now. This should run similarly to the `cleanup` CLI.  Attempt to
do so fails because of `qgis` import order issue (see HACK in config.py).

Since this doesn't currently run in the container, it writes out a series of
`sudo rm -rf` commands that you need to maunally run.
"""
import os

from qgreenland.util.config.config import CONFIG

INPUT_CACHE_DIR = '/share/appdata/qgreenland-input-cache/'
DATASETS_CONFIG = 'qgreenland/config/datasets.yml'


def _get_dataset_cache_ids():
    dataset_configs = [
        dataset_config
        for dataset_config in CONFIG['datasets']
        if dataset_config['access_method'] != 'gdal_remote'
    ]

    cache_ids = []
    for dataset_config in dataset_configs:
        for source in dataset_config['sources']:
            cache_ids.append(f"{dataset_config['id']}.{source['id']}")

    return cache_ids


if __name__ == '__main__':
    DRY_RUN = False

    cache_ids_from_config = _get_dataset_cache_ids()
    existing_cache_ids = [
        item
        for item in os.listdir(INPUT_CACHE_DIR)
        if os.path.isdir(os.path.join(INPUT_CACHE_DIR, item))
    ]

    rm_commands = []
    for existing_cache_id in existing_cache_ids:
        if existing_cache_id not in cache_ids_from_config:
            path_to_remove = os.path.join(INPUT_CACHE_DIR, existing_cache_id)
            if DRY_RUN:
                print(f'Would remvoe {path_to_remove}')
            else:
                response = None
                while response not in ('yes', 'no'):
                    print("'yes' | 'no' inputs accepted")
                    response = input(f'Remove {path_to_remove}?\n')

                if response == 'yes':
                    rm_commands.append(f'sudo rm -rf {path_to_remove}')

                    # print(f'Removing {path_to_remove}')
                    # shutil.rmtree(path_to_remove)

    with open('DATASET_CACHE_CLEANUP_COMMANDS.txt', 'w') as f:
        for rm_command in rm_commands:
            f.write(rm_command + '\n')

    print('Wrote out DATASET_CACHE_CLEANUP_COMMANDS.txt')

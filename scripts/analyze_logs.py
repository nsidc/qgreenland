#!/usr/bin/env python

import os
import re
import sys
from datetime import datetime
from pprint import pprint

from humanize import naturalsize

try:
    REPO_ROOT = os.path.abspath(
        os.path.join(sys.path[0], os.pardir)
    )
except Exception as e:
    raise RuntimeError(f'Failed to find script path: {e}')


def logs_file_path(cmdl_args):
    """Return the logs file path.

    If the user passed a path as positional argument, use that. Otherwise, if
    the NFS location is available, use it. Otherwise, use the local location.
    """
    EXPECTED_FN = 'zip_access.log'
    LOCAL_LOGS_DIR = os.path.join(REPO_ROOT, 'logs')
    LOCAL_LOGS_FILE = os.path.join(LOCAL_LOGS_DIR, EXPECTED_FN)
    NFS_LOGS_FILE = os.path.join('/share/logs/qgreenland', EXPECTED_FN)

    if os.path.isfile(LOCAL_LOGS_FILE):
        LOGS_FILE = LOCAL_LOGS_FILE

    if os.path.isfile(NFS_LOGS_FILE):
        LOGS_FILE = NFS_LOGS_FILE

    if len(cmdl_args) > 1:
        LOGS_FILE = cmdl_args[1]

    if not os.path.isfile(LOGS_FILE):
        print(f"Log file '{LOGS_FILE}' does not exist.")
        sys.exit(1)

    return LOGS_FILE


def unusable_filename(fn):
    """TODO: Switch to logging.debug to hide spam."""
    print(f'WARNING: Unusable filename: {fn}')


class Parser:
    """Read log lines and build up stats for reporting.

    Example:

        {'v0.1.2': { 'downloads': 0,
                      'bytes': 0 }
         'v0.23.0dev': { 'downloads': 131,
                         'bytes': 31549151 }
        }
    """
    def __init__(self):
        self.state = {}

    def parse(self, line):
        line = line.strip('\n')
        ip, timestamp, status_code, num_bytes, filepath = line.split('|')
        timestamp = datetime.fromisoformat(timestamp)
        status_code = int(status_code)
        num_bytes = int(num_bytes)
        filename = os.path.basename(filepath)

        if status_code != 200:
            return

        if 'QGreenland' not in filename:
            unusable_filename(filename)
            return

        matcher = re.compile('QGreenland_(v.+).zip')
        try:
            qgr_version = matcher.match(filename).groups()[0]
        except AttributeError as e:
            unusable_filename(filename)
            return

        if qgr_version in self.state:
            self.state[qgr_version]['downloads'] += 1
            self.state[qgr_version]['bytes'] += num_bytes
        else:
            self.state[qgr_version] = {'downloads': 1,
                                       'bytes': num_bytes}


    def report(self):
        """Print a human-readable report.

        TODO: Consider printing in a nicer format than pprint(dict)
        """

        for key, val in self.state.items():
            print()
            print(f'== {key} ==')
            print(f"  Download count: {val['downloads']}")
            print(f"  Total size: {naturalsize(val['bytes'])}")


if __name__ == '__main__':
    logs_fp = logs_file_path(sys.argv)
    parser = Parser()

    with open(logs_fp, 'r') as logs_file:
        print(f'Parsing log file: {logs_fp}...')
        lines = logs_file.readlines()

        if len(lines) == 0:
            print('Log file is empty.')
            sys.exit(0)

        for line in lines:
            parser.parse(line)

    parser.report()

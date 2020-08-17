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

LOGS_DIR = os.path.join(REPO_ROOT, 'logs')
LOGS_FILE = os.path.join(LOGS_DIR, 'zip_access.log')


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
    parser = Parser()

    with open(LOGS_FILE, 'r') as logs_file:
        print(f'Parsing log file: {LOGS_FILE}...')
        lines = logs_file.readlines()

        if len(lines) == 0:
            print('Log file is empty.')
            sys.exit(0)

        for line in lines:
            parser.parse(line)

    parser.report()

#!/usr/bin/env python

import os
import re
import sys
from datetime import datetime

from humanize import naturalsize

try:
    REPO_ROOT = os.path.abspath(
        os.path.join(sys.path[0], os.pardir),
    )
except Exception as e:
    raise RuntimeError(f'Failed to find script path: {e}')


def logs_file_path(cmdl_args):
    """Return the logs file path.

    If the user passed a path as positional argument, use that. Otherwise, if
    the NFS location is available, use it. Otherwise, use the local location.
    """
    expected_fn = 'zip_access.log'
    local_logs_dir = os.path.join(REPO_ROOT, 'logs')
    local_logs_file = os.path.join(local_logs_dir, expected_fn)
    nfs_logs_file = os.path.join('/share/logs/qgreenland', expected_fn)

    if os.path.isfile(local_logs_file):
        logs_file = local_logs_file

    if os.path.isfile(nfs_logs_file):
        logs_file = nfs_logs_file

    if len(cmdl_args) > 1:
        logs_file = cmdl_args[1]

    if not os.path.isfile(logs_file):
        print(f"Log file '{logs_file}' does not exist.")
        sys.exit(1)

    return logs_file


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
        except AttributeError:
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

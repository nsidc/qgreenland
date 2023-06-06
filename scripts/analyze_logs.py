#!/usr/bin/env python

import os
import re
import sys
from datetime import datetime
from functools import reduce

from humanize import naturalsize

try:
    REPO_ROOT = os.path.abspath(
        os.path.join(sys.path[0], os.pardir),
    )
except Exception as e:
    raise RuntimeError(f"Failed to find script path: {e}")


def logs_file_path(cmdl_args):
    """Return the logs file path.

    If the user passed a path as positional argument, use that. Otherwise, if
    the NFS location is available, use it. Otherwise, use the local location.
    """
    expected_fn = "zip_access.log"
    local_logs_dir = os.path.join(REPO_ROOT, "logs")
    local_logs_file = os.path.join(local_logs_dir, expected_fn)
    nfs_logs_file = os.path.join("/share/logs/qgreenland", expected_fn)

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
    print(f"WARNING: Unusable filename: {fn}")


class Parser:
    """Read log lines and build up stats for reporting.

    Example:
    -------
        {
            'v0.1.2': { 'downloads': 0, 'bytes': 0}
            'v0.23.0dev': { 'downloads': 131, 'bytes': 31549151}
        }
    """

    def __init__(self):
        self.state = {}

    def parse(self, line):
        line = line.strip("\n")
        ip, timestamp, status_code, num_bytes, filepath = line.split("|")
        timestamp = datetime.fromisoformat(timestamp)
        status_code = int(status_code)
        num_bytes = int(num_bytes)
        filename = os.path.basename(filepath)

        if status_code != 200:
            return

        if "QGreenland" not in filename:
            unusable_filename(filename)
            return

        matcher = re.compile("QGreenland_(v.+).zip")
        if match := matcher.match(filename):
            qgr_version = match.groups()[0]
        else:
            unusable_filename(filename)
            return

        if qgr_version in self.state:
            self.state[qgr_version]["downloads"] += 1
            self.state[qgr_version]["bytes"] += num_bytes
        else:
            self.state[qgr_version] = {"downloads": 1, "bytes": num_bytes}

    def major_versions(self):
        """Detect unique major versions (e.g. v0, v1, v2) present in log data."""
        major_versions = [k[0:2] for k in self.state.keys()]
        problems = [
            v for v in major_versions if not v.startswith("v") or not v[1].isnumeric()
        ]
        if problems:
            raise RuntimeError(f"Found problematic major versions: {problems}")

        return set(major_versions)

    def aggregate_major_version(self, major_version: str):
        """Sum all values for given major version."""
        filtered_entries = {
            k: v for k, v in self.state.items() if k.startswith(major_version)
        }

        return {
            "release_count": len(filtered_entries),
            "downloads": reduce(
                lambda total, current: total + current["downloads"],
                filtered_entries.values(),
                0,
            ),
            "bytes": reduce(
                lambda total, current: total + current["bytes"],
                filtered_entries.values(),
                0,
            ),
        }

    def report(self):
        """Print a human-readable report."""
        for key, val in self.state.items():
            print()
            print(f"== {key} ==")
            print(f"  Download count: {val['downloads']}")
            print(f"  Total size: {naturalsize(val['bytes'])}")

        print()
        for major_version in self.major_versions():
            agg = self.aggregate_major_version(major_version)
            print()
            print(f"=== Major version {major_version} total ===")
            print(f"  Number of releases: {agg['release_count']}")
            print(f"  Download count: {agg['downloads']}")
            print(f"  Total size: {naturalsize(agg['bytes'])}")


if __name__ == "__main__":
    logs_fp = logs_file_path(sys.argv)
    parser = Parser()

    with open(logs_fp) as logs_file:
        print(f"Parsing log file: {logs_fp}...")
        lines = logs_file.readlines()

        if len(lines) == 0:
            print("Log file is empty.")
            sys.exit(0)

        for line in lines:
            parser.parse(line)

    parser.report()

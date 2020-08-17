import os
import sys
from datetime import datetime
from pprint import pprint

try:
    REPO_ROOT = os.path.abspath(
        os.path.join(sys.path[0], os.pardir)
    )
except Exception as e:
    raise RuntimeError(f'Failed to find script path: {e}')

LOGS_DIR = os.path.join(REPO_ROOT, 'logs')
LOGS_FILE = os.path.join(LOGS_DIR, 'zip_access.log')


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

        qgr_version = filename.rstrip('.zip').lstrip('QGreenland_')
        if qgr_version in self.state:
            self.state[qgr_version]['downloads'] += 1
            self.state[qgr_version]['bytes'] += num_bytes
        else:
            self.state[qgr_version] = {'downloads': 1,
                                       'bytes': num_bytes}


    def report(self):
        """Print a human-readable report.

        TODO: Print e.g. '452MB' instead of '452235211' for bytes.
        TODO: Consider printing in a nicer format than pprint(dict)
        """
        pprint(self.state)


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

import functools
import os
import re
import subprocess

import qgreenland.exceptions as exc
from qgreenland import __version__

VERSION_REGEX = re.compile(r'^v\d+\.\d+\.\d+(?P<modifier>.*)$')


def _version_tags(tags):
    """Retun any members of tags that start with vX.Y.Z."""
    return [t for t in tags if VERSION_REGEX.match(t)]


# TODO: In Python 3.9, @functools.cache() is an alias for this.
@functools.lru_cache(maxsize=None)
def get_version():
    package_version = __version__
    tags = subprocess.run(
        ['/usr/bin/git', 'tag', '--points-at', 'HEAD'],
        cwd=os.path.dirname(os.path.realpath(__file__)),
        stdout=subprocess.PIPE,
        check=True,
    ).stdout.decode('utf-8').strip('\n').split('\n')
    commit_id = subprocess.run(
        ['/usr/bin/git', 'rev-parse', '--short', 'HEAD'],
        cwd=os.path.dirname(os.path.realpath(__file__)),
        stdout=subprocess.PIPE,
        check=True,
    ).stdout.decode('utf-8').strip('\n')

    version_tags = _version_tags(tags)
    if len(version_tags) > 1:
        raise exc.QgrVersionError(
            f'Can not determine desired version from tags: {tags}'
        )

    if len(version_tags) == 1:
        version = version_tags[0]
    else:
        # If there is no version tag, build a unique version string
        version = f'{package_version}-{commit_id}'

    return version


def version_is_release(version_string):
    """Check if a version string is a release version `vX.Y.Z`.

    Exclude any "named" versions like `vX.Y.Z-rc1`, `vX.Y.Zfoobarbaz`.
    """
    match = VERSION_REGEX.match(version_string)

    if match and match.groupdict()['modifier'] == '':
        return True
    else:
        return False

import functools
import os
import re
import subprocess

import qgreenland.exceptions as exc
from qgreenland import __version__

VERSION_REGEX = re.compile(r'^v\d+\.\d+\.\d+(?P<modifier>.*)$')


def _select_version_tags(tags):
    """Return any members of tags that start with `vX.Y.Z`.

    Includes pre-release tags, e.g. `vX.Y.Zfoobar`.
    """
    return [t for t in tags if VERSION_REGEX.match(t)]


@functools.cache
def get_build_version():
    """Generate a useful version string for a QGreenland build.

    It's not always enough to use bumpversion to manage versions. If we want to
    release a dev build or a pre-release for human validation, it needs a
    fully-unique name so we know exactly what the user tested.

    * For release builds (tagged with 'vX.Y.Z' release version), just use the tag
      as the build version; e.g. 'v1.2.3'.
    * For pre-release builds (tagged 'vX.Y.Z' with a 'modifier' suffix), again
      use the tag as the build version; e.g. 'v1.2.3-rc1'.
    * For dev builds, use the current version determined by bumpversion, appended
      with the current commit ID; e.g. 'v1.2.3-aef10ea'.
    """
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

    version_tags = _select_version_tags(tags)
    if len(version_tags) > 1:
        raise exc.QgrVersionError(
            f'Can not determine desired version from tags: {tags}',
        )

    if len(version_tags) == 1:
        version = version_tags[0]
    else:
        # If there is no version tag, build a unique version string
        version = f'{package_version}-{commit_id}'

    return version


def version_is_full_release(version_string):
    """Check if a version string is a release version `vX.Y.Z`.

    Exclude any pre-release versions like `vX.Y.Z-rc1`, `vX.Y.Zfoobarbaz`.
    """
    match = VERSION_REGEX.match(version_string)

    if match and match.groupdict()['modifier'] == '':
        return True
    else:
        return False

import sys
from itertools import groupby
from pprint import pprint

import anytree
from invoke import call, task

from .config import diff, validate
from .util import PROJECT_DIR, print_and_run

sys.path.append(str(PROJECT_DIR))

from qgreenland.constants.paths import (
    LAYERS_CFG_DIR,
    PACKAGE_DIR,
    PROJECT_DIR,
    SCRIPTS_DIR,
)
from qgreenland.test.constants import TEST_DATA_DIR, TEST_DIR


@task
def shellcheck(ctx):
    # It's unclear why, but the return code seems to be getting swallowed.
    print_and_run(
        f"cd {PROJECT_DIR} &&"
        f' for file in $(find {SCRIPTS_DIR} -type f -name "*.sh"); do'
        "    shellcheck $file;"
        "  done;",
        pty=True,
    )


@task(
    pre=[shellcheck],
    aliases=["flake8"],
)
def lint(ctx):
    """Run flake8 and vulture linting."""
    print_and_run(
        f"cd {PROJECT_DIR} &&" f" flake8 {PACKAGE_DIR} {SCRIPTS_DIR}",
        pty=True,
    )
    print_and_run(
        f"cd {PROJECT_DIR} &&"
        f" vulture --min-confidence 100 {PACKAGE_DIR} {SCRIPTS_DIR}"
        " vulture_allowlist.py",
        pty=True,
    )
    print("🎉🙈 Linting passed.")


@task(aliases=["mypy"])
def typecheck(ctx, check_config=False):
    """Run mypy static type analysis.

    TODO: If/when the below issues are resolved, remove exclude-pathmasks and
    conditional calls to mypy.

    Skip scanning the layers config. Mypy complains about "duplicate module
    name" for the __settings__.py files in our config. This wouldn't be a
    problem if those files could be in a package with __init__.py, but Python
    itself has a problem with that, as our directories have spaces in their
    names.
        https://github.com/python/mypy/issues/10428
        https://github.com/python/mypy/issues/4008
    """

    config_pathmask = f"{LAYERS_CFG_DIR.relative_to(PROJECT_DIR)}/*"
    # Skip scanning the test data for the same reason; we'll just never scan it.
    test_data_pathmask = f"{TEST_DATA_DIR.relative_to(PROJECT_DIR)}/*"
    # Skip scanning QGIS scripts
    qgis_scripts_dir = SCRIPTS_DIR / "qgis_examples"
    qgis_scripts_pathmask = f"{qgis_scripts_dir.relative_to(PROJECT_DIR)}/*"

    exclude_masks = (
        f"{config_pathmask}" f"|{test_data_pathmask}" f"|{qgis_scripts_pathmask}"
    )

    print_and_run(
        f"cd {PROJECT_DIR} &&"
        f' mypy --exclude "{exclude_masks}"'
        f" --config-file={PROJECT_DIR}/.mypy.ini"
        f" {PACKAGE_DIR} {SCRIPTS_DIR}",
        pty=True,
    )

    # To get around this, we scan the files with non-unique names one-by-one.
    if check_config:
        print(
            "Type-checking layer configuration. WARNING: This requires many"
            "invocations of mypy and may look kind of spammy. SORRY!!!",
        )
        # Split into set of unique and non-unique filenames.
        path_name_key_func = lambda p: p.name
        layer_cfg_files = sorted(
            LAYERS_CFG_DIR.rglob("*.py"),
            key=path_name_key_func,
        )
        layer_cfg_files_by_name = groupby(
            layer_cfg_files,
            key=path_name_key_func,
        )
        unique_layer_cfg_files, conflicting_layer_cfg_files = [], []
        for filename, paths_iter in layer_cfg_files_by_name:
            paths = list(paths_iter)
            if len(paths) > 1:
                conflicting_layer_cfg_files.extend(paths)
            else:
                unique_layer_cfg_files.extend(paths)

        # Scan unique ones all together. This is fine until the number of files
        # exceeds ARG_MAX...
        unique_layer_cfg_files_str = (f'"{str(fp)}"' for fp in unique_layer_cfg_files)
        print_and_run(
            f"cd {PROJECT_DIR} &&"
            # Enable mypy to find modules in the main project that are
            # imported by these scripts
            f" mypy --namespace-packages --explicit-package-bases"
            f" --config-file={PROJECT_DIR}/.mypy.ini"
            f' {" ".join(unique_layer_cfg_files_str)}',
            pty=True,
        )
        # Scan non-unique ones one-by-one.
        for fp in conflicting_layer_cfg_files:
            print_and_run(
                f"cd {PROJECT_DIR} &&"
                # Enable mypy to find modules in the main project that are
                # imported by these scripts
                f" mypy --namespace-packages --explicit-package-bases"
                f' --config-file={PROJECT_DIR}/.mypy.ini "{fp}"',
                pty=True,
            )

    print("🎉🦆 Type checking passed.")


@task
def formatcheck(ctx):
    """Check that the code conforms to formatting standards."""
    print_and_run(f"isort --check-only {PROJECT_DIR}")
    print_and_run(f"black --check {PROJECT_DIR}")

    print("🎉🙈 Format check passed.")


@task(
    pre=[
        lint,
        formatcheck,
        call(typecheck, check_config=True),
        validate,
    ]
)
def static(ctx):
    """Run static analysis."""
    print(f"🎉🌩️  All static analysis passed.")


@task
def unit(ctx, verbose=False):
    verbose_str = "-vv" if verbose else ""
    print_and_run(
        f"cd {PROJECT_DIR} &&"
        f" pytest {verbose_str} -c setup.cfg --cov-config=setup.cfg"
        f" {TEST_DIR}",
        pty=True,
    )
    print("🎉🛠️  Unit tests passed.")


@task(
    pre=[static, unit],
    default=True,
)
def all(ctx):
    """Run all tasks."""
    print("🎉❤️  All tests passed!")


@task(
    pre=[
        static,
        call(unit, verbose=True),
        diff,
    ],
)
def ci(ctx):
    """Run all tasks with increased verbosity for CI."""
    print("🎉❤️  All tests passed!")

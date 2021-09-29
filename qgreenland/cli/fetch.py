import textwrap
from fnmatch import fnmatch
from typing import Any

import click
import luigi
from funcy import lmapcat, select

from qgreenland.util.luigi import fetch_tasks_from_dataset
from qgreenland.util.config.config import CONFIG


@click.command()
@click.option(
    '--dry-run', '-d',
    is_flag=True,
    help='Skip actual fetch, just list out dataset matches.',
)
@click.option(
    '--workers', '-w',
    default=4, show_default=True,
    help='Number of workers to use.',
)
@click.argument(
    'pattern',
)
def fetch(pattern, dry_run, workers) -> None:
    """Fetch assets for datasets matching PATTERN."""
    dataset_matches = select(
        lambda i: fnmatch(i[1].id, pattern),
        CONFIG.datasets,
    ).values()

    print('Fetching all assets for the following datasets:')
    print(textwrap.indent(
        '\n'.join([d.id for d in dataset_matches]),
        '  - ',
    ))
    if dry_run:
        print('DRY RUN enabled. Aborting fetch.')
        return

    fetch_tasks = lmapcat(
        lambda i: fetch_tasks_from_dataset(i),
        dataset_matches,
    )

    result = luigi.build(
        fetch_tasks,
        workers=workers,
        # Unlike CLI, running tasks from Python does not feature an "identical
        # process lock" by default.
        no_lock=False,
        detailed_summary=True,
    )

import click
import luigi

from qgreenland.util.config.config import (
    get_config,
    init_config,
)
from qgreenland.util.luigi.tasks.pipeline import (
    CreateQgisProjectFile,
    IngestAllLayers,
    ZipQGreenland,
)


@click.command()
@click.option(
    '--dry-run', '-d',
    is_flag=True,
    help='Skip actual run, just list out tasks.',
)
@click.option(
    '--fetch-only', '-f',
    help='Fetch the data, but do not process it.',
    is_flag=True,
)
@click.option(
    '--workers', '-w',
    default=1, show_default=True,
    help='Number of workers to use.',
)
@click.option(
    '--include', '-i',
    help='Include layers matching PATTERN',
    metavar='PATTERN',
    required=False,
    multiple=True,
)
@click.option(
    '--exclude', '-e',
    help='Exclude layers matching PATTERN',
    metavar='PATTERN',
    required=False,
    multiple=True,
)
def run(
    include: tuple[str],
    exclude: tuple[str],
    dry_run: bool,
    fetch_only: bool,
    workers: int,
) -> None:
    """Run pipelines for layers matching filters."""
    init_config(
        include_patterns=include,
        exclude_patterns=exclude,
    )
    config = get_config()


    if fetch_only:
        # Don't do anything except fetch the input asset for each layer.
        tasks = [IngestAllLayers(
            fetch_only=fetch_only,
        )]
    elif include or exclude:
        # Don't actually zip, just compile.
        tasks = [CreateQgisProjectFile()]
    else:
        # Do everything!!!
        tasks = [ZipQGreenland()]

    print(f'Running tasks: {str(tasks)}')
    print()

    if include or exclude:
        action = 'Fetching data' if fetch_only else 'Running pipelines'
        print(f'{action} for the following layers:')
        for layer in config.layers.keys():
            print(f'  - {layer}')
        print()

    if dry_run:
        print('DRY RUN enabled. Aborting run.')
        return

    result = luigi.build(
        tasks,
        workers=workers,
        # Unlike CLI, running tasks from Python does not feature an "identical
        # process lock" by default.
        no_lock=False,
        detailed_summary=True,
    )

    if not result.scheduling_succeeded:
        raise SystemExit('Scheduling failed. See log above for details.')

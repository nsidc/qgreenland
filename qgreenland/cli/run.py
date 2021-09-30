import textwrap

import click
import luigi

from qgreenland.util.luigi.tasks.pipeline import (
    CreateQgisProjectFile,
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
@click.argument(
    'pattern', required=False,
)
def run(pattern, dry_run, fetch_only, workers) -> None:
    """Run pipelines for layers matching PATTERN."""
    get_config(pattern=pattern)


    if fetch_only:
        # Don't do anything except fetch the input asset for each layer.
        tasks = [IngestAllLayers(
            pattern=pattern,
            fetch_only=fetch_only,
        )]
    elif pattern:
        # Don't actually zip, just compile.
        tasks = [CreateQgisProjectFile(
            pattern=pattern,
        )]
    else:
        tasks = [ZipQGreenland()]

    # This is not useful output. TODO: List the layers for which we're running
    # tasks, unless it's all of them?
    print('Running the following tasks:')
    print(textwrap.indent(
        '\n'.join(str(t) for t in tasks),
        '  - ',
    ))
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
        raise click.UsageError(
            (
                'Scheduling failed. If you received any error like:\n'
                "  PermissionError: [Errno 13] Permission denied: '/luigi'\n\n"
                '...you probably need to run this command within a container,'
                ' e.g.: `./scripts/container_cli.sh run [OPTIONS]`.'
            ),
        )

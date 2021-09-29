import click
import luigi

from qgreenland.util.luigi.tasks.pipeline import ZipQGreenland


@click.command()
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
def run(fetch_only, workers, pattern) -> None:
    """Run pipelines for layers matching PATTERN."""
    if pattern:
        raise NotImplementedError(f'{pattern=} not implemented.')
    elif fetch_only:
        # TODO!
        # for layer in matches:
        #    fetch_task_from_layer(...)  # ??
        raise NotImplementedError(f'{fetch_only=} not implemented.')
    else:
        tasks = [ZipQGreenland()]

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

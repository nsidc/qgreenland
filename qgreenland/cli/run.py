import click
import luigi


@click.command()
@click.option(
    "--dry-run",
    "-d",
    is_flag=True,
    help="Skip actual run, just list out tasks.",
)
@click.option(
    "--fetch-only",
    "-f",
    help="Fetch the data, but do not process it.",
    is_flag=True,
)
@click.option(
    "--workers",
    "-w",
    default=1,
    show_default=True,
    help="Number of workers to use.",
)
@click.option(
    "--include",
    "-i",
    help="Include layers matching PATTERN.",
    metavar="PATTERN",
    required=False,
    multiple=True,
)
@click.option(
    "--exclude",
    "-e",
    help="Exclude layers matching PATTERN.",
    metavar="PATTERN",
    required=False,
    multiple=True,
)
@click.option(
    "--exclude-manual-assets",
    is_flag=True,
    help='Exclude all "manual access" assets.',
    required=False,
)
@click.option(
    "--force-package-zip",
    "-z",
    is_flag=True,
    help="Zip the package even if `--include` or `--exclude` are true.",
    required=False,
)
@click.option(
    "--force-no-package-zip",
    "-Z",
    is_flag=True,
    help="DO NOT zip the package even if the whole pipeline was run.",
    required=False,
)
def run(
    include: tuple[str, ...],
    exclude: tuple[str, ...],
    exclude_manual_assets: bool,
    force_package_zip,
    force_no_package_zip,
    dry_run: bool,
    fetch_only: bool,
    workers: int,
) -> None:
    """Run pipelines for layers matching filters."""
    # Hack to work around issue with sphinx-click:
    #     https://github.com/click-contrib/sphinx-click/issues/86#issuecomment-991196764
    from qgreenland.util.config.config import get_config, init_config
    from qgreenland.util.luigi.tasks.pipeline import (
        QGreenlandPackages,
        QGreenlandPackagesNoZip,
    )

    if force_package_zip and force_no_package_zip:
        raise RuntimeError("Can not force zip AND no zip.")

    init_config(
        include_patterns=include,
        exclude_patterns=exclude,
        exclude_manual_assets=exclude_manual_assets,
    )
    config = get_config()
    filtered = include or exclude
    skip_zip = force_no_package_zip or (filtered and not force_package_zip)

    if fetch_only:
        # Don't do anything except fetch the input asset for each layer.
        # TODO: How to keep "fetch all" functionality? Bring back LayerPipelines solely
        # for this? Or make the user pass a specific package, or specific a magic word
        # like "__all__"? ¯\_(ツ)_/¯
        # tasks = [LayerPipelines(fetch_only=fetch_only)]
        ...
    elif skip_zip:
        tasks = [QGreenlandPackagesNoZip()]
    else:
        tasks = [QGreenlandPackages()]

    print(f"Running tasks: {str(tasks)}")
    print()

    if include or exclude or exclude_manual_assets or dry_run:
        action = "Fetching data" if fetch_only else "Running pipelines"
        print(f"{action} for the following layers:")
        for layer in config.layers.keys():
            print(f"  - {layer}")
        print()

    if dry_run:
        print("DRY RUN enabled. Aborting run.")
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
        raise SystemExit("Scheduling failed. See log above for details.")

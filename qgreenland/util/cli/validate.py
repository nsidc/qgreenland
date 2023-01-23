import click


# TODO: Rename. This is specific to the cleanup cli.
def validate_ambiguous_command(kwargs):
    """Validate for conflicting options and suggest a fix."""
    msg = (
        "Ambiguous command! You have requested both to delete all"
        " {resource}s _and_ to delete {resource}s"  # noqa: FS003
        " by PATTERN. Please choose only one."
    )

    if kwargs["delete_all_fetch"] and kwargs["delete_fetch_by_pattern"]:
        raise click.UsageError(msg.format(resource="fetch datasets"))

    if kwargs["delete_all_wip_layers"] and kwargs["delete_wip_layers_by_pattern"]:
        raise click.UsageError(msg.format(resource="WIP layers"))

    if (
        kwargs["delete_all_release_layers"]
        and kwargs["delete_release_layers_by_pattern"]
    ):
        raise click.UsageError(msg.format(resource="release layers"))

    if (
        kwargs["delete_all_release_packages"]
        and kwargs["delete_all_dev_release_packages"]
    ):
        raise click.UsageError(msg.format(resource="release packages"))

    return kwargs

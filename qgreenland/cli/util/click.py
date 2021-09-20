BOOLEAN_CHOICE = click.Choice(['True', 'False'], case_sensitive=False)


def _validate_boolean_choice(_ctx, _param, value):
    if value == 'True':
        return True
    if value == 'False':
        return False

    raise click.BadParameter(
        f'Expected "True" or "False"; Received "{value}"',
    )


def _validate_ambiguous_command(kwargs):
    """Validate for conflicting options and suggest a fix."""
    msg = (
        'Ambiguous command! You have requested both to delete all'
        ' {resource}s _and_ to delete {resource}s'  # noqa: FS003
        ' by layer ID. Please choose only one.'
    )
    if kwargs['delete_all_wip'] and kwargs['delete_wips_by_pattern']:
        raise click.UsageError(msg.format(resource='WIP'))

    if kwargs['delete_all_input'] and kwargs['delete_inputs_by_pattern']:
        raise click.UsageError(msg.format(resource='input'))

    return kwargs

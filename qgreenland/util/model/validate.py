import inspect


def clean_string(string: str) -> str:
    """Clean up `string` with `cleandoc`.

    This adjusts indentation and removes leading and trailing newlines, enabling
    cleaner use of triple-quoted strings, just like docstrings.
    """
    return inspect.cleandoc(string)

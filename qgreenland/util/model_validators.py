from typing import Any, Callable

from pydantic import validator


def reusable_validator(
    name: str,
    validation_func: Callable[..., Any],
) -> classmethod:
    """Provide a common way to re-use validator functions."""
    return validator(name, allow_reuse=True)(validation_func)


def validate_paragraph_text(text: str):
    """Validate paragraph text has appropriate content.

    Paragraph text must not be empty, must begin with an upper-case letter, and
    must end with a period.
    """
    if not text:
        raise ValueError("Paragraph text must not be empty.")

    if not text[0].isupper():
        raise ValueError("Paragraph text must begin with an upper-case letter.")

    if not text.endswith("."):
        raise ValueError("Paragraph text must end with a period.")

    return text

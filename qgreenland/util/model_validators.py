from typing import Any, Callable

from pydantic import validator


def reusable_validator(name: str, validation_func: Callable[..., Any]) -> classmethod:
    return validator(name, allow_reuse=True)(validation_func)


def validate_paragraph_text(text: str):
    if not text[0].isupper():
        raise ValueError('Paragraph text must begin with an upper-case letter.')

    if not text.endswith('.'):
        raise ValueError('Paragraph text must end with a period.')

    return text

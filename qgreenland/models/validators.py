import inspect
from typing import Any, Callable

from pydantic import validator


def reusable_validator(name: str, validation_func: Callable[..., Any]) -> classmethod:
    return validator(name, allow_reuse=True)(validation_func)


def validate_paragraph_text(text: str):
    # TODO: make this validator always run after `clean_all_string_fields`?
    if not inspect.cleandoc(text).endswith('.'):
        raise ValueError('Paragraph text must end with a period.')

    return text

from collections import UserString
from pathlib import Path
from typing import Optional

import qgreenland.exceptions as exc


# Make this a dataclass? :shrug:
class EvalPath(object):
    """Path with `eval` method for runtime string interpolation."""

    val: str

    @classmethod
    def __get_validators__(cls):
        # TODO: Validate that a file exists at the path?
        # Or create a subclass of this class with that validator?
        yield cls.validate_arg

    @classmethod
    def validate_arg(cls, value):
        if not isinstance(value, str):
            raise TypeError(f'`str` requried. Got {type(value)}.')
        return cls(value)

    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return f'{self.__class__}({self.val})'

    def __json__(self):
        return str(self)

    def __str__(self):
        return str(self.val)

    def eval(self, **kwargs) -> Path:
        return Path(
            EvalStr(
                str(self),
            ).eval(**kwargs),
        )


class EvalFilePath(EvalPath):
    """An EvalPath that must exist on the filesystem.

    WARNING: This can't be used with runtime-only slugs like {input_dir} and
    {output_dir}. Those are populated by the Luigi context."""

    @classmethod
    def __get_validators__(cls):
        # TODO: Validate that a file exists at the path?
        # Or create a subclass of this class with that validator?
        yield super().__get_validators__()
        yield cls.validate_exists

    def validate_exists(self) -> Path:
        evaluated = self.eval()
        self._validate_is_file(evaluated)
        return value

    def _validate_is_file(self, path: Path) -> None:
        if not path.is_file():
            raise ValueError(
                f'No file found at evaluated path "{path}".'
                ' NOTE: {input_dir} and {output_dir} are not supported by'
                ' `EvalFilePath` fields. Use `EvalStr` instead.'
            )

    def eval(self, **kwargs) -> Path:
        evaluated = super().eval(**kwargs)
        self._validate_is_file(evaluated)
        return evaluated


class EvalStr(UserString):
    """String with `eval` method for runtime string interpolation."""

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if not isinstance(value, str) and not isinstance(value, EvalStr):
            raise TypeError(f'`str` or `EvalStr` requried. Got {type(value)}.')

        return cls(value)

    def __json__(self):
        return str(self)

    def eval(
        self,
        *,
        # Clever.
        input_dir: Optional[str] = '{input_dir}',
        output_dir: Optional[str] = '{output_dir}',
    ) -> str:
        # Circular import if we import this at module level because `_typing`
        # imports `EvalStr` and `constants` imports `_typing`.
        from qgreenland.constants import ANCILLARY_DIR, ASSETS_DIR

        return self.format(
            input_dir=input_dir,
            output_dir=output_dir,
            assets_dir=ASSETS_DIR,
            ancillary_dir=ANCILLARY_DIR,
        )

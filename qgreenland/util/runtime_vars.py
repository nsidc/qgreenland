from collections import UserString
from pathlib import Path
from typing import Optional

import qgreenland.exceptions as exc
from qgreenland.constants.paths import ASSETS_DIR


# TODO: Make this a dataclass? :shrug:
# TODO: Move to _typing module/package?
class EvalPath:
    """Path with `eval` method for runtime string interpolation."""

    val: str

    @classmethod
    def __get_validators__(cls):
        """Pydantic magic method for implicit validation and conversion."""
        yield cls.validate_arg

    @classmethod
    def validate_arg(cls, value):
        if not (isinstance(value, str) or issubclass(type(value), EvalPath)):
            raise TypeError(
                "`str` or `EvalPath` required. Received:" f" `{type(value).__name__}`",
            )
        return cls(value)

    def __init__(self, val):
        self.val = val

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.val}')"

    def __str__(self) -> str:
        return str(self.val)

    def __json__(self) -> str:
        return str(self)

    def eval(self, **kwargs) -> Path:
        return Path(
            EvalStr(
                str(self),
            ).eval(**kwargs),
        )


class EvalFilePath(EvalPath):
    """An EvalPath that must be a real file on the filesystem."""

    @classmethod
    def __get_validators__(cls):
        """Pydantic magic method for implicit validation and conversion."""
        yield from super().__get_validators__()
        yield cls.validate_exists

    @classmethod
    def validate_exists(cls, value) -> Path:
        """Check for file existence.

        WARNING: This can't be used in the config with runtime-only variables
        like {input_dir} and {output_dir}. Those are populated by the Luigi
        context, so a file like that is _not_ expected to exist at
        config-compilation-time.
        """
        evaluated = value.eval()
        cls._validate_is_file(evaluated)
        return value

    def eval(self, **kwargs) -> Path:
        evaluated = super().eval(**kwargs)
        self._validate_is_file(evaluated)
        return evaluated

    @classmethod
    def _validate_is_file(cls, path: Path) -> None:
        if not path.is_file():
            raise exc.QgrInterpolationError(
                f'No file found at evaluated path "{path}".'
                f" NOTE: {{input_dir}} and {{output_dir}} are not supported by"
                " `EvalFilePath` fields. If you want to use these, use"
                " `EvalPath` instead.",
            )


class EvalStr(UserString):
    """String with `eval` method for runtime string interpolation."""

    @classmethod
    def __get_validators__(cls):
        """Pydantic magic method for implicit validation and conversion."""
        yield cls.validate

    @classmethod
    def validate(cls, value):
        # Is it stringifiable?
        try:
            str(value)
        except Exception as e:
            raise type(e)(
                f"Stringifiable type expected. Received: `{type(value).__name__}`",
            )

        return cls(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self}')"

    def __json__(self) -> str:
        return str(self)

    def eval(
        self,
        *,
        input_dir: Optional[str] = "{input_dir}",
        output_dir: Optional[str] = "{output_dir}",
    ) -> str:
        return self.format(
            input_dir=input_dir,
            output_dir=output_dir,
            assets_dir=ASSETS_DIR,
        )

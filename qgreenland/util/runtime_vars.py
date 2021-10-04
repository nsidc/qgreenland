from collections import UserString
from typing import Optional


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
        input_dir: Optional[str] = None,
        output_dir: Optional[str] = None,
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

# Pydantic and Mypy

This project uses Mypy for typechecking, and Pydantic for runtime validation.

While Pydantic uses type annotations to determine runtime validation behavior, it also
effectively overrides your annotation with `Any` (try `reveal_type(MyModel)`!). This is
because Pydantic needs to be able to convert compatible values. [Pydantic's mypy
plugin](https://docs.pydantic.dev/1.10/mypy_plugin/#plugin-settings), which we use,
offers an `init_typed` setting, which we do not use, to "correctly" annotate the
`__init__` method of models, with the downside that Mypy throws errors when you take
advantage of Pydantic's type conversion behavior.

For this reason, it is expected that QGreenland config files would **pass** type
checking when instantiating Pydantic models with incorrect field types. These
would instead **fail** runtime validation.

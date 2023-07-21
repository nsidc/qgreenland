from layer_group_settings_less_magic_order.convert_strings_to_class_instances import (
    ConvertStringsToClassInstances,
)
from libcst.codemod import CodemodContext, CodemodTest

MOCK_FILEPATH = "/path/to/__settings__.py"


class TestConvertStringsToClassInstances(CodemodTest):
    maxDiff = None
    TRANSFORM = ConvertStringsToClassInstances

    def test_noop(self) -> None:
        """Verify that if we don't have a valid match, we don't make any changes."""
        before = """
            foo = "bar"
        """
        after = str(before)

        self.assertCodemod(
            before,
            after,
            context_override=CodemodContext(filename=MOCK_FILEPATH),
        )

    def test_noop_realistic(self) -> None:
        """Verify that if the code is in a good state, we don't make any changes."""
        before = """
            from qgreenland.models.config.layer_group import LayerGroupSettings, LayerIdentifier

            settings = LayerGroupSettings(
                order=[
                    LayerIdentifier("foo"),
                    LayerIdentifier("bar"),
                ],
            )
        """
        after = str(before)

        self.assertCodemod(
            before,
            after,
            context_override=CodemodContext(filename=MOCK_FILEPATH),
        )

    def test_migration(self) -> None:
        """Verify that the old style migrates to the new style."""
        before = """
            from qgreenland.models.config.layer_group import LayerGroupSettings

            settings = LayerGroupSettings(
                order=[
                    ":foo",
                    ":bar",
                    "Baz",
                ],
            )
        """
        after = """
            from qgreenland.models.config.layer_group import LayerGroupIdentifier, LayerIdentifier, LayerGroupSettings

            settings = LayerGroupSettings(
                order=[
                    LayerIdentifier("foo"),
                    LayerIdentifier("bar"),
                    LayerGroupIdentifier("Baz"),
                ],
            )
        """

        self.assertCodemod(
            before,
            after,
            context_override=CodemodContext(filename=MOCK_FILEPATH),
        )

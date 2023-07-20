"""Make the layer group order configuration less magical.

The "old" way is to specify groups as plain strings matching a subdirectory name, and
layers as strings matching layer ids with a `:` prefix.

This was magical, and we moved to `LayerIdentifier("some_layer_id")` and
`LayerGroupIdentifier("Some group directory")` to explicitly differentiate between the
two things represented with simple strings.

To run:

    python -m libcst.tool codemod \
        convert_strings_to_class_instances.ConvertStringsToClassInstances ../..
"""
from pathlib import Path

# Regular `breakpoint()`s don't work because stdin is trapped or something ¯\_(ツ)_/¯
# from remote_pdb import set_trace
import libcst as cst
from libcst.codemod import CodemodContext, VisitorBasedCodemodCommand
from libcst.codemod.visitors import AddImportsVisitor


def log(string: str) -> None:
    print()
    print(f">> {string}")
    print()


class ConvertStringsToClassInstances(VisitorBasedCodemodCommand):
    DESCRIPTION: str = """Converts magical stringy layer order specifications in
    __settings__.py files to explicit class-based layer group order specifications.
    Required for QGreenland v3 configuration schema change.
    """
    METADATA_DEPENDENCIES = (cst.metadata.ParentNodeProvider,)

    def __init__(self, context: CodemodContext) -> None:
        # "context" is state shared between transforms; e.g. contains the current
        # module/package/filename being modified and any "wrappers".
        super().__init__(context)

    def leave_SimpleString(
        self,
        original_node: cst.SimpleString,
        updated_node: cst.SimpleString,
    ) -> cst.Call | cst.SimpleString:
        """Call this function for every simple string in the CST."""
        # Help the typechecker. This should always be populated in this context, but the
        # typechecker doesn't know that.
        assert self.context.filename

        # Only operate on `__settings__.py` files
        file = Path(self.context.filename)
        if file.name != "__settings__.py":
            raise cst.codemod.SkipFile

        # Skip test data which is intentionally incorrect
        if "/qgreenland/test/" in str(file):
            raise cst.codemod.SkipFile

        # Get the ancestor node 3 levels above this string
        arg_node: cst.CSTNode = original_node
        for _ in range(3):
            arg_node = self.get_metadata(cst.metadata.ParentNodeProvider, arg_node)

        arg_node_parent = self.get_metadata(cst.metadata.ParentNodeProvider, arg_node)

        # We're looking for a call to "LayerGroupSettings" or "RootGroupSettings"
        # containing an `order` arg. That `order` arg's value should be a list
        # containing this node.
        is_what_we_looking_for = (
            isinstance(arg_node, cst.Arg)
            and arg_node.keyword
            and arg_node.keyword.value == "order"
            and isinstance(arg_node_parent, cst.Call)
            and isinstance(arg_node_parent.func, cst.Name)
            and arg_node_parent.func.value
            in [
                "LayerGroupSettings",
                "RootGroupSettings",
            ]
        )

        # Do nothing if this string is NOT a member of the expected structure
        if not is_what_we_looking_for:
            return updated_node

        if updated_node.raw_value.startswith(":"):
            # Handle layer: Wrap the string in a call and remove leading colon
            AddImportsVisitor.add_needed_import(
                self.context,
                "qgreenland.models.config.layer_group",
                "LayerIdentifier",
            )
            return cst.Call(
                func=cst.Name("LayerIdentifier"),
                args=[
                    cst.Arg(
                        cst.SimpleString(
                            f'"{updated_node.raw_value[1:]}"',
                        )
                    )
                ],
            )

        else:
            # Handle layer group: Wrap the string in a call
            AddImportsVisitor.add_needed_import(
                self.context,
                "qgreenland.models.config.layer_group",
                "LayerGroupIdentifier",
            )
            return cst.Call(
                func=cst.Name("LayerGroupIdentifier"),
                args=[
                    cst.Arg(
                        cst.SimpleString(
                            updated_node.value,
                        )
                    )
                ],
            )

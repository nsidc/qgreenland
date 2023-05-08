"""Support a `toctree-only` directive which enables filtering a toctree on tags.

Inspired by / based on <https://stackoverflow.com/a/46600038>.
"""
import re

from sphinx.directives.other import TocTree
from sphinx.util import logging

logger = logging.getLogger(__name__)


def setup(app):
    app.add_directive("toctree-select-builder", TocTreeSelectBuilder)
    return {"version": "1.0.0"}


class TocTreeSelectBuilder(TocTree):
    """A version of `toctree` directive which supports selecting items by builder name.

    We filter the content of the directive and then call the super's version of run.
    Any table of prefixed with a string will be included only if the builder name
    matches that string. If the builder name is `html`, the following toc entries will
    have the following results:

    * `foo`: included because there is no prefix
    * `:html:bar`: included because the prefix matches the builder name
    * `:baz:qux`: excluded because the prefix mismatches the builder name
    """

    prefixPattern = re.compile("^\s*:(.+):(.+)$")

    def filter_entries(self, entries):
        """Discard entries whose prefix mismatches the current builder.

        Prefixes are removed in the process.
        """
        valid_prefixes = ["html", "latex"]
        builder_name = self.env.app.builder.name

        selected = []
        for e in entries:
            m = self.prefixPattern.match(e)

            # Keep the whole entry if no prefix found. Move on to the next entry.
            if m is None:
                selected.append(e)
                continue

            prefix = m.groups()[0]
            value = m.groups()[1]

            if prefix not in valid_prefixes:
                msg = (
                    f"Entry '{e}' from toc named '{self.options['name']}'"
                    f" has invalid {prefix=}; must be one of {valid_prefixes=} "
                )
                logger.error(msg)
                raise RuntimeError(msg)

            # If there's a prefix, keep only if it matches builder name
            if prefix == builder_name:
                # Keep the value but not the prefix
                selected.append(value)

            else:
                logger.warning(
                    f"Discarding entry '{e}' from toc named '{self.options['name']}':"
                    f" {prefix=} does not match {builder_name=}"
                )

        return selected

    def run(self):
        self.content = self.filter_entries(self.content)
        return super().run()

import inspect
import os
from pathlib import Path
from contextlib import contextmanager
from typing import Generator

import jinja2
from invoke import run

PROJECT_DIR = Path(__file__).parent.parent
DOC_DIR = PROJECT_DIR / 'doc'
INDEX_FILEPATH = DOC_DIR / 'index.rst'
INDEX_TEMPLATE_FILEPATH = INDEX_FILEPATH.parent / f'{INDEX_FILEPATH.name}.j2'


def print_and_run(cmd, **run_kwargs):
    print(cmd)
    return run(cmd, **run_kwargs)


@contextmanager
def rendered_doc_index_file(pdf: bool = False) -> Generator[Path, None, None]:
    """Use Jinja2 templating to hack in support for conditional content.

    We don't want our contributor docs to be included in the PDF output that will be
    bundled with QGreenland, and Sphinx's `only` directive isn't capable of doing what
    we want (https://github.com/sphinx-doc/sphinx/issues/2150).
    """
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader(str(DOC_DIR)))
    template = environment.get_template(
        str(INDEX_TEMPLATE_FILEPATH.relative_to(DOC_DIR)),
    )

    filled = template.render(pdf=pdf)

    INDEX_FILEPATH.unlink(missing_ok=True)
    with open(INDEX_FILEPATH, 'w') as index_file:
        index_file.write(filled)
        index_file.flush()
        yield index_file

    INDEX_FILEPATH.unlink()

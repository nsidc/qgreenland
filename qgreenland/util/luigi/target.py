import shutil
from contextlib import contextmanager
from pathlib import Path
from typing import Generator

import luigi


@contextmanager
def temporary_path_dir(target: luigi.Target) -> Generator[Path, None, None]:
    """Standardizes Luigi task file output behavior.

    target: a Luigi.FileSystemTarget
            https://luigi.readthedocs.io/en/stable/api/luigi.target.html#luigi.target.FileSystemTarget.temporary_path
    """
    with target.temporary_path() as p:
        path = Path(p)
        try:
            path.mkdir(parents=True, exist_ok=True)
            yield path
        except Exception as e:
            shutil.rmtree(path)
            raise e
    return

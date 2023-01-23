import inspect
import os
from pathlib import Path

from invoke import run

PROJECT_DIR = Path(__file__).parent.parent


def print_and_run(cmd, **run_kwargs):
    print(cmd)
    return run(cmd, **run_kwargs)

from invoke import run


def print_and_run(cmd, **run_kwargs):
    print(cmd)
    return run(cmd, **run_kwargs)

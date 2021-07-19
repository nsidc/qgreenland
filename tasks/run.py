from invoke import task

from .util import print_and_run, PROJECT_DIR


@task(default=True)
def run(ctx):
    print_and_run(f'cd {PROJECT_DIR} && ./scripts/run_task.sh', pty=True)


@task
def clean(ctx):
    # TODO: How to pass arguments in?
    print_and_run(f'cd {PROJECT_DIR} && ./scripts/cleanup.sh', pty=True)

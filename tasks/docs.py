from invoke import call, task

from .util import print_and_run, PROJECT_DIR


@task
def build(ctx, pdf=False):
    docs_dir = PROJECT_DIR / 'doc'
    command = f'make html{" && make latexpdf" if pdf else ""}'
    print_and_run(
        f'cd {docs_dir} && make clean && {command}',
        pty=True,
    )


@task
def watch(ctx):
    script_path = (
        PROJECT_DIR /
        'scripts' / 'experimental' /
        'build_docs_on_change.sh'
    )

    print_and_run(
        str(script_path),
        pty=True,
    )

from invoke import call, task

from .util import print_and_run, PROJECT_DIR


@task
def build(ctx):
    docs_dir = PROJECT_DIR / 'doc'
    print_and_run(
        f'cd {docs_dir} &&'
        ' make clean &&'
        ' make html',
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

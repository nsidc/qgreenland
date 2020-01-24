from invoke import task


@task
def flake8(ctx):
    ctx.run('flake8 .')

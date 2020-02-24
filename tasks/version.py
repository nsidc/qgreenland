from invoke import task


@task
def bump(ctx, part):
    ctx.run(f'bumpversion {part}')

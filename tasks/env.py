from invoke import task

from .util import PROJECT_DIR, print_and_run

ENV_LOCKFILE = PROJECT_DIR / "environment-lock.yml"


@task(default=True)
def lock(ctx):
    """Update the environment-lock.yml file from the current `qgreenland` environment."""
    print_and_run(f"conda env export -n qgreenland > {ENV_LOCKFILE}")

    with open(ENV_LOCKFILE, "r") as f:
        lines = f.readlines()

    with open(ENV_LOCKFILE, "w") as f:
        for line in lines:
            # The prefix line contains machine-specific directory
            if line.startswith("prefix: "):
                continue

            # We don't want to use the NSIDC conda channel
            if "- nsidc" in line:
                continue

            # We want to replace the "defaults" channel with "nodefaults" so conda-forge
            # is used for everything.
            if "- defaults" in line:
                f.write(line.replace("- defaults", "- nodefaults"))
                continue

            f.write(line)

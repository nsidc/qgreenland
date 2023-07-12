# This docker image simply runs luigi's centralized scheduler with the needed
# dependencies installed into a conda environment. All QGreenland tasks are
# available at `TASKS_DIR`.

FROM axiom/docker-luigi:3.0.3-alpine AS luigi
# This build stage only exists to grab the luigi run script. Luigi dependency
# itself is specified in `environment.yml`
# TODO: Why is this necessary? Does `luigid` not come along with the conda package?

FROM mambaorg/micromamba:1.4.2 AS micromamba
COPY --from=luigi /bin/run /usr/local/bin/luigid
USER root

# `libgl1-mesa-glx` is required for pyqgis
# `git` is required for analyzing the current version
# `make` is required for building sphinx docs
# `texlive-latex-extra` is required for pdf doc builds
# TODO: Remove `make`
RUN apt-get update && apt-get install -y \
  git \
  make \
  libgl1-mesa-glx \
  texlive-latex-extra

ENV TASKS_DIR=/luigi/tasks/qgreenland
WORKDIR "${TASKS_DIR}"
COPY --chown=$MAMBA_USER:$MAMBA_USER . .

# Our code needs to run git commands (for example, to determine a full version
# string), but if tasks  repo is mounted from the host machine, the owner of
# the repo won't match the container user. A "safe directory" allows Git to
# tolerate this user mismatch.
RUN git config --global --add safe.directory "${TASKS_DIR}"

# Set up the Luigi task environment and the command environment
RUN micromamba install -y -n base -f conda-lock.yml
RUN micromamba create -y -f environment.cmd.yml

# Cleanup
RUN micromamba clean --all --yes

WORKDIR /luigi

# Everything is installed to the base conda environment, but the docker image
# doesn't activate the env automatically, which is how the PYTHONPATH normally
# gets populated. Additionally, /luigi/tasks is where we expect python code to
# be mounted.
# TODO: With modern micromamba, can we clean this up?
ENV PYTHONPATH "${TASKS_DIR}:/opt/conda/share/qgis/python/plugins:/opt/conda/share/qgis/python"
ENV PATH "/opt/conda/bin:${PATH}"

CMD ["/usr/local/bin/luigid"]

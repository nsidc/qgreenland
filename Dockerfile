# This docker image simply runs luigi's centralized scheduler with the needed
# dependencies installed into a conda environment. It's expected that task code
# will always be mounted in using volumes!

FROM axiom/docker-luigi:3.0.3-alpine AS luigi
# This build stage only exists to grab the luigi run script. Luigi dependency
# itself is specified in `environment.yml`

FROM mambaorg/micromamba:1.4.2 AS micromamba
COPY --from=luigi /bin/run /usr/local/bin/luigid
USER root

ENV TASKS_MOUNT_DIR=/luigi/tasks/qgreenland

# `libgl1-mesa-glx` is required for pyqgis
# `git` is required for analyzing the current version
# `make` is required for building sphinx docs
# `texlive-latex-extra` is required for pdf doc builds
RUN apt-get update && apt-get install -y \
  git \
  make \
  libgl1-mesa-glx \
  texlive-latex-extra

# Enable our code (which runs git commands) to run as a different user than the
# current user on the host machine (who will be the owner of the mounted git
# repository)
RUN git config --global --add safe.directory "${TASKS_MOUNT_DIR}"

# Why are we copying these files to /tmp?
COPY --chown=$MAMBA_USER:$MAMBA_USER conda-lock.yml /tmp/conda-lock.yml
RUN micromamba install -y -n base -f /tmp/conda-lock.yml

# Create environments
RUN micromamba install -y -c conda-forge -n base conda mamba~=1.4.2

COPY --chown=$MAMBA_USER:$MAMBA_USER environment.cmd.yml /tmp/environment.cmd.yml
RUN micromamba create -y -f /tmp/environment.cmd.yml

# Cleanup
RUN micromamba clean --all --yes

WORKDIR /luigi

# Everything is installed to the base conda environment, but the docker image
# doesn't activate the env automatically, which is how the PYTHONPATH normally
# gets populated. Additionally, /luigi/tasks is where we expect python code to
# be mounted.
# TODO: With modern micromamba, can we clean this up?
ENV PYTHONPATH "${TASKS_MOUNT_DIR}:/opt/conda/share/qgis/python/plugins:/opt/conda/share/qgis/python"
ENV PATH "/opt/conda/bin:${PATH}"

CMD ["/usr/local/bin/luigid"]

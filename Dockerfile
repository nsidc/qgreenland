FROM axiom/docker-luigi:2.8.13-alpine as luigi
# Build stage only exists to grab files

FROM mambaorg/micromamba:0.17.0
COPY --from=luigi /bin/run /usr/local/bin/luigid

# `git` is required for analyzing the current version
USER root
RUN apt-get update && apt-get install -y git
USER micromamba

# Create environments and cleanup

COPY --chown=micromamba:micromamba environment-lock.yml /tmp/environment.yml
RUN micromamba install -y -n base -f /tmp/environment.yml

COPY --chown=micromamba:micromamba environment.cmd.yml /tmp/environment.cmd.yml
RUN micromamba create -y -f /tmp/environment.cmd.yml

RUN micromamba clean --all --yes

WORKDIR /luigi

# Everything is installed to the base conda environment, but the docker image
# doesn't activate the env automatically, which is how the PYTHONPATH normally
# gets populated. Additionally, /luigi/tasks is where we expect python code to
# be mounted.
ENV PYTHONPATH /luigi/tasks/qgreenland:/opt/conda/share/qgis/python/plugins:/opt/conda/share/qgis/python

CMD ["/usr/local/bin/luigid"]

# NOTE: We do not use this version of Luigi, because a Docker image isn't
# available for our desired version. `environment.yml` specifies the actual
# version we use.
FROM axiom/docker-luigi:2.8.13

# `libgl1-mesa-glx` is required for qgis to work
# `unrar` is required for layer pipelines
# `git` is required for analyzing the current version
RUN apt-get update
RUN apt-get install -y libgl1-mesa-glx \
                       unrar \
                       git

# TODO install to `qgreenland` specific environment. Activate in Dockerfile if
# possible.
COPY environment-lock.yml .
RUN conda env update --file environment-lock.yml --name base

# Create a dedicated env for shelling out to gdal
COPY environment.gdal.yml .
RUN conda env create --file environment.gdal.yml

# Use this method to install to non-root? Need to edit luigid.sh...
# COPY environment.yml .
# RUN conda env create
# ENV PATH="/something/bin:$PATH"

# It's probably better to use the `conda run` method if we're editing luigid.sh
# anyway.

WORKDIR /luigi

# Everything is installed to the base conda environment, but the docker image
# doesn't activate the env automatically, which is how the PYTHONPATH normally
# gets populated. Additionally, /luigi/tasks is where we expect python code to
# be mounted.
ENV PYTHONPATH /luigi/tasks/qgreenland:/opt/conda/share/qgis/python/plugins:/opt/conda/share/qgis/python

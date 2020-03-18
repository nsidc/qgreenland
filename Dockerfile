FROM axiom/docker-luigi:2.8.11

# libgl1 is required for qgis to work. `unrar` is required for layer pipelines.
RUN apt-get update && apt-get install -y libgl1-mesa-glx unrar

# TODO install to `qgreenland` specific environment. Activate in Dockerfile if
# possible.
COPY environment-lock.yml .
RUN conda env update -f environment-lock.yml -n base

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
ENV PYTHONPATH /luigi/tasks:/opt/conda/share/qgis/python/plugins:/opt/conda/share/qgis/python

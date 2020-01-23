FROM axiom/docker-luigi:2.8.11

# This is required for qgis to work
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# TODO: Figure out a way to avoid using root env
# Use environment.yml
RUN conda config --remove channels defaults
RUN conda install --yes --freeze-installed \
    python=="3.8*" \
    geopandas=="0.6.2" \
    earthpy=="0.8.0" \
    pyyaml=="5.3" \
    requests=="2.22.0" \
    qgis=="3.10.1"

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

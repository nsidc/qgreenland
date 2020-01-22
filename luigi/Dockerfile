FROM axiom/docker-luigi:2.8.11

WORKDIR /luigi
ENV PYTHONPATH /luigi/tasks


# COPY environment.yml .
# RUN conda env create

# ENV PATH="/something/bin:$PATH"

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

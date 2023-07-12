# QGreenland's main `conda` environment

QGreenland needs this environment for its framework to function. This includes Luigi,
for generating a DAG of the tasks that need to be done; Pydantic, for data validation;
and PyQGIS for making QGIS project files.

Individual layer processing steps are handled by the [command
environment](/environments/command/README.md).

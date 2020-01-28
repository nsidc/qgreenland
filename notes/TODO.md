* Settle on one pattern for tasks that write out many files.
  * Write to a temp location and when done, write out to a text file with paths
    to real output files.
  * PREFERRED: Use the output directory as output(), but in run(), write to a
    temporary dir and then rename to the final location.

* Merge functionality of qgis and luigi in to one container and conda env:
  * Run qgis with `docker exec luigi qgis ...`? How to forward X?
  * Modify Luigi Docker image's luigid.sh to use non-base env

* Puppetry
  * Mount: `/share/appdata/qgreenland` (See: https://nsidc.org/jira/browse/SAS-13855)

* Code quality checks:
  * Lint:
    * flake8-bugbear
    * flake8-debugger
    * flake8-string-format
    * flake8-comprehensions
  * Unit tests
  * Regression tests?

* Continuous Integration/Deployment
  * Build Docker image
  * Test
  * On master commit:
    * Push Docker image (latest)
  * On tag vX.Y.Z:
    * Push Docker image (vX.Y.Z)
    * Run pipeline
    * Deploy package vX.Y.Z

* Bumpversion integration

* Build a dockerhub image (public!)
  * Update CircleCI jobs to use the docker image instead of building a conda
    environment every time :rage:


# Long Term

* Metadata
  * Provenance
  * Citation

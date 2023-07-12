# QGreenland's "command" `conda` environment

This environment exists for running `CommandStep` layer data processing steps.

The original rationale for creation of this environment was conflict between
QGreenland's [main environment](/environments/main/README.md) dependencies and
dependencies needed for layer data processing.


## TODO

* Ideally all data processing, including Python steps, would run in this environment for
  reproducibility.  When that's implemented, consider renaming this environment to the
  "step" environment?  In the long term, we may consider extracting the framework
  elements to a library, and in that case we'd want the end-user to define data
  processing steps, and the dependencies required to execute those steps, preferably
  with a lock-file defining the exact environment that was _actually_ used. So this
  pattern of defining a data-processing lock-file is probably here to stay.

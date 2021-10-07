# About

## Create a new `git` branch

Avoid conflicts with other developers! Create a branch called
`migrate-{yourlayer}`.


## Select layers and datasets of interest

Examine the old QGreenland config:

    https://github.com/nsidc/qgreenland/tree/v1.0.2/qgreenland/config

Find the layer and dataset IDs you are interested in and note them for the next
steps.

The dataset ID is listed as `data_source` on the layer config in the format
`<dataset_id>.<source_id>`, e.g.:

    data_source: seismograph_stations.only


## Run dataset migration

Run the following command to create a basic migration of dataset(s). Validate
that it looks correct afterwards. Manual changes may or may not be required.

`./scripts/cli.sh config-migrate dataset {dataset_pattern} > qgreenland/config/datasets/{dataset}.py`

* Specifically examine the whitespace in large strings like `abstract` or
  `description` fields. Blank lines may need to be added to compensate for
incorrect YAML in the old format. Compare against the YAML as a guide.

## Run layer migration

### Prep directories

Ensure that the layer's group path is represented in the `layers/config`
directory structure. This can be found in the YAML config as, e.g.:

    group_path: 'Human activity/Research stations'

Please ensure that the capitalization of these directories is identical to the
text found in the old YAML config.

If layers are ordered in a special way, you may also need to create a
`__settings__.py` file in the root of new directories you've created. Follow
the example set in other directories. If you are adding a directory to an
existing directory with a `__settings__.py`, that file may need to be updated.


### Migrate layer

Run the following command to create a basic migration of layer(s). Validate
that it looks correct afterwards. Manual changes _WILL_ be required. Write the
new layer file out to the new directory you just created.

```
./scripts/cli.sh config-migrate layer {layer_pattern} > \
  qgreenland/config/layers/{group}/{dir}/{layer}.py
```

e.g.:
```
./scripts/cli.sh config-migrate layer seismo* > \
  qgreenland/config/layers/Human activity/Research stations/seismograph_stations.py
```

* Look for `# TODO` markers in the output and fill those in. Don't forget to
  delete to TODOs!

* Specifically examine the whitespace in large strings like `abstract` or
  `description` fields. Blank lines may need to be added to compensate for
  incorrect YAML in the old format. Compare against the YAML as a guide.


### Manually populate steps

Examine the `ingest_task` element of the YAML layer config. e.g.:

    ingest_task: online_vector

To find the relevant python code, look for this string in
`qgreenland/tasks/layers/__init__.py`

    # ...
    from qgreenland.tasks.layers.online_vector import OnlineVector
    # ...

    INGEST_TASKS = {
        # ...
        'online_vector': OnlineVector,
        # ...
    }

This tells you that the `online_vector` module's `OnlineVector` class
(`LayerPipeline`) will be used to process this layer. The `requires` method of
this pipeline class shows the tasks the pipeline is composed of. e.g.:

    class OnlineVector(LayerPipeline):
        """Download and process any vector data that ogr2ogr can read."""
    
        def requires(self):
            fetch_data = FetchDataFiles(
                dataset_cfg=self.cfg['dataset'],
                source_cfg=self.cfg['source'],
            )  # ->
            return Ogr2OgrVector(
                requires_task=fetch_data,
                layer_id=self.layer_id
            )


This pipeline runs a fetch first (fetches don't count as steps in the new
model, they're defined by the `input` section of a layer, so you probably don't
need to worry about it).

Then it runs `Ogr2OgrVector`. Examine this class and see which layer config
elements it looks at. For example:

    input_ogr2ogr_kwargs = self.layer_cfg.get('ogr2ogr_kwargs', {})

This task looks at the `ogr2ogr_kwargs` key of the layer config. Reference the
YAML:

    ogr2ogr_kwargs:
        input_filename: 'stations.kmz'

This part is open-ended and fuzzy: Reference the code and the inputs provided
by the config to translate the python code + YAML config into a resulting CLI
command or commands, in this case `ogr2ogr`. Where possible, use existing
helpers in `qgreenland/config/helpers/steps` or create new helpers which can be
re-used for similar code.


# Testing

Run a single layer like so:

    ./scripts/container_cli.sh run seismograph_stations

NOTE: You should do a cleanup before running to ensure all the expected tasks
are run.

    ./scripts/container_cli.sh cleanup \
      -C True -R True -w seismograph_stations -i "seismograph*"

Compare the output from this job to a known good output (e.g. QGreenland
v1.0.2) until the outputs are identical. Look at things like statistics to make
sure that the min and max and average are the same, and may be some spot
checking of specific pixels or points to make sure nothing sneaky happened.

Every layer must be clipped to a shape. Look for the `boundary` key in the
layers YAML to see which shape the layer should be clipped to. If the boundary
key isn't present, I'm not sure what that means. Edit this section later if we
figure it out. You can always check QGreenland in QGIS to see which way a layer
was clipped. Rasters and Vectors are clipped differently (`gdalwarp` vs
`ogr2ogr`), so use another similar layer as an example.

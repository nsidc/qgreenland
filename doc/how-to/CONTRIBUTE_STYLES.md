# How to contribute styles

You can contribute style changes without editing any Python code using the
following process:

* Download (or build) and open the most recent version of the project in QGIS.
* In the 'Layers' menu, double click on the layer you wish to edit.
* Open the 'symbology' tab.
* Make your desired style changes.
* In the lower-left corner, click the 'Style' dropdown.
* In this menu, select 'Save Style...'

![Save style](images/save_style.png)

* At this point, if you're uncomfortable with Git and GitHub, you can email us
  your style file at qgreenland.info@gmail.com. Otherwise, continue on...
* Save the style to `qgreenland/assets/styles/<name>.qml` directory of this
  repository or your fork. Keep in mind that styles can be shared between
  layers, so give the style a generic name instead of a layer-specific name
  where possible.
* Edit the relevant layer configuration file in `qgreenland/config/layers` and
  find the layer(s) you wish to apply this style to. Populate the `style`
  attribute for each layer with the name of the `.qml` file you saved in the
  previous step, excluding the file extension. For example, if you saved
  `foo.qml`, then populate `style='foo'`.

![Style in YAML](images/style_in_yaml.png)


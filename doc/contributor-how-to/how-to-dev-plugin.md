# How to install QGreenland Custom as a developer

QGreenland Custom is a QGIS plugin for downloading a custom set of data, including data which 
is not part of the QGreenland Core zip package. This how-to guide walks through how to install the plugin as a developer.

First, clone the QGreenland Custom repo from Faunalia:

```
git clone https://github.com/faunalia/qgreenland-plugin.git
```

Use the QGIS GUI to locate the QGreenland Custom directory by going to
Settings -> User Profiles -> Open Active Profile Folder.
Then, navigate to the /.python/plugins directory, echo $PWD and copy the full filpath. 

Next symlink the plugin repo to the plugin directory:
```
ln -s $PWD '/filepath'
```
## Installing and reloading QGreenland Custom

To begin installing QGreenland Custom, access the Plugin tab 
in the top menu bar, and select 'Manage and Install Plugins'. 

![menu_bar](/_images/menu_bar.png)

This will open the plugin pop-up window. First, click the Settings tab and select the check box 
labeled 'Show also experimental plugins' so that QGreenland will be included. 

![plugin_settings](/_images/plugin_settings.png)

Navigate to the 'Installed' tab in the plugin window, and check the box for 'QGreenland Custom'. 

Instead of restarting QGIS after installing QGreenland Custom, 
install the plugin, Plugin Reloader. Plugin Reloader will allow you to immediately
see your changes instead of needing to restart QGIS. You can do this by navigating to 
Plugin -> Manage and Install Plugins, then searching for Plugin Reloader in the
search bar. Install the plugin then press OK.

To use the plugin, navigate to the Menu Bar and select Plugins -> Plugin Reloader -> Configure.
Select qgreenland-plugin in the drop down. Uncheck the 'run the commands
below before reloading' option. Leave the 'display' option checked, and press OK.

![configure_plugin](/_images/configure_plugin.png)

Navigate to Plugins -> Plugin Reloader -> Reload Plugin: qgreenland-plugin.

![reload_plugin](/_images/reload_plugin.png)

You should receive a message notifying you that the plugin has been reloaded.

## Configuring QGreenland Custom
To use QGreenland Custom, first navigate to Web -> QGreenland -> Configure the Server. Leave the default options and press OK. 

![configure_server](/_images/configure_server.png)

## Using the plugin to download data
To dowload data to your project, navigate to Web -> QGreenland -> Download Data.
In the Download Data window, select the desired layer then press Next.

![plugin_search_window](/_images/plugin_search_window.png)

Next, you will need to choose a location to download the data. Select your location using the 
three dot icon, and once you have chosen a location, click the 'Download' button. When the download
is finished, you will see a blue bar at the bottom of the window showing your downloaded layer. 

![download_bar](/_images/download_bar.png)

Next, you will be asked to select which downloaded layers you would like to add to your QGIS 
project. This will be a full list of downloaded layers, so there may be more than one layer listed
if you have used the plugin more than once or selected to download multiple layers at once. 

![downloaded_layer](/_images/downloaded_layers.png)

Find your layer of interest and click the checkbox, then click 'Add to project'. Once the layer has been added, you should see the new layer in the QGIS Layer panel and in the Map View. Click 'Close' to exit the plugin.
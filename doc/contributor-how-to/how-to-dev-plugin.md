# How to install Qgreenland Custom as a developer

QGreenland Custom is a QGIS plugin for downloading a custom set of data, including data which 
is not part of the QGreenland Core zip package. This how-to guide walks through how to install the plugin as a developer.

First, clone the plugin repo from Faunalia:

```
git clone https://github.com/faunalia/qgreenland-plugin.git
```

Use the QGIS GUI to locate the plugin directory by going to
Settings -> User Profiles -> Open Active Profile Folder.
Then, navigate to the /python/plugins directory, PWD and copy the full filpath. 

Next symlink the plugin repo to the plugin directory:
```
ln -s $PWD '/filepath'
```
## Installing QGreenland Custom

To install Qgreenland, navigate to plugins -> Installed -> Check box on Qgreenland -> OK

Instead of restarting QGIS after installing Qgreenland, 
install the plugin, Plugin Reloader. You can do this by navigating to 
Plugin -> Manage and Install Plugins, then searching for Plugin Reloader in the
search bar. Install the plugin then press OK.

To use the plugin, navigate to Plugins -> Plugin Reloader -> Configure.
Select qgreenland-plugin in the drop down. Uncheck the 'run the commands
below before reloading' option. Leave the 'display' option checked, and press OK.

![configure_plugin](/_images/configure_plugin.png)


Navigate to Plugins -> Plugin Reloader -> Reload Plugin: qgreenland-plugin.

![reload_plugin](/_images/reload_plugin.png)

You should receive a message notifying you that the plugin has been reloaded.

## Configuring the plugin
To use the Qgreenland plugin, first navigate to Web -> Qgreenland -> Configure the Server.

![configure_server](/_images/configure_server.png)

Leave the default options and press OK. 

## Using the plugin to download data
To dowload data to your project, navigate to Web -> Qgreenland -> Download Data.
In the Download Data window, select the desired layer then press Next.
Choose a location to put the downloaded data, then press Download. 

Once the data has finished downloading, press Next. Check the downloaded layers
that you would like to add to your project, press Add to Project, then press Close.
You should now see your downloaded data layers in your QGIS project. 
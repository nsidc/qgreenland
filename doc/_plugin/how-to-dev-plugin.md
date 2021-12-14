# How to install the Qgreenland plugin as a developer

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
## Installing the QGreenland plugin

To install Qgreenland, navigate to plugins -> Installed -> Check box on Qgreenland -> OK

Instead of restarting QGIS after installing Qgreenland, 
install the plugin, Plugin Reloader. You can do this by navigating to 
Plugin -> Manage and Install Plugins, then searching for Plugin Reloader in the
search bar. Install the plugin then press OK.

To use the plugin, navigate to Plugins -> Plugin Reloader -> Configure.
Select qgreenland-plugin in the drop down. Uncheck the 'run the commands
below before reloading' option. Leave the 'display' option checked, and press OK.

Navigate to Plugins -> Plugin Reloader -> Reload Plugin: qgreenland-plugin.
You should receive a message notifying you that the plugin has been reloaded.

## Configuring the plugin
To use the Qgreenland plugin, first navigate to Web -> Qgreenland -> Configure the Server.
Leave the default options and press OK. 

## Using the plugin to download data
To dowload data to your project, navigate to Web -> Qgreenland -> Download Data.
In the Download Data window, select the desired layer then press Next.
Choose a location to put the downloaded data, then press Download. 

Once the data has finished downloading, press Next. Check the downloaded layers
that you would like to add to your project, press Add to Project, then press Close.
You should now see your downloaded data layers in your QGIS project. 
# How to install QGreenland Custom as a developer

QGreenland Custom is a QGIS plugin for downloading a custom set of data, including data which 
is not part of the QGreenland Core zip package. This how-to guide walks through how to install the plugin as a developer.

First, clone the QGreenland Custom repo from Faunalia:

```
git clone https://github.com/faunalia/qgreenland-plugin.git
```

Use the QGIS GUI to locate the QGreenland Custom directory by going to
**Settings -> User Profiles -> Open Active Profile Folder**.
Then, navigate to the /.python/plugins directory, echo $PWD and copy the full filepath. 

Next symlink the plugin repo to the plugin directory using the filepath from the previous step:
```
ln -s $PWD '/filepath'
```
## Installing and reloading QGreenland Custom

To begin installing QGreenland Custom, access the **Plugin** tab 
in the top **Menu Bar**, and select **Manage and Install Plugins**. 

![menu_bar](/_images/menu_bar.png)

Navigate to the **Installed** tab in the **Plugin** window, and check the box for QGreenland Custom. 

Instead of restarting QGIS after installing QGreenland Custom, 
install the plugin, **Plugin Reloader**. **Plugin Reloader** will allow you to immediately
see your changes instead of needing to restart QGIS. You can do this by navigating to 
**Plugin -> Manage and Install Plugins**, then searching for **Plugin Reloader** in the
search bar. Install the plugin then press OK.

To use the plugin, navigate to the **Menu Bar** and select **Plugins -> Plugin Reloader -> Configure**.
Select **qgreenland-plugin** in the drop down. Uncheck the **run the commands below before reloading** option. Leave the display option checked, and press OK.

![configure_plugin](/_images/configure_plugin.png)

Navigate to **Plugins -> Plugin Reloader -> Reload Plugin: qgreenland-plugin**.

![reload_plugin](/_images/reload_plugin.png)

You should receive a message notifying you that the plugin has been reloaded.

After reloading the plugin, you are all set to begin using QGreenland Custom. Reference the user guide,
**How to install and use QGreenland Custom**, to get started.

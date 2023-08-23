# Troubleshooting

```{contents} Contents
:local:

```


## Difficulty opening the project

If you are having trouble opening the project, first ensure you are using QGIS
3.16 LTR or greater. If you want to move QGreenland to a different location on
your filesystem, move the entire directory; do not attempt to move only the
`.qgs`/`.qgz` project file.


### QGIS will not start on OSX Catalina

QGIS is currently not 'notarized' for Mac OSX. If you receive `The developer of
this app needs to update it to work with this version of macOS. Contact the
developer for more information.`, then, in your OSX menus, try:

- 'Security and Privacy'
- 'Allow apps downloaded from...'
- 'App Store and identified developers'
- Locate QGIS here and select 'Open anyway'


### 'Unable to open' from QGIS when opening project

If you opened QGreenland from the command line, ensure you got the project name
correct. E.g., from inside the unzipped QGreenland directory:

```
qgis qgreenland.qgs
```


### No layers are present in the Layers Panel

If you do not see layers in the **Layers Panel**, you have not correctly opened
a project. Click **Project** in the **Menu Bar**, then select **Add Project**,
then navigate to your QGreenland directory, wherever you saved it, and open the
`.qgs`/`.qgz` file inside.


## Difficulty using the project

### After opening QGreenland, I only see blue ocean

Right click on a layer in the **Layers Panel** that you would like to view, and
select **Zoom to Layer**.

If you experience this issue, please [contact
us](mailto:qgreenland.info@gmail.com) with information about your Operating
System and QGIS version. A small number of users have reported this issue, but
we haven't been able to identify the cause thus far.

### `Too many open files` on Linux

Your system may have multiple ways of limiting open files in different
contexts. To check your limits:

```
ulimit -Sn  # soft limit
ulimit -Hn  # hard limit
```

Edit the `/etc/security/limits.conf` to add or update rules that apply to your
user. If there are no rules, you can try adding:

```
* soft nofile 20480
* hard nofile 1048576
```

If your system uses `systemd`, also edit the `/etc/systemd/system.conf` and
`/etc/systemd/user.conf` files to ensure the following variable is set to a
large value in *both* files:

```
DefaultLimitNOFILE=20480
```

After applying these changes, you may find that new terminal windows are not
affected. Reboot your computer to make the changes permanent.


### I see `ERROR: Too many connections: max 64` in my terminal

We do not think this is an issue. This started happening when we switched to
GeoPackages for vector data, but we have observed no negative impact of this error
message.


### The QGIS interface has no buttons or toolbars

Right-click the toolbar area in the QGIS interface and check the toolbars you
wish to turn on so that they are displayed. You can also go to 
**View -> Toolbars** in the **Menu Bar**.


### I cannot see a layer in the Map View even though it is turned on and I have zoomed to it

Double-check that there is not another layer overlaying and thus obscuring the
layer you want to see in the **Map View**. Remember that layer are displayed in the
**Map View** in the same order that they are listed in the **Layers Panel** - layers
listed at the top of the **Layers Panel** show up on top on the **Map View**. You can
either turn off any layer that might be obscuring the layer you wish to see by
unchecking it in the **Layers Panel**, or re-arrange the order of layers by
clicking and dragging them up or down in the **Layers Panel**.

Some QGreenland data layers are only visible at a specific map scale (see
_QGreenland User Guide section 4.3.1: [Scale-dependent
rendering](#scale-dependent-rendering)_ for more information). Try zooming in.


### When I open QGreenland, I get the warning `Font "Helvetica" not available on system`

Please upgrade to QGreenland v3 and a supported version of QGIS (>=3.28).

For more context, see the [GitHub
issue](https://github.com/nsidc/qgreenland/issues/515).


### When I open QGreenland, I get the warning `This project file was created by a newer version of QGIS`

For example:

```
This project file was created by a newer version of QGIS (3.28.8-Firenze) and could not
be completely loaded.
```

We have not observed any adverse effects from this warning. If you want to get rid of the
message permanently, update to the latest release of a supported QGIS version.


### Navigating QGIS errors

If you are opening QGIS using a terminal or using the QGIS Python console, it is possible you
might see one of a few different error messages while using QGIS that the QGreenland team
has determined can be ignored:

   -**Warning: Logged warning: Creating Warped VRT**
   This error message is likely triggered by a raster layer in the QGreenland project but
   should not have any impact on the data layers or project usability.

   -**ERROR: Too many connections: max 64**
   This error is thought to be related to the GeoPackage file format but should not have any
   impact on the layers themselves or the project usability.


## I am having other problems. How do I contact the QGreenland team?

If you have feedback or questions about the QGreenland data package, or want to
contribute datasets to future QGreenland releases, please participate in our [GitHub
Discussions](https://github.com/nsidc/qgreenland/discussions/) space. If you're
uncomfortable with or otherwise can not participate there, please contact us directly at
<qgreenland.info@gmail.com>. 

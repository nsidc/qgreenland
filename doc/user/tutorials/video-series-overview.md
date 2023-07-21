# Beginner Video Series

## Overview
In this video series, you will become familiar with QGIS, download and browse the QGreenland Core data package, and explore the basic geospatial data anlysis tools that make QGreenland a powerful tool for research, education, and local decision making. The video tutorial series contains 7 short video sessions.

```
### Goals
* Learn what data is included in the QGreenland Core Package
* Analyze Greenland data using geoprocessing tools
* Find analysis tools and data relevant to you or your classes

### Format
Videos
Reflection and dicussion
QGIS

### Total Time
1 hour

```

In order to get the most out of this series, we recommend the following:
* Install QGIS on your computer. Go to [qgis.org](https://www.qgis.org/) and download the free QGIS software. QGIS version 3.16 is the oldest version supported by QGreenland.
* Download the QGreenland Core data package at [https://qgreenland.org/download](https://qgreenland.org/download). Go to [Get started with QGreenland](https://qgreenland.readthedocs.io/en/latest/tutorials/get-started.html) for more information.
* When watching the videos, click on the settings icon to adjust the subtitles (in Englishor other languages) and adjust the playback speed
* Take time to engage in the practice tasks and take notes

## Introduction to QGreenland (15 minutes)

If you are not familiar with geographic information systems (GIS) and geospatial data, this video will introduce you to GIS and what it can be used for.
### [Session 1: Introduction to QGreenland](https://www.youtube.com/watch?v=gD0vkP5JUmA&list=PLSRiyMridUCwyu-vqpAFtm8bVERgTvs7q&index=1)


### [Session 2: Introduction to QGIS and QGreenland Core Package](https://www.youtube.com/watch?v=u8exrxhwme4&list=PLSRiyMridUCwyu-vqpAFtm8bVERgTvs7q&index=2)

- How to download QGIS and QGreenland Core package
- Obtain a general understanding of what GIS and QGreenland are
- Explore the QGreenland Core package folders

## [Session 3: Navigating the Core package](https://www.youtube.com/watch?v=WhboP5u5HqE&list=PLSRiyMridUCwyu-vqpAFtm8bVERgTvs7q&index=3)

- Navigate the QGIS interface
- Toggle panels on and off
- Turn toolbars on and off

## [Session 4: Layers and Properties](https://www.youtube.com/watch?v=hAMw-_dFWng&list=PLSRiyMridUCwyu-vqpAFtm8bVERgTvs7q&index=4)

- Access properties, attributes, and metadata of layers
- Know the difference between vector and raster layers
- Identify different layer types in Layers Panel
- Change display or symbology of layers

## [Session 5: Processing Toolbox and Data Analysis](https://www.youtube.com/watch?v=znKeiV3-Amo&list=PLSRiyMridUCwyu-vqpAFtm8bVERgTvs7q&index=5)

- Locate and open the processing toolbox
- Select by attribute in a vector layer
- Run basic statistics on a vector attribute field including sum, mean, and range
- Calculate the surface volume area of a raster layer

```{note}
In our example, ‘select by attribute’ for a population greater than 5000 would only work on an integer field. In v2.0,  the population size field is a text string and you will first need to use the field calculator to convert the population field into an integer. To do so:

1. Open up the attribute table, and click the ‘Open field calculator’ icon.

    ![OpenFieldcalculator_Larger](/_images/OpenFieldcalculator_Larger.png)

2. Check ‘Create a new field’. Designate an output field name (example: pop_numeric) and select the output field type ‘Integer (32 bit)’. In the expression panel, choose the field ‘population’. Click OK.

    ![create_new_field](/_images/create_new_field.png)
```


## [Session 6: Editing Existing and New Layers](https://www.youtube.com/watch?v=98nF6YJAnns&list=PLSRiyMridUCwyu-vqpAFtm8bVERgTvs7q&index=6)

- Edit existing layers in the QGreenland Core Package
- Create a new Vector layer
- Manage layer locations and removal of layers

## [Session 7: Preparing Map for Export and Publication](https://www.youtube.com/watch?v=6YG_Jc7HcOo&list=PLSRiyMridUCwyu-vqpAFtm8bVERgTvs7q&index=7)

- Export a QGreenland Map for publication

<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis hasScaleBasedVisibilityFlag="0" minScale="1e+08" version="3.10.7-A Coruña" styleCategories="AllStyleCategories" maxScale="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <customproperties>
    <property key="WMSBackgroundLayer" value="false"/>
    <property key="WMSPublishDataSourceUrl" value="false"/>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="identify/format" value="Value"/>
  </customproperties>
  <pipe>
    <rasterrenderer angle="45" opacity="1" zfactor="5" multidirection="0" band="1" azimuth="315" alphaBand="-1" type="hillshade">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0"/>
    <huesaturation colorizeStrength="100" saturation="0" grayscaleMode="0" colorizeBlue="128" colorizeRed="255" colorizeGreen="128" colorizeOn="0"/>
    <rasterresampler zoomedInResampler="bilinear" maxOversampling="2" zoomedOutResampler="bilinear"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

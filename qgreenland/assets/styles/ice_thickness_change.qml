<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis hasScaleBasedVisibilityFlag="0" styleCategories="AllStyleCategories" maxScale="0" version="3.14.0-Pi" minScale="1e+08">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <temporal enabled="0" mode="0" fetchMode="0">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <customproperties>
    <property key="WMSBackgroundLayer" value="false"/>
    <property key="WMSPublishDataSourceUrl" value="false"/>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="identify/format" value="Value"/>
  </customproperties>
  <pipe>
    <rasterrenderer nodataColor="" opacity="1" type="singlebandpseudocolor" classificationMin="-2" alphaBand="-1" classificationMax="2" band="1">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Exact</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <rastershader>
        <colorrampshader maximumValue="2" colorRampType="INTERPOLATED" clip="0" minimumValue="-2" classificationMode="1">
          <colorramp name="[source]" type="gradient">
            <prop v="202,0,32,255" k="color1"/>
            <prop v="5,113,176,255" k="color2"/>
            <prop v="0" k="discrete"/>
            <prop v="gradient" k="rampType"/>
            <prop v="0.25;244,165,130,255:0.5;247,247,247,255:0.75;146,197,222,255" k="stops"/>
          </colorramp>
          <item alpha="255" color="#ca0020" label="-2" value="-2"/>
          <item alpha="255" color="#f4a582" label="-1" value="-1"/>
          <item alpha="255" color="#f7f7f7" label="0" value="0"/>
          <item alpha="255" color="#92c5de" label="1" value="1"/>
          <item alpha="255" color="#0571b0" label="2" value="2"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0"/>
    <huesaturation colorizeStrength="100" colorizeRed="255" colorizeBlue="128" grayscaleMode="0" colorizeOn="0" saturation="0" colorizeGreen="128"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

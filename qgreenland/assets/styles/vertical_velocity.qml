<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis hasScaleBasedVisibilityFlag="0" version="3.10.3-A Coruña" styleCategories="AllStyleCategories" minScale="1e+08" maxScale="0">
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
    <rasterrenderer classificationMin="-0.3" classificationMax="0.3" opacity="1" alphaBand="-1" band="1" type="singlebandpseudocolor">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <rastershader>
        <colorrampshader classificationMode="1" colorRampType="INTERPOLATED" clip="0">
          <colorramp name="[source]" type="gradient">
            <prop v="58,73,89,255" k="color1"/>
            <prop v="140,18,14,255" k="color2"/>
            <prop v="0" k="discrete"/>
            <prop v="gradient" k="rampType"/>
            <prop v="0.1;58,73,89,255:0.2;64,90,121,255:0.3;69,108,153,255:0.4;150,166,180,255:0.5;230,223,207,255:0.6;224,136,125,255:0.7;217,49,43,255:0.8;178,34,28,255:0.9;140,18,14,255" k="stops"/>
          </colorramp>
          <item alpha="255" color="#3a4959" label="-0.3" value="-0.3"/>
          <item alpha="255" color="#3a4959" label="-0.24" value="-0.24"/>
          <item alpha="255" color="#405a79" label="-0.18" value="-0.18"/>
          <item alpha="255" color="#456c99" label="-0.12" value="-0.12"/>
          <item alpha="255" color="#96a6b4" label="-0.06" value="-0.06"/>
          <item alpha="255" color="#e6dfcf" label="0" value="0"/>
          <item alpha="255" color="#e0887d" label="0.06" value="0.06"/>
          <item alpha="255" color="#d9312b" label="0.12" value="0.12"/>
          <item alpha="255" color="#b2221c" label="0.18" value="0.18"/>
          <item alpha="255" color="#8c120e" label="0.24" value="0.24"/>
          <item alpha="255" color="#8c120e" label="0.3" value="0.3"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0"/>
    <huesaturation saturation="0" colorizeOn="0" grayscaleMode="0" colorizeGreen="128" colorizeStrength="100" colorizeRed="255" colorizeBlue="128"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

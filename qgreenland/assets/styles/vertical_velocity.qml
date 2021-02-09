<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="1e+08" version="3.10.4-A Coruña" maxScale="0" hasScaleBasedVisibilityFlag="0" styleCategories="AllStyleCategories">
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
    <rasterrenderer classificationMin="-0.3" band="1" classificationMax="0.3" opacity="1" type="singlebandpseudocolor" alphaBand="-1">
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
        <colorrampshader classificationMode="1" clip="0" colorRampType="INTERPOLATED">
          <colorramp name="[source]" type="gradient">
            <prop v="58,73,89,255" k="color1"/>
            <prop v="140,18,14,255" k="color2"/>
            <prop v="0" k="discrete"/>
            <prop v="gradient" k="rampType"/>
            <prop v="0.1;58,73,89,255:0.2;64,90,121,255:0.3;69,108,153,255:0.4;150,166,180,255:0.5;230,223,207,255:0.6;224,136,125,255:0.7;217,49,43,255:0.8;178,34,28,255:0.9;140,18,14,255" k="stops"/>
          </colorramp>
          <item label="-0.3 m/d" color="#3a4959" alpha="255" value="-0.3"/>
          <item label="-0.24 m/d" color="#3a4959" alpha="255" value="-0.24"/>
          <item label="-0.18 m/d" color="#405a79" alpha="255" value="-0.18"/>
          <item label="-0.12 m/d" color="#456c99" alpha="255" value="-0.12"/>
          <item label="-0.06 m/d" color="#96a6b4" alpha="255" value="-0.06"/>
          <item label="0 m/d" color="#e6dfcf" alpha="255" value="0"/>
          <item label="0.06 m/d" color="#e0887d" alpha="255" value="0.06"/>
          <item label="0.12 m/d" color="#d9312b" alpha="255" value="0.12"/>
          <item label="0.18 m/d" color="#b2221c" alpha="255" value="0.18"/>
          <item label="0.24 m/d" color="#8c120e" alpha="255" value="0.24"/>
          <item label="0.3 m/d" color="#8c120e" alpha="255" value="0.3"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0"/>
    <huesaturation grayscaleMode="0" colorizeOn="0" colorizeGreen="128" saturation="0" colorizeBlue="128" colorizeStrength="100" colorizeRed="255"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

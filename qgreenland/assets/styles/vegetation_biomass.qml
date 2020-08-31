<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" maxScale="0" minScale="1e+08" version="3.12.3-București">
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
    <rasterrenderer nodataColor="" band="1" alphaBand="-1" opacity="1" classificationMax="inf" type="singlebandpseudocolor" classificationMin="0.1">
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
        <colorrampshader classificationMode="2" colorRampType="DISCRETE" clip="0">
          <colorramp name="[source]" type="gradient">
            <prop k="color1" v="247,252,245,255"/>
            <prop k="color2" v="0,68,27,255"/>
            <prop k="discrete" v="0"/>
            <prop k="rampType" v="gradient"/>
            <prop k="stops" v="0.13;229,245,224,255:0.26;199,233,192,255:0.39;161,217,155,255:0.52;116,196,118,255:0.65;65,171,93,255:0.78;35,139,69,255:0.9;0,109,44,255"/>
          </colorramp>
          <item color="#f7fcf5" alpha="255" label="&lt;= 0.10 kg/m2" value="0.1"/>
          <item color="#e8f6e3" alpha="255" label="0.10 - 0.20 kg/m2" value="0.2"/>
          <item color="#d0edca" alpha="255" label="0.20 - 0.30 kg/m2" value="0.3"/>
          <item color="#b2e0ab" alpha="255" label="0.30 - 0.40 kg/m2" value="0.4"/>
          <item color="#8ed18c" alpha="255" label="0.40 - 0.50 kg/m2" value="0.5"/>
          <item color="#66bd6f" alpha="255" label="0.50 - 0.60 kg/m2" value="0.6"/>
          <item color="#3da75a" alpha="255" label="0.60 - 0.70 kg/m2" value="0.7"/>
          <item color="#238c45" alpha="255" label="0.70 - 0.80 kg/m2" value="0.8"/>
          <item color="#03702e" alpha="255" label="0.80 - 0.90 kg/m2" value="0.9"/>
          <item color="#00441b" alpha="255" label="> 0.90 kg/m2" value="inf"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0"/>
    <huesaturation saturation="0" grayscaleMode="0" colorizeStrength="100" colorizeBlue="128" colorizeOn="0" colorizeGreen="128" colorizeRed="255"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

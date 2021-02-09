<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="1e+08" styleCategories="AllStyleCategories" maxScale="0" hasScaleBasedVisibilityFlag="0" version="3.10.3-A Coruña">
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
    <rasterrenderer classificationMin="0" type="singlebandpseudocolor" band="1" classificationMax="5000" opacity="1" alphaBand="-1">
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
        <colorrampshader colorRampType="INTERPOLATED" clip="0" classificationMode="2">
          <colorramp type="gradient" name="[source]">
            <prop v="255,255,255,255" k="color1"/>
            <prop v="0,42,168,255" k="color2"/>
            <prop v="0" k="discrete"/>
            <prop v="gradient" k="rampType"/>
            <prop v="0.016;253,252,244,255:0.032;251,249,232,255:0.048;249,246,221,255:0.063;247,243,210,255:0.079;244,239,198,255:0.095;242,236,188,255:0.111;243,232,182,255:0.127;243,228,175,255:0.143;243,223,168,255:0.159;242,219,161,255:0.175;242,215,155,255:0.19;242,210,149,255:0.206;243,206,144,255:0.222;243,201,139,255:0.238;244,196,134,255:0.254;244,192,130,255:0.27;244,187,125,255:0.286;244,182,122,255:0.302;245,177,119,255:0.317;245,172,116,255:0.333;245,167,113,255:0.349;245,162,110,255:0.365;245,157,108,255:0.381;245,152,107,255:0.397;245,146,106,255:0.413;244,141,105,255:0.429;244,136,104,255:0.444;243,130,103,255:0.46;243,125,103,255:0.476;241,120,104,255:0.492;240,114,105,255:0.508;239,109,105,255:0.524;237,104,106,255:0.54;236,98,107,255:0.556;234,93,108,255:0.571;231,87,110,255:0.587;229,82,112,255:0.603;226,77,113,255:0.619;224,71,115,255:0.635;221,65,117,255:0.651;217,61,119,255:0.667;213,56,122,255:0.683;209,52,124,255:0.698;205,47,127,255:0.714;200,42,129,255:0.73;196,37,131,255:0.746;190,35,134,255:0.762;184,32,137,255:0.778;178,30,139,255:0.794;172,27,142,255:0.81;166,25,145,255:0.825;159,25,147,255:0.841;151,26,149,255:0.857;143,27,152,255:0.873;134,29,154,255:0.889;125,30,156,255:0.905;116,31,159,255:0.921;105,33,160,255:0.937;92,36,162,255:0.952;79,38,163,255:0.968;63,39,165,255:0.984;41,41,166,255" k="stops"/>
          </colorramp>
          <item alpha="255" label="0 mm w.e." color="#ffffff" value="0"/>
          <item alpha="255" label="1000 mm w.e." color="#f3d092" value="1000"/>
          <item alpha="255" label="2000 mm w.e." color="#f5916a" value="2000"/>
          <item alpha="255" label="3000 mm w.e." color="#e34e71" value="3000"/>
          <item alpha="255" label="4000 mm w.e." color="#aa1a8f" value="4000"/>
          <item alpha="255" label="5000 mm w.e." color="#002aa8" value="5000"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0"/>
    <huesaturation colorizeRed="255" colorizeGreen="128" colorizeBlue="128" colorizeStrength="100" colorizeOn="0" saturation="0" grayscaleMode="0"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

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
    <rasterrenderer classificationMin="-160" type="singlebandpseudocolor" band="1" classificationMax="160" opacity="1" alphaBand="-1">
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
            <prop v="168,144,8,255" k="color1"/>
            <prop v="58,144,254,255" k="color2"/>
            <prop v="0" k="discrete"/>
            <prop v="gradient" k="rampType"/>
            <prop v="0.016;171,146,24,255:0.032;174,149,34,255:0.048;176,152,43,255:0.063;179,155,51,255:0.079;182,158,59,255:0.095;185,161,66,255:0.111;187,164,73,255:0.127;190,167,80,255:0.143;193,170,87,255:0.159;195,173,94,255:0.175;198,176,101,255:0.19;200,179,107,255:0.206;203,182,114,255:0.222;205,185,121,255:0.238;208,188,127,255:0.254;210,191,134,255:0.27;212,194,141,255:0.286;215,197,147,255:0.302;217,200,154,255:0.317;219,203,161,255:0.333;221,206,167,255:0.349;223,209,174,255:0.365;225,213,181,255:0.381;227,216,188,255:0.397;229,219,194,255:0.413;231,222,201,255:0.429;233,225,208,255:0.444;234,229,215,255:0.46;236,232,222,255:0.476;237,235,228,255:0.492;238,236,234,255:0.508;236,236,239,255:0.524;233,235,241,255:0.54;229,232,242,255:0.556;225,229,243,255:0.571;221,225,243,255:0.587;216,222,244,255:0.603;212,219,244,255:0.619;207,216,245,255:0.635;203,213,245,255:0.651;198,210,246,255:0.667;194,206,246,255:0.683;189,203,247,255:0.698;184,200,247,255:0.714;180,197,248,255:0.73;175,194,248,255:0.746;170,191,248,255:0.762;165,188,249,255:0.778;160,185,249,255:0.794;154,182,250,255:0.81;149,179,250,255:0.825;143,176,250,255:0.841;138,173,251,255:0.857;132,170,251,255:0.873;126,167,252,255:0.889;119,164,252,255:0.905;113,161,252,255:0.921;105,158,253,255:0.937;98,156,253,255:0.952;90,153,253,255:0.968;81,150,254,255:0.984;70,147,254,255" k="stops"/>
          </colorramp>
          <item alpha="255" label="-160 mm w.e." color="#a89008" value="-160"/>
          <item alpha="255" label="-120 mm w.e." color="#bea74f" value="-120"/>
          <item alpha="255" label="-80 mm w.e." color="#d2be84" value="-80"/>
          <item alpha="255" label="-40 mm w.e." color="#e3d7ba" value="-40"/>
          <item alpha="255" label="0 mm w.e." color="#edeced" value="0"/>
          <item alpha="255" label="40 mm w.e." color="#ced7f5" value="40"/>
          <item alpha="255" label="80 mm w.e." color="#a9bef9" value="80"/>
          <item alpha="255" label="120 mm w.e." color="#7da7fc" value="120"/>
          <item alpha="255" label="160 mm w.e." color="#3a90fe" value="160"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0"/>
    <huesaturation colorizeRed="255" colorizeGreen="128" colorizeBlue="128" colorizeStrength="100" colorizeOn="0" saturation="0" grayscaleMode="0"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

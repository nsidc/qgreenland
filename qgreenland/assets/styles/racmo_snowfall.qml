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
    <rasterrenderer classificationMin="0" type="singlebandpseudocolor" band="1" classificationMax="4000" opacity="1" alphaBand="-1">
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
            <prop v="241,241,241,255" k="color1"/>
            <prop v="59,124,178,255" k="color2"/>
            <prop v="0" k="discrete"/>
            <prop v="gradient" k="rampType"/>
            <prop v="0.016;237,239,240,255:0.032;234,237,240,255:0.048;231,235,240,255:0.063;228,233,240,255:0.079;225,231,239,255:0.095;222,229,239,255:0.111;219,227,239,255:0.127;216,225,238,255:0.143;213,223,238,255:0.159;210,221,238,255:0.175;207,220,237,255:0.19;203,218,237,255:0.206;200,216,236,255:0.222;197,214,236,255:0.238;194,212,235,255:0.254;191,210,235,255:0.27;188,208,234,255:0.286;185,206,234,255:0.302;182,204,233,255:0.317;179,203,233,255:0.333;176,201,232,255:0.349;173,199,231,255:0.365;170,197,231,255:0.381;167,195,230,255:0.397;164,193,229,255:0.413;161,191,228,255:0.429;158,189,227,255:0.444;156,188,225,255:0.46;153,186,224,255:0.476;151,184,223,255:0.492;148,182,221,255:0.508;146,180,220,255:0.524;144,178,218,255:0.54;141,176,216,255:0.556;139,174,215,255:0.571;137,172,213,255:0.587;135,170,211,255:0.603;133,169,209,255:0.619;130,167,208,255:0.635;128,165,206,255:0.651;126,163,204,255:0.667;124,161,202,255:0.683;122,159,200,255:0.698;120,157,198,255:0.714;118,155,197,255:0.73;116,153,195,255:0.746;113,152,194,255:0.762;111,150,192,255:0.778;108,148,191,255:0.794;105,146,190,255:0.81;102,144,189,255:0.825;99,143,188,255:0.841;96,141,186,255:0.857;93,139,185,255:0.873;90,137,185,255:0.889;86,136,184,255:0.905;83,134,183,255:0.921;79,132,182,255:0.937;76,130,181,255:0.952;72,129,180,255:0.968;68,127,179,255:0.984;63,125,179,255" k="stops"/>
          </colorramp>
          <item alpha="255" label="0 mm w.e." color="#f1f1f1" value="0"/>
          <item alpha="255" label="800 mm w.e." color="#c9d9ed" value="800"/>
          <item alpha="255" label="1600 mm w.e." color="#a4c1e5" value="1600"/>
          <item alpha="255" label="2400 mm w.e." color="#85a9d2" value="2400"/>
          <item alpha="255" label="3200 mm w.e." color="#6891be" value="3200"/>
          <item alpha="255" label="4000 mm w.e." color="#3b7cb2" value="4000"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0"/>
    <huesaturation colorizeRed="255" colorizeGreen="128" colorizeBlue="128" colorizeStrength="100" colorizeOn="0" saturation="0" grayscaleMode="0"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

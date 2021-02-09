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
    <rasterrenderer classificationMin="-210" type="singlebandpseudocolor" band="1" classificationMax="210" opacity="1" alphaBand="-1">
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
            <prop v="57,151,14,255" k="color1"/>
            <prop v="184,89,228,255" k="color2"/>
            <prop v="0" k="discrete"/>
            <prop v="gradient" k="rampType"/>
            <prop v="0.016;65,154,26,255:0.032;72,157,36,255:0.048;79,159,44,255:0.063;86,162,52,255:0.079;92,165,60,255:0.095;99,168,67,255:0.111;105,171,74,255:0.127;111,174,81,255:0.143;117,177,87,255:0.159;123,180,94,255:0.175;129,182,101,255:0.19;134,185,107,255:0.206;140,188,114,255:0.222;145,191,121,255:0.238;151,194,127,255:0.254;156,197,134,255:0.27;162,199,140,255:0.286;167,202,147,255:0.302;173,205,154,255:0.317;178,208,160,255:0.333;184,211,167,255:0.349;189,213,174,255:0.365;194,216,181,255:0.381;200,219,187,255:0.397;205,222,194,255:0.413;210,225,201,255:0.429;216,227,208,255:0.444;221,230,215,255:0.46;226,233,221,255:0.476;230,234,228,255:0.492;234,235,233,255:0.508;236,234,237,255:0.524;237,231,239,255:0.54;236,228,239,255:0.556;235,223,240,255:0.571;234,219,239,255:0.587;233,214,239,255:0.603;231,209,239,255:0.619;230,205,238,255:0.635;228,200,238,255:0.651;226,196,238,255:0.667;225,191,237,255:0.683;223,186,237,255:0.698;222,182,237,255:0.714;220,177,236,255:0.73;218,172,236,255:0.746;216,168,236,255:0.762;215,163,235,255:0.778;213,158,235,255:0.794;211,154,234,255:0.81;209,149,234,255:0.825;207,144,234,255:0.841;205,139,233,255:0.857;203,135,233,255:0.873;201,130,232,255:0.889;199,125,232,255:0.905;197,120,231,255:0.921;195,115,231,255:0.937;193,110,230,255:0.952;190,105,230,255:0.968;188,100,229,255:0.984;186,95,229,255" k="stops"/>
          </colorramp>
          <item alpha="255" label="-210 mm w.e." color="#39970e" value="-210"/>
          <item alpha="255" label="-150 mm w.e." color="#75b157" value="-150"/>
          <item alpha="255" label="-90 mm w.e." color="#a7ca93" value="-90"/>
          <item alpha="255" label="-30 mm w.e." color="#d8e3d0" value="-30"/>
          <item alpha="255" label="30 mm w.e." color="#eadbef" value="30"/>
          <item alpha="255" label="90 mm w.e." color="#dcb1ec" value="90"/>
          <item alpha="255" label="150 mm w.e." color="#cb87e9" value="150"/>
          <item alpha="255" label="210 mm w.e." color="#b859e4" value="210"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0"/>
    <huesaturation colorizeRed="255" colorizeGreen="128" colorizeBlue="128" colorizeStrength="100" colorizeOn="0" saturation="0" grayscaleMode="0"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

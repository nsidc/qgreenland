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
            <prop v="241,241,241,255" k="color1"/>
            <prop v="17,17,17,255" k="color2"/>
            <prop v="0" k="discrete"/>
            <prop v="gradient" k="rampType"/>
            <prop v="0.016;239,236,229,255:0.032;238,232,218,255:0.048;236,228,208,255:0.063;234,224,198,255:0.079;232,220,187,255:0.095;230,215,178,255:0.111;227,211,168,255:0.127;225,207,159,255:0.143;222,203,151,255:0.159;219,199,143,255:0.175;215,195,135,255:0.19;212,191,127,255:0.206;209,187,120,255:0.222;205,183,114,255:0.238;201,180,108,255:0.254;198,176,103,255:0.27;194,172,98,255:0.286;190,168,94,255:0.302;185,164,92,255:0.317;181,160,90,255:0.333;177,157,89,255:0.349;172,153,89,255:0.365;167,149,91,255:0.381;162,146,94,255:0.397;157,142,97,255:0.413;151,138,101,255:0.429;146,135,104,255:0.444;141,131,108,255:0.46;135,127,111,255:0.476;130,124,114,255:0.492;124,120,117,255:0.508;118,117,120,255:0.524;112,113,123,255:0.54;106,109,126,255:0.556;99,106,129,255:0.571;93,102,132,255:0.587;85,99,134,255:0.603;78,95,137,255:0.619;69,92,140,255:0.635;60,89,142,255:0.651;51,85,143,255:0.667;42,82,142,255:0.683;34,79,141,255:0.698;25,75,138,255:0.714;17,72,135,255:0.73;9,69,131,255:0.746;2,66,127,255:0.762;0,63,122,255:0.778;0,59,116,255:0.794;0,56,111,255:0.81;1,53,104,255:0.825;4,50,98,255:0.841;7,47,91,255:0.857;10,44,84,255:0.873;13,41,77,255:0.889;16,38,70,255:0.905;18,35,63,255:0.921;19,32,55,255:0.937;20,29,48,255:0.952;20,26,40,255:0.968;20,23,33,255:0.984;19,20,25,255" k="stops"/>
          </colorramp>
          <item alpha="255" label="0 mm w.e." color="#f1f1f1" value="0"/>
          <item alpha="255" label="625 mm w.e." color="#e2d0a0" value="625"/>
          <item alpha="255" label="1250 mm w.e." color="#c7b168" value="1250"/>
          <item alpha="255" label="1875 mm w.e." color="#a4935d" value="1875"/>
          <item alpha="255" label="2500 mm w.e." color="#797676" value="2500"/>
          <item alpha="255" label="3125 mm w.e." color="#415b8d" value="3125"/>
          <item alpha="255" label="3750 mm w.e." color="#01417e" value="3750"/>
          <item alpha="255" label="4375 mm w.e." color="#0d284c" value="4375"/>
          <item alpha="255" label="5000 mm w.e." color="#111111" value="5000"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0"/>
    <huesaturation colorizeRed="255" colorizeGreen="128" colorizeBlue="128" colorizeStrength="100" colorizeOn="0" saturation="0" grayscaleMode="0"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

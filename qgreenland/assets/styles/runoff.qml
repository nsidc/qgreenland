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
            <prop v="249,249,249,255" k="color1"/>
            <prop v="5,0,172,255" k="color2"/>
            <prop v="0" k="discrete"/>
            <prop v="gradient" k="rampType"/>
            <prop v="0.016;255,247,198,255:0.032;255,245,158,255:0.048;253,242,127,255:0.063;251,239,102,255:0.079;248,235,82,255:0.095;246,232,68,255:0.111;243,228,58,255:0.127;239,225,50,255:0.143;235,221,43,255:0.159;229,219,37,255:0.175;223,216,31,255:0.19;216,213,26,255:0.206;210,211,21,255:0.222;202,208,16,255:0.238;195,206,12,255:0.254;187,203,8,255:0.27;179,201,5,255:0.286;171,199,4,255:0.302;163,196,3,255:0.317;154,194,2,255:0.333;145,192,3,255:0.349;136,189,5,255:0.365;127,187,9,255:0.381;119,184,14,255:0.397;110,182,19,255:0.413;102,179,25,255:0.429;94,176,30,255:0.444;87,173,36,255:0.46;80,170,41,255:0.476;73,167,47,255:0.492;67,163,53,255:0.508;62,160,60,255:0.524;57,156,66,255:0.54;53,152,74,255:0.556;51,148,82,255:0.571;49,144,90,255:0.587;48,140,100,255:0.603;47,136,109,255:0.619;44,131,118,255:0.635;41,127,127,255:0.651;37,123,135,255:0.667;33,118,143,255:0.683;27,114,150,255:0.698;20,109,157,255:0.714;13,104,163,255:0.73;7,99,168,255:0.746;6,94,173,255:0.762;8,89,176,255:0.778;9,85,178,255:0.794;11,80,180,255:0.81;12,75,180,255:0.825;13,70,181,255:0.841;13,65,181,255:0.857;14,61,181,255:0.873;14,56,180,255:0.889;14,51,180,255:0.905;13,45,179,255:0.921;13,40,178,255:0.937;12,34,177,255:0.952;10,28,176,255:0.968;9,20,175,255:0.984;7,11,173,255" k="stops"/>
          </colorramp>
          <item alpha="255" label="0 mm w.e." color="#f9f9f9" value="0"/>
          <item alpha="255" label="500 mm w.e." color="#f0e233" value="500"/>
          <item alpha="255" label="1000 mm w.e." color="#bdcc09" value="1000"/>
          <item alpha="255" label="1500 mm w.e." color="#7ab90c" value="1500"/>
          <item alpha="255" label="2000 mm w.e." color="#40a238" value="2000"/>
          <item alpha="255" label="2500 mm w.e." color="#2b8279" value="2500"/>
          <item alpha="255" label="3000 mm w.e." color="#065dae" value="3000"/>
          <item alpha="255" label="3500 mm w.e." color="#0e37b4" value="3500"/>
          <item alpha="255" label="4000 mm w.e." color="#0500ac" value="4000"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0"/>
    <huesaturation colorizeRed="255" colorizeGreen="128" colorizeBlue="128" colorizeStrength="100" colorizeOn="0" saturation="0" grayscaleMode="0"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

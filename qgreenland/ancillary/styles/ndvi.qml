<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="1e+08" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" version="3.10.4-A Coruña" maxScale="0">
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
    <rasterrenderer type="singlebandpseudocolor" alphaBand="-1" band="1" classificationMin="-1" classificationMax="1" opacity="1">
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
        <colorrampshader clip="0" classificationMode="1" colorRampType="INTERPOLATED">
          <colorramp type="gradient" name="[source]">
            <prop v="5,24,82,255" k="color1"/>
            <prop v="0,0,0,255" k="color2"/>
            <prop v="0" k="discrete"/>
            <prop v="gradient" k="rampType"/>
            <prop v="0.35;5,24,82,255:0.41;255,255,255,255:0.5;255,255,255,255:0.5125;206,197,180,255:0.5375;191,163,124,255:0.5625;179,174,96,255:0.575;163,181,80,255:0.5875;144,170,60,255:0.6165;166,195,29,255:0.633;135,183,3,255:0.6665;121,175,1,255:0.683;101,163,0,255:0.7165;78,151,0,255:0.733;43,132,4,255:0.775;0,114,0,255:0.825;0,90,1,255:0.875;0,73,0,255:0.925;0,56,0,255:0.975;0,31,0,255" k="stops"/>
          </colorramp>
          <item label="-1 kg/m2" color="#051852" value="-1" alpha="255"/>
          <item label="-0.3 kg/m2" color="#051852" value="-0.3" alpha="255"/>
          <item label="-0.18 kg/m2" color="#ffffff" value="-0.18" alpha="255"/>
          <item label="0 kg/m2" color="#ffffff" value="0" alpha="255"/>
          <item label="0.0249999999999999 kg/m2" color="#cec5b4" value="0.0249999999999999" alpha="255"/>
          <item label="0.075 kg/m2" color="#bfa37c" value="0.075" alpha="255"/>
          <item label="0.125 kg/m2" color="#b3ae60" value="0.125" alpha="255"/>
          <item label="0.15 kg/m2" color="#a3b550" value="0.15" alpha="255"/>
          <item label="0.175 kg/m2" color="#90aa3c" value="0.175" alpha="255"/>
          <item label="0.233 kg/m2" color="#a6c31d" value="0.233" alpha="255"/>
          <item label="0.266 kg/m2" color="#87b703" value="0.266" alpha="255"/>
          <item label="0.333 kg/m2" color="#79af01" value="0.333" alpha="255"/>
          <item label="0.366 kg/m2" color="#65a300" value="0.366" alpha="255"/>
          <item label="0.433 kg/m2" color="#4e9700" value="0.433" alpha="255"/>
          <item label="0.466 kg/m2" color="#2b8404" value="0.466" alpha="255"/>
          <item label="0.55 kg/m2" color="#007200" value="0.55" alpha="255"/>
          <item label="0.65 kg/m2" color="#005a01" value="0.65" alpha="255"/>
          <item label="0.75 kg/m2" color="#004900" value="0.75" alpha="255"/>
          <item label="0.85 kg/m2" color="#003800" value="0.85" alpha="255"/>
          <item label="0.95 kg/m2" color="#001f00" value="0.95" alpha="255"/>
          <item label="1 kg/m2" color="#000000" value="1" alpha="255"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0"/>
    <huesaturation colorizeOn="0" colorizeStrength="100" colorizeRed="255" saturation="0" colorizeBlue="128" colorizeGreen="128" grayscaleMode="0"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="1e+08" version="3.10.4-A Coruña" hasScaleBasedVisibilityFlag="0" maxScale="0" styleCategories="AllStyleCategories">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <customproperties>
    <property value="false" key="WMSBackgroundLayer"/>
    <property value="false" key="WMSPublishDataSourceUrl"/>
    <property value="0" key="embeddedWidgets/count"/>
    <property value="Value" key="identify/format"/>
  </customproperties>
  <pipe>
    <rasterrenderer band="1" classificationMin="0" classificationMax="8712.24" type="singlebandpseudocolor" opacity="1" alphaBand="-1">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>MinMax</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <rastershader>
        <colorrampshader colorRampType="INTERPOLATED" clip="0" classificationMode="2">
          <colorramp name="[source]" type="gradient">
            <prop k="color1" v="68,1,84,255"/>
            <prop k="color2" v="253,231,37,255"/>
            <prop k="discrete" v="0"/>
            <prop k="rampType" v="gradient"/>
            <prop k="stops" v="0.0196078;70,8,92,255:0.0392157;71,16,99,255:0.0588235;72,23,105,255:0.0784314;72,29,111,255:0.0980392;72,36,117,255:0.117647;71,42,122,255:0.137255;70,48,126,255:0.156863;69,55,129,255:0.176471;67,61,132,255:0.196078;65,66,135,255:0.215686;63,72,137,255:0.235294;61,78,138,255:0.254902;58,83,139,255:0.27451;56,89,140,255:0.294118;53,94,141,255:0.313725;51,99,141,255:0.333333;49,104,142,255:0.352941;46,109,142,255:0.372549;44,113,142,255:0.392157;42,118,142,255:0.411765;41,123,142,255:0.431373;39,128,142,255:0.45098;37,132,142,255:0.470588;35,137,142,255:0.490196;33,142,141,255:0.509804;32,146,140,255:0.529412;31,151,139,255:0.54902;30,156,137,255:0.568627;31,161,136,255:0.588235;33,165,133,255:0.607843;36,170,131,255:0.627451;40,174,128,255:0.647059;46,179,124,255:0.666667;53,183,121,255:0.686275;61,188,116,255:0.705882;70,192,111,255:0.72549;80,196,106,255:0.745098;90,200,100,255:0.764706;101,203,94,255:0.784314;112,207,87,255:0.803922;124,210,80,255:0.823529;137,213,72,255:0.843137;149,216,64,255:0.862745;162,218,55,255:0.882353;176,221,47,255:0.901961;189,223,38,255:0.921569;202,225,31,255:0.941176;216,226,25,255:0.960784;229,228,25,255:0.980392;241,229,29,255"/>
          </colorramp>
          <item label="0 mm w.e." value="0" color="#440154" alpha="255"/>
          <item label="1089.03 mm w.e." value="1089.03" color="#462c7b" alpha="255"/>
          <item label="2178.06 mm w.e." value="2178.06" color="#3a528b" alpha="255"/>
          <item label="3267.09 mm w.e." value="3267.09" color="#2b728e" alpha="255"/>
          <item label="4356.12 mm w.e." value="4356.12" color="#20908d" alpha="255"/>
          <item label="5445.15 mm w.e." value="5445.15" color="#27ae80" alpha="255"/>
          <item label="6534.18 mm w.e." value="6534.18" color="#5dc962" alpha="255"/>
          <item label="7623.21 mm w.e." value="7623.21" color="#abdc32" alpha="255"/>
          <item label="8712.24 mm w.e." value="8712.24" color="#fde725" alpha="255"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0"/>
    <huesaturation colorizeOn="0" colorizeStrength="100" saturation="0" colorizeRed="255" colorizeBlue="128" colorizeGreen="128" grayscaleMode="0"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

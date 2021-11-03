<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="1e+08" maxScale="0" hasScaleBasedVisibilityFlag="0" version="3.16.3-Hannover" styleCategories="AllStyleCategories">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <temporal mode="0" enabled="0" fetchMode="0">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <customproperties>
    <property value="false" key="WMSBackgroundLayer"/>
    <property value="false" key="WMSPublishDataSourceUrl"/>
    <property value="0" key="embeddedWidgets/count"/>
    <property value="Value" key="identify/format"/>
  </customproperties>
  <pipe>
    <provider>
      <resampling maxOversampling="2" enabled="false" zoomedInResamplingMethod="nearestNeighbour" zoomedOutResamplingMethod="nearestNeighbour"/>
    </provider>
    <rasterrenderer type="singlebandpseudocolor" opacity="0.7" classificationMin="30.442749" classificationMax="158.5387115" nodataColor="" band="1" alphaBand="-1">
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
        <colorrampshader classificationMode="2" clip="0" labelPrecision="6" colorRampType="INTERPOLATED" maximumValue="158.5387115" minimumValue="30.442749">
          <colorramp type="gradient" name="[source]">
            <prop k="color1" v="68,1,84,255"/>
            <prop k="color2" v="253,231,37,255"/>
            <prop k="discrete" v="0"/>
            <prop k="rampType" v="gradient"/>
            <prop k="stops" v="0.0196078;70,8,92,255:0.0392157;71,16,99,255:0.0588235;72,23,105,255:0.0784314;72,29,111,255:0.0980392;72,36,117,255:0.117647;71,42,122,255:0.137255;70,48,126,255:0.156863;69,55,129,255:0.176471;67,61,132,255:0.196078;65,66,135,255:0.215686;63,72,137,255:0.235294;61,78,138,255:0.254902;58,83,139,255:0.27451;56,89,140,255:0.294118;53,94,141,255:0.313725;51,99,141,255:0.333333;49,104,142,255:0.352941;46,109,142,255:0.372549;44,113,142,255:0.392157;42,118,142,255:0.411765;41,123,142,255:0.431373;39,128,142,255:0.45098;37,132,142,255:0.470588;35,137,142,255:0.490196;33,142,141,255:0.509804;32,146,140,255:0.529412;31,151,139,255:0.54902;30,156,137,255:0.568627;31,161,136,255:0.588235;33,165,133,255:0.607843;36,170,131,255:0.627451;40,174,128,255:0.647059;46,179,124,255:0.666667;53,183,121,255:0.686275;61,188,116,255:0.705882;70,192,111,255:0.72549;80,196,106,255:0.745098;90,200,100,255:0.764706;101,203,94,255:0.784314;112,207,87,255:0.803922;124,210,80,255:0.823529;137,213,72,255:0.843137;149,216,64,255:0.862745;162,218,55,255:0.882353;176,221,47,255:0.901961;189,223,38,255:0.921569;202,225,31,255:0.941176;216,226,25,255:0.960784;229,228,25,255:0.980392;241,229,29,255"/>
          </colorramp>
          <item color="#440154" label="31.004000" value="31.004" alpha="255"/>
          <item color="#481e70" label="39.668167" value="39.668166666666664" alpha="255"/>
          <item color="#443a83" label="48.332333" value="48.33233333333333" alpha="255"/>
          <item color="#3a528b" label="56.996500" value="56.9965" alpha="255"/>
          <item color="#31688e" label="65.660667" value="65.66066666666666" alpha="255"/>
          <item color="#287c8e" label="74.324833" value="74.32483333333333" alpha="255"/>
          <item color="#20908d" label="82.989000" value="82.98899999999999" alpha="255"/>
          <item color="#20a486" label="91.653167" value="91.65316666666665" alpha="255"/>
          <item color="#35b779" label="100.317333" value="100.31733333333332" alpha="255"/>
          <item color="#5dc962" label="108.981500" value="108.98149999999998" alpha="255"/>
          <item color="#8fd744" label="117.645667" value="117.64566666666666" alpha="255"/>
          <item color="#c7e120" label="126.309833" value="126.30983333333332" alpha="255"/>
          <item color="#fde725" label="134.974000" value="134.97399999999996" alpha="255"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast gamma="1" brightness="0" contrast="0"/>
    <huesaturation colorizeRed="255" colorizeStrength="100" colorizeBlue="128" saturation="0" grayscaleMode="0" colorizeOn="0" colorizeGreen="128"/>
    <rasterresampler maxOversampling="2"/>
    <resamplingStage>resamplingFilter</resamplingStage>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

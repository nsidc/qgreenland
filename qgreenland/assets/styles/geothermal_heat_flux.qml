<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="3.10.4-A Coruña" styleCategories="AllStyleCategories" minScale="1e+08" hasScaleBasedVisibilityFlag="0" maxScale="0">
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
    <rasterrenderer band="1" classificationMax="134.974" alphaBand="-1" type="singlebandpseudocolor" classificationMin="31.004" opacity="0.7">
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
        <colorrampshader colorRampType="DISCRETE" classificationMode="2" clip="0">
          <colorramp type="gradient" name="[source]">
            <prop k="color1" v="68,1,84,255"/>
            <prop k="color2" v="253,231,37,255"/>
            <prop k="discrete" v="0"/>
            <prop k="rampType" v="gradient"/>
            <prop k="stops" v="0.0196078;70,8,92,255:0.0392157;71,16,99,255:0.0588235;72,23,105,255:0.0784314;72,29,111,255:0.0980392;72,36,117,255:0.117647;71,42,122,255:0.137255;70,48,126,255:0.156863;69,55,129,255:0.176471;67,61,132,255:0.196078;65,66,135,255:0.215686;63,72,137,255:0.235294;61,78,138,255:0.254902;58,83,139,255:0.27451;56,89,140,255:0.294118;53,94,141,255:0.313725;51,99,141,255:0.333333;49,104,142,255:0.352941;46,109,142,255:0.372549;44,113,142,255:0.392157;42,118,142,255:0.411765;41,123,142,255:0.431373;39,128,142,255:0.45098;37,132,142,255:0.470588;35,137,142,255:0.490196;33,142,141,255:0.509804;32,146,140,255:0.529412;31,151,139,255:0.54902;30,156,137,255:0.568627;31,161,136,255:0.588235;33,165,133,255:0.607843;36,170,131,255:0.627451;40,174,128,255:0.647059;46,179,124,255:0.666667;53,183,121,255:0.686275;61,188,116,255:0.705882;70,192,111,255:0.72549;80,196,106,255:0.745098;90,200,100,255:0.764706;101,203,94,255:0.784314;112,207,87,255:0.803922;124,210,80,255:0.823529;137,213,72,255:0.843137;149,216,64,255:0.862745;162,218,55,255:0.882353;176,221,47,255:0.901961;189,223,38,255:0.921569;202,225,31,255:0.941176;216,226,25,255:0.960784;229,228,25,255:0.980392;241,229,29,255"/>
          </colorramp>
          <item alpha="255" value="39.0016761192909" label="&lt;= 39.0016761192909 MW/m2" color="#440154"/>
          <item alpha="255" value="46.9994002122145" label="39.0016761192909 - 46.9994002122145 MW/m2" color="#481e70"/>
          <item alpha="255" value="54.9971243051382" label="46.9994002122145 - 54.9971243051382 MW/m2" color="#443a83"/>
          <item alpha="255" value="62.9948483980619" label="54.9971243051382 - 62.9948483980619 MW/m2" color="#3a528b"/>
          <item alpha="255" value="70.9925724909856" label="62.9948483980619 - 70.9925724909856 MW/m2" color="#31688e"/>
          <item alpha="255" value="78.9902965839093" label="70.9925724909856 - 78.9902965839093 MW/m2" color="#287c8e"/>
          <item alpha="255" value="86.9880206768329" label="78.9902965839093 - 86.9880206768329 MW/m2" color="#20908d"/>
          <item alpha="255" value="94.9857447697566" label="86.9880206768329 - 94.9857447697566 MW/m2" color="#20a486"/>
          <item alpha="255" value="102.98346886268" label="94.9857447697566 - 102.98346886268 MW/m2" color="#35b779"/>
          <item alpha="255" value="110.981192955604" label="102.98346886268 - 110.981192955604 MW/m2" color="#5dc962"/>
          <item alpha="255" value="118.978917048528" label="110.981192955604 - 118.978917048528 MW/m2" color="#8fd744"/>
          <item alpha="255" value="126.976641141451" label="118.978917048528 - 126.976641141451 MW/m2" color="#c7e120"/>
          <item alpha="255" value="inf" label="> 126.976641141451 MW/m2" color="#fde725"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0"/>
    <huesaturation colorizeStrength="100" saturation="0" grayscaleMode="0" colorizeBlue="128" colorizeGreen="128" colorizeOn="0" colorizeRed="255"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

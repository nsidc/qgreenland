<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" hasScaleBasedVisibilityFlag="0" minScale="1e+08" version="3.28.7-Firenze" styleCategories="AllStyleCategories">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
    <Private>0</Private>
  </flags>
  <temporal mode="0" enabled="0" fetchMode="0">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <elevation zscale="1" band="1" enabled="0" symbology="Line" zoffset="0">
    <data-defined-properties>
      <Option type="Map">
        <Option type="QString" value="" name="name"/>
        <Option name="properties"/>
        <Option type="QString" value="collection" name="type"/>
      </Option>
    </data-defined-properties>
    <profileLineSymbol>
      <symbol type="line" clip_to_extent="1" is_animated="0" name="" alpha="1" force_rhr="0" frame_rate="10">
        <data_defined_properties>
          <Option type="Map">
            <Option type="QString" value="" name="name"/>
            <Option name="properties"/>
            <Option type="QString" value="collection" name="type"/>
          </Option>
        </data_defined_properties>
        <layer pass="0" locked="0" enabled="1" class="SimpleLine">
          <Option type="Map">
            <Option type="QString" value="0" name="align_dash_pattern"/>
            <Option type="QString" value="square" name="capstyle"/>
            <Option type="QString" value="5;2" name="customdash"/>
            <Option type="QString" value="3x:0,0,0,0,0,0" name="customdash_map_unit_scale"/>
            <Option type="QString" value="MM" name="customdash_unit"/>
            <Option type="QString" value="0" name="dash_pattern_offset"/>
            <Option type="QString" value="3x:0,0,0,0,0,0" name="dash_pattern_offset_map_unit_scale"/>
            <Option type="QString" value="MM" name="dash_pattern_offset_unit"/>
            <Option type="QString" value="0" name="draw_inside_polygon"/>
            <Option type="QString" value="bevel" name="joinstyle"/>
            <Option type="QString" value="255,158,23,255" name="line_color"/>
            <Option type="QString" value="solid" name="line_style"/>
            <Option type="QString" value="0.6" name="line_width"/>
            <Option type="QString" value="MM" name="line_width_unit"/>
            <Option type="QString" value="0" name="offset"/>
            <Option type="QString" value="3x:0,0,0,0,0,0" name="offset_map_unit_scale"/>
            <Option type="QString" value="MM" name="offset_unit"/>
            <Option type="QString" value="0" name="ring_filter"/>
            <Option type="QString" value="0" name="trim_distance_end"/>
            <Option type="QString" value="3x:0,0,0,0,0,0" name="trim_distance_end_map_unit_scale"/>
            <Option type="QString" value="MM" name="trim_distance_end_unit"/>
            <Option type="QString" value="0" name="trim_distance_start"/>
            <Option type="QString" value="3x:0,0,0,0,0,0" name="trim_distance_start_map_unit_scale"/>
            <Option type="QString" value="MM" name="trim_distance_start_unit"/>
            <Option type="QString" value="0" name="tweak_dash_pattern_on_corners"/>
            <Option type="QString" value="0" name="use_custom_dash"/>
            <Option type="QString" value="3x:0,0,0,0,0,0" name="width_map_unit_scale"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </profileLineSymbol>
    <profileFillSymbol>
      <symbol type="fill" clip_to_extent="1" is_animated="0" name="" alpha="1" force_rhr="0" frame_rate="10">
        <data_defined_properties>
          <Option type="Map">
            <Option type="QString" value="" name="name"/>
            <Option name="properties"/>
            <Option type="QString" value="collection" name="type"/>
          </Option>
        </data_defined_properties>
        <layer pass="0" locked="0" enabled="1" class="SimpleFill">
          <Option type="Map">
            <Option type="QString" value="3x:0,0,0,0,0,0" name="border_width_map_unit_scale"/>
            <Option type="QString" value="255,158,23,255" name="color"/>
            <Option type="QString" value="bevel" name="joinstyle"/>
            <Option type="QString" value="0,0" name="offset"/>
            <Option type="QString" value="3x:0,0,0,0,0,0" name="offset_map_unit_scale"/>
            <Option type="QString" value="MM" name="offset_unit"/>
            <Option type="QString" value="35,35,35,255" name="outline_color"/>
            <Option type="QString" value="no" name="outline_style"/>
            <Option type="QString" value="0.26" name="outline_width"/>
            <Option type="QString" value="MM" name="outline_width_unit"/>
            <Option type="QString" value="solid" name="style"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </profileFillSymbol>
  </elevation>
  <customproperties>
    <Option type="Map">
      <Option type="QString" value="false" name="WMSBackgroundLayer"/>
      <Option type="QString" value="false" name="WMSPublishDataSourceUrl"/>
      <Option type="QString" value="0" name="embeddedWidgets/count"/>
      <Option type="QString" value="Value" name="identify/format"/>
    </Option>
  </customproperties>
  <pipe-data-defined-properties>
    <Option type="Map">
      <Option type="QString" value="" name="name"/>
      <Option name="properties"/>
      <Option type="QString" value="collection" name="type"/>
    </Option>
  </pipe-data-defined-properties>
  <pipe>
    <provider>
      <resampling zoomedOutResamplingMethod="nearestNeighbour" zoomedInResamplingMethod="nearestNeighbour" enabled="false" maxOversampling="2"/>
    </provider>
    <rasterrenderer type="singlebandpseudocolor" band="1" nodataColor="" classificationMax="67.514496420723" opacity="1" classificationMin="-6.7646300744401" alphaBand="-1">
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
        <colorrampshader clip="0" classificationMode="2" labelPrecision="1" colorRampType="INTERPOLATED" minimumValue="-6.7646300744400998" maximumValue="67.514496420723006">
          <colorramp type="gradient" name="[source]">
            <Option type="Map">
              <Option type="QString" value="68,1,84,255" name="color1"/>
              <Option type="QString" value="253,231,37,255" name="color2"/>
              <Option type="QString" value="ccw" name="direction"/>
              <Option type="QString" value="0" name="discrete"/>
              <Option type="QString" value="gradient" name="rampType"/>
              <Option type="QString" value="rgb" name="spec"/>
              <Option type="QString" value="0.0196078;70,8,92,255;rgb;ccw:0.0392157;71,16,99,255;rgb;ccw:0.0588235;72,23,105,255;rgb;ccw:0.0784314;72,29,111,255;rgb;ccw:0.0980392;72,36,117,255;rgb;ccw:0.117647;71,42,122,255;rgb;ccw:0.137255;70,48,126,255;rgb;ccw:0.156863;69,55,129,255;rgb;ccw:0.176471;67,61,132,255;rgb;ccw:0.196078;65,66,135,255;rgb;ccw:0.215686;63,72,137,255;rgb;ccw:0.235294;61,78,138,255;rgb;ccw:0.254902;58,83,139,255;rgb;ccw:0.27451;56,89,140,255;rgb;ccw:0.294118;53,94,141,255;rgb;ccw:0.313725;51,99,141,255;rgb;ccw:0.333333;49,104,142,255;rgb;ccw:0.352941;46,109,142,255;rgb;ccw:0.372549;44,113,142,255;rgb;ccw:0.392157;42,118,142,255;rgb;ccw:0.411765;41,123,142,255;rgb;ccw:0.431373;39,128,142,255;rgb;ccw:0.45098;37,132,142,255;rgb;ccw:0.470588;35,137,142,255;rgb;ccw:0.490196;33,142,141,255;rgb;ccw:0.509804;32,146,140,255;rgb;ccw:0.529412;31,151,139,255;rgb;ccw:0.54902;30,156,137,255;rgb;ccw:0.568627;31,161,136,255;rgb;ccw:0.588235;33,165,133,255;rgb;ccw:0.607843;36,170,131,255;rgb;ccw:0.627451;40,174,128,255;rgb;ccw:0.647059;46,179,124,255;rgb;ccw:0.666667;53,183,121,255;rgb;ccw:0.686275;61,188,116,255;rgb;ccw:0.705882;70,192,111,255;rgb;ccw:0.72549;80,196,106,255;rgb;ccw:0.745098;90,200,100,255;rgb;ccw:0.764706;101,203,94,255;rgb;ccw:0.784314;112,207,87,255;rgb;ccw:0.803922;124,210,80,255;rgb;ccw:0.823529;137,213,72,255;rgb;ccw:0.843137;149,216,64,255;rgb;ccw:0.862745;162,218,55,255;rgb;ccw:0.882353;176,221,47,255;rgb;ccw:0.901961;189,223,38,255;rgb;ccw:0.921569;202,225,31,255;rgb;ccw:0.941176;216,226,25,255;rgb;ccw:0.960784;229,228,25,255;rgb;ccw:0.980392;241,229,29,255;rgb;ccw" name="stops"/>
            </Option>
          </colorramp>
          <item label="-6.8 m" value="-6.7646300744401" color="#440154" alpha="255"/>
          <item label="0.7 m" value="0.663282575076211" color="#482576" alpha="255"/>
          <item label="8.1 m" value="8.091195224592521" color="#414387" alpha="255"/>
          <item label="15.5 m" value="15.519107874108833" color="#345f8d" alpha="255"/>
          <item label="22.9 m" value="22.947020523625145" color="#2a788e" alpha="255"/>
          <item label="30.4 m" value="30.374933173141457" color="#21908d" alpha="255"/>
          <item label="37.8 m" value="37.802845822657765" color="#23a884" alpha="255"/>
          <item label="45.2 m" value="45.23075847217408" color="#43bf70" alpha="255"/>
          <item label="52.7 m" value="52.65867112169039" color="#7ad151" alpha="255"/>
          <item label="60.1 m" value="60.0865837712067" color="#bcdf27" alpha="255"/>
          <item label="67.5 m" value="67.514496420723" color="#fde725" alpha="255"/>
          <rampLegendSettings useContinuousLegend="1" minimumLabel="" direction="0" maximumLabel="" suffix=" m" orientation="1" prefix="">
            <numericFormat id="basic">
              <Option type="Map">
                <Option type="invalid" name="decimal_separator"/>
                <Option type="int" value="1" name="decimals"/>
                <Option type="int" value="0" name="rounding_type"/>
                <Option type="bool" value="false" name="show_plus"/>
                <Option type="bool" value="true" name="show_thousand_separator"/>
                <Option type="bool" value="false" name="show_trailing_zeros"/>
                <Option type="invalid" name="thousand_separator"/>
              </Option>
            </numericFormat>
          </rampLegendSettings>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0" gamma="1"/>
    <huesaturation grayscaleMode="0" colorizeStrength="100" colorizeGreen="128" colorizeBlue="128" colorizeOn="0" invertColors="0" colorizeRed="255" saturation="0"/>
    <rasterresampler maxOversampling="2"/>
    <resamplingStage>resamplingFilter</resamplingStage>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

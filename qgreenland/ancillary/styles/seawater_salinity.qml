<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="1e+08" version="3.28.8-Firenze" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" maxScale="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
    <Private>0</Private>
  </flags>
  <temporal fetchMode="0" enabled="0" mode="0">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <elevation symbology="Line" enabled="0" zoffset="0" zscale="1" band="1">
    <data-defined-properties>
      <Option type="Map">
        <Option name="name" value="" type="QString"/>
        <Option name="properties"/>
        <Option name="type" value="collection" type="QString"/>
      </Option>
    </data-defined-properties>
    <profileLineSymbol>
      <symbol name="" force_rhr="0" alpha="1" clip_to_extent="1" frame_rate="10" type="line" is_animated="0">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" value="" type="QString"/>
            <Option name="properties"/>
            <Option name="type" value="collection" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" pass="0" class="SimpleLine" enabled="1">
          <Option type="Map">
            <Option name="align_dash_pattern" value="0" type="QString"/>
            <Option name="capstyle" value="square" type="QString"/>
            <Option name="customdash" value="5;2" type="QString"/>
            <Option name="customdash_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="customdash_unit" value="MM" type="QString"/>
            <Option name="dash_pattern_offset" value="0" type="QString"/>
            <Option name="dash_pattern_offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="dash_pattern_offset_unit" value="MM" type="QString"/>
            <Option name="draw_inside_polygon" value="0" type="QString"/>
            <Option name="joinstyle" value="bevel" type="QString"/>
            <Option name="line_color" value="231,113,72,255" type="QString"/>
            <Option name="line_style" value="solid" type="QString"/>
            <Option name="line_width" value="0.6" type="QString"/>
            <Option name="line_width_unit" value="MM" type="QString"/>
            <Option name="offset" value="0" type="QString"/>
            <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="offset_unit" value="MM" type="QString"/>
            <Option name="ring_filter" value="0" type="QString"/>
            <Option name="trim_distance_end" value="0" type="QString"/>
            <Option name="trim_distance_end_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="trim_distance_end_unit" value="MM" type="QString"/>
            <Option name="trim_distance_start" value="0" type="QString"/>
            <Option name="trim_distance_start_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="trim_distance_start_unit" value="MM" type="QString"/>
            <Option name="tweak_dash_pattern_on_corners" value="0" type="QString"/>
            <Option name="use_custom_dash" value="0" type="QString"/>
            <Option name="width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </profileLineSymbol>
    <profileFillSymbol>
      <symbol name="" force_rhr="0" alpha="1" clip_to_extent="1" frame_rate="10" type="fill" is_animated="0">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" value="" type="QString"/>
            <Option name="properties"/>
            <Option name="type" value="collection" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" pass="0" class="SimpleFill" enabled="1">
          <Option type="Map">
            <Option name="border_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="color" value="231,113,72,255" type="QString"/>
            <Option name="joinstyle" value="bevel" type="QString"/>
            <Option name="offset" value="0,0" type="QString"/>
            <Option name="offset_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="offset_unit" value="MM" type="QString"/>
            <Option name="outline_color" value="35,35,35,255" type="QString"/>
            <Option name="outline_style" value="no" type="QString"/>
            <Option name="outline_width" value="0.26" type="QString"/>
            <Option name="outline_width_unit" value="MM" type="QString"/>
            <Option name="style" value="solid" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </profileFillSymbol>
  </elevation>
  <customproperties>
    <Option type="Map">
      <Option name="WMSBackgroundLayer" value="false" type="QString"/>
      <Option name="WMSPublishDataSourceUrl" value="false" type="QString"/>
      <Option name="embeddedWidgets/count" value="0" type="QString"/>
      <Option name="identify/format" value="Value" type="QString"/>
    </Option>
  </customproperties>
  <pipe-data-defined-properties>
    <Option type="Map">
      <Option name="name" value="" type="QString"/>
      <Option name="properties"/>
      <Option name="type" value="collection" type="QString"/>
    </Option>
  </pipe-data-defined-properties>
  <pipe>
    <provider>
      <resampling zoomedOutResamplingMethod="nearestNeighbour" zoomedInResamplingMethod="nearestNeighbour" maxOversampling="2" enabled="false"/>
    </provider>
    <rasterrenderer classificationMax="39" classificationMin="5" nodataColor="" opacity="1" alphaBand="-1" type="singlebandpseudocolor" band="1">
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
        <colorrampshader classificationMode="1" minimumValue="5" labelPrecision="4" maximumValue="39" colorRampType="INTERPOLATED" clip="0">
          <colorramp name="[source]" type="gradient">
            <Option type="Map">
              <Option name="color1" value="68,1,84,255" type="QString"/>
              <Option name="color2" value="253,231,37,255" type="QString"/>
              <Option name="direction" value="ccw" type="QString"/>
              <Option name="discrete" value="0" type="QString"/>
              <Option name="rampType" value="gradient" type="QString"/>
              <Option name="spec" value="rgb" type="QString"/>
              <Option name="stops" value="0.0196078;70,8,92,255;rgb;ccw:0.0392157;71,16,99,255;rgb;ccw:0.0588235;72,23,105,255;rgb;ccw:0.0784314;72,29,111,255;rgb;ccw:0.0980392;72,36,117,255;rgb;ccw:0.117647;71,42,122,255;rgb;ccw:0.137255;70,48,126,255;rgb;ccw:0.156863;69,55,129,255;rgb;ccw:0.176471;67,61,132,255;rgb;ccw:0.196078;65,66,135,255;rgb;ccw:0.215686;63,72,137,255;rgb;ccw:0.235294;61,78,138,255;rgb;ccw:0.254902;58,83,139,255;rgb;ccw:0.27451;56,89,140,255;rgb;ccw:0.294118;53,94,141,255;rgb;ccw:0.313725;51,99,141,255;rgb;ccw:0.333333;49,104,142,255;rgb;ccw:0.352941;46,109,142,255;rgb;ccw:0.372549;44,113,142,255;rgb;ccw:0.392157;42,118,142,255;rgb;ccw:0.411765;41,123,142,255;rgb;ccw:0.431373;39,128,142,255;rgb;ccw:0.45098;37,132,142,255;rgb;ccw:0.470588;35,137,142,255;rgb;ccw:0.490196;33,142,141,255;rgb;ccw:0.509804;32,146,140,255;rgb;ccw:0.529412;31,151,139,255;rgb;ccw:0.54902;30,156,137,255;rgb;ccw:0.568627;31,161,136,255;rgb;ccw:0.588235;33,165,133,255;rgb;ccw:0.607843;36,170,131,255;rgb;ccw:0.627451;40,174,128,255;rgb;ccw:0.647059;46,179,124,255;rgb;ccw:0.666667;53,183,121,255;rgb;ccw:0.686275;61,188,116,255;rgb;ccw:0.705882;70,192,111,255;rgb;ccw:0.72549;80,196,106,255;rgb;ccw:0.745098;90,200,100,255;rgb;ccw:0.764706;101,203,94,255;rgb;ccw:0.784314;112,207,87,255;rgb;ccw:0.803922;124,210,80,255;rgb;ccw:0.823529;137,213,72,255;rgb;ccw:0.843137;149,216,64,255;rgb;ccw:0.862745;162,218,55,255;rgb;ccw:0.882353;176,221,47,255;rgb;ccw:0.901961;189,223,38,255;rgb;ccw:0.921569;202,225,31,255;rgb;ccw:0.941176;216,226,25,255;rgb;ccw:0.960784;229,228,25,255;rgb;ccw:0.980392;241,229,29,255;rgb;ccw" type="QString"/>
            </Option>
          </colorramp>
          <item label="5.0000" value="5" alpha="255" color="#440154"/>
          <item label="5.6667" value="5.6666652" alpha="255" color="#46085c"/>
          <item label="6.3333" value="6.3333338" alpha="255" color="#471063"/>
          <item label="7.0000" value="6.999999" alpha="255" color="#481769"/>
          <item label="7.6667" value="7.6666676" alpha="255" color="#481d6f"/>
          <item label="8.3333" value="8.3333328" alpha="255" color="#482475"/>
          <item label="9.0000" value="8.999998" alpha="255" color="#472a7a"/>
          <item label="9.6667" value="9.66667" alpha="255" color="#46307e"/>
          <item label="10.3333" value="10.333342" alpha="255" color="#453781"/>
          <item label="11.0000" value="11.000014" alpha="255" color="#433d84"/>
          <item label="11.6667" value="11.666652" alpha="255" color="#414287"/>
          <item label="12.3333" value="12.333324" alpha="255" color="#3f4889"/>
          <item label="13.0000" value="12.999996" alpha="255" color="#3d4e8a"/>
          <item label="13.6667" value="13.666668000000001" alpha="255" color="#3a538b"/>
          <item label="14.3333" value="14.33334" alpha="255" color="#38598c"/>
          <item label="15.0000" value="15.000012" alpha="255" color="#355e8d"/>
          <item label="15.6666" value="15.666649999999999" alpha="255" color="#33638d"/>
          <item label="16.3333" value="16.333322" alpha="255" color="#31688e"/>
          <item label="17.0000" value="16.999994" alpha="255" color="#2e6d8e"/>
          <item label="17.6667" value="17.666666" alpha="255" color="#2c718e"/>
          <item label="18.3333" value="18.333337999999998" alpha="255" color="#2a768e"/>
          <item label="19.0000" value="19.00001" alpha="255" color="#297b8e"/>
          <item label="19.6667" value="19.666682" alpha="255" color="#27808e"/>
          <item label="20.3333" value="20.33332" alpha="255" color="#25848e"/>
          <item label="21.0000" value="20.999992" alpha="255" color="#23898e"/>
          <item label="21.6667" value="21.666664" alpha="255" color="#218e8d"/>
          <item label="22.3333" value="22.333336000000003" alpha="255" color="#20928c"/>
          <item label="23.0000" value="23.000008" alpha="255" color="#1f978b"/>
          <item label="23.6667" value="23.66668" alpha="255" color="#1e9c89"/>
          <item label="24.3333" value="24.333318" alpha="255" color="#1fa188"/>
          <item label="25.0000" value="24.999989999999997" alpha="255" color="#21a585"/>
          <item label="25.6667" value="25.666662000000002" alpha="255" color="#24aa83"/>
          <item label="26.3333" value="26.333334" alpha="255" color="#28ae80"/>
          <item label="27.0000" value="27.000006000000003" alpha="255" color="#2eb37c"/>
          <item label="27.6667" value="27.666678" alpha="255" color="#35b779"/>
          <item label="28.3333" value="28.33335" alpha="255" color="#3dbc74"/>
          <item label="29.0000" value="28.999988000000002" alpha="255" color="#46c06f"/>
          <item label="29.6667" value="29.66666" alpha="255" color="#50c46a"/>
          <item label="30.3333" value="30.333332000000002" alpha="255" color="#5ac864"/>
          <item label="31.0000" value="31.000004" alpha="255" color="#65cb5e"/>
          <item label="31.6667" value="31.666676" alpha="255" color="#70cf57"/>
          <item label="32.3333" value="32.333348" alpha="255" color="#7cd250"/>
          <item label="33.0000" value="32.999986" alpha="255" color="#89d548"/>
          <item label="33.6667" value="33.666658" alpha="255" color="#95d840"/>
          <item label="34.3333" value="34.333330000000004" alpha="255" color="#a2da37"/>
          <item label="35.0000" value="35.000002" alpha="255" color="#b0dd2f"/>
          <item label="35.6667" value="35.666674" alpha="255" color="#bddf26"/>
          <item label="36.3333" value="36.333346" alpha="255" color="#cae11f"/>
          <item label="37.0000" value="36.999984" alpha="255" color="#d8e219"/>
          <item label="37.6667" value="37.666655999999996" alpha="255" color="#e5e419"/>
          <item label="38.3333" value="38.333328" alpha="255" color="#f1e51d"/>
          <item label="39.0000" value="39" alpha="255" color="#fde725"/>
          <rampLegendSettings minimumLabel="" orientation="1" maximumLabel="" useContinuousLegend="1" direction="0" prefix="" suffix=" PSS">
            <numericFormat id="basic">
              <Option type="Map">
                <Option name="decimal_separator" type="invalid"/>
                <Option name="decimals" value="1" type="int"/>
                <Option name="rounding_type" value="0" type="int"/>
                <Option name="show_plus" value="false" type="bool"/>
                <Option name="show_thousand_separator" value="true" type="bool"/>
                <Option name="show_trailing_zeros" value="false" type="bool"/>
                <Option name="thousand_separator" type="invalid"/>
              </Option>
            </numericFormat>
          </rampLegendSettings>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast contrast="0" gamma="1" brightness="0"/>
    <huesaturation grayscaleMode="0" colorizeGreen="128" colorizeBlue="128" saturation="0" invertColors="0" colorizeStrength="100" colorizeOn="0" colorizeRed="255"/>
    <rasterresampler maxOversampling="2"/>
    <resamplingStage>resamplingFilter</resamplingStage>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

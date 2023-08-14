<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis hasScaleBasedVisibilityFlag="0" styleCategories="AllStyleCategories" minScale="1e+08" maxScale="0" version="3.28.6-Firenze">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
    <Private>0</Private>
  </flags>
  <temporal enabled="0" mode="0" fetchMode="0">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <elevation zoffset="0" zscale="1" band="1" enabled="0" symbology="Line">
    <data-defined-properties>
      <Option type="Map">
        <Option type="QString" name="name" value=""/>
        <Option name="properties"/>
        <Option type="QString" name="type" value="collection"/>
      </Option>
    </data-defined-properties>
    <profileLineSymbol>
      <symbol type="line" alpha="1" frame_rate="10" is_animated="0" force_rhr="0" clip_to_extent="1" name="">
        <data_defined_properties>
          <Option type="Map">
            <Option type="QString" name="name" value=""/>
            <Option name="properties"/>
            <Option type="QString" name="type" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer pass="0" locked="0" class="SimpleLine" enabled="1">
          <Option type="Map">
            <Option type="QString" name="align_dash_pattern" value="0"/>
            <Option type="QString" name="capstyle" value="square"/>
            <Option type="QString" name="customdash" value="5;2"/>
            <Option type="QString" name="customdash_map_unit_scale" value="3x:0,0,0,0,0,0"/>
            <Option type="QString" name="customdash_unit" value="MM"/>
            <Option type="QString" name="dash_pattern_offset" value="0"/>
            <Option type="QString" name="dash_pattern_offset_map_unit_scale" value="3x:0,0,0,0,0,0"/>
            <Option type="QString" name="dash_pattern_offset_unit" value="MM"/>
            <Option type="QString" name="draw_inside_polygon" value="0"/>
            <Option type="QString" name="joinstyle" value="bevel"/>
            <Option type="QString" name="line_color" value="255,158,23,255"/>
            <Option type="QString" name="line_style" value="solid"/>
            <Option type="QString" name="line_width" value="0.6"/>
            <Option type="QString" name="line_width_unit" value="MM"/>
            <Option type="QString" name="offset" value="0"/>
            <Option type="QString" name="offset_map_unit_scale" value="3x:0,0,0,0,0,0"/>
            <Option type="QString" name="offset_unit" value="MM"/>
            <Option type="QString" name="ring_filter" value="0"/>
            <Option type="QString" name="trim_distance_end" value="0"/>
            <Option type="QString" name="trim_distance_end_map_unit_scale" value="3x:0,0,0,0,0,0"/>
            <Option type="QString" name="trim_distance_end_unit" value="MM"/>
            <Option type="QString" name="trim_distance_start" value="0"/>
            <Option type="QString" name="trim_distance_start_map_unit_scale" value="3x:0,0,0,0,0,0"/>
            <Option type="QString" name="trim_distance_start_unit" value="MM"/>
            <Option type="QString" name="tweak_dash_pattern_on_corners" value="0"/>
            <Option type="QString" name="use_custom_dash" value="0"/>
            <Option type="QString" name="width_map_unit_scale" value="3x:0,0,0,0,0,0"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </profileLineSymbol>
    <profileFillSymbol>
      <symbol type="fill" alpha="1" frame_rate="10" is_animated="0" force_rhr="0" clip_to_extent="1" name="">
        <data_defined_properties>
          <Option type="Map">
            <Option type="QString" name="name" value=""/>
            <Option name="properties"/>
            <Option type="QString" name="type" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer pass="0" locked="0" class="SimpleFill" enabled="1">
          <Option type="Map">
            <Option type="QString" name="border_width_map_unit_scale" value="3x:0,0,0,0,0,0"/>
            <Option type="QString" name="color" value="255,158,23,255"/>
            <Option type="QString" name="joinstyle" value="bevel"/>
            <Option type="QString" name="offset" value="0,0"/>
            <Option type="QString" name="offset_map_unit_scale" value="3x:0,0,0,0,0,0"/>
            <Option type="QString" name="offset_unit" value="MM"/>
            <Option type="QString" name="outline_color" value="35,35,35,255"/>
            <Option type="QString" name="outline_style" value="no"/>
            <Option type="QString" name="outline_width" value="0.26"/>
            <Option type="QString" name="outline_width_unit" value="MM"/>
            <Option type="QString" name="style" value="solid"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </profileFillSymbol>
  </elevation>
  <customproperties>
    <Option type="Map">
      <Option type="QString" name="WMSBackgroundLayer" value="false"/>
      <Option type="QString" name="WMSPublishDataSourceUrl" value="false"/>
      <Option type="QString" name="embeddedWidgets/count" value="0"/>
      <Option type="QString" name="identify/format" value="Value"/>
    </Option>
  </customproperties>
  <pipe-data-defined-properties>
    <Option type="Map">
      <Option type="QString" name="name" value=""/>
      <Option name="properties"/>
      <Option type="QString" name="type" value="collection"/>
    </Option>
  </pipe-data-defined-properties>
  <pipe>
    <provider>
      <resampling enabled="false" zoomedOutResamplingMethod="nearestNeighbour" zoomedInResamplingMethod="nearestNeighbour" maxOversampling="2"/>
    </provider>
    <rasterrenderer classificationMax="500" type="singlebandpseudocolor" nodataColor="" band="1" opacity="1" alphaBand="-1" classificationMin="0">
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
        <colorrampshader colorRampType="INTERPOLATED" classificationMode="1" labelPrecision="3" maximumValue="500" clip="0" minimumValue="0">
          <colorramp type="gradient" name="[source]">
            <Option type="Map">
              <Option type="QString" name="color1" value="68,1,84,255"/>
              <Option type="QString" name="color2" value="253,231,37,255"/>
              <Option type="QString" name="direction" value="ccw"/>
              <Option type="QString" name="discrete" value="0"/>
              <Option type="QString" name="rampType" value="gradient"/>
              <Option type="QString" name="spec" value="rgb"/>
              <Option type="QString" name="stops" value="0.0196078;70,8,92,255;rgb;ccw:0.0392157;71,16,99,255;rgb;ccw:0.0588235;72,23,105,255;rgb;ccw:0.0784314;72,29,111,255;rgb;ccw:0.0980392;72,36,117,255;rgb;ccw:0.117647;71,42,122,255;rgb;ccw:0.137255;70,48,126,255;rgb;ccw:0.156863;69,55,129,255;rgb;ccw:0.176471;67,61,132,255;rgb;ccw:0.196078;65,66,135,255;rgb;ccw:0.215686;63,72,137,255;rgb;ccw:0.235294;61,78,138,255;rgb;ccw:0.254902;58,83,139,255;rgb;ccw:0.27451;56,89,140,255;rgb;ccw:0.294118;53,94,141,255;rgb;ccw:0.313725;51,99,141,255;rgb;ccw:0.333333;49,104,142,255;rgb;ccw:0.352941;46,109,142,255;rgb;ccw:0.372549;44,113,142,255;rgb;ccw:0.392157;42,118,142,255;rgb;ccw:0.411765;41,123,142,255;rgb;ccw:0.431373;39,128,142,255;rgb;ccw:0.45098;37,132,142,255;rgb;ccw:0.470588;35,137,142,255;rgb;ccw:0.490196;33,142,141,255;rgb;ccw:0.509804;32,146,140,255;rgb;ccw:0.529412;31,151,139,255;rgb;ccw:0.54902;30,156,137,255;rgb;ccw:0.568627;31,161,136,255;rgb;ccw:0.588235;33,165,133,255;rgb;ccw:0.607843;36,170,131,255;rgb;ccw:0.627451;40,174,128,255;rgb;ccw:0.647059;46,179,124,255;rgb;ccw:0.666667;53,183,121,255;rgb;ccw:0.686275;61,188,116,255;rgb;ccw:0.705882;70,192,111,255;rgb;ccw:0.72549;80,196,106,255;rgb;ccw:0.745098;90,200,100,255;rgb;ccw:0.764706;101,203,94,255;rgb;ccw:0.784314;112,207,87,255;rgb;ccw:0.803922;124,210,80,255;rgb;ccw:0.823529;137,213,72,255;rgb;ccw:0.843137;149,216,64,255;rgb;ccw:0.862745;162,218,55,255;rgb;ccw:0.882353;176,221,47,255;rgb;ccw:0.901961;189,223,38,255;rgb;ccw:0.921569;202,225,31,255;rgb;ccw:0.941176;216,226,25,255;rgb;ccw:0.960784;229,228,25,255;rgb;ccw:0.980392;241,229,29,255;rgb;ccw"/>
            </Option>
          </colorramp>
          <item color="#440154" label="0.000 m/y" alpha="255" value="0"/>
          <item color="#46085c" label="9.804 m/y" alpha="255" value="9.8039"/>
          <item color="#471063" label="19.608 m/y" alpha="255" value="19.60785"/>
          <item color="#481769" label="29.412 m/y" alpha="255" value="29.41175"/>
          <item color="#481d6f" label="39.216 m/y" alpha="255" value="39.2157"/>
          <item color="#482475" label="49.020 m/y" alpha="255" value="49.019600000000004"/>
          <item color="#472a7a" label="58.824 m/y" alpha="255" value="58.8235"/>
          <item color="#46307e" label="68.627 m/y" alpha="255" value="68.6275"/>
          <item color="#453781" label="78.431 m/y" alpha="255" value="78.4315"/>
          <item color="#433d84" label="88.235 m/y" alpha="255" value="88.23549999999999"/>
          <item color="#414287" label="98.039 m/y" alpha="255" value="98.039"/>
          <item color="#3f4889" label="107.843 m/y" alpha="255" value="107.84299999999999"/>
          <item color="#3d4e8a" label="117.647 m/y" alpha="255" value="117.647"/>
          <item color="#3a538b" label="127.451 m/y" alpha="255" value="127.45100000000001"/>
          <item color="#38598c" label="137.255 m/y" alpha="255" value="137.255"/>
          <item color="#355e8d" label="147.059 m/y" alpha="255" value="147.059"/>
          <item color="#33638d" label="156.862 m/y" alpha="255" value="156.86249999999998"/>
          <item color="#31688e" label="166.666 m/y" alpha="255" value="166.66649999999998"/>
          <item color="#2e6d8e" label="176.471 m/y" alpha="255" value="176.47050000000002"/>
          <item color="#2c718e" label="186.275 m/y" alpha="255" value="186.27450000000002"/>
          <item color="#2a768e" label="196.078 m/y" alpha="255" value="196.0785"/>
          <item color="#297b8e" label="205.882 m/y" alpha="255" value="205.8825"/>
          <item color="#27808e" label="215.686 m/y" alpha="255" value="215.6865"/>
          <item color="#25848e" label="225.490 m/y" alpha="255" value="225.49"/>
          <item color="#23898e" label="235.294 m/y" alpha="255" value="235.294"/>
          <item color="#218e8d" label="245.098 m/y" alpha="255" value="245.098"/>
          <item color="#20928c" label="254.902 m/y" alpha="255" value="254.90200000000002"/>
          <item color="#1f978b" label="264.706 m/y" alpha="255" value="264.706"/>
          <item color="#1e9c89" label="274.510 m/y" alpha="255" value="274.51"/>
          <item color="#1fa188" label="284.313 m/y" alpha="255" value="284.3135"/>
          <item color="#21a585" label="294.117 m/y" alpha="255" value="294.11749999999995"/>
          <item color="#24aa83" label="303.922 m/y" alpha="255" value="303.92150000000004"/>
          <item color="#28ae80" label="313.726 m/y" alpha="255" value="313.7255"/>
          <item color="#2eb37c" label="323.530 m/y" alpha="255" value="323.52950000000004"/>
          <item color="#35b779" label="333.334 m/y" alpha="255" value="333.3335"/>
          <item color="#3dbc74" label="343.137 m/y" alpha="255" value="343.1375"/>
          <item color="#46c06f" label="352.941 m/y" alpha="255" value="352.94100000000003"/>
          <item color="#50c46a" label="362.745 m/y" alpha="255" value="362.745"/>
          <item color="#5ac864" label="372.549 m/y" alpha="255" value="372.54900000000004"/>
          <item color="#65cb5e" label="382.353 m/y" alpha="255" value="382.353"/>
          <item color="#70cf57" label="392.157 m/y" alpha="255" value="392.157"/>
          <item color="#7cd250" label="401.961 m/y" alpha="255" value="401.961"/>
          <item color="#89d548" label="411.764 m/y" alpha="255" value="411.7645"/>
          <item color="#95d840" label="421.569 m/y" alpha="255" value="421.56850000000003"/>
          <item color="#a2da37" label="431.373 m/y" alpha="255" value="431.3725"/>
          <item color="#b0dd2f" label="441.177 m/y" alpha="255" value="441.17650000000003"/>
          <item color="#bddf26" label="450.981 m/y" alpha="255" value="450.9805"/>
          <item color="#cae11f" label="460.784 m/y" alpha="255" value="460.7845"/>
          <item color="#d8e219" label="470.588 m/y" alpha="255" value="470.588"/>
          <item color="#e5e419" label="480.392 m/y" alpha="255" value="480.392"/>
          <item color="#f1e51d" label="490.196 m/y" alpha="255" value="490.196"/>
          <item color="#fde725" label="500.000 m/y" alpha="255" value="500"/>
          <rampLegendSettings direction="0" orientation="1" useContinuousLegend="1" suffix=" m/y" minimumLabel="" maximumLabel="" prefix="">
            <numericFormat id="basic">
              <Option type="Map">
                <Option type="invalid" name="decimal_separator"/>
                <Option type="int" name="decimals" value="6"/>
                <Option type="int" name="rounding_type" value="0"/>
                <Option type="bool" name="show_plus" value="false"/>
                <Option type="bool" name="show_thousand_separator" value="true"/>
                <Option type="bool" name="show_trailing_zeros" value="false"/>
                <Option type="invalid" name="thousand_separator"/>
              </Option>
            </numericFormat>
          </rampLegendSettings>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast gamma="1" brightness="0" contrast="0"/>
    <huesaturation colorizeBlue="128" grayscaleMode="0" invertColors="0" colorizeRed="255" colorizeGreen="128" colorizeStrength="100" saturation="0" colorizeOn="0"/>
    <rasterresampler maxOversampling="2"/>
    <resamplingStage>resamplingFilter</resamplingStage>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

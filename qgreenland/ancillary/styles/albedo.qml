<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis hasScaleBasedVisibilityFlag="0" maxScale="0" version="3.28.7-Firenze" minScale="1e+08" styleCategories="AllStyleCategories">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
    <Private>0</Private>
  </flags>
  <temporal mode="0" fetchMode="0" enabled="0">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <elevation enabled="0" zoffset="0" band="1" zscale="1" symbology="Line">
    <data-defined-properties>
      <Option type="Map">
        <Option name="name" type="QString" value=""/>
        <Option name="properties"/>
        <Option name="type" type="QString" value="collection"/>
      </Option>
    </data-defined-properties>
    <profileLineSymbol>
      <symbol is_animated="0" frame_rate="10" name="" force_rhr="0" type="line" alpha="1" clip_to_extent="1">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer pass="0" class="SimpleLine" enabled="1" locked="0">
          <Option type="Map">
            <Option name="align_dash_pattern" type="QString" value="0"/>
            <Option name="capstyle" type="QString" value="square"/>
            <Option name="customdash" type="QString" value="5;2"/>
            <Option name="customdash_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="customdash_unit" type="QString" value="MM"/>
            <Option name="dash_pattern_offset" type="QString" value="0"/>
            <Option name="dash_pattern_offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="dash_pattern_offset_unit" type="QString" value="MM"/>
            <Option name="draw_inside_polygon" type="QString" value="0"/>
            <Option name="joinstyle" type="QString" value="bevel"/>
            <Option name="line_color" type="QString" value="231,113,72,255"/>
            <Option name="line_style" type="QString" value="solid"/>
            <Option name="line_width" type="QString" value="0.6"/>
            <Option name="line_width_unit" type="QString" value="MM"/>
            <Option name="offset" type="QString" value="0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="ring_filter" type="QString" value="0"/>
            <Option name="trim_distance_end" type="QString" value="0"/>
            <Option name="trim_distance_end_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="trim_distance_end_unit" type="QString" value="MM"/>
            <Option name="trim_distance_start" type="QString" value="0"/>
            <Option name="trim_distance_start_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="trim_distance_start_unit" type="QString" value="MM"/>
            <Option name="tweak_dash_pattern_on_corners" type="QString" value="0"/>
            <Option name="use_custom_dash" type="QString" value="0"/>
            <Option name="width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </profileLineSymbol>
    <profileFillSymbol>
      <symbol is_animated="0" frame_rate="10" name="" force_rhr="0" type="fill" alpha="1" clip_to_extent="1">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer pass="0" class="SimpleFill" enabled="1" locked="0">
          <Option type="Map">
            <Option name="border_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="color" type="QString" value="231,113,72,255"/>
            <Option name="joinstyle" type="QString" value="bevel"/>
            <Option name="offset" type="QString" value="0,0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="outline_color" type="QString" value="35,35,35,255"/>
            <Option name="outline_style" type="QString" value="no"/>
            <Option name="outline_width" type="QString" value="0.26"/>
            <Option name="outline_width_unit" type="QString" value="MM"/>
            <Option name="style" type="QString" value="solid"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </profileFillSymbol>
  </elevation>
  <customproperties>
    <Option type="Map">
      <Option name="WMSBackgroundLayer" type="QString" value="false"/>
      <Option name="WMSPublishDataSourceUrl" type="QString" value="false"/>
      <Option name="embeddedWidgets/count" type="QString" value="0"/>
      <Option name="identify/format" type="QString" value="Value"/>
    </Option>
  </customproperties>
  <pipe-data-defined-properties>
    <Option type="Map">
      <Option name="name" type="QString" value=""/>
      <Option name="properties"/>
      <Option name="type" type="QString" value="collection"/>
    </Option>
  </pipe-data-defined-properties>
  <pipe>
    <provider>
      <resampling zoomedInResamplingMethod="nearestNeighbour" zoomedOutResamplingMethod="nearestNeighbour" enabled="false" maxOversampling="2"/>
    </provider>
    <rasterrenderer alphaBand="-1" nodataColor="" opacity="1" type="singlebandpseudocolor" band="1" classificationMin="0" classificationMax="0.8799497">
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
        <colorrampshader minimumValue="0" labelPrecision="4" colorRampType="INTERPOLATED" classificationMode="2" maximumValue="0.87994969999999995" clip="0">
          <colorramp name="[source]" type="gradient">
            <Option type="Map">
              <Option name="color1" type="QString" value="68,1,84,255"/>
              <Option name="color2" type="QString" value="253,231,37,255"/>
              <Option name="direction" type="QString" value="ccw"/>
              <Option name="discrete" type="QString" value="0"/>
              <Option name="rampType" type="QString" value="gradient"/>
              <Option name="spec" type="QString" value="rgb"/>
              <Option name="stops" type="QString" value="0.0196078;70,8,92,255;rgb;ccw:0.0392157;71,16,99,255;rgb;ccw:0.0588235;72,23,105,255;rgb;ccw:0.0784314;72,29,111,255;rgb;ccw:0.0980392;72,36,117,255;rgb;ccw:0.117647;71,42,122,255;rgb;ccw:0.137255;70,48,126,255;rgb;ccw:0.156863;69,55,129,255;rgb;ccw:0.176471;67,61,132,255;rgb;ccw:0.196078;65,66,135,255;rgb;ccw:0.215686;63,72,137,255;rgb;ccw:0.235294;61,78,138,255;rgb;ccw:0.254902;58,83,139,255;rgb;ccw:0.27451;56,89,140,255;rgb;ccw:0.294118;53,94,141,255;rgb;ccw:0.313725;51,99,141,255;rgb;ccw:0.333333;49,104,142,255;rgb;ccw:0.352941;46,109,142,255;rgb;ccw:0.372549;44,113,142,255;rgb;ccw:0.392157;42,118,142,255;rgb;ccw:0.411765;41,123,142,255;rgb;ccw:0.431373;39,128,142,255;rgb;ccw:0.45098;37,132,142,255;rgb;ccw:0.470588;35,137,142,255;rgb;ccw:0.490196;33,142,141,255;rgb;ccw:0.509804;32,146,140,255;rgb;ccw:0.529412;31,151,139,255;rgb;ccw:0.54902;30,156,137,255;rgb;ccw:0.568627;31,161,136,255;rgb;ccw:0.588235;33,165,133,255;rgb;ccw:0.607843;36,170,131,255;rgb;ccw:0.627451;40,174,128,255;rgb;ccw:0.647059;46,179,124,255;rgb;ccw:0.666667;53,183,121,255;rgb;ccw:0.686275;61,188,116,255;rgb;ccw:0.705882;70,192,111,255;rgb;ccw:0.72549;80,196,106,255;rgb;ccw:0.745098;90,200,100,255;rgb;ccw:0.764706;101,203,94,255;rgb;ccw:0.784314;112,207,87,255;rgb;ccw:0.803922;124,210,80,255;rgb;ccw:0.823529;137,213,72,255;rgb;ccw:0.843137;149,216,64,255;rgb;ccw:0.862745;162,218,55,255;rgb;ccw:0.882353;176,221,47,255;rgb;ccw:0.901961;189,223,38,255;rgb;ccw:0.921569;202,225,31,255;rgb;ccw:0.941176;216,226,25,255;rgb;ccw:0.960784;229,228,25,255;rgb;ccw:0.980392;241,229,29,255;rgb;ccw"/>
            </Option>
          </colorramp>
          <item label="0.0000" color="#440154" value="0" alpha="255"/>
          <item label="0.2200" color="#3a528b" value="0.219987425" alpha="255"/>
          <item label="0.4400" color="#20908d" value="0.43997485" alpha="255"/>
          <item label="0.6600" color="#5dc962" value="0.659962275" alpha="255"/>
          <item label="0.8799" color="#fde725" value="0.8799497" alpha="255"/>
          <rampLegendSettings orientation="1" suffix=" " direction="0" useContinuousLegend="1" maximumLabel="" minimumLabel="" prefix="">
            <numericFormat id="basic">
              <Option type="Map">
                <Option name="decimal_separator" type="invalid"/>
                <Option name="decimals" type="int" value="1"/>
                <Option name="rounding_type" type="int" value="0"/>
                <Option name="show_plus" type="bool" value="false"/>
                <Option name="show_thousand_separator" type="bool" value="true"/>
                <Option name="show_trailing_zeros" type="bool" value="false"/>
                <Option name="thousand_separator" type="invalid"/>
              </Option>
            </numericFormat>
          </rampLegendSettings>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0" gamma="1"/>
    <huesaturation grayscaleMode="0" colorizeStrength="100" saturation="0" invertColors="0" colorizeOn="0" colorizeBlue="128" colorizeRed="255" colorizeGreen="128"/>
    <rasterresampler maxOversampling="2"/>
    <resamplingStage>resamplingFilter</resamplingStage>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

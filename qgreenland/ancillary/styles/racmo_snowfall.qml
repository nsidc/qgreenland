<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis hasScaleBasedVisibilityFlag="0" styleCategories="AllStyleCategories" maxScale="0" minScale="1e+08" version="3.28.6-Firenze">
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
  <elevation zscale="1" symbology="Line" enabled="0" band="1" zoffset="0">
    <data-defined-properties>
      <Option type="Map">
        <Option name="name" value="" type="QString"/>
        <Option name="properties"/>
        <Option name="type" value="collection" type="QString"/>
      </Option>
    </data-defined-properties>
    <profileLineSymbol>
      <symbol name="" alpha="1" force_rhr="0" is_animated="0" clip_to_extent="1" frame_rate="10" type="line">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" value="" type="QString"/>
            <Option name="properties"/>
            <Option name="type" value="collection" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer pass="0" enabled="1" class="SimpleLine" locked="0">
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
            <Option name="line_color" value="190,207,80,255" type="QString"/>
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
      <symbol name="" alpha="1" force_rhr="0" is_animated="0" clip_to_extent="1" frame_rate="10" type="fill">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" value="" type="QString"/>
            <Option name="properties"/>
            <Option name="type" value="collection" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer pass="0" enabled="1" class="SimpleFill" locked="0">
          <Option type="Map">
            <Option name="border_width_map_unit_scale" value="3x:0,0,0,0,0,0" type="QString"/>
            <Option name="color" value="190,207,80,255" type="QString"/>
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
      <resampling zoomedOutResamplingMethod="nearestNeighbour" enabled="false" zoomedInResamplingMethod="nearestNeighbour" maxOversampling="2"/>
    </provider>
    <rasterrenderer classificationMax="4000" alphaBand="-1" band="1" nodataColor="" classificationMin="0" type="singlebandpseudocolor" opacity="1">
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
        <colorrampshader maximumValue="4000" colorRampType="INTERPOLATED" minimumValue="0" classificationMode="2" clip="0" labelPrecision="0">
          <colorramp name="[source]" type="gradient">
            <Option type="Map">
              <Option name="color1" value="241,241,241,255" type="QString"/>
              <Option name="color2" value="59,124,178,255" type="QString"/>
              <Option name="direction" value="ccw" type="QString"/>
              <Option name="discrete" value="0" type="QString"/>
              <Option name="rampType" value="gradient" type="QString"/>
              <Option name="spec" value="rgb" type="QString"/>
              <Option name="stops" value="0.016;237,239,240,255;rgb;ccw:0.032;234,237,240,255;rgb;ccw:0.048;231,235,240,255;rgb;ccw:0.063;228,233,240,255;rgb;ccw:0.079;225,231,239,255;rgb;ccw:0.095;222,229,239,255;rgb;ccw:0.111;219,227,239,255;rgb;ccw:0.127;216,225,238,255;rgb;ccw:0.143;213,223,238,255;rgb;ccw:0.159;210,221,238,255;rgb;ccw:0.175;207,220,237,255;rgb;ccw:0.19;203,218,237,255;rgb;ccw:0.206;200,216,236,255;rgb;ccw:0.222;197,214,236,255;rgb;ccw:0.238;194,212,235,255;rgb;ccw:0.254;191,210,235,255;rgb;ccw:0.27;188,208,234,255;rgb;ccw:0.286;185,206,234,255;rgb;ccw:0.302;182,204,233,255;rgb;ccw:0.317;179,203,233,255;rgb;ccw:0.333;176,201,232,255;rgb;ccw:0.349;173,199,231,255;rgb;ccw:0.365;170,197,231,255;rgb;ccw:0.381;167,195,230,255;rgb;ccw:0.397;164,193,229,255;rgb;ccw:0.413;161,191,228,255;rgb;ccw:0.429;158,189,227,255;rgb;ccw:0.444;156,188,225,255;rgb;ccw:0.46;153,186,224,255;rgb;ccw:0.476;151,184,223,255;rgb;ccw:0.492;148,182,221,255;rgb;ccw:0.508;146,180,220,255;rgb;ccw:0.524;144,178,218,255;rgb;ccw:0.54;141,176,216,255;rgb;ccw:0.556;139,174,215,255;rgb;ccw:0.571;137,172,213,255;rgb;ccw:0.587;135,170,211,255;rgb;ccw:0.603;133,169,209,255;rgb;ccw:0.619;130,167,208,255;rgb;ccw:0.635;128,165,206,255;rgb;ccw:0.651;126,163,204,255;rgb;ccw:0.667;124,161,202,255;rgb;ccw:0.683;122,159,200,255;rgb;ccw:0.698;120,157,198,255;rgb;ccw:0.714;118,155,197,255;rgb;ccw:0.73;116,153,195,255;rgb;ccw:0.746;113,152,194,255;rgb;ccw:0.762;111,150,192,255;rgb;ccw:0.778;108,148,191,255;rgb;ccw:0.794;105,146,190,255;rgb;ccw:0.81;102,144,189,255;rgb;ccw:0.825;99,143,188,255;rgb;ccw:0.841;96,141,186,255;rgb;ccw:0.857;93,139,185,255;rgb;ccw:0.873;90,137,185,255;rgb;ccw:0.889;86,136,184,255;rgb;ccw:0.905;83,134,183,255;rgb;ccw:0.921;79,132,182,255;rgb;ccw:0.937;76,130,181,255;rgb;ccw:0.952;72,129,180,255;rgb;ccw:0.968;68,127,179,255;rgb;ccw:0.984;63,125,179,255;rgb;ccw" type="QString"/>
            </Option>
          </colorramp>
          <item alpha="255" color="#f1f1f1" label="0mm w.e." value="0"/>
          <item alpha="255" color="#c9d9ec" label="800mm w.e." value="800"/>
          <item alpha="255" color="#a3c1e5" label="1600mm w.e." value="1600"/>
          <item alpha="255" color="#85a9d1" label="2400mm w.e." value="2400"/>
          <item alpha="255" color="#6891be" label="3200mm w.e." value="3200"/>
          <item alpha="255" color="#3b7cb2" label="4000mm w.e." value="4000"/>
          <rampLegendSettings prefix="" useContinuousLegend="1" direction="0" minimumLabel="" suffix="mm w.e." orientation="1" maximumLabel="">
            <numericFormat id="basic">
              <Option type="Map">
                <Option name="decimal_separator" type="invalid"/>
                <Option name="decimals" value="6" type="int"/>
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
    <brightnesscontrast contrast="0" gamma="1" brightness="6"/>
    <huesaturation colorizeBlue="128" saturation="0" grayscaleMode="0" colorizeGreen="128" invertColors="0" colorizeRed="255" colorizeStrength="100" colorizeOn="0"/>
    <rasterresampler maxOversampling="2"/>
    <resamplingStage>resamplingFilter</resamplingStage>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

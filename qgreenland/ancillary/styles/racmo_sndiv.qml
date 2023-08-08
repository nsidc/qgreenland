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
            <Option name="line_color" value="114,155,111,255" type="QString"/>
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
            <Option name="color" value="114,155,111,255" type="QString"/>
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
    <rasterrenderer classificationMax="160" alphaBand="-1" band="1" nodataColor="" classificationMin="-160" type="singlebandpseudocolor" opacity="1">
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
        <colorrampshader maximumValue="160" colorRampType="INTERPOLATED" minimumValue="-160" classificationMode="2" clip="0" labelPrecision="0">
          <colorramp name="[source]" type="gradient">
            <Option type="Map">
              <Option name="color1" value="168,144,8,255" type="QString"/>
              <Option name="color2" value="58,144,254,255" type="QString"/>
              <Option name="direction" value="ccw" type="QString"/>
              <Option name="discrete" value="0" type="QString"/>
              <Option name="rampType" value="gradient" type="QString"/>
              <Option name="spec" value="rgb" type="QString"/>
              <Option name="stops" value="0.016;171,146,24,255;rgb;ccw:0.032;174,149,34,255;rgb;ccw:0.048;176,152,43,255;rgb;ccw:0.063;179,155,51,255;rgb;ccw:0.079;182,158,59,255;rgb;ccw:0.095;185,161,66,255;rgb;ccw:0.111;187,164,73,255;rgb;ccw:0.127;190,167,80,255;rgb;ccw:0.143;193,170,87,255;rgb;ccw:0.159;195,173,94,255;rgb;ccw:0.175;198,176,101,255;rgb;ccw:0.19;200,179,107,255;rgb;ccw:0.206;203,182,114,255;rgb;ccw:0.222;205,185,121,255;rgb;ccw:0.238;208,188,127,255;rgb;ccw:0.254;210,191,134,255;rgb;ccw:0.27;212,194,141,255;rgb;ccw:0.286;215,197,147,255;rgb;ccw:0.302;217,200,154,255;rgb;ccw:0.317;219,203,161,255;rgb;ccw:0.333;221,206,167,255;rgb;ccw:0.349;223,209,174,255;rgb;ccw:0.365;225,213,181,255;rgb;ccw:0.381;227,216,188,255;rgb;ccw:0.397;229,219,194,255;rgb;ccw:0.413;231,222,201,255;rgb;ccw:0.429;233,225,208,255;rgb;ccw:0.444;234,229,215,255;rgb;ccw:0.46;236,232,222,255;rgb;ccw:0.476;237,235,228,255;rgb;ccw:0.492;238,236,234,255;rgb;ccw:0.508;236,236,239,255;rgb;ccw:0.524;233,235,241,255;rgb;ccw:0.54;229,232,242,255;rgb;ccw:0.556;225,229,243,255;rgb;ccw:0.571;221,225,243,255;rgb;ccw:0.587;216,222,244,255;rgb;ccw:0.603;212,219,244,255;rgb;ccw:0.619;207,216,245,255;rgb;ccw:0.635;203,213,245,255;rgb;ccw:0.651;198,210,246,255;rgb;ccw:0.667;194,206,246,255;rgb;ccw:0.683;189,203,247,255;rgb;ccw:0.698;184,200,247,255;rgb;ccw:0.714;180,197,248,255;rgb;ccw:0.73;175,194,248,255;rgb;ccw:0.746;170,191,248,255;rgb;ccw:0.762;165,188,249,255;rgb;ccw:0.778;160,185,249,255;rgb;ccw:0.794;154,182,250,255;rgb;ccw:0.81;149,179,250,255;rgb;ccw:0.825;143,176,250,255;rgb;ccw:0.841;138,173,251,255;rgb;ccw:0.857;132,170,251,255;rgb;ccw:0.873;126,167,252,255;rgb;ccw:0.889;119,164,252,255;rgb;ccw:0.905;113,161,252,255;rgb;ccw:0.921;105,158,253,255;rgb;ccw:0.937;98,156,253,255;rgb;ccw:0.952;90,153,253,255;rgb;ccw:0.968;81,150,254,255;rgb;ccw:0.984;70,147,254,255;rgb;ccw" type="QString"/>
            </Option>
          </colorramp>
          <item alpha="255" color="#a89008" label="-160mm w.e." value="-160"/>
          <item alpha="255" color="#bea74f" label="-120mm w.e." value="-120"/>
          <item alpha="255" color="#d2be84" label="-80mm w.e." value="-80"/>
          <item alpha="255" color="#e2d7b9" label="-40mm w.e." value="-40"/>
          <item alpha="255" color="#edeced" label="0mm w.e." value="0"/>
          <item alpha="255" color="#ced7f5" label="40mm w.e." value="40"/>
          <item alpha="255" color="#a9bef8" label="80mm w.e." value="80"/>
          <item alpha="255" color="#7da7fc" label="120mm w.e." value="120"/>
          <item alpha="255" color="#3a90fe" label="160mm w.e." value="160"/>
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
    <brightnesscontrast contrast="0" gamma="1" brightness="0"/>
    <huesaturation colorizeBlue="128" saturation="0" grayscaleMode="0" colorizeGreen="128" invertColors="0" colorizeRed="255" colorizeStrength="100" colorizeOn="0"/>
    <rasterresampler maxOversampling="2"/>
    <resamplingStage>resamplingFilter</resamplingStage>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

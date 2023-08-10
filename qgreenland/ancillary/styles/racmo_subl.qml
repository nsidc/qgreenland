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
            <Option name="line_color" value="141,90,153,255" type="QString"/>
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
            <Option name="color" value="141,90,153,255" type="QString"/>
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
    <rasterrenderer classificationMax="210" alphaBand="-1" band="1" nodataColor="" classificationMin="-210" type="singlebandpseudocolor" opacity="1">
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
        <colorrampshader maximumValue="210" colorRampType="INTERPOLATED" minimumValue="-210" classificationMode="2" clip="0" labelPrecision="0">
          <colorramp name="[source]" type="gradient">
            <Option type="Map">
              <Option name="color1" value="57,151,14,255" type="QString"/>
              <Option name="color2" value="184,89,228,255" type="QString"/>
              <Option name="direction" value="ccw" type="QString"/>
              <Option name="discrete" value="0" type="QString"/>
              <Option name="rampType" value="gradient" type="QString"/>
              <Option name="spec" value="rgb" type="QString"/>
              <Option name="stops" value="0.016;65,154,26,255;rgb;ccw:0.032;72,157,36,255;rgb;ccw:0.048;79,159,44,255;rgb;ccw:0.063;86,162,52,255;rgb;ccw:0.079;92,165,60,255;rgb;ccw:0.095;99,168,67,255;rgb;ccw:0.111;105,171,74,255;rgb;ccw:0.127;111,174,81,255;rgb;ccw:0.143;117,177,87,255;rgb;ccw:0.159;123,180,94,255;rgb;ccw:0.175;129,182,101,255;rgb;ccw:0.19;134,185,107,255;rgb;ccw:0.206;140,188,114,255;rgb;ccw:0.222;145,191,121,255;rgb;ccw:0.238;151,194,127,255;rgb;ccw:0.254;156,197,134,255;rgb;ccw:0.27;162,199,140,255;rgb;ccw:0.286;167,202,147,255;rgb;ccw:0.302;173,205,154,255;rgb;ccw:0.317;178,208,160,255;rgb;ccw:0.333;184,211,167,255;rgb;ccw:0.349;189,213,174,255;rgb;ccw:0.365;194,216,181,255;rgb;ccw:0.381;200,219,187,255;rgb;ccw:0.397;205,222,194,255;rgb;ccw:0.413;210,225,201,255;rgb;ccw:0.429;216,227,208,255;rgb;ccw:0.444;221,230,215,255;rgb;ccw:0.46;226,233,221,255;rgb;ccw:0.476;230,234,228,255;rgb;ccw:0.492;234,235,233,255;rgb;ccw:0.508;236,234,237,255;rgb;ccw:0.524;237,231,239,255;rgb;ccw:0.54;236,228,239,255;rgb;ccw:0.556;235,223,240,255;rgb;ccw:0.571;234,219,239,255;rgb;ccw:0.587;233,214,239,255;rgb;ccw:0.603;231,209,239,255;rgb;ccw:0.619;230,205,238,255;rgb;ccw:0.635;228,200,238,255;rgb;ccw:0.651;226,196,238,255;rgb;ccw:0.667;225,191,237,255;rgb;ccw:0.683;223,186,237,255;rgb;ccw:0.698;222,182,237,255;rgb;ccw:0.714;220,177,236,255;rgb;ccw:0.73;218,172,236,255;rgb;ccw:0.746;216,168,236,255;rgb;ccw:0.762;215,163,235,255;rgb;ccw:0.778;213,158,235,255;rgb;ccw:0.794;211,154,234,255;rgb;ccw:0.81;209,149,234,255;rgb;ccw:0.825;207,144,234,255;rgb;ccw:0.841;205,139,233,255;rgb;ccw:0.857;203,135,233,255;rgb;ccw:0.873;201,130,232,255;rgb;ccw:0.889;199,125,232,255;rgb;ccw:0.905;197,120,231,255;rgb;ccw:0.921;195,115,231,255;rgb;ccw:0.937;193,110,230,255;rgb;ccw:0.952;190,105,230,255;rgb;ccw:0.968;188,100,229,255;rgb;ccw:0.984;186,95,229,255;rgb;ccw" type="QString"/>
            </Option>
          </colorramp>
          <item alpha="255" color="#39970e" label="-210 mm w.e." value="-210"/>
          <item alpha="255" color="#75b157" label="-150 mm w.e." value="-150"/>
          <item alpha="255" color="#a7ca93" label="-90 mm w.e." value="-90"/>
          <item alpha="255" color="#d8e3d0" label="-30 mm w.e." value="-30"/>
          <item alpha="255" color="#eadbef" label="30 mm w.e." value="30"/>
          <item alpha="255" color="#dcb1ec" label="90 mm w.e." value="90"/>
          <item alpha="255" color="#cb87e9" label="150 mm w.e." value="150"/>
          <item alpha="255" color="#b859e4" label="210 mm w.e." value="210"/>
          <rampLegendSettings prefix="" useContinuousLegend="1" direction="0" minimumLabel="" suffix="mm w.e" orientation="1" maximumLabel="">
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

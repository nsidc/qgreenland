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
            <Option name="line_color" value="229,182,54,255" type="QString"/>
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
            <Option name="color" value="229,182,54,255" type="QString"/>
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
    <rasterrenderer classificationMax="5000" alphaBand="-1" band="1" nodataColor="" classificationMin="0" type="singlebandpseudocolor" opacity="1">
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
        <colorrampshader maximumValue="5000" colorRampType="INTERPOLATED" minimumValue="0" classificationMode="2" clip="0" labelPrecision="0">
          <colorramp name="[source]" type="gradient">
            <Option type="Map">
              <Option name="color1" value="241,241,241,255" type="QString"/>
              <Option name="color2" value="17,17,17,255" type="QString"/>
              <Option name="direction" value="ccw" type="QString"/>
              <Option name="discrete" value="0" type="QString"/>
              <Option name="rampType" value="gradient" type="QString"/>
              <Option name="spec" value="rgb" type="QString"/>
              <Option name="stops" value="0.016;239,236,229,255;rgb;ccw:0.032;238,232,218,255;rgb;ccw:0.048;236,228,208,255;rgb;ccw:0.063;234,224,198,255;rgb;ccw:0.079;232,220,187,255;rgb;ccw:0.095;230,215,178,255;rgb;ccw:0.111;227,211,168,255;rgb;ccw:0.127;225,207,159,255;rgb;ccw:0.143;222,203,151,255;rgb;ccw:0.159;219,199,143,255;rgb;ccw:0.175;215,195,135,255;rgb;ccw:0.19;212,191,127,255;rgb;ccw:0.206;209,187,120,255;rgb;ccw:0.222;205,183,114,255;rgb;ccw:0.238;201,180,108,255;rgb;ccw:0.254;198,176,103,255;rgb;ccw:0.27;194,172,98,255;rgb;ccw:0.286;190,168,94,255;rgb;ccw:0.302;185,164,92,255;rgb;ccw:0.317;181,160,90,255;rgb;ccw:0.333;177,157,89,255;rgb;ccw:0.349;172,153,89,255;rgb;ccw:0.365;167,149,91,255;rgb;ccw:0.381;162,146,94,255;rgb;ccw:0.397;157,142,97,255;rgb;ccw:0.413;151,138,101,255;rgb;ccw:0.429;146,135,104,255;rgb;ccw:0.444;141,131,108,255;rgb;ccw:0.46;135,127,111,255;rgb;ccw:0.476;130,124,114,255;rgb;ccw:0.492;124,120,117,255;rgb;ccw:0.508;118,117,120,255;rgb;ccw:0.524;112,113,123,255;rgb;ccw:0.54;106,109,126,255;rgb;ccw:0.556;99,106,129,255;rgb;ccw:0.571;93,102,132,255;rgb;ccw:0.587;85,99,134,255;rgb;ccw:0.603;78,95,137,255;rgb;ccw:0.619;69,92,140,255;rgb;ccw:0.635;60,89,142,255;rgb;ccw:0.651;51,85,143,255;rgb;ccw:0.667;42,82,142,255;rgb;ccw:0.683;34,79,141,255;rgb;ccw:0.698;25,75,138,255;rgb;ccw:0.714;17,72,135,255;rgb;ccw:0.73;9,69,131,255;rgb;ccw:0.746;2,66,127,255;rgb;ccw:0.762;0,63,122,255;rgb;ccw:0.778;0,59,116,255;rgb;ccw:0.794;0,56,111,255;rgb;ccw:0.81;1,53,104,255;rgb;ccw:0.825;4,50,98,255;rgb;ccw:0.841;7,47,91,255;rgb;ccw:0.857;10,44,84,255;rgb;ccw:0.873;13,41,77,255;rgb;ccw:0.889;16,38,70,255;rgb;ccw:0.905;18,35,63,255;rgb;ccw:0.921;19,32,55,255;rgb;ccw:0.937;20,29,48,255;rgb;ccw:0.952;20,26,40,255;rgb;ccw:0.968;20,23,33,255;rgb;ccw:0.984;19,20,25,255;rgb;ccw" type="QString"/>
            </Option>
          </colorramp>
          <item alpha="255" color="#f1f1f1" label="0mm w.e" value="0"/>
          <item alpha="255" color="#e1d0a0" label="625mm w.e" value="625"/>
          <item alpha="255" color="#c7b168" label="1250mm w.e" value="1250"/>
          <item alpha="255" color="#a4935d" label="1875mm w.e" value="1875"/>
          <item alpha="255" color="#797777" label="2500mm w.e" value="2500"/>
          <item alpha="255" color="#425b8d" label="3125mm w.e" value="3125"/>
          <item alpha="255" color="#02417e" label="3750mm w.e" value="3750"/>
          <item alpha="255" color="#0d294c" label="4375mm w.e" value="4375"/>
          <item alpha="255" color="#111111" label="5000mm w.e" value="5000"/>
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

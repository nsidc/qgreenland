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
            <Option type="QString" name="line_color" value="231,113,72,255"/>
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
            <Option type="QString" name="color" value="231,113,72,255"/>
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
    <rasterrenderer classificationMax="15" type="singlebandpseudocolor" nodataColor="" band="1" opacity="1" alphaBand="-1" classificationMin="-2">
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
        <colorrampshader colorRampType="INTERPOLATED" classificationMode="1" labelPrecision="4" maximumValue="15" clip="0" minimumValue="-2">
          <colorramp type="gradient" name="[source]">
            <Option type="Map">
              <Option type="QString" name="color1" value="4,35,51,255"/>
              <Option type="QString" name="color2" value="232,250,91,255"/>
              <Option type="QString" name="direction" value="ccw"/>
              <Option type="QString" name="discrete" value="0"/>
              <Option type="QString" name="rampType" value="gradient"/>
              <Option type="QString" name="spec" value="rgb"/>
              <Option type="QString" name="stops" value="0.0039;4,35,51,255;rgb;ccw:0.0039;4,36,53,255;rgb;ccw:0.0078;4,36,53,255;rgb;ccw:0.0078;4,37,55,255;rgb;ccw:0.0117;4,37,55,255;rgb;ccw:0.0117;4,37,57,255;rgb;ccw:0.0156;4,37,57,255;rgb;ccw:0.0156;5,38,59,255;rgb;ccw:0.0195;5,38,59,255;rgb;ccw:0.0195;5,39,61,255;rgb;ccw:0.0234;5,39,61,255;rgb;ccw:0.0234;5,39,63,255;rgb;ccw:0.0273;5,39,63,255;rgb;ccw:0.0273;5,40,65,255;rgb;ccw:0.0312;5,40,65,255;rgb;ccw:0.0312;5,41,67,255;rgb;ccw:0.0352;5,41,67,255;rgb;ccw:0.0352;6,41,69,255;rgb;ccw:0.0391;6,41,69,255;rgb;ccw:0.0391;6,42,71,255;rgb;ccw:0.043;6,42,71,255;rgb;ccw:0.043;6,43,73,255;rgb;ccw:0.0469;6,43,73,255;rgb;ccw:0.0469;7,43,75,255;rgb;ccw:0.0508;7,43,75,255;rgb;ccw:0.0508;7,44,77,255;rgb;ccw:0.0547;7,44,77,255;rgb;ccw:0.0547;7,44,80,255;rgb;ccw:0.0586;7,44,80,255;rgb;ccw:0.0586;8,45,82,255;rgb;ccw:0.0625;8,45,82,255;rgb;ccw:0.0625;8,46,84,255;rgb;ccw:0.0664;8,46,84,255;rgb;ccw:0.0664;9,46,86,255;rgb;ccw:0.0703;9,46,86,255;rgb;ccw:0.0703;9,47,89,255;rgb;ccw:0.0742;9,47,89,255;rgb;ccw:0.0742;10,47,91,255;rgb;ccw:0.0781;10,47,91,255;rgb;ccw:0.0781;11,48,93,255;rgb;ccw:0.082;11,48,93,255;rgb;ccw:0.082;12,48,96,255;rgb;ccw:0.0859;12,48,96,255;rgb;ccw:0.0859;12,48,98,255;rgb;ccw:0.0898;12,48,98,255;rgb;ccw:0.0898;13,49,101,255;rgb;ccw:0.0938;13,49,101,255;rgb;ccw:0.0938;14,49,103,255;rgb;ccw:0.0977;14,49,103,255;rgb;ccw:0.0977;15,50,106,255;rgb;ccw:0.1016;15,50,106,255;rgb;ccw:0.1016;16,50,108,255;rgb;ccw:0.1055;16,50,108,255;rgb;ccw:0.1055;18,50,111,255;rgb;ccw:0.1094;18,50,111,255;rgb;ccw:0.1094;19,51,114,255;rgb;ccw:0.1133;19,51,114,255;rgb;ccw:0.1133;20,51,116,255;rgb;ccw:0.1172;20,51,116,255;rgb;ccw:0.1172;22,51,119,255;rgb;ccw:0.1211;22,51,119,255;rgb;ccw:0.1211;23,51,122,255;rgb;ccw:0.125;23,51,122,255;rgb;ccw:0.125;25,51,124,255;rgb;ccw:0.1289;25,51,124,255;rgb;ccw:0.1289;26,52,127,255;rgb;ccw:0.1328;26,52,127,255;rgb;ccw:0.1328;28,52,130,255;rgb;ccw:0.1367;28,52,130,255;rgb;ccw:0.1367;30,52,132,255;rgb;ccw:0.1406;30,52,132,255;rgb;ccw:0.1406;31,52,135,255;rgb;ccw:0.1445;31,52,135,255;rgb;ccw:0.1445;33,52,138,255;rgb;ccw:0.1484;33,52,138,255;rgb;ccw:0.1484;35,52,140,255;rgb;ccw:0.1523;35,52,140,255;rgb;ccw:0.1523;37,52,143,255;rgb;ccw:0.1562;37,52,143,255;rgb;ccw:0.1562;39,52,145,255;rgb;ccw:0.1602;39,52,145,255;rgb;ccw:0.1602;42,51,147,255;rgb;ccw:0.1641;42,51,147,255;rgb;ccw:0.1641;44,51,149,255;rgb;ccw:0.168;44,51,149,255;rgb;ccw:0.168;46,51,151,255;rgb;ccw:0.1719;46,51,151,255;rgb;ccw:0.1719;48,51,153,255;rgb;ccw:0.1758;48,51,153,255;rgb;ccw:0.1758;51,51,155,255;rgb;ccw:0.1797;51,51,155,255;rgb;ccw:0.1797;53,51,156,255;rgb;ccw:0.1836;53,51,156,255;rgb;ccw:0.1836;55,51,157,255;rgb;ccw:0.1875;55,51,157,255;rgb;ccw:0.1875;57,51,158,255;rgb;ccw:0.1914;57,51,158,255;rgb;ccw:0.1914;60,51,159,255;rgb;ccw:0.1953;60,51,159,255;rgb;ccw:0.1953;62,52,159,255;rgb;ccw:0.1992;62,52,159,255;rgb;ccw:0.1992;64,52,159,255;rgb;ccw:0.2031;64,52,159,255;rgb;ccw:0.2031;66,52,160,255;rgb;ccw:0.207;66,52,160,255;rgb;ccw:0.207;68,53,160,255;rgb;ccw:0.2109;68,53,160,255;rgb;ccw:0.2109;70,53,160,255;rgb;ccw:0.2148;70,53,160,255;rgb;ccw:0.2148;71,54,160,255;rgb;ccw:0.2188;71,54,160,255;rgb;ccw:0.2188;73,54,159,255;rgb;ccw:0.2227;73,54,159,255;rgb;ccw:0.2227;75,55,159,255;rgb;ccw:0.2266;75,55,159,255;rgb;ccw:0.2266;77,55,159,255;rgb;ccw:0.2305;77,55,159,255;rgb;ccw:0.2305;78,56,158,255;rgb;ccw:0.2344;78,56,158,255;rgb;ccw:0.2344;80,57,158,255;rgb;ccw:0.2383;80,57,158,255;rgb;ccw:0.2383;82,57,157,255;rgb;ccw:0.2422;82,57,157,255;rgb;ccw:0.2422;83,58,157,255;rgb;ccw:0.2461;83,58,157,255;rgb;ccw:0.2461;85,59,157,255;rgb;ccw:0.25;85,59,157,255;rgb;ccw:0.25;86,59,156,255;rgb;ccw:0.2539;86,59,156,255;rgb;ccw:0.2539;88,60,156,255;rgb;ccw:0.2578;88,60,156,255;rgb;ccw:0.2578;89,61,155,255;rgb;ccw:0.2617;89,61,155,255;rgb;ccw:0.2617;91,61,155,255;rgb;ccw:0.2656;91,61,155,255;rgb;ccw:0.2656;92,62,154,255;rgb;ccw:0.2695;92,62,154,255;rgb;ccw:0.2695;94,63,154,255;rgb;ccw:0.2734;94,63,154,255;rgb;ccw:0.2734;95,63,153,255;rgb;ccw:0.2773;95,63,153,255;rgb;ccw:0.2773;96,64,153,255;rgb;ccw:0.2812;96,64,153,255;rgb;ccw:0.2812;98,65,152,255;rgb;ccw:0.2852;98,65,152,255;rgb;ccw:0.2852;99,65,152,255;rgb;ccw:0.2891;99,65,152,255;rgb;ccw:0.2891;101,66,151,255;rgb;ccw:0.293;101,66,151,255;rgb;ccw:0.293;102,67,151,255;rgb;ccw:0.2969;102,67,151,255;rgb;ccw:0.2969;103,67,150,255;rgb;ccw:0.3008;103,67,150,255;rgb;ccw:0.3008;105,68,150,255;rgb;ccw:0.3047;105,68,150,255;rgb;ccw:0.3047;106,69,149,255;rgb;ccw:0.3086;106,69,149,255;rgb;ccw:0.3086;108,69,149,255;rgb;ccw:0.3125;108,69,149,255;rgb;ccw:0.3125;109,70,148,255;rgb;ccw:0.3164;109,70,148,255;rgb;ccw:0.3164;110,71,148,255;rgb;ccw:0.3203;110,71,148,255;rgb;ccw:0.3203;112,71,148,255;rgb;ccw:0.3242;112,71,148,255;rgb;ccw:0.3242;113,72,147,255;rgb;ccw:0.3281;113,72,147,255;rgb;ccw:0.3281;114,72,147,255;rgb;ccw:0.332;114,72,147,255;rgb;ccw:0.332;116,73,146,255;rgb;ccw:0.3359;116,73,146,255;rgb;ccw:0.3359;117,74,146,255;rgb;ccw:0.3398;117,74,146,255;rgb;ccw:0.3398;118,74,146,255;rgb;ccw:0.3438;118,74,146,255;rgb;ccw:0.3438;120,75,145,255;rgb;ccw:0.3477;120,75,145,255;rgb;ccw:0.3477;121,75,145,255;rgb;ccw:0.3516;121,75,145,255;rgb;ccw:0.3516;122,76,145,255;rgb;ccw:0.3555;122,76,145,255;rgb;ccw:0.3555;124,77,144,255;rgb;ccw:0.3594;124,77,144,255;rgb;ccw:0.3594;125,77,144,255;rgb;ccw:0.3633;125,77,144,255;rgb;ccw:0.3633;126,78,144,255;rgb;ccw:0.3672;126,78,144,255;rgb;ccw:0.3672;128,78,143,255;rgb;ccw:0.3711;128,78,143,255;rgb;ccw:0.3711;129,79,143,255;rgb;ccw:0.375;129,79,143,255;rgb;ccw:0.375;131,80,143,255;rgb;ccw:0.3789;131,80,143,255;rgb;ccw:0.3789;132,80,142,255;rgb;ccw:0.3828;132,80,142,255;rgb;ccw:0.3828;133,81,142,255;rgb;ccw:0.3867;133,81,142,255;rgb;ccw:0.3867;135,81,142,255;rgb;ccw:0.3906;135,81,142,255;rgb;ccw:0.3906;136,82,141,255;rgb;ccw:0.3945;136,82,141,255;rgb;ccw:0.3945;137,82,141,255;rgb;ccw:0.3984;137,82,141,255;rgb;ccw:0.3984;139,83,141,255;rgb;ccw:0.4023;139,83,141,255;rgb;ccw:0.4023;140,83,140,255;rgb;ccw:0.4062;140,83,140,255;rgb;ccw:0.4062;142,84,140,255;rgb;ccw:0.4102;142,84,140,255;rgb;ccw:0.4102;143,84,140,255;rgb;ccw:0.4141;143,84,140,255;rgb;ccw:0.4141;144,85,139,255;rgb;ccw:0.418;144,85,139,255;rgb;ccw:0.418;146,85,139,255;rgb;ccw:0.4219;146,85,139,255;rgb;ccw:0.4219;147,86,139,255;rgb;ccw:0.4258;147,86,139,255;rgb;ccw:0.4258;149,86,138,255;rgb;ccw:0.4297;149,86,138,255;rgb;ccw:0.4297;150,87,138,255;rgb;ccw:0.4336;150,87,138,255;rgb;ccw:0.4336;151,87,138,255;rgb;ccw:0.4375;151,87,138,255;rgb;ccw:0.4375;153,88,137,255;rgb;ccw:0.4414;153,88,137,255;rgb;ccw:0.4414;154,88,137,255;rgb;ccw:0.4453;154,88,137,255;rgb;ccw:0.4453;156,89,137,255;rgb;ccw:0.4492;156,89,137,255;rgb;ccw:0.4492;157,89,136,255;rgb;ccw:0.4531;157,89,136,255;rgb;ccw:0.4531;159,90,136,255;rgb;ccw:0.457;159,90,136,255;rgb;ccw:0.457;160,90,135,255;rgb;ccw:0.4609;160,90,135,255;rgb;ccw:0.4609;162,91,135,255;rgb;ccw:0.4648;162,91,135,255;rgb;ccw:0.4648;163,91,134,255;rgb;ccw:0.4688;163,91,134,255;rgb;ccw:0.4688;165,92,134,255;rgb;ccw:0.4727;165,92,134,255;rgb;ccw:0.4727;166,92,134,255;rgb;ccw:0.4766;166,92,134,255;rgb;ccw:0.4766;168,93,133,255;rgb;ccw:0.4805;168,93,133,255;rgb;ccw:0.4805;169,93,132,255;rgb;ccw:0.4844;169,93,132,255;rgb;ccw:0.4844;171,93,132,255;rgb;ccw:0.4883;171,93,132,255;rgb;ccw:0.4883;172,94,131,255;rgb;ccw:0.4922;172,94,131,255;rgb;ccw:0.4922;174,94,131,255;rgb;ccw:0.4961;174,94,131,255;rgb;ccw:0.4961;175,95,130,255;rgb;ccw:0.5;175,95,130,255;rgb;ccw:0.5;177,95,130,255;rgb;ccw:0.5039;177,95,130,255;rgb;ccw:0.5039;178,96,129,255;rgb;ccw:0.5078;178,96,129,255;rgb;ccw:0.5078;180,96,128,255;rgb;ccw:0.5117;180,96,128,255;rgb;ccw:0.5117;181,97,128,255;rgb;ccw:0.5156;181,97,128,255;rgb;ccw:0.5156;183,97,127,255;rgb;ccw:0.5195;183,97,127,255;rgb;ccw:0.5195;184,98,126,255;rgb;ccw:0.5234;184,98,126,255;rgb;ccw:0.5234;186,98,126,255;rgb;ccw:0.5273;186,98,126,255;rgb;ccw:0.5273;187,98,125,255;rgb;ccw:0.5312;187,98,125,255;rgb;ccw:0.5312;189,99,124,255;rgb;ccw:0.5352;189,99,124,255;rgb;ccw:0.5352;190,99,123,255;rgb;ccw:0.5391;190,99,123,255;rgb;ccw:0.5391;192,100,123,255;rgb;ccw:0.543;192,100,123,255;rgb;ccw:0.543;193,100,122,255;rgb;ccw:0.5469;193,100,122,255;rgb;ccw:0.5469;195,101,121,255;rgb;ccw:0.5508;195,101,121,255;rgb;ccw:0.5508;196,101,120,255;rgb;ccw:0.5547;196,101,120,255;rgb;ccw:0.5547;198,102,119,255;rgb;ccw:0.5586;198,102,119,255;rgb;ccw:0.5586;199,102,118,255;rgb;ccw:0.5625;199,102,118,255;rgb;ccw:0.5625;201,103,117,255;rgb;ccw:0.5664;201,103,117,255;rgb;ccw:0.5664;202,103,116,255;rgb;ccw:0.5703;202,103,116,255;rgb;ccw:0.5703;204,104,115,255;rgb;ccw:0.5742;204,104,115,255;rgb;ccw:0.5742;205,104,114,255;rgb;ccw:0.5781;205,104,114,255;rgb;ccw:0.5781;206,105,113,255;rgb;ccw:0.582;206,105,113,255;rgb;ccw:0.582;208,105,112,255;rgb;ccw:0.5859;208,105,112,255;rgb;ccw:0.5859;209,106,111,255;rgb;ccw:0.5898;209,106,111,255;rgb;ccw:0.5898;211,106,110,255;rgb;ccw:0.5938;211,106,110,255;rgb;ccw:0.5938;212,107,109,255;rgb;ccw:0.5977;212,107,109,255;rgb;ccw:0.5977;214,108,108,255;rgb;ccw:0.6016;214,108,108,255;rgb;ccw:0.6016;215,108,107,255;rgb;ccw:0.6055;215,108,107,255;rgb;ccw:0.6055;216,109,106,255;rgb;ccw:0.6094;216,109,106,255;rgb;ccw:0.6094;218,110,105,255;rgb;ccw:0.6133;218,110,105,255;rgb;ccw:0.6133;219,110,104,255;rgb;ccw:0.6172;219,110,104,255;rgb;ccw:0.6172;220,111,102,255;rgb;ccw:0.6211;220,111,102,255;rgb;ccw:0.6211;222,112,101,255;rgb;ccw:0.625;222,112,101,255;rgb;ccw:0.625;223,112,100,255;rgb;ccw:0.6289;223,112,100,255;rgb;ccw:0.6289;224,113,99,255;rgb;ccw:0.6328;224,113,99,255;rgb;ccw:0.6328;225,114,98,255;rgb;ccw:0.6367;225,114,98,255;rgb;ccw:0.6367;227,114,96,255;rgb;ccw:0.6406;227,114,96,255;rgb;ccw:0.6406;228,115,95,255;rgb;ccw:0.6445;228,115,95,255;rgb;ccw:0.6445;229,116,94,255;rgb;ccw:0.6484;229,116,94,255;rgb;ccw:0.6484;230,117,93,255;rgb;ccw:0.6523;230,117,93,255;rgb;ccw:0.6523;231,118,91,255;rgb;ccw:0.6562;231,118,91,255;rgb;ccw:0.6562;232,119,90,255;rgb;ccw:0.6602;232,119,90,255;rgb;ccw:0.6602;234,120,89,255;rgb;ccw:0.6641;234,120,89,255;rgb;ccw:0.6641;235,121,88,255;rgb;ccw:0.668;235,121,88,255;rgb;ccw:0.668;236,121,86,255;rgb;ccw:0.6719;236,121,86,255;rgb;ccw:0.6719;237,122,85,255;rgb;ccw:0.6758;237,122,85,255;rgb;ccw:0.6758;238,123,84,255;rgb;ccw:0.6797;238,123,84,255;rgb;ccw:0.6797;238,125,83,255;rgb;ccw:0.6836;238,125,83,255;rgb;ccw:0.6836;239,126,82,255;rgb;ccw:0.6875;239,126,82,255;rgb;ccw:0.6875;240,127,80,255;rgb;ccw:0.6914;240,127,80,255;rgb;ccw:0.6914;241,128,79,255;rgb;ccw:0.6953;241,128,79,255;rgb;ccw:0.6953;242,129,78,255;rgb;ccw:0.6992;242,129,78,255;rgb;ccw:0.6992;243,130,77,255;rgb;ccw:0.7031;243,130,77,255;rgb;ccw:0.7031;243,131,76,255;rgb;ccw:0.707;243,131,76,255;rgb;ccw:0.707;244,133,75,255;rgb;ccw:0.7109;244,133,75,255;rgb;ccw:0.7109;245,134,74,255;rgb;ccw:0.7148;245,134,74,255;rgb;ccw:0.7148;245,135,73,255;rgb;ccw:0.7188;245,135,73,255;rgb;ccw:0.7188;246,136,72,255;rgb;ccw:0.7227;246,136,72,255;rgb;ccw:0.7227;246,138,71,255;rgb;ccw:0.7266;246,138,71,255;rgb;ccw:0.7266;247,139,70,255;rgb;ccw:0.7305;247,139,70,255;rgb;ccw:0.7305;247,140,69,255;rgb;ccw:0.7344;247,140,69,255;rgb;ccw:0.7344;248,142,68,255;rgb;ccw:0.7383;248,142,68,255;rgb;ccw:0.7383;248,143,67,255;rgb;ccw:0.7422;248,143,67,255;rgb;ccw:0.7422;249,145,67,255;rgb;ccw:0.7461;249,145,67,255;rgb;ccw:0.7461;249,146,66,255;rgb;ccw:0.75;249,146,66,255;rgb;ccw:0.75;249,147,65,255;rgb;ccw:0.7539;249,147,65,255;rgb;ccw:0.7539;250,149,65,255;rgb;ccw:0.7578;250,149,65,255;rgb;ccw:0.7578;250,150,64,255;rgb;ccw:0.7617;250,150,64,255;rgb;ccw:0.7617;250,152,63,255;rgb;ccw:0.7656;250,152,63,255;rgb;ccw:0.7656;251,153,63,255;rgb;ccw:0.7695;251,153,63,255;rgb;ccw:0.7695;251,155,62,255;rgb;ccw:0.7734;251,155,62,255;rgb;ccw:0.7734;251,156,62,255;rgb;ccw:0.7773;251,156,62,255;rgb;ccw:0.7773;251,158,62,255;rgb;ccw:0.7812;251,158,62,255;rgb;ccw:0.7812;251,159,61,255;rgb;ccw:0.7852;251,159,61,255;rgb;ccw:0.7852;251,161,61,255;rgb;ccw:0.7891;251,161,61,255;rgb;ccw:0.7891;252,163,61,255;rgb;ccw:0.793;252,163,61,255;rgb;ccw:0.793;252,164,61,255;rgb;ccw:0.7969;252,164,61,255;rgb;ccw:0.7969;252,166,60,255;rgb;ccw:0.8008;252,166,60,255;rgb;ccw:0.8008;252,167,60,255;rgb;ccw:0.8047;252,167,60,255;rgb;ccw:0.8047;252,169,60,255;rgb;ccw:0.8086;252,169,60,255;rgb;ccw:0.8086;252,170,60,255;rgb;ccw:0.8125;252,170,60,255;rgb;ccw:0.8125;252,172,60,255;rgb;ccw:0.8164;252,172,60,255;rgb;ccw:0.8164;252,174,60,255;rgb;ccw:0.8203;252,174,60,255;rgb;ccw:0.8203;252,175,60,255;rgb;ccw:0.8242;252,175,60,255;rgb;ccw:0.8242;252,177,60,255;rgb;ccw:0.8281;252,177,60,255;rgb;ccw:0.8281;251,178,61,255;rgb;ccw:0.832;251,178,61,255;rgb;ccw:0.832;251,180,61,255;rgb;ccw:0.8359;251,180,61,255;rgb;ccw:0.8359;251,182,61,255;rgb;ccw:0.8398;251,182,61,255;rgb;ccw:0.8398;251,183,61,255;rgb;ccw:0.8438;251,183,61,255;rgb;ccw:0.8438;251,185,62,255;rgb;ccw:0.8477;251,185,62,255;rgb;ccw:0.8477;251,187,62,255;rgb;ccw:0.8516;251,187,62,255;rgb;ccw:0.8516;251,188,62,255;rgb;ccw:0.8555;251,188,62,255;rgb;ccw:0.8555;250,190,63,255;rgb;ccw:0.8594;250,190,63,255;rgb;ccw:0.8594;250,191,63,255;rgb;ccw:0.8633;250,191,63,255;rgb;ccw:0.8633;250,193,64,255;rgb;ccw:0.8672;250,193,64,255;rgb;ccw:0.8672;250,195,64,255;rgb;ccw:0.8711;250,195,64,255;rgb;ccw:0.8711;249,196,65,255;rgb;ccw:0.875;249,196,65,255;rgb;ccw:0.875;249,198,65,255;rgb;ccw:0.8789;249,198,65,255;rgb;ccw:0.8789;249,200,66,255;rgb;ccw:0.8828;249,200,66,255;rgb;ccw:0.8828;248,201,67,255;rgb;ccw:0.8867;248,201,67,255;rgb;ccw:0.8867;248,203,67,255;rgb;ccw:0.8906;248,203,67,255;rgb;ccw:0.8906;248,205,68,255;rgb;ccw:0.8945;248,205,68,255;rgb;ccw:0.8945;247,206,69,255;rgb;ccw:0.8984;247,206,69,255;rgb;ccw:0.8984;247,208,69,255;rgb;ccw:0.9023;247,208,69,255;rgb;ccw:0.9023;247,210,70,255;rgb;ccw:0.9062;247,210,70,255;rgb;ccw:0.9062;246,211,71,255;rgb;ccw:0.9102;246,211,71,255;rgb;ccw:0.9102;246,213,71,255;rgb;ccw:0.9141;246,213,71,255;rgb;ccw:0.9141;245,215,72,255;rgb;ccw:0.918;245,215,72,255;rgb;ccw:0.918;245,216,73,255;rgb;ccw:0.9219;245,216,73,255;rgb;ccw:0.9219;244,218,74,255;rgb;ccw:0.9258;244,218,74,255;rgb;ccw:0.9258;244,220,75,255;rgb;ccw:0.9297;244,220,75,255;rgb;ccw:0.9297;243,221,75,255;rgb;ccw:0.9336;243,221,75,255;rgb;ccw:0.9336;243,223,76,255;rgb;ccw:0.9375;243,223,76,255;rgb;ccw:0.9375;242,225,77,255;rgb;ccw:0.9414;242,225,77,255;rgb;ccw:0.9414;242,226,78,255;rgb;ccw:0.9453;242,226,78,255;rgb;ccw:0.9453;241,228,79,255;rgb;ccw:0.9492;241,228,79,255;rgb;ccw:0.9492;241,230,80,255;rgb;ccw:0.9531;241,230,80,255;rgb;ccw:0.9531;240,232,81,255;rgb;ccw:0.957;240,232,81,255;rgb;ccw:0.957;239,233,81,255;rgb;ccw:0.9609;239,233,81,255;rgb;ccw:0.9609;239,235,82,255;rgb;ccw:0.9648;239,235,82,255;rgb;ccw:0.9648;238,237,83,255;rgb;ccw:0.9688;238,237,83,255;rgb;ccw:0.9688;237,238,84,255;rgb;ccw:0.9727;237,238,84,255;rgb;ccw:0.9727;237,240,85,255;rgb;ccw:0.9766;237,240,85,255;rgb;ccw:0.9766;236,242,86,255;rgb;ccw:0.9805;236,242,86,255;rgb;ccw:0.9805;235,244,87,255;rgb;ccw:0.9844;235,244,87,255;rgb;ccw:0.9844;234,245,88,255;rgb;ccw:0.9883;234,245,88,255;rgb;ccw:0.9883;234,247,89,255;rgb;ccw:0.9922;234,247,89,255;rgb;ccw:0.9922;233,249,90,255;rgb;ccw:0.9961;233,249,90,255;rgb;ccw:0.9961;232,250,91,255;rgb;ccw"/>
            </Option>
          </colorramp>
          <item color="#042333" label="-2.0000 °C" alpha="255" value="-2"/>
          <item color="#042435" label="-1.9337 °C" alpha="255" value="-1.9337"/>
          <item color="#042435" label="-1.9337 °C" alpha="255" value="-1.9337"/>
          <item color="#042537" label="-1.8674 °C" alpha="255" value="-1.8674"/>
          <item color="#042537" label="-1.8674 °C" alpha="255" value="-1.8674"/>
          <item color="#042539" label="-1.8011 °C" alpha="255" value="-1.8011"/>
          <item color="#042539" label="-1.8011 °C" alpha="255" value="-1.8011"/>
          <item color="#05263b" label="-1.7348 °C" alpha="255" value="-1.7348"/>
          <item color="#05263b" label="-1.7348 °C" alpha="255" value="-1.7348"/>
          <item color="#05273d" label="-1.6685 °C" alpha="255" value="-1.6685"/>
          <item color="#05273d" label="-1.6685 °C" alpha="255" value="-1.6685"/>
          <item color="#05273f" label="-1.6022 °C" alpha="255" value="-1.6022"/>
          <item color="#05273f" label="-1.6022 °C" alpha="255" value="-1.6022"/>
          <item color="#052841" label="-1.5359 °C" alpha="255" value="-1.5359"/>
          <item color="#052841" label="-1.5359 °C" alpha="255" value="-1.5359"/>
          <item color="#052943" label="-1.4696 °C" alpha="255" value="-1.4696"/>
          <item color="#052943" label="-1.4696 °C" alpha="255" value="-1.4696"/>
          <item color="#062945" label="-1.4016 °C" alpha="255" value="-1.4016"/>
          <item color="#062945" label="-1.4016 °C" alpha="255" value="-1.4016"/>
          <item color="#062a47" label="-1.3353 °C" alpha="255" value="-1.3353"/>
          <item color="#062a47" label="-1.3353 °C" alpha="255" value="-1.3353"/>
          <item color="#062b49" label="-1.2690 °C" alpha="255" value="-1.269"/>
          <item color="#062b49" label="-1.2690 °C" alpha="255" value="-1.269"/>
          <item color="#072b4b" label="-1.2027 °C" alpha="255" value="-1.2027"/>
          <item color="#072b4b" label="-1.2027 °C" alpha="255" value="-1.2027"/>
          <item color="#072c4d" label="-1.1364 °C" alpha="255" value="-1.1364"/>
          <item color="#072c4d" label="-1.1364 °C" alpha="255" value="-1.1364"/>
          <item color="#072c50" label="-1.0701 °C" alpha="255" value="-1.0701"/>
          <item color="#072c50" label="-1.0701 °C" alpha="255" value="-1.0701"/>
          <item color="#082d52" label="-1.0038 °C" alpha="255" value="-1.0038"/>
          <item color="#082d52" label="-1.0038 °C" alpha="255" value="-1.0038"/>
          <item color="#082e54" label="-0.9375 °C" alpha="255" value="-0.9375"/>
          <item color="#082e54" label="-0.9375 °C" alpha="255" value="-0.9375"/>
          <item color="#092e56" label="-0.8712 °C" alpha="255" value="-0.8712"/>
          <item color="#092e56" label="-0.8712 °C" alpha="255" value="-0.8712"/>
          <item color="#092f59" label="-0.8049 °C" alpha="255" value="-0.8049"/>
          <item color="#092f59" label="-0.8049 °C" alpha="255" value="-0.8049"/>
          <item color="#0a2f5b" label="-0.7386 °C" alpha="255" value="-0.7386"/>
          <item color="#0a2f5b" label="-0.7386 °C" alpha="255" value="-0.7386"/>
          <item color="#0b305d" label="-0.6723 °C" alpha="255" value="-0.6723"/>
          <item color="#0b305d" label="-0.6723 °C" alpha="255" value="-0.6723"/>
          <item color="#0c3060" label="-0.6060 °C" alpha="255" value="-0.606"/>
          <item color="#0c3060" label="-0.6060 °C" alpha="255" value="-0.606"/>
          <item color="#0c3062" label="-0.5397 °C" alpha="255" value="-0.5397"/>
          <item color="#0c3062" label="-0.5397 °C" alpha="255" value="-0.5397"/>
          <item color="#0d3165" label="-0.4734 °C" alpha="255" value="-0.4734"/>
          <item color="#0d3165" label="-0.4734 °C" alpha="255" value="-0.4734"/>
          <item color="#0e3167" label="-0.4054 °C" alpha="255" value="-0.4054"/>
          <item color="#0e3167" label="-0.4054 °C" alpha="255" value="-0.4054"/>
          <item color="#0f326a" label="-0.3391 °C" alpha="255" value="-0.3391"/>
          <item color="#0f326a" label="-0.3391 °C" alpha="255" value="-0.3391"/>
          <item color="#10326c" label="-0.2728 °C" alpha="255" value="-0.2728"/>
          <item color="#10326c" label="-0.2728 °C" alpha="255" value="-0.2728"/>
          <item color="#12326f" label="-0.2065 °C" alpha="255" value="-0.2065"/>
          <item color="#12326f" label="-0.2065 °C" alpha="255" value="-0.2065"/>
          <item color="#133372" label="-0.1402 °C" alpha="255" value="-0.1402"/>
          <item color="#133372" label="-0.1402 °C" alpha="255" value="-0.1402"/>
          <item color="#143374" label="-0.0739 °C" alpha="255" value="-0.0739000000000001"/>
          <item color="#143374" label="-0.0739 °C" alpha="255" value="-0.0739000000000001"/>
          <item color="#163377" label="-0.0076 °C" alpha="255" value="-0.00760000000000005"/>
          <item color="#163377" label="-0.0076 °C" alpha="255" value="-0.00760000000000005"/>
          <item color="#17337a" label="0.0587 °C" alpha="255" value="0.0587"/>
          <item color="#17337a" label="0.0587 °C" alpha="255" value="0.0587"/>
          <item color="#19337c" label="0.1250 °C" alpha="255" value="0.125"/>
          <item color="#19337c" label="0.1250 °C" alpha="255" value="0.125"/>
          <item color="#1a347f" label="0.1913 °C" alpha="255" value="0.1913"/>
          <item color="#1a347f" label="0.1913 °C" alpha="255" value="0.1913"/>
          <item color="#1c3482" label="0.2576 °C" alpha="255" value="0.2576"/>
          <item color="#1c3482" label="0.2576 °C" alpha="255" value="0.2576"/>
          <item color="#1e3484" label="0.3239 °C" alpha="255" value="0.3239"/>
          <item color="#1e3484" label="0.3239 °C" alpha="255" value="0.3239"/>
          <item color="#1f3487" label="0.3902 °C" alpha="255" value="0.3902"/>
          <item color="#1f3487" label="0.3902 °C" alpha="255" value="0.3902"/>
          <item color="#21348a" label="0.4565 °C" alpha="255" value="0.4565"/>
          <item color="#21348a" label="0.4565 °C" alpha="255" value="0.4565"/>
          <item color="#23348c" label="0.5228 °C" alpha="255" value="0.5228"/>
          <item color="#23348c" label="0.5228 °C" alpha="255" value="0.5228"/>
          <item color="#25348f" label="0.5891 °C" alpha="255" value="0.5891"/>
          <item color="#25348f" label="0.5891 °C" alpha="255" value="0.5891"/>
          <item color="#273491" label="0.6554 °C" alpha="255" value="0.6554"/>
          <item color="#273491" label="0.6554 °C" alpha="255" value="0.6554"/>
          <item color="#2a3393" label="0.7234 °C" alpha="255" value="0.7234"/>
          <item color="#2a3393" label="0.7234 °C" alpha="255" value="0.7234"/>
          <item color="#2c3395" label="0.7897 °C" alpha="255" value="0.7897"/>
          <item color="#2c3395" label="0.7897 °C" alpha="255" value="0.7897"/>
          <item color="#2e3397" label="0.8560 °C" alpha="255" value="0.856"/>
          <item color="#2e3397" label="0.8560 °C" alpha="255" value="0.856"/>
          <item color="#303399" label="0.9223 °C" alpha="255" value="0.9223"/>
          <item color="#303399" label="0.9223 °C" alpha="255" value="0.9223"/>
          <item color="#33339b" label="0.9886 °C" alpha="255" value="0.9886"/>
          <item color="#33339b" label="0.9886 °C" alpha="255" value="0.9886"/>
          <item color="#35339c" label="1.0549 °C" alpha="255" value="1.0549"/>
          <item color="#35339c" label="1.0549 °C" alpha="255" value="1.0549"/>
          <item color="#37339d" label="1.1212 °C" alpha="255" value="1.1212"/>
          <item color="#37339d" label="1.1212 °C" alpha="255" value="1.1212"/>
          <item color="#39339e" label="1.1875 °C" alpha="255" value="1.1875"/>
          <item color="#39339e" label="1.1875 °C" alpha="255" value="1.1875"/>
          <item color="#3c339f" label="1.2538 °C" alpha="255" value="1.2538"/>
          <item color="#3c339f" label="1.2538 °C" alpha="255" value="1.2538"/>
          <item color="#3e349f" label="1.3201 °C" alpha="255" value="1.3201"/>
          <item color="#3e349f" label="1.3201 °C" alpha="255" value="1.3201"/>
          <item color="#40349f" label="1.3864 °C" alpha="255" value="1.3864"/>
          <item color="#40349f" label="1.3864 °C" alpha="255" value="1.3864"/>
          <item color="#4234a0" label="1.4527 °C" alpha="255" value="1.4527"/>
          <item color="#4234a0" label="1.4527 °C" alpha="255" value="1.4527"/>
          <item color="#4435a0" label="1.5190 °C" alpha="255" value="1.519"/>
          <item color="#4435a0" label="1.5190 °C" alpha="255" value="1.519"/>
          <item color="#4635a0" label="1.5853 °C" alpha="255" value="1.5853"/>
          <item color="#4635a0" label="1.5853 °C" alpha="255" value="1.5853"/>
          <item color="#4736a0" label="1.6516 °C" alpha="255" value="1.6516"/>
          <item color="#4736a0" label="1.6516 °C" alpha="255" value="1.6516"/>
          <item color="#49369f" label="1.7196 °C" alpha="255" value="1.7196"/>
          <item color="#49369f" label="1.7196 °C" alpha="255" value="1.7196"/>
          <item color="#4b379f" label="1.7859 °C" alpha="255" value="1.7859"/>
          <item color="#4b379f" label="1.7859 °C" alpha="255" value="1.7859"/>
          <item color="#4d379f" label="1.8522 °C" alpha="255" value="1.8522"/>
          <item color="#4d379f" label="1.8522 °C" alpha="255" value="1.8522"/>
          <item color="#4e389e" label="1.9185 °C" alpha="255" value="1.9185"/>
          <item color="#4e389e" label="1.9185 °C" alpha="255" value="1.9185"/>
          <item color="#50399e" label="1.9848 °C" alpha="255" value="1.9848"/>
          <item color="#50399e" label="1.9848 °C" alpha="255" value="1.9848"/>
          <item color="#52399d" label="2.0511 °C" alpha="255" value="2.0511"/>
          <item color="#52399d" label="2.0511 °C" alpha="255" value="2.0511"/>
          <item color="#533a9d" label="2.1174 °C" alpha="255" value="2.1174"/>
          <item color="#533a9d" label="2.1174 °C" alpha="255" value="2.1174"/>
          <item color="#553b9d" label="2.1837 °C" alpha="255" value="2.1837"/>
          <item color="#553b9d" label="2.1837 °C" alpha="255" value="2.1837"/>
          <item color="#563b9c" label="2.2500 °C" alpha="255" value="2.25"/>
          <item color="#563b9c" label="2.2500 °C" alpha="255" value="2.25"/>
          <item color="#583c9c" label="2.3163 °C" alpha="255" value="2.3163"/>
          <item color="#583c9c" label="2.3163 °C" alpha="255" value="2.3163"/>
          <item color="#593d9b" label="2.3826 °C" alpha="255" value="2.3826"/>
          <item color="#593d9b" label="2.3826 °C" alpha="255" value="2.3826"/>
          <item color="#5b3d9b" label="2.4489 °C" alpha="255" value="2.4489"/>
          <item color="#5b3d9b" label="2.4489 °C" alpha="255" value="2.4489"/>
          <item color="#5c3e9a" label="2.5152 °C" alpha="255" value="2.5152"/>
          <item color="#5c3e9a" label="2.5152 °C" alpha="255" value="2.5152"/>
          <item color="#5e3f9a" label="2.5815 °C" alpha="255" value="2.5815"/>
          <item color="#5e3f9a" label="2.5815 °C" alpha="255" value="2.5815"/>
          <item color="#5f3f99" label="2.6478 °C" alpha="255" value="2.6478"/>
          <item color="#5f3f99" label="2.6478 °C" alpha="255" value="2.6478"/>
          <item color="#604099" label="2.7141 °C" alpha="255" value="2.7141"/>
          <item color="#604099" label="2.7141 °C" alpha="255" value="2.7141"/>
          <item color="#624198" label="2.7804 °C" alpha="255" value="2.7804"/>
          <item color="#624198" label="2.7804 °C" alpha="255" value="2.7804"/>
          <item color="#634198" label="2.8484 °C" alpha="255" value="2.8484"/>
          <item color="#634198" label="2.8484 °C" alpha="255" value="2.8484"/>
          <item color="#654297" label="2.9147 °C" alpha="255" value="2.914700000000001"/>
          <item color="#654297" label="2.9147 °C" alpha="255" value="2.914700000000001"/>
          <item color="#664397" label="2.9810 °C" alpha="255" value="2.981"/>
          <item color="#664397" label="2.9810 °C" alpha="255" value="2.981"/>
          <item color="#674396" label="3.0473 °C" alpha="255" value="3.0473"/>
          <item color="#674396" label="3.0473 °C" alpha="255" value="3.0473"/>
          <item color="#694496" label="3.1136 °C" alpha="255" value="3.1136"/>
          <item color="#694496" label="3.1136 °C" alpha="255" value="3.1136"/>
          <item color="#6a4595" label="3.1799 °C" alpha="255" value="3.179900000000001"/>
          <item color="#6a4595" label="3.1799 °C" alpha="255" value="3.179900000000001"/>
          <item color="#6c4595" label="3.2462 °C" alpha="255" value="3.2462"/>
          <item color="#6c4595" label="3.2462 °C" alpha="255" value="3.2462"/>
          <item color="#6d4694" label="3.3125 °C" alpha="255" value="3.3125"/>
          <item color="#6d4694" label="3.3125 °C" alpha="255" value="3.3125"/>
          <item color="#6e4794" label="3.3788 °C" alpha="255" value="3.3788"/>
          <item color="#6e4794" label="3.3788 °C" alpha="255" value="3.3788"/>
          <item color="#704794" label="3.4451 °C" alpha="255" value="3.4451"/>
          <item color="#704794" label="3.4451 °C" alpha="255" value="3.4451"/>
          <item color="#714893" label="3.5114 °C" alpha="255" value="3.5114"/>
          <item color="#714893" label="3.5114 °C" alpha="255" value="3.5114"/>
          <item color="#724893" label="3.5777 °C" alpha="255" value="3.5777"/>
          <item color="#724893" label="3.5777 °C" alpha="255" value="3.5777"/>
          <item color="#744992" label="3.6440 °C" alpha="255" value="3.644"/>
          <item color="#744992" label="3.6440 °C" alpha="255" value="3.644"/>
          <item color="#754a92" label="3.7103 °C" alpha="255" value="3.7103"/>
          <item color="#754a92" label="3.7103 °C" alpha="255" value="3.7103"/>
          <item color="#764a92" label="3.7766 °C" alpha="255" value="3.7766"/>
          <item color="#764a92" label="3.7766 °C" alpha="255" value="3.7766"/>
          <item color="#784b91" label="3.8446 °C" alpha="255" value="3.8446"/>
          <item color="#784b91" label="3.8446 °C" alpha="255" value="3.8446"/>
          <item color="#794b91" label="3.9109 °C" alpha="255" value="3.9109"/>
          <item color="#794b91" label="3.9109 °C" alpha="255" value="3.9109"/>
          <item color="#7a4c91" label="3.9772 °C" alpha="255" value="3.977200000000001"/>
          <item color="#7a4c91" label="3.9772 °C" alpha="255" value="3.977200000000001"/>
          <item color="#7c4d90" label="4.0435 °C" alpha="255" value="4.0435"/>
          <item color="#7c4d90" label="4.0435 °C" alpha="255" value="4.0435"/>
          <item color="#7d4d90" label="4.1098 °C" alpha="255" value="4.1098"/>
          <item color="#7d4d90" label="4.1098 °C" alpha="255" value="4.1098"/>
          <item color="#7e4e90" label="4.1761 °C" alpha="255" value="4.1761"/>
          <item color="#7e4e90" label="4.1761 °C" alpha="255" value="4.1761"/>
          <item color="#804e8f" label="4.2424 °C" alpha="255" value="4.242400000000001"/>
          <item color="#804e8f" label="4.2424 °C" alpha="255" value="4.242400000000001"/>
          <item color="#814f8f" label="4.3087 °C" alpha="255" value="4.3087"/>
          <item color="#814f8f" label="4.3087 °C" alpha="255" value="4.3087"/>
          <item color="#83508f" label="4.3750 °C" alpha="255" value="4.375"/>
          <item color="#83508f" label="4.3750 °C" alpha="255" value="4.375"/>
          <item color="#84508e" label="4.4413 °C" alpha="255" value="4.4413"/>
          <item color="#84508e" label="4.4413 °C" alpha="255" value="4.4413"/>
          <item color="#85518e" label="4.5076 °C" alpha="255" value="4.5076"/>
          <item color="#85518e" label="4.5076 °C" alpha="255" value="4.5076"/>
          <item color="#87518e" label="4.5739 °C" alpha="255" value="4.5739"/>
          <item color="#87518e" label="4.5739 °C" alpha="255" value="4.5739"/>
          <item color="#88528d" label="4.6402 °C" alpha="255" value="4.6402"/>
          <item color="#88528d" label="4.6402 °C" alpha="255" value="4.6402"/>
          <item color="#89528d" label="4.7065 °C" alpha="255" value="4.7065"/>
          <item color="#89528d" label="4.7065 °C" alpha="255" value="4.7065"/>
          <item color="#8b538d" label="4.7728 °C" alpha="255" value="4.7728"/>
          <item color="#8b538d" label="4.7728 °C" alpha="255" value="4.7728"/>
          <item color="#8c538c" label="4.8391 °C" alpha="255" value="4.8391"/>
          <item color="#8c538c" label="4.8391 °C" alpha="255" value="4.8391"/>
          <item color="#8e548c" label="4.9054 °C" alpha="255" value="4.9054"/>
          <item color="#8e548c" label="4.9054 °C" alpha="255" value="4.9054"/>
          <item color="#8f548c" label="4.9734 °C" alpha="255" value="4.9734"/>
          <item color="#8f548c" label="4.9734 °C" alpha="255" value="4.9734"/>
          <item color="#90558b" label="5.0397 °C" alpha="255" value="5.039700000000001"/>
          <item color="#90558b" label="5.0397 °C" alpha="255" value="5.039700000000001"/>
          <item color="#92558b" label="5.1060 °C" alpha="255" value="5.106"/>
          <item color="#92558b" label="5.1060 °C" alpha="255" value="5.106"/>
          <item color="#93568b" label="5.1723 °C" alpha="255" value="5.1723"/>
          <item color="#93568b" label="5.1723 °C" alpha="255" value="5.1723"/>
          <item color="#95568a" label="5.2386 °C" alpha="255" value="5.2386"/>
          <item color="#95568a" label="5.2386 °C" alpha="255" value="5.2386"/>
          <item color="#96578a" label="5.3049 °C" alpha="255" value="5.304900000000001"/>
          <item color="#96578a" label="5.3049 °C" alpha="255" value="5.304900000000001"/>
          <item color="#97578a" label="5.3712 °C" alpha="255" value="5.3712"/>
          <item color="#97578a" label="5.3712 °C" alpha="255" value="5.3712"/>
          <item color="#995889" label="5.4375 °C" alpha="255" value="5.4375"/>
          <item color="#995889" label="5.4375 °C" alpha="255" value="5.4375"/>
          <item color="#9a5889" label="5.5038 °C" alpha="255" value="5.5038"/>
          <item color="#9a5889" label="5.5038 °C" alpha="255" value="5.5038"/>
          <item color="#9c5989" label="5.5701 °C" alpha="255" value="5.5701"/>
          <item color="#9c5989" label="5.5701 °C" alpha="255" value="5.5701"/>
          <item color="#9d5988" label="5.6364 °C" alpha="255" value="5.6364"/>
          <item color="#9d5988" label="5.6364 °C" alpha="255" value="5.6364"/>
          <item color="#9f5a88" label="5.7027 °C" alpha="255" value="5.7027"/>
          <item color="#9f5a88" label="5.7027 °C" alpha="255" value="5.7027"/>
          <item color="#a05a87" label="5.7690 °C" alpha="255" value="5.769"/>
          <item color="#a05a87" label="5.7690 °C" alpha="255" value="5.769"/>
          <item color="#a25b87" label="5.8353 °C" alpha="255" value="5.8353"/>
          <item color="#a25b87" label="5.8353 °C" alpha="255" value="5.8353"/>
          <item color="#a35b86" label="5.9016 °C" alpha="255" value="5.9016"/>
          <item color="#a35b86" label="5.9016 °C" alpha="255" value="5.9016"/>
          <item color="#a55c86" label="5.9696 °C" alpha="255" value="5.9696"/>
          <item color="#a55c86" label="5.9696 °C" alpha="255" value="5.9696"/>
          <item color="#a65c86" label="6.0359 °C" alpha="255" value="6.0359"/>
          <item color="#a65c86" label="6.0359 °C" alpha="255" value="6.0359"/>
          <item color="#a85d85" label="6.1022 °C" alpha="255" value="6.1022"/>
          <item color="#a85d85" label="6.1022 °C" alpha="255" value="6.1022"/>
          <item color="#a95d84" label="6.1685 °C" alpha="255" value="6.1685"/>
          <item color="#a95d84" label="6.1685 °C" alpha="255" value="6.1685"/>
          <item color="#ab5d84" label="6.2348 °C" alpha="255" value="6.2348"/>
          <item color="#ab5d84" label="6.2348 °C" alpha="255" value="6.2348"/>
          <item color="#ac5e83" label="6.3011 °C" alpha="255" value="6.3011"/>
          <item color="#ac5e83" label="6.3011 °C" alpha="255" value="6.3011"/>
          <item color="#ae5e83" label="6.3674 °C" alpha="255" value="6.3674"/>
          <item color="#ae5e83" label="6.3674 °C" alpha="255" value="6.3674"/>
          <item color="#af5f82" label="6.4337 °C" alpha="255" value="6.4337"/>
          <item color="#af5f82" label="6.4337 °C" alpha="255" value="6.4337"/>
          <item color="#b15f82" label="6.5000 °C" alpha="255" value="6.5"/>
          <item color="#b15f82" label="6.5000 °C" alpha="255" value="6.5"/>
          <item color="#b26081" label="6.5663 °C" alpha="255" value="6.5663"/>
          <item color="#b26081" label="6.5663 °C" alpha="255" value="6.5663"/>
          <item color="#b46080" label="6.6326 °C" alpha="255" value="6.6326"/>
          <item color="#b46080" label="6.6326 °C" alpha="255" value="6.6326"/>
          <item color="#b56180" label="6.6989 °C" alpha="255" value="6.6989"/>
          <item color="#b56180" label="6.6989 °C" alpha="255" value="6.6989"/>
          <item color="#b7617f" label="6.7652 °C" alpha="255" value="6.765199999999998"/>
          <item color="#b7617f" label="6.7652 °C" alpha="255" value="6.765199999999998"/>
          <item color="#b8627e" label="6.8315 °C" alpha="255" value="6.8315"/>
          <item color="#b8627e" label="6.8315 °C" alpha="255" value="6.8315"/>
          <item color="#ba627e" label="6.8978 °C" alpha="255" value="6.8978"/>
          <item color="#ba627e" label="6.8978 °C" alpha="255" value="6.8978"/>
          <item color="#bb627d" label="6.9641 °C" alpha="255" value="6.9641"/>
          <item color="#bb627d" label="6.9641 °C" alpha="255" value="6.9641"/>
          <item color="#bd637c" label="7.0304 °C" alpha="255" value="7.0304"/>
          <item color="#bd637c" label="7.0304 °C" alpha="255" value="7.0304"/>
          <item color="#be637b" label="7.0984 °C" alpha="255" value="7.0984"/>
          <item color="#be637b" label="7.0984 °C" alpha="255" value="7.0984"/>
          <item color="#c0647b" label="7.1647 °C" alpha="255" value="7.1647"/>
          <item color="#c0647b" label="7.1647 °C" alpha="255" value="7.1647"/>
          <item color="#c1647a" label="7.2310 °C" alpha="255" value="7.231"/>
          <item color="#c1647a" label="7.2310 °C" alpha="255" value="7.231"/>
          <item color="#c36579" label="7.2973 °C" alpha="255" value="7.297300000000002"/>
          <item color="#c36579" label="7.2973 °C" alpha="255" value="7.297300000000002"/>
          <item color="#c46578" label="7.3636 °C" alpha="255" value="7.3636"/>
          <item color="#c46578" label="7.3636 °C" alpha="255" value="7.3636"/>
          <item color="#c66677" label="7.4299 °C" alpha="255" value="7.4299"/>
          <item color="#c66677" label="7.4299 °C" alpha="255" value="7.4299"/>
          <item color="#c76676" label="7.4962 °C" alpha="255" value="7.4962"/>
          <item color="#c76676" label="7.4962 °C" alpha="255" value="7.4962"/>
          <item color="#c96775" label="7.5625 °C" alpha="255" value="7.5625"/>
          <item color="#c96775" label="7.5625 °C" alpha="255" value="7.5625"/>
          <item color="#ca6774" label="7.6288 °C" alpha="255" value="7.6288"/>
          <item color="#ca6774" label="7.6288 °C" alpha="255" value="7.6288"/>
          <item color="#cc6873" label="7.6951 °C" alpha="255" value="7.6951"/>
          <item color="#cc6873" label="7.6951 °C" alpha="255" value="7.6951"/>
          <item color="#cd6872" label="7.7614 °C" alpha="255" value="7.7614"/>
          <item color="#cd6872" label="7.7614 °C" alpha="255" value="7.7614"/>
          <item color="#ce6971" label="7.8277 °C" alpha="255" value="7.827699999999998"/>
          <item color="#ce6971" label="7.8277 °C" alpha="255" value="7.827699999999998"/>
          <item color="#d06970" label="7.8940 °C" alpha="255" value="7.894"/>
          <item color="#d06970" label="7.8940 °C" alpha="255" value="7.894"/>
          <item color="#d16a6f" label="7.9603 °C" alpha="255" value="7.9603"/>
          <item color="#d16a6f" label="7.9603 °C" alpha="255" value="7.9603"/>
          <item color="#d36a6e" label="8.0266 °C" alpha="255" value="8.0266"/>
          <item color="#d36a6e" label="8.0266 °C" alpha="255" value="8.0266"/>
          <item color="#d46b6d" label="8.0946 °C" alpha="255" value="8.0946"/>
          <item color="#d46b6d" label="8.0946 °C" alpha="255" value="8.0946"/>
          <item color="#d66c6c" label="8.1609 °C" alpha="255" value="8.1609"/>
          <item color="#d66c6c" label="8.1609 °C" alpha="255" value="8.1609"/>
          <item color="#d76c6b" label="8.2272 °C" alpha="255" value="8.2272"/>
          <item color="#d76c6b" label="8.2272 °C" alpha="255" value="8.2272"/>
          <item color="#d86d6a" label="8.2935 °C" alpha="255" value="8.2935"/>
          <item color="#d86d6a" label="8.2935 °C" alpha="255" value="8.2935"/>
          <item color="#da6e69" label="8.3598 °C" alpha="255" value="8.359800000000002"/>
          <item color="#da6e69" label="8.3598 °C" alpha="255" value="8.359800000000002"/>
          <item color="#db6e68" label="8.4261 °C" alpha="255" value="8.4261"/>
          <item color="#db6e68" label="8.4261 °C" alpha="255" value="8.4261"/>
          <item color="#dc6f66" label="8.4924 °C" alpha="255" value="8.4924"/>
          <item color="#dc6f66" label="8.4924 °C" alpha="255" value="8.4924"/>
          <item color="#de7065" label="8.5587 °C" alpha="255" value="8.5587"/>
          <item color="#de7065" label="8.5587 °C" alpha="255" value="8.5587"/>
          <item color="#df7064" label="8.6250 °C" alpha="255" value="8.625"/>
          <item color="#df7064" label="8.6250 °C" alpha="255" value="8.625"/>
          <item color="#e07163" label="8.6913 °C" alpha="255" value="8.6913"/>
          <item color="#e07163" label="8.6913 °C" alpha="255" value="8.6913"/>
          <item color="#e17262" label="8.7576 °C" alpha="255" value="8.7576"/>
          <item color="#e17262" label="8.7576 °C" alpha="255" value="8.7576"/>
          <item color="#e37260" label="8.8239 °C" alpha="255" value="8.8239"/>
          <item color="#e37260" label="8.8239 °C" alpha="255" value="8.8239"/>
          <item color="#e4735f" label="8.8902 °C" alpha="255" value="8.890199999999998"/>
          <item color="#e4735f" label="8.8902 °C" alpha="255" value="8.890199999999998"/>
          <item color="#e5745e" label="8.9565 °C" alpha="255" value="8.9565"/>
          <item color="#e5745e" label="8.9565 °C" alpha="255" value="8.9565"/>
          <item color="#e6755d" label="9.0228 °C" alpha="255" value="9.0228"/>
          <item color="#e6755d" label="9.0228 °C" alpha="255" value="9.0228"/>
          <item color="#e7765b" label="9.0891 °C" alpha="255" value="9.0891"/>
          <item color="#e7765b" label="9.0891 °C" alpha="255" value="9.0891"/>
          <item color="#e8775a" label="9.1554 °C" alpha="255" value="9.1554"/>
          <item color="#e8775a" label="9.1554 °C" alpha="255" value="9.1554"/>
          <item color="#ea7859" label="9.2234 °C" alpha="255" value="9.2234"/>
          <item color="#ea7859" label="9.2234 °C" alpha="255" value="9.2234"/>
          <item color="#eb7958" label="9.2897 °C" alpha="255" value="9.2897"/>
          <item color="#eb7958" label="9.2897 °C" alpha="255" value="9.2897"/>
          <item color="#ec7956" label="9.3560 °C" alpha="255" value="9.356"/>
          <item color="#ec7956" label="9.3560 °C" alpha="255" value="9.356"/>
          <item color="#ed7a55" label="9.4223 °C" alpha="255" value="9.422300000000002"/>
          <item color="#ed7a55" label="9.4223 °C" alpha="255" value="9.422300000000002"/>
          <item color="#ee7b54" label="9.4886 °C" alpha="255" value="9.4886"/>
          <item color="#ee7b54" label="9.4886 °C" alpha="255" value="9.4886"/>
          <item color="#ee7d53" label="9.5549 °C" alpha="255" value="9.5549"/>
          <item color="#ee7d53" label="9.5549 °C" alpha="255" value="9.5549"/>
          <item color="#ef7e52" label="9.6212 °C" alpha="255" value="9.6212"/>
          <item color="#ef7e52" label="9.6212 °C" alpha="255" value="9.6212"/>
          <item color="#f07f50" label="9.6875 °C" alpha="255" value="9.6875"/>
          <item color="#f07f50" label="9.6875 °C" alpha="255" value="9.6875"/>
          <item color="#f1804f" label="9.7538 °C" alpha="255" value="9.7538"/>
          <item color="#f1804f" label="9.7538 °C" alpha="255" value="9.7538"/>
          <item color="#f2814e" label="9.8201 °C" alpha="255" value="9.8201"/>
          <item color="#f2814e" label="9.8201 °C" alpha="255" value="9.8201"/>
          <item color="#f3824d" label="9.8864 °C" alpha="255" value="9.8864"/>
          <item color="#f3824d" label="9.8864 °C" alpha="255" value="9.8864"/>
          <item color="#f3834c" label="9.9527 °C" alpha="255" value="9.952699999999998"/>
          <item color="#f3834c" label="9.9527 °C" alpha="255" value="9.952699999999998"/>
          <item color="#f4854b" label="10.0190 °C" alpha="255" value="10.019"/>
          <item color="#f4854b" label="10.0190 °C" alpha="255" value="10.019"/>
          <item color="#f5864a" label="10.0853 °C" alpha="255" value="10.0853"/>
          <item color="#f5864a" label="10.0853 °C" alpha="255" value="10.0853"/>
          <item color="#f58749" label="10.1516 °C" alpha="255" value="10.1516"/>
          <item color="#f58749" label="10.1516 °C" alpha="255" value="10.1516"/>
          <item color="#f68848" label="10.2196 °C" alpha="255" value="10.2196"/>
          <item color="#f68848" label="10.2196 °C" alpha="255" value="10.2196"/>
          <item color="#f68a47" label="10.2859 °C" alpha="255" value="10.2859"/>
          <item color="#f68a47" label="10.2859 °C" alpha="255" value="10.2859"/>
          <item color="#f78b46" label="10.3522 °C" alpha="255" value="10.3522"/>
          <item color="#f78b46" label="10.3522 °C" alpha="255" value="10.3522"/>
          <item color="#f78c45" label="10.4185 °C" alpha="255" value="10.4185"/>
          <item color="#f78c45" label="10.4185 °C" alpha="255" value="10.4185"/>
          <item color="#f88e44" label="10.4848 °C" alpha="255" value="10.484800000000002"/>
          <item color="#f88e44" label="10.4848 °C" alpha="255" value="10.484800000000002"/>
          <item color="#f88f43" label="10.5511 °C" alpha="255" value="10.5511"/>
          <item color="#f88f43" label="10.5511 °C" alpha="255" value="10.5511"/>
          <item color="#f99143" label="10.6174 °C" alpha="255" value="10.6174"/>
          <item color="#f99143" label="10.6174 °C" alpha="255" value="10.6174"/>
          <item color="#f99242" label="10.6837 °C" alpha="255" value="10.6837"/>
          <item color="#f99242" label="10.6837 °C" alpha="255" value="10.6837"/>
          <item color="#f99341" label="10.7500 °C" alpha="255" value="10.75"/>
          <item color="#f99341" label="10.7500 °C" alpha="255" value="10.75"/>
          <item color="#fa9541" label="10.8163 °C" alpha="255" value="10.8163"/>
          <item color="#fa9541" label="10.8163 °C" alpha="255" value="10.8163"/>
          <item color="#fa9640" label="10.8826 °C" alpha="255" value="10.8826"/>
          <item color="#fa9640" label="10.8826 °C" alpha="255" value="10.8826"/>
          <item color="#fa983f" label="10.9489 °C" alpha="255" value="10.9489"/>
          <item color="#fa983f" label="10.9489 °C" alpha="255" value="10.9489"/>
          <item color="#fb993f" label="11.0152 °C" alpha="255" value="11.015199999999998"/>
          <item color="#fb993f" label="11.0152 °C" alpha="255" value="11.015199999999998"/>
          <item color="#fb9b3e" label="11.0815 °C" alpha="255" value="11.0815"/>
          <item color="#fb9b3e" label="11.0815 °C" alpha="255" value="11.0815"/>
          <item color="#fb9c3e" label="11.1478 °C" alpha="255" value="11.1478"/>
          <item color="#fb9c3e" label="11.1478 °C" alpha="255" value="11.1478"/>
          <item color="#fb9e3e" label="11.2141 °C" alpha="255" value="11.2141"/>
          <item color="#fb9e3e" label="11.2141 °C" alpha="255" value="11.2141"/>
          <item color="#fb9f3d" label="11.2804 °C" alpha="255" value="11.2804"/>
          <item color="#fb9f3d" label="11.2804 °C" alpha="255" value="11.2804"/>
          <item color="#fba13d" label="11.3484 °C" alpha="255" value="11.3484"/>
          <item color="#fba13d" label="11.3484 °C" alpha="255" value="11.3484"/>
          <item color="#fca33d" label="11.4147 °C" alpha="255" value="11.4147"/>
          <item color="#fca33d" label="11.4147 °C" alpha="255" value="11.4147"/>
          <item color="#fca43d" label="11.4810 °C" alpha="255" value="11.481"/>
          <item color="#fca43d" label="11.4810 °C" alpha="255" value="11.481"/>
          <item color="#fca63c" label="11.5473 °C" alpha="255" value="11.547300000000002"/>
          <item color="#fca63c" label="11.5473 °C" alpha="255" value="11.547300000000002"/>
          <item color="#fca73c" label="11.6136 °C" alpha="255" value="11.6136"/>
          <item color="#fca73c" label="11.6136 °C" alpha="255" value="11.6136"/>
          <item color="#fca93c" label="11.6799 °C" alpha="255" value="11.6799"/>
          <item color="#fca93c" label="11.6799 °C" alpha="255" value="11.6799"/>
          <item color="#fcaa3c" label="11.7462 °C" alpha="255" value="11.7462"/>
          <item color="#fcaa3c" label="11.7462 °C" alpha="255" value="11.7462"/>
          <item color="#fcac3c" label="11.8125 °C" alpha="255" value="11.8125"/>
          <item color="#fcac3c" label="11.8125 °C" alpha="255" value="11.8125"/>
          <item color="#fcae3c" label="11.8788 °C" alpha="255" value="11.8788"/>
          <item color="#fcae3c" label="11.8788 °C" alpha="255" value="11.8788"/>
          <item color="#fcaf3c" label="11.9451 °C" alpha="255" value="11.9451"/>
          <item color="#fcaf3c" label="11.9451 °C" alpha="255" value="11.9451"/>
          <item color="#fcb13c" label="12.0114 °C" alpha="255" value="12.0114"/>
          <item color="#fcb13c" label="12.0114 °C" alpha="255" value="12.0114"/>
          <item color="#fbb23d" label="12.0777 °C" alpha="255" value="12.077699999999998"/>
          <item color="#fbb23d" label="12.0777 °C" alpha="255" value="12.077699999999998"/>
          <item color="#fbb43d" label="12.1440 °C" alpha="255" value="12.144"/>
          <item color="#fbb43d" label="12.1440 °C" alpha="255" value="12.144"/>
          <item color="#fbb63d" label="12.2103 °C" alpha="255" value="12.2103"/>
          <item color="#fbb63d" label="12.2103 °C" alpha="255" value="12.2103"/>
          <item color="#fbb73d" label="12.2766 °C" alpha="255" value="12.2766"/>
          <item color="#fbb73d" label="12.2766 °C" alpha="255" value="12.2766"/>
          <item color="#fbb93e" label="12.3446 °C" alpha="255" value="12.3446"/>
          <item color="#fbb93e" label="12.3446 °C" alpha="255" value="12.3446"/>
          <item color="#fbbb3e" label="12.4109 °C" alpha="255" value="12.4109"/>
          <item color="#fbbb3e" label="12.4109 °C" alpha="255" value="12.4109"/>
          <item color="#fbbc3e" label="12.4772 °C" alpha="255" value="12.4772"/>
          <item color="#fbbc3e" label="12.4772 °C" alpha="255" value="12.4772"/>
          <item color="#fabe3f" label="12.5435 °C" alpha="255" value="12.5435"/>
          <item color="#fabe3f" label="12.5435 °C" alpha="255" value="12.5435"/>
          <item color="#fabf3f" label="12.6098 °C" alpha="255" value="12.609800000000002"/>
          <item color="#fabf3f" label="12.6098 °C" alpha="255" value="12.609800000000002"/>
          <item color="#fac140" label="12.6761 °C" alpha="255" value="12.6761"/>
          <item color="#fac140" label="12.6761 °C" alpha="255" value="12.6761"/>
          <item color="#fac340" label="12.7424 °C" alpha="255" value="12.7424"/>
          <item color="#fac340" label="12.7424 °C" alpha="255" value="12.7424"/>
          <item color="#f9c441" label="12.8087 °C" alpha="255" value="12.8087"/>
          <item color="#f9c441" label="12.8087 °C" alpha="255" value="12.8087"/>
          <item color="#f9c641" label="12.8750 °C" alpha="255" value="12.875"/>
          <item color="#f9c641" label="12.8750 °C" alpha="255" value="12.875"/>
          <item color="#f9c842" label="12.9413 °C" alpha="255" value="12.9413"/>
          <item color="#f9c842" label="12.9413 °C" alpha="255" value="12.9413"/>
          <item color="#f8c943" label="13.0076 °C" alpha="255" value="13.0076"/>
          <item color="#f8c943" label="13.0076 °C" alpha="255" value="13.0076"/>
          <item color="#f8cb43" label="13.0739 °C" alpha="255" value="13.0739"/>
          <item color="#f8cb43" label="13.0739 °C" alpha="255" value="13.0739"/>
          <item color="#f8cd44" label="13.1402 °C" alpha="255" value="13.140199999999998"/>
          <item color="#f8cd44" label="13.1402 °C" alpha="255" value="13.140199999999998"/>
          <item color="#f7ce45" label="13.2065 °C" alpha="255" value="13.2065"/>
          <item color="#f7ce45" label="13.2065 °C" alpha="255" value="13.2065"/>
          <item color="#f7d045" label="13.2728 °C" alpha="255" value="13.2728"/>
          <item color="#f7d045" label="13.2728 °C" alpha="255" value="13.2728"/>
          <item color="#f7d246" label="13.3391 °C" alpha="255" value="13.3391"/>
          <item color="#f7d246" label="13.3391 °C" alpha="255" value="13.3391"/>
          <item color="#f6d347" label="13.4054 °C" alpha="255" value="13.4054"/>
          <item color="#f6d347" label="13.4054 °C" alpha="255" value="13.4054"/>
          <item color="#f6d547" label="13.4734 °C" alpha="255" value="13.4734"/>
          <item color="#f6d547" label="13.4734 °C" alpha="255" value="13.4734"/>
          <item color="#f5d748" label="13.5397 °C" alpha="255" value="13.5397"/>
          <item color="#f5d748" label="13.5397 °C" alpha="255" value="13.5397"/>
          <item color="#f5d849" label="13.6060 °C" alpha="255" value="13.606"/>
          <item color="#f5d849" label="13.6060 °C" alpha="255" value="13.606"/>
          <item color="#f4da4a" label="13.6723 °C" alpha="255" value="13.672300000000002"/>
          <item color="#f4da4a" label="13.6723 °C" alpha="255" value="13.672300000000002"/>
          <item color="#f4dc4b" label="13.7386 °C" alpha="255" value="13.7386"/>
          <item color="#f4dc4b" label="13.7386 °C" alpha="255" value="13.7386"/>
          <item color="#f3dd4b" label="13.8049 °C" alpha="255" value="13.8049"/>
          <item color="#f3dd4b" label="13.8049 °C" alpha="255" value="13.8049"/>
          <item color="#f3df4c" label="13.8712 °C" alpha="255" value="13.8712"/>
          <item color="#f3df4c" label="13.8712 °C" alpha="255" value="13.8712"/>
          <item color="#f2e14d" label="13.9375 °C" alpha="255" value="13.9375"/>
          <item color="#f2e14d" label="13.9375 °C" alpha="255" value="13.9375"/>
          <item color="#f2e24e" label="14.0038 °C" alpha="255" value="14.003800000000002"/>
          <item color="#f2e24e" label="14.0038 °C" alpha="255" value="14.003800000000002"/>
          <item color="#f1e44f" label="14.0701 °C" alpha="255" value="14.0701"/>
          <item color="#f1e44f" label="14.0701 °C" alpha="255" value="14.0701"/>
          <item color="#f1e650" label="14.1364 °C" alpha="255" value="14.136400000000002"/>
          <item color="#f1e650" label="14.1364 °C" alpha="255" value="14.136400000000002"/>
          <item color="#f0e851" label="14.2027 °C" alpha="255" value="14.2027"/>
          <item color="#f0e851" label="14.2027 °C" alpha="255" value="14.2027"/>
          <item color="#efe951" label="14.2690 °C" alpha="255" value="14.268999999999998"/>
          <item color="#efe951" label="14.2690 °C" alpha="255" value="14.268999999999998"/>
          <item color="#efeb52" label="14.3353 °C" alpha="255" value="14.3353"/>
          <item color="#efeb52" label="14.3353 °C" alpha="255" value="14.3353"/>
          <item color="#eeed53" label="14.4016 °C" alpha="255" value="14.401599999999998"/>
          <item color="#eeed53" label="14.4016 °C" alpha="255" value="14.401599999999998"/>
          <item color="#edee54" label="14.4696 °C" alpha="255" value="14.4696"/>
          <item color="#edee54" label="14.4696 °C" alpha="255" value="14.4696"/>
          <item color="#edf055" label="14.5359 °C" alpha="255" value="14.535900000000002"/>
          <item color="#edf055" label="14.5359 °C" alpha="255" value="14.535900000000002"/>
          <item color="#ecf256" label="14.6022 °C" alpha="255" value="14.6022"/>
          <item color="#ecf256" label="14.6022 °C" alpha="255" value="14.6022"/>
          <item color="#ebf457" label="14.6685 °C" alpha="255" value="14.668500000000002"/>
          <item color="#ebf457" label="14.6685 °C" alpha="255" value="14.668500000000002"/>
          <item color="#eaf558" label="14.7348 °C" alpha="255" value="14.7348"/>
          <item color="#eaf558" label="14.7348 °C" alpha="255" value="14.7348"/>
          <item color="#eaf759" label="14.8011 °C" alpha="255" value="14.801099999999998"/>
          <item color="#eaf759" label="14.8011 °C" alpha="255" value="14.801099999999998"/>
          <item color="#e9f95a" label="14.8674 °C" alpha="255" value="14.8674"/>
          <item color="#e9f95a" label="14.8674 °C" alpha="255" value="14.8674"/>
          <item color="#e8fa5b" label="14.9337 °C" alpha="255" value="14.933699999999998"/>
          <item color="#e8fa5b" label="14.9337 °C" alpha="255" value="14.933699999999998"/>
          <item color="#e8fa5b" label="15.0000 °C" alpha="255" value="15"/>
          <rampLegendSettings direction="0" orientation="1" useContinuousLegend="1" suffix=" °C" minimumLabel="" maximumLabel="" prefix="">
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

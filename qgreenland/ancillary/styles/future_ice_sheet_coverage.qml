<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="3.28.6-Firenze" hasScaleBasedVisibilityFlag="0" styleCategories="AllStyleCategories" maxScale="0" minScale="1e+08">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
    <Private>0</Private>
  </flags>
  <temporal enabled="0" fetchMode="0" mode="0">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <elevation enabled="0" symbology="Line" zscale="1" band="1" zoffset="0">
    <data-defined-properties>
      <Option type="Map">
        <Option name="name" type="QString" value=""/>
        <Option name="properties"/>
        <Option name="type" type="QString" value="collection"/>
      </Option>
    </data-defined-properties>
    <profileLineSymbol>
      <symbol name="" is_animated="0" type="line" frame_rate="10" clip_to_extent="1" alpha="1" force_rhr="0">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer enabled="1" pass="0" locked="0" class="SimpleLine">
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
            <Option name="line_color" type="QString" value="190,207,80,255"/>
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
      <symbol name="" is_animated="0" type="fill" frame_rate="10" clip_to_extent="1" alpha="1" force_rhr="0">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer enabled="1" pass="0" locked="0" class="SimpleFill">
          <Option type="Map">
            <Option name="border_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="color" type="QString" value="190,207,80,255"/>
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
      <resampling enabled="false" zoomedOutResamplingMethod="nearestNeighbour" zoomedInResamplingMethod="nearestNeighbour" maxOversampling="2"/>
    </provider>
    <rasterrenderer alphaBand="-1" nodataColor="" classificationMax="100" type="singlebandpseudocolor" band="1" opacity="1" classificationMin="0">
      <rasterTransparency>
        <singleValuePixelList>
          <pixelListEntry min="0" max="16" percentTransparent="100"/>
        </singleValuePixelList>
      </rasterTransparency>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <rastershader>
        <colorrampshader clip="0" colorRampType="INTERPOLATED" maximumValue="100" minimumValue="0" labelPrecision="2" classificationMode="1">
          <colorramp name="[source]" type="gradient">
            <Option type="Map">
              <Option name="color1" type="QString" value="4,6,19,255"/>
              <Option name="color2" type="QString" value="234,253,253,255"/>
              <Option name="direction" type="QString" value="ccw"/>
              <Option name="discrete" type="QString" value="0"/>
              <Option name="rampType" type="QString" value="gradient"/>
              <Option name="spec" type="QString" value="rgb"/>
              <Option name="stops" type="QString" value="0.0039;4,6,19,255;rgb;ccw:0.0039;5,6,20,255;rgb;ccw:0.0078;5,6,20,255;rgb;ccw:0.0078;5,7,21,255;rgb;ccw:0.0117;5,7,21,255;rgb;ccw:0.0117;6,8,23,255;rgb;ccw:0.0156;6,8,23,255;rgb;ccw:0.0156;7,9,24,255;rgb;ccw:0.0195;7,9,24,255;rgb;ccw:0.0195;8,10,26,255;rgb;ccw:0.0234;8,10,26,255;rgb;ccw:0.0234;9,11,27,255;rgb;ccw:0.0273;9,11,27,255;rgb;ccw:0.0273;10,12,29,255;rgb;ccw:0.0312;10,12,29,255;rgb;ccw:0.0312;11,13,30,255;rgb;ccw:0.0352;11,13,30,255;rgb;ccw:0.0352;12,13,31,255;rgb;ccw:0.0391;12,13,31,255;rgb;ccw:0.0391;13,14,33,255;rgb;ccw:0.043;13,14,33,255;rgb;ccw:0.043;14,15,34,255;rgb;ccw:0.0469;14,15,34,255;rgb;ccw:0.0469;15,16,36,255;rgb;ccw:0.0508;15,16,36,255;rgb;ccw:0.0508;16,17,37,255;rgb;ccw:0.0547;16,17,37,255;rgb;ccw:0.0547;17,18,39,255;rgb;ccw:0.0586;17,18,39,255;rgb;ccw:0.0586;18,19,40,255;rgb;ccw:0.0625;18,19,40,255;rgb;ccw:0.0625;19,19,42,255;rgb;ccw:0.0664;19,19,42,255;rgb;ccw:0.0664;20,20,43,255;rgb;ccw:0.0703;20,20,43,255;rgb;ccw:0.0703;21,21,44,255;rgb;ccw:0.0742;21,21,44,255;rgb;ccw:0.0742;22,22,46,255;rgb;ccw:0.0781;22,22,46,255;rgb;ccw:0.0781;23,23,47,255;rgb;ccw:0.082;23,23,47,255;rgb;ccw:0.082;23,24,49,255;rgb;ccw:0.0859;23,24,49,255;rgb;ccw:0.0859;24,24,50,255;rgb;ccw:0.0898;24,24,50,255;rgb;ccw:0.0898;25,25,52,255;rgb;ccw:0.0938;25,25,52,255;rgb;ccw:0.0938;26,26,53,255;rgb;ccw:0.0977;26,26,53,255;rgb;ccw:0.0977;27,27,55,255;rgb;ccw:0.1016;27,27,55,255;rgb;ccw:0.1016;28,28,56,255;rgb;ccw:0.1055;28,28,56,255;rgb;ccw:0.1055;29,28,58,255;rgb;ccw:0.1094;29,28,58,255;rgb;ccw:0.1094;30,29,59,255;rgb;ccw:0.1133;30,29,59,255;rgb;ccw:0.1133;31,30,61,255;rgb;ccw:0.1172;31,30,61,255;rgb;ccw:0.1172;31,31,62,255;rgb;ccw:0.1211;31,31,62,255;rgb;ccw:0.1211;32,31,64,255;rgb;ccw:0.125;32,31,64,255;rgb;ccw:0.125;33,32,65,255;rgb;ccw:0.1289;33,32,65,255;rgb;ccw:0.1289;34,33,67,255;rgb;ccw:0.1328;34,33,67,255;rgb;ccw:0.1328;35,34,68,255;rgb;ccw:0.1367;35,34,68,255;rgb;ccw:0.1367;36,34,70,255;rgb;ccw:0.1406;36,34,70,255;rgb;ccw:0.1406;37,35,71,255;rgb;ccw:0.1445;37,35,71,255;rgb;ccw:0.1445;37,36,73,255;rgb;ccw:0.1484;37,36,73,255;rgb;ccw:0.1484;38,37,74,255;rgb;ccw:0.1523;38,37,74,255;rgb;ccw:0.1523;39,37,76,255;rgb;ccw:0.1562;39,37,76,255;rgb;ccw:0.1562;40,38,78,255;rgb;ccw:0.1602;40,38,78,255;rgb;ccw:0.1602;41,39,79,255;rgb;ccw:0.1641;41,39,79,255;rgb;ccw:0.1641;41,40,81,255;rgb;ccw:0.168;41,40,81,255;rgb;ccw:0.168;42,40,82,255;rgb;ccw:0.1719;42,40,82,255;rgb;ccw:0.1719;43,41,84,255;rgb;ccw:0.1758;43,41,84,255;rgb;ccw:0.1758;44,42,85,255;rgb;ccw:0.1797;44,42,85,255;rgb;ccw:0.1797;44,43,87,255;rgb;ccw:0.1836;44,43,87,255;rgb;ccw:0.1836;45,43,89,255;rgb;ccw:0.1875;45,43,89,255;rgb;ccw:0.1875;46,44,90,255;rgb;ccw:0.1914;46,44,90,255;rgb;ccw:0.1914;47,45,92,255;rgb;ccw:0.1953;47,45,92,255;rgb;ccw:0.1953;47,46,94,255;rgb;ccw:0.1992;47,46,94,255;rgb;ccw:0.1992;48,47,95,255;rgb;ccw:0.2031;48,47,95,255;rgb;ccw:0.2031;49,47,97,255;rgb;ccw:0.207;49,47,97,255;rgb;ccw:0.207;49,48,98,255;rgb;ccw:0.2109;49,48,98,255;rgb;ccw:0.2109;50,49,100,255;rgb;ccw:0.2148;50,49,100,255;rgb;ccw:0.2148;51,50,102,255;rgb;ccw:0.2188;51,50,102,255;rgb;ccw:0.2188;51,50,103,255;rgb;ccw:0.2227;51,50,103,255;rgb;ccw:0.2227;52,51,105,255;rgb;ccw:0.2266;52,51,105,255;rgb;ccw:0.2266;53,52,107,255;rgb;ccw:0.2305;53,52,107,255;rgb;ccw:0.2305;53,53,108,255;rgb;ccw:0.2344;53,53,108,255;rgb;ccw:0.2344;54,53,110,255;rgb;ccw:0.2383;54,53,110,255;rgb;ccw:0.2383;54,54,112,255;rgb;ccw:0.2422;54,54,112,255;rgb;ccw:0.2422;55,55,113,255;rgb;ccw:0.2461;55,55,113,255;rgb;ccw:0.2461;56,56,115,255;rgb;ccw:0.25;56,56,115,255;rgb;ccw:0.25;56,57,117,255;rgb;ccw:0.2539;56,57,117,255;rgb;ccw:0.2539;57,57,118,255;rgb;ccw:0.2578;57,57,118,255;rgb;ccw:0.2578;57,58,120,255;rgb;ccw:0.2617;57,58,120,255;rgb;ccw:0.2617;58,59,122,255;rgb;ccw:0.2656;58,59,122,255;rgb;ccw:0.2656;58,60,123,255;rgb;ccw:0.2695;58,60,123,255;rgb;ccw:0.2695;58,61,125,255;rgb;ccw:0.2734;58,61,125,255;rgb;ccw:0.2734;59,62,127,255;rgb;ccw:0.2773;59,62,127,255;rgb;ccw:0.2773;59,62,128,255;rgb;ccw:0.2812;59,62,128,255;rgb;ccw:0.2812;60,63,130,255;rgb;ccw:0.2852;60,63,130,255;rgb;ccw:0.2852;60,64,132,255;rgb;ccw:0.2891;60,64,132,255;rgb;ccw:0.2891;60,65,133,255;rgb;ccw:0.293;60,65,133,255;rgb;ccw:0.293;61,66,135,255;rgb;ccw:0.2969;61,66,135,255;rgb;ccw:0.2969;61,67,137,255;rgb;ccw:0.3008;61,67,137,255;rgb;ccw:0.3008;61,68,138,255;rgb;ccw:0.3047;61,68,138,255;rgb;ccw:0.3047;62,69,140,255;rgb;ccw:0.3086;62,69,140,255;rgb;ccw:0.3086;62,70,141,255;rgb;ccw:0.3125;62,70,141,255;rgb;ccw:0.3125;62,71,143,255;rgb;ccw:0.3164;62,71,143,255;rgb;ccw:0.3164;62,72,144,255;rgb;ccw:0.3203;62,72,144,255;rgb;ccw:0.3203;62,73,146,255;rgb;ccw:0.3242;62,73,146,255;rgb;ccw:0.3242;62,73,147,255;rgb;ccw:0.3281;62,73,147,255;rgb;ccw:0.3281;63,74,149,255;rgb;ccw:0.332;63,74,149,255;rgb;ccw:0.332;63,75,150,255;rgb;ccw:0.3359;63,75,150,255;rgb;ccw:0.3359;63,76,151,255;rgb;ccw:0.3398;63,76,151,255;rgb;ccw:0.3398;63,78,153,255;rgb;ccw:0.3438;63,78,153,255;rgb;ccw:0.3438;63,79,154,255;rgb;ccw:0.3477;63,79,154,255;rgb;ccw:0.3477;63,80,155,255;rgb;ccw:0.3516;63,80,155,255;rgb;ccw:0.3516;63,81,157,255;rgb;ccw:0.3555;63,81,157,255;rgb;ccw:0.3555;63,82,158,255;rgb;ccw:0.3594;63,82,158,255;rgb;ccw:0.3594;63,83,159,255;rgb;ccw:0.3633;63,83,159,255;rgb;ccw:0.3633;63,84,160,255;rgb;ccw:0.3672;63,84,160,255;rgb;ccw:0.3672;63,85,161,255;rgb;ccw:0.3711;63,85,161,255;rgb;ccw:0.3711;63,86,162,255;rgb;ccw:0.375;63,86,162,255;rgb;ccw:0.375;63,87,163,255;rgb;ccw:0.3789;63,87,163,255;rgb;ccw:0.3789;63,88,164,255;rgb;ccw:0.3828;63,88,164,255;rgb;ccw:0.3828;63,89,165,255;rgb;ccw:0.3867;63,89,165,255;rgb;ccw:0.3867;62,90,166,255;rgb;ccw:0.3906;62,90,166,255;rgb;ccw:0.3906;62,92,167,255;rgb;ccw:0.3945;62,92,167,255;rgb;ccw:0.3945;62,93,168,255;rgb;ccw:0.3984;62,93,168,255;rgb;ccw:0.3984;62,94,169,255;rgb;ccw:0.4023;62,94,169,255;rgb;ccw:0.4023;62,95,170,255;rgb;ccw:0.4062;62,95,170,255;rgb;ccw:0.4062;62,96,171,255;rgb;ccw:0.4102;62,96,171,255;rgb;ccw:0.4102;62,97,171,255;rgb;ccw:0.4141;62,97,171,255;rgb;ccw:0.4141;62,98,172,255;rgb;ccw:0.418;62,98,172,255;rgb;ccw:0.418;62,99,173,255;rgb;ccw:0.4219;62,99,173,255;rgb;ccw:0.4219;62,101,173,255;rgb;ccw:0.4258;62,101,173,255;rgb;ccw:0.4258;62,102,174,255;rgb;ccw:0.4297;62,102,174,255;rgb;ccw:0.4297;62,103,175,255;rgb;ccw:0.4336;62,103,175,255;rgb;ccw:0.4336;62,104,175,255;rgb;ccw:0.4375;62,104,175,255;rgb;ccw:0.4375;62,105,176,255;rgb;ccw:0.4414;62,105,176,255;rgb;ccw:0.4414;62,106,176,255;rgb;ccw:0.4453;62,106,176,255;rgb;ccw:0.4453;63,107,177,255;rgb;ccw:0.4492;63,107,177,255;rgb;ccw:0.4492;63,108,178,255;rgb;ccw:0.4531;63,108,178,255;rgb;ccw:0.4531;63,110,178,255;rgb;ccw:0.457;63,110,178,255;rgb;ccw:0.457;63,111,179,255;rgb;ccw:0.4609;63,111,179,255;rgb;ccw:0.4609;63,112,179,255;rgb;ccw:0.4648;63,112,179,255;rgb;ccw:0.4648;63,113,180,255;rgb;ccw:0.4688;63,113,180,255;rgb;ccw:0.4688;64,114,180,255;rgb;ccw:0.4727;64,114,180,255;rgb;ccw:0.4727;64,115,180,255;rgb;ccw:0.4766;64,115,180,255;rgb;ccw:0.4766;64,116,181,255;rgb;ccw:0.4805;64,116,181,255;rgb;ccw:0.4805;64,117,181,255;rgb;ccw:0.4844;64,117,181,255;rgb;ccw:0.4844;65,118,182,255;rgb;ccw:0.4883;65,118,182,255;rgb;ccw:0.4883;65,120,182,255;rgb;ccw:0.4922;65,120,182,255;rgb;ccw:0.4922;66,121,183,255;rgb;ccw:0.4961;66,121,183,255;rgb;ccw:0.4961;66,122,183,255;rgb;ccw:0.5;66,122,183,255;rgb;ccw:0.5;66,123,183,255;rgb;ccw:0.5039;66,123,183,255;rgb;ccw:0.5039;67,124,184,255;rgb;ccw:0.5078;67,124,184,255;rgb;ccw:0.5078;67,125,184,255;rgb;ccw:0.5117;67,125,184,255;rgb;ccw:0.5117;68,126,185,255;rgb;ccw:0.5156;68,126,185,255;rgb;ccw:0.5156;68,127,185,255;rgb;ccw:0.5195;68,127,185,255;rgb;ccw:0.5195;69,128,185,255;rgb;ccw:0.5234;69,128,185,255;rgb;ccw:0.5234;69,129,186,255;rgb;ccw:0.5273;69,129,186,255;rgb;ccw:0.5273;70,130,186,255;rgb;ccw:0.5312;70,130,186,255;rgb;ccw:0.5312;70,132,187,255;rgb;ccw:0.5352;70,132,187,255;rgb;ccw:0.5352;71,133,187,255;rgb;ccw:0.5391;71,133,187,255;rgb;ccw:0.5391;71,134,187,255;rgb;ccw:0.543;71,134,187,255;rgb;ccw:0.543;72,135,188,255;rgb;ccw:0.5469;72,135,188,255;rgb;ccw:0.5469;73,136,188,255;rgb;ccw:0.5508;73,136,188,255;rgb;ccw:0.5508;73,137,188,255;rgb;ccw:0.5547;73,137,188,255;rgb;ccw:0.5547;74,138,189,255;rgb;ccw:0.5586;74,138,189,255;rgb;ccw:0.5586;75,139,189,255;rgb;ccw:0.5625;75,139,189,255;rgb;ccw:0.5625;75,140,189,255;rgb;ccw:0.5664;75,140,189,255;rgb;ccw:0.5664;76,141,190,255;rgb;ccw:0.5703;76,141,190,255;rgb;ccw:0.5703;77,142,190,255;rgb;ccw:0.5742;77,142,190,255;rgb;ccw:0.5742;78,143,191,255;rgb;ccw:0.5781;78,143,191,255;rgb;ccw:0.5781;78,144,191,255;rgb;ccw:0.582;78,144,191,255;rgb;ccw:0.582;79,145,191,255;rgb;ccw:0.5859;79,145,191,255;rgb;ccw:0.5859;80,146,192,255;rgb;ccw:0.5898;80,146,192,255;rgb;ccw:0.5898;81,148,192,255;rgb;ccw:0.5938;81,148,192,255;rgb;ccw:0.5938;81,149,192,255;rgb;ccw:0.5977;81,149,192,255;rgb;ccw:0.5977;82,150,193,255;rgb;ccw:0.6016;82,150,193,255;rgb;ccw:0.6016;83,151,193,255;rgb;ccw:0.6055;83,151,193,255;rgb;ccw:0.6055;84,152,194,255;rgb;ccw:0.6094;84,152,194,255;rgb;ccw:0.6094;85,153,194,255;rgb;ccw:0.6133;85,153,194,255;rgb;ccw:0.6133;85,154,194,255;rgb;ccw:0.6172;85,154,194,255;rgb;ccw:0.6172;86,155,195,255;rgb;ccw:0.6211;86,155,195,255;rgb;ccw:0.6211;87,156,195,255;rgb;ccw:0.625;87,156,195,255;rgb;ccw:0.625;88,157,195,255;rgb;ccw:0.6289;88,157,195,255;rgb;ccw:0.6289;89,158,196,255;rgb;ccw:0.6328;89,158,196,255;rgb;ccw:0.6328;90,159,196,255;rgb;ccw:0.6367;90,159,196,255;rgb;ccw:0.6367;91,160,197,255;rgb;ccw:0.6406;91,160,197,255;rgb;ccw:0.6406;92,161,197,255;rgb;ccw:0.6445;92,161,197,255;rgb;ccw:0.6445;93,162,197,255;rgb;ccw:0.6484;93,162,197,255;rgb;ccw:0.6484;94,163,198,255;rgb;ccw:0.6523;94,163,198,255;rgb;ccw:0.6523;95,164,198,255;rgb;ccw:0.6562;95,164,198,255;rgb;ccw:0.6562;95,166,199,255;rgb;ccw:0.6602;95,166,199,255;rgb;ccw:0.6602;96,167,199,255;rgb;ccw:0.6641;96,167,199,255;rgb;ccw:0.6641;97,168,199,255;rgb;ccw:0.668;97,168,199,255;rgb;ccw:0.668;98,169,200,255;rgb;ccw:0.6719;98,169,200,255;rgb;ccw:0.6719;99,170,200,255;rgb;ccw:0.6758;99,170,200,255;rgb;ccw:0.6758;100,171,201,255;rgb;ccw:0.6797;100,171,201,255;rgb;ccw:0.6797;101,172,201,255;rgb;ccw:0.6836;101,172,201,255;rgb;ccw:0.6836;103,173,201,255;rgb;ccw:0.6875;103,173,201,255;rgb;ccw:0.6875;104,174,202,255;rgb;ccw:0.6914;104,174,202,255;rgb;ccw:0.6914;105,175,202,255;rgb;ccw:0.6953;105,175,202,255;rgb;ccw:0.6953;106,176,203,255;rgb;ccw:0.6992;106,176,203,255;rgb;ccw:0.6992;107,177,203,255;rgb;ccw:0.7031;107,177,203,255;rgb;ccw:0.7031;108,178,203,255;rgb;ccw:0.707;108,178,203,255;rgb;ccw:0.707;109,179,204,255;rgb;ccw:0.7109;109,179,204,255;rgb;ccw:0.7109;110,180,204,255;rgb;ccw:0.7148;110,180,204,255;rgb;ccw:0.7148;111,181,205,255;rgb;ccw:0.7188;111,181,205,255;rgb;ccw:0.7188;113,182,205,255;rgb;ccw:0.7227;113,182,205,255;rgb;ccw:0.7227;114,184,206,255;rgb;ccw:0.7266;114,184,206,255;rgb;ccw:0.7266;115,185,206,255;rgb;ccw:0.7305;115,185,206,255;rgb;ccw:0.7305;116,186,206,255;rgb;ccw:0.7344;116,186,206,255;rgb;ccw:0.7344;117,187,207,255;rgb;ccw:0.7383;117,187,207,255;rgb;ccw:0.7383;119,188,207,255;rgb;ccw:0.7422;119,188,207,255;rgb;ccw:0.7422;120,189,208,255;rgb;ccw:0.7461;120,189,208,255;rgb;ccw:0.7461;121,190,208,255;rgb;ccw:0.75;121,190,208,255;rgb;ccw:0.75;123,191,208,255;rgb;ccw:0.7539;123,191,208,255;rgb;ccw:0.7539;124,192,209,255;rgb;ccw:0.7578;124,192,209,255;rgb;ccw:0.7578;125,193,209,255;rgb;ccw:0.7617;125,193,209,255;rgb;ccw:0.7617;127,194,210,255;rgb;ccw:0.7656;127,194,210,255;rgb;ccw:0.7656;128,195,210,255;rgb;ccw:0.7695;128,195,210,255;rgb;ccw:0.7695;130,196,211,255;rgb;ccw:0.7734;130,196,211,255;rgb;ccw:0.7734;131,197,211,255;rgb;ccw:0.7773;131,197,211,255;rgb;ccw:0.7773;133,198,211,255;rgb;ccw:0.7812;133,198,211,255;rgb;ccw:0.7812;134,199,212,255;rgb;ccw:0.7852;134,199,212,255;rgb;ccw:0.7852;136,200,212,255;rgb;ccw:0.7891;136,200,212,255;rgb;ccw:0.7891;137,201,213,255;rgb;ccw:0.793;137,201,213,255;rgb;ccw:0.793;139,202,213,255;rgb;ccw:0.7969;139,202,213,255;rgb;ccw:0.7969;140,203,214,255;rgb;ccw:0.8008;140,203,214,255;rgb;ccw:0.8008;142,204,214,255;rgb;ccw:0.8047;142,204,214,255;rgb;ccw:0.8047;144,205,215,255;rgb;ccw:0.8086;144,205,215,255;rgb;ccw:0.8086;146,206,215,255;rgb;ccw:0.8125;146,206,215,255;rgb;ccw:0.8125;147,207,216,255;rgb;ccw:0.8164;147,207,216,255;rgb;ccw:0.8164;149,208,216,255;rgb;ccw:0.8203;149,208,216,255;rgb;ccw:0.8203;151,209,217,255;rgb;ccw:0.8242;151,209,217,255;rgb;ccw:0.8242;153,210,217,255;rgb;ccw:0.8281;153,210,217,255;rgb;ccw:0.8281;154,211,218,255;rgb;ccw:0.832;154,211,218,255;rgb;ccw:0.832;156,212,218,255;rgb;ccw:0.8359;156,212,218,255;rgb;ccw:0.8359;158,213,219,255;rgb;ccw:0.8398;158,213,219,255;rgb;ccw:0.8398;160,214,220,255;rgb;ccw:0.8438;160,214,220,255;rgb;ccw:0.8438;162,214,220,255;rgb;ccw:0.8477;162,214,220,255;rgb;ccw:0.8477;164,215,221,255;rgb;ccw:0.8516;164,215,221,255;rgb;ccw:0.8516;166,216,222,255;rgb;ccw:0.8555;166,216,222,255;rgb;ccw:0.8555;168,217,222,255;rgb;ccw:0.8594;168,217,222,255;rgb;ccw:0.8594;169,218,223,255;rgb;ccw:0.8633;169,218,223,255;rgb;ccw:0.8633;171,219,224,255;rgb;ccw:0.8672;171,219,224,255;rgb;ccw:0.8672;173,220,224,255;rgb;ccw:0.8711;173,220,224,255;rgb;ccw:0.8711;175,221,225,255;rgb;ccw:0.875;175,221,225,255;rgb;ccw:0.875;177,222,226,255;rgb;ccw:0.8789;177,222,226,255;rgb;ccw:0.8789;179,223,227,255;rgb;ccw:0.8828;179,223,227,255;rgb;ccw:0.8828;181,224,227,255;rgb;ccw:0.8867;181,224,227,255;rgb;ccw:0.8867;183,225,228,255;rgb;ccw:0.8906;183,225,228,255;rgb;ccw:0.8906;185,226,229,255;rgb;ccw:0.8945;185,226,229,255;rgb;ccw:0.8945;186,227,230,255;rgb;ccw:0.8984;186,227,230,255;rgb;ccw:0.8984;188,228,231,255;rgb;ccw:0.9023;188,228,231,255;rgb;ccw:0.9023;190,229,231,255;rgb;ccw:0.9062;190,229,231,255;rgb;ccw:0.9062;192,230,232,255;rgb;ccw:0.9102;192,230,232,255;rgb;ccw:0.9102;194,230,233,255;rgb;ccw:0.9141;194,230,233,255;rgb;ccw:0.9141;196,231,234,255;rgb;ccw:0.918;196,231,234,255;rgb;ccw:0.918;198,232,235,255;rgb;ccw:0.9219;198,232,235,255;rgb;ccw:0.9219;200,233,236,255;rgb;ccw:0.9258;200,233,236,255;rgb;ccw:0.9258;201,234,237,255;rgb;ccw:0.9297;201,234,237,255;rgb;ccw:0.9297;203,235,238,255;rgb;ccw:0.9336;203,235,238,255;rgb;ccw:0.9336;205,236,239,255;rgb;ccw:0.9375;205,236,239,255;rgb;ccw:0.9375;207,237,239,255;rgb;ccw:0.9414;207,237,239,255;rgb;ccw:0.9414;209,238,240,255;rgb;ccw:0.9453;209,238,240,255;rgb;ccw:0.9453;211,239,241,255;rgb;ccw:0.9492;211,239,241,255;rgb;ccw:0.9492;213,240,242,255;rgb;ccw:0.9531;213,240,242,255;rgb;ccw:0.9531;214,241,243,255;rgb;ccw:0.957;214,241,243,255;rgb;ccw:0.957;216,242,244,255;rgb;ccw:0.9609;216,242,244,255;rgb;ccw:0.9609;218,243,245,255;rgb;ccw:0.9648;218,243,245,255;rgb;ccw:0.9648;220,244,246,255;rgb;ccw:0.9688;220,244,246,255;rgb;ccw:0.9688;222,245,247,255;rgb;ccw:0.9727;222,245,247,255;rgb;ccw:0.9727;224,246,248,255;rgb;ccw:0.9766;224,246,248,255;rgb;ccw:0.9766;225,247,249,255;rgb;ccw:0.9805;225,247,249,255;rgb;ccw:0.9805;227,249,250,255;rgb;ccw:0.9844;227,249,250,255;rgb;ccw:0.9844;229,250,251,255;rgb;ccw:0.9883;229,250,251,255;rgb;ccw:0.9883;231,251,251,255;rgb;ccw:0.9922;231,251,251,255;rgb;ccw:0.9922;232,252,252,255;rgb;ccw:0.9961;232,252,252,255;rgb;ccw:0.9961;234,253,253,255;rgb;ccw"/>
            </Option>
          </colorramp>
          <item value="0" color="#040613" alpha="255" label="0.00%"/>
          <item value="0.39" color="#050614" alpha="255" label="0.39%"/>
          <item value="0.39" color="#050614" alpha="255" label="0.39%"/>
          <item value="0.78" color="#050715" alpha="255" label="0.78%"/>
          <item value="0.78" color="#050715" alpha="255" label="0.78%"/>
          <item value="1.17" color="#060817" alpha="255" label="1.17%"/>
          <item value="1.17" color="#060817" alpha="255" label="1.17%"/>
          <item value="1.56" color="#070918" alpha="255" label="1.56%"/>
          <item value="1.56" color="#070918" alpha="255" label="1.56%"/>
          <item value="1.95" color="#080a1a" alpha="255" label="1.95%"/>
          <item value="1.95" color="#080a1a" alpha="255" label="1.95%"/>
          <item value="2.34" color="#090b1b" alpha="255" label="2.34%"/>
          <item value="2.34" color="#090b1b" alpha="255" label="2.34%"/>
          <item value="2.73" color="#0a0c1d" alpha="255" label="2.73%"/>
          <item value="2.73" color="#0a0c1d" alpha="255" label="2.73%"/>
          <item value="3.12" color="#0b0d1e" alpha="255" label="3.12%"/>
          <item value="3.12" color="#0b0d1e" alpha="255" label="3.12%"/>
          <item value="3.52" color="#0c0d1f" alpha="255" label="3.52%"/>
          <item value="3.52" color="#0c0d1f" alpha="255" label="3.52%"/>
          <item value="3.91" color="#0d0e21" alpha="255" label="3.91%"/>
          <item value="3.91" color="#0d0e21" alpha="255" label="3.91%"/>
          <item value="4.3" color="#0e0f22" alpha="255" label="4.30%"/>
          <item value="4.3" color="#0e0f22" alpha="255" label="4.30%"/>
          <item value="4.69" color="#0f1024" alpha="255" label="4.69%"/>
          <item value="4.69" color="#0f1024" alpha="255" label="4.69%"/>
          <item value="5.08" color="#101125" alpha="255" label="5.08%"/>
          <item value="5.08" color="#101125" alpha="255" label="5.08%"/>
          <item value="5.47" color="#111227" alpha="255" label="5.47%"/>
          <item value="5.47" color="#111227" alpha="255" label="5.47%"/>
          <item value="5.86" color="#121328" alpha="255" label="5.86%"/>
          <item value="5.86" color="#121328" alpha="255" label="5.86%"/>
          <item value="6.25" color="#13132a" alpha="255" label="6.25%"/>
          <item value="6.25" color="#13132a" alpha="255" label="6.25%"/>
          <item value="6.64" color="#14142b" alpha="255" label="6.64%"/>
          <item value="6.64" color="#14142b" alpha="255" label="6.64%"/>
          <item value="7.03" color="#15152c" alpha="255" label="7.03%"/>
          <item value="7.03" color="#15152c" alpha="255" label="7.03%"/>
          <item value="7.42" color="#16162e" alpha="255" label="7.42%"/>
          <item value="7.42" color="#16162e" alpha="255" label="7.42%"/>
          <item value="7.8100000000000005" color="#17172f" alpha="255" label="7.81%"/>
          <item value="7.8100000000000005" color="#17172f" alpha="255" label="7.81%"/>
          <item value="8.200000000000001" color="#171831" alpha="255" label="8.20%"/>
          <item value="8.200000000000001" color="#171831" alpha="255" label="8.20%"/>
          <item value="8.59" color="#181832" alpha="255" label="8.59%"/>
          <item value="8.59" color="#181832" alpha="255" label="8.59%"/>
          <item value="8.98" color="#191934" alpha="255" label="8.98%"/>
          <item value="8.98" color="#191934" alpha="255" label="8.98%"/>
          <item value="9.379999999999999" color="#1a1a35" alpha="255" label="9.38%"/>
          <item value="9.379999999999999" color="#1a1a35" alpha="255" label="9.38%"/>
          <item value="9.77" color="#1b1b37" alpha="255" label="9.77%"/>
          <item value="9.77" color="#1b1b37" alpha="255" label="9.77%"/>
          <item value="10.16" color="#1c1c38" alpha="255" label="10.16%"/>
          <item value="10.16" color="#1c1c38" alpha="255" label="10.16%"/>
          <item value="10.549999999999999" color="#1d1c3a" alpha="255" label="10.55%"/>
          <item value="10.549999999999999" color="#1d1c3a" alpha="255" label="10.55%"/>
          <item value="10.94" color="#1e1d3b" alpha="255" label="10.94%"/>
          <item value="10.94" color="#1e1d3b" alpha="255" label="10.94%"/>
          <item value="11.33" color="#1f1e3d" alpha="255" label="11.33%"/>
          <item value="11.33" color="#1f1e3d" alpha="255" label="11.33%"/>
          <item value="11.72" color="#1f1f3e" alpha="255" label="11.72%"/>
          <item value="11.72" color="#1f1f3e" alpha="255" label="11.72%"/>
          <item value="12.11" color="#201f40" alpha="255" label="12.11%"/>
          <item value="12.11" color="#201f40" alpha="255" label="12.11%"/>
          <item value="12.5" color="#212041" alpha="255" label="12.50%"/>
          <item value="12.5" color="#212041" alpha="255" label="12.50%"/>
          <item value="12.889999999999999" color="#222143" alpha="255" label="12.89%"/>
          <item value="12.889999999999999" color="#222143" alpha="255" label="12.89%"/>
          <item value="13.28" color="#232244" alpha="255" label="13.28%"/>
          <item value="13.28" color="#232244" alpha="255" label="13.28%"/>
          <item value="13.669999999999998" color="#242246" alpha="255" label="13.67%"/>
          <item value="13.669999999999998" color="#242246" alpha="255" label="13.67%"/>
          <item value="14.06" color="#252347" alpha="255" label="14.06%"/>
          <item value="14.06" color="#252347" alpha="255" label="14.06%"/>
          <item value="14.45" color="#252449" alpha="255" label="14.45%"/>
          <item value="14.45" color="#252449" alpha="255" label="14.45%"/>
          <item value="14.84" color="#26254a" alpha="255" label="14.84%"/>
          <item value="14.84" color="#26254a" alpha="255" label="14.84%"/>
          <item value="15.229999999999999" color="#27254c" alpha="255" label="15.23%"/>
          <item value="15.229999999999999" color="#27254c" alpha="255" label="15.23%"/>
          <item value="15.620000000000001" color="#28264e" alpha="255" label="15.62%"/>
          <item value="15.620000000000001" color="#28264e" alpha="255" label="15.62%"/>
          <item value="16.02" color="#29274f" alpha="255" label="16.02%"/>
          <item value="16.02" color="#29274f" alpha="255" label="16.02%"/>
          <item value="16.41" color="#292851" alpha="255" label="16.41%"/>
          <item value="16.41" color="#292851" alpha="255" label="16.41%"/>
          <item value="16.8" color="#2a2852" alpha="255" label="16.80%"/>
          <item value="16.8" color="#2a2852" alpha="255" label="16.80%"/>
          <item value="17.19" color="#2b2954" alpha="255" label="17.19%"/>
          <item value="17.19" color="#2b2954" alpha="255" label="17.19%"/>
          <item value="17.580000000000002" color="#2c2a55" alpha="255" label="17.58%"/>
          <item value="17.580000000000002" color="#2c2a55" alpha="255" label="17.58%"/>
          <item value="17.97" color="#2c2b57" alpha="255" label="17.97%"/>
          <item value="17.97" color="#2c2b57" alpha="255" label="17.97%"/>
          <item value="18.360000000000003" color="#2d2b59" alpha="255" label="18.36%"/>
          <item value="18.360000000000003" color="#2d2b59" alpha="255" label="18.36%"/>
          <item value="18.75" color="#2e2c5a" alpha="255" label="18.75%"/>
          <item value="18.75" color="#2e2c5a" alpha="255" label="18.75%"/>
          <item value="19.139999999999997" color="#2f2d5c" alpha="255" label="19.14%"/>
          <item value="19.139999999999997" color="#2f2d5c" alpha="255" label="19.14%"/>
          <item value="19.53" color="#2f2e5e" alpha="255" label="19.53%"/>
          <item value="19.53" color="#2f2e5e" alpha="255" label="19.53%"/>
          <item value="19.919999999999998" color="#302f5f" alpha="255" label="19.92%"/>
          <item value="19.919999999999998" color="#302f5f" alpha="255" label="19.92%"/>
          <item value="20.31" color="#312f61" alpha="255" label="20.31%"/>
          <item value="20.31" color="#312f61" alpha="255" label="20.31%"/>
          <item value="20.7" color="#313062" alpha="255" label="20.70%"/>
          <item value="20.7" color="#313062" alpha="255" label="20.70%"/>
          <item value="21.09" color="#323164" alpha="255" label="21.09%"/>
          <item value="21.09" color="#323164" alpha="255" label="21.09%"/>
          <item value="21.48" color="#333266" alpha="255" label="21.48%"/>
          <item value="21.48" color="#333266" alpha="255" label="21.48%"/>
          <item value="21.88" color="#333267" alpha="255" label="21.88%"/>
          <item value="21.88" color="#333267" alpha="255" label="21.88%"/>
          <item value="22.27" color="#343369" alpha="255" label="22.27%"/>
          <item value="22.27" color="#343369" alpha="255" label="22.27%"/>
          <item value="22.66" color="#35346b" alpha="255" label="22.66%"/>
          <item value="22.66" color="#35346b" alpha="255" label="22.66%"/>
          <item value="23.05" color="#35356c" alpha="255" label="23.05%"/>
          <item value="23.05" color="#35356c" alpha="255" label="23.05%"/>
          <item value="23.44" color="#36356e" alpha="255" label="23.44%"/>
          <item value="23.44" color="#36356e" alpha="255" label="23.44%"/>
          <item value="23.830000000000002" color="#363670" alpha="255" label="23.83%"/>
          <item value="23.830000000000002" color="#363670" alpha="255" label="23.83%"/>
          <item value="24.22" color="#373771" alpha="255" label="24.22%"/>
          <item value="24.22" color="#373771" alpha="255" label="24.22%"/>
          <item value="24.610000000000003" color="#383873" alpha="255" label="24.61%"/>
          <item value="24.610000000000003" color="#383873" alpha="255" label="24.61%"/>
          <item value="25" color="#383975" alpha="255" label="25.00%"/>
          <item value="25" color="#383975" alpha="255" label="25.00%"/>
          <item value="25.39" color="#393976" alpha="255" label="25.39%"/>
          <item value="25.39" color="#393976" alpha="255" label="25.39%"/>
          <item value="25.779999999999998" color="#393a78" alpha="255" label="25.78%"/>
          <item value="25.779999999999998" color="#393a78" alpha="255" label="25.78%"/>
          <item value="26.169999999999998" color="#3a3b7a" alpha="255" label="26.17%"/>
          <item value="26.169999999999998" color="#3a3b7a" alpha="255" label="26.17%"/>
          <item value="26.56" color="#3a3c7b" alpha="255" label="26.56%"/>
          <item value="26.56" color="#3a3c7b" alpha="255" label="26.56%"/>
          <item value="26.950000000000003" color="#3a3d7d" alpha="255" label="26.95%"/>
          <item value="26.950000000000003" color="#3a3d7d" alpha="255" label="26.95%"/>
          <item value="27.339999999999996" color="#3b3e7f" alpha="255" label="27.34%"/>
          <item value="27.339999999999996" color="#3b3e7f" alpha="255" label="27.34%"/>
          <item value="27.73" color="#3b3e80" alpha="255" label="27.73%"/>
          <item value="27.73" color="#3b3e80" alpha="255" label="27.73%"/>
          <item value="28.12" color="#3c3f82" alpha="255" label="28.12%"/>
          <item value="28.12" color="#3c3f82" alpha="255" label="28.12%"/>
          <item value="28.52" color="#3c4084" alpha="255" label="28.52%"/>
          <item value="28.52" color="#3c4084" alpha="255" label="28.52%"/>
          <item value="28.910000000000004" color="#3c4185" alpha="255" label="28.91%"/>
          <item value="28.910000000000004" color="#3c4185" alpha="255" label="28.91%"/>
          <item value="29.299999999999997" color="#3d4287" alpha="255" label="29.30%"/>
          <item value="29.299999999999997" color="#3d4287" alpha="255" label="29.30%"/>
          <item value="29.69" color="#3d4389" alpha="255" label="29.69%"/>
          <item value="29.69" color="#3d4389" alpha="255" label="29.69%"/>
          <item value="30.080000000000002" color="#3d448a" alpha="255" label="30.08%"/>
          <item value="30.080000000000002" color="#3d448a" alpha="255" label="30.08%"/>
          <item value="30.470000000000002" color="#3e458c" alpha="255" label="30.47%"/>
          <item value="30.470000000000002" color="#3e458c" alpha="255" label="30.47%"/>
          <item value="30.86" color="#3e468d" alpha="255" label="30.86%"/>
          <item value="30.86" color="#3e468d" alpha="255" label="30.86%"/>
          <item value="31.25" color="#3e478f" alpha="255" label="31.25%"/>
          <item value="31.25" color="#3e478f" alpha="255" label="31.25%"/>
          <item value="31.64" color="#3e4890" alpha="255" label="31.64%"/>
          <item value="31.64" color="#3e4890" alpha="255" label="31.64%"/>
          <item value="32.029999999999994" color="#3e4992" alpha="255" label="32.03%"/>
          <item value="32.029999999999994" color="#3e4992" alpha="255" label="32.03%"/>
          <item value="32.42" color="#3e4993" alpha="255" label="32.42%"/>
          <item value="32.42" color="#3e4993" alpha="255" label="32.42%"/>
          <item value="32.81" color="#3f4a95" alpha="255" label="32.81%"/>
          <item value="32.81" color="#3f4a95" alpha="255" label="32.81%"/>
          <item value="33.2" color="#3f4b96" alpha="255" label="33.20%"/>
          <item value="33.2" color="#3f4b96" alpha="255" label="33.20%"/>
          <item value="33.589999999999996" color="#3f4c97" alpha="255" label="33.59%"/>
          <item value="33.589999999999996" color="#3f4c97" alpha="255" label="33.59%"/>
          <item value="33.98" color="#3f4e99" alpha="255" label="33.98%"/>
          <item value="33.98" color="#3f4e99" alpha="255" label="33.98%"/>
          <item value="34.38" color="#3f4f9a" alpha="255" label="34.38%"/>
          <item value="34.38" color="#3f4f9a" alpha="255" label="34.38%"/>
          <item value="34.77" color="#3f509b" alpha="255" label="34.77%"/>
          <item value="34.77" color="#3f509b" alpha="255" label="34.77%"/>
          <item value="35.160000000000004" color="#3f519d" alpha="255" label="35.16%"/>
          <item value="35.160000000000004" color="#3f519d" alpha="255" label="35.16%"/>
          <item value="35.55" color="#3f529e" alpha="255" label="35.55%"/>
          <item value="35.55" color="#3f529e" alpha="255" label="35.55%"/>
          <item value="35.94" color="#3f539f" alpha="255" label="35.94%"/>
          <item value="35.94" color="#3f539f" alpha="255" label="35.94%"/>
          <item value="36.33" color="#3f54a0" alpha="255" label="36.33%"/>
          <item value="36.33" color="#3f54a0" alpha="255" label="36.33%"/>
          <item value="36.720000000000006" color="#3f55a1" alpha="255" label="36.72%"/>
          <item value="36.720000000000006" color="#3f55a1" alpha="255" label="36.72%"/>
          <item value="37.11" color="#3f56a2" alpha="255" label="37.11%"/>
          <item value="37.11" color="#3f56a2" alpha="255" label="37.11%"/>
          <item value="37.5" color="#3f57a3" alpha="255" label="37.50%"/>
          <item value="37.5" color="#3f57a3" alpha="255" label="37.50%"/>
          <item value="37.89" color="#3f58a4" alpha="255" label="37.89%"/>
          <item value="37.89" color="#3f58a4" alpha="255" label="37.89%"/>
          <item value="38.279999999999994" color="#3f59a5" alpha="255" label="38.28%"/>
          <item value="38.279999999999994" color="#3f59a5" alpha="255" label="38.28%"/>
          <item value="38.67" color="#3e5aa6" alpha="255" label="38.67%"/>
          <item value="38.67" color="#3e5aa6" alpha="255" label="38.67%"/>
          <item value="39.06" color="#3e5ca7" alpha="255" label="39.06%"/>
          <item value="39.06" color="#3e5ca7" alpha="255" label="39.06%"/>
          <item value="39.45" color="#3e5da8" alpha="255" label="39.45%"/>
          <item value="39.45" color="#3e5da8" alpha="255" label="39.45%"/>
          <item value="39.839999999999996" color="#3e5ea9" alpha="255" label="39.84%"/>
          <item value="39.839999999999996" color="#3e5ea9" alpha="255" label="39.84%"/>
          <item value="40.23" color="#3e5faa" alpha="255" label="40.23%"/>
          <item value="40.23" color="#3e5faa" alpha="255" label="40.23%"/>
          <item value="40.62" color="#3e60ab" alpha="255" label="40.62%"/>
          <item value="40.62" color="#3e60ab" alpha="255" label="40.62%"/>
          <item value="41.02" color="#3e61ab" alpha="255" label="41.02%"/>
          <item value="41.02" color="#3e61ab" alpha="255" label="41.02%"/>
          <item value="41.410000000000004" color="#3e62ac" alpha="255" label="41.41%"/>
          <item value="41.410000000000004" color="#3e62ac" alpha="255" label="41.41%"/>
          <item value="41.8" color="#3e63ad" alpha="255" label="41.80%"/>
          <item value="41.8" color="#3e63ad" alpha="255" label="41.80%"/>
          <item value="42.19" color="#3e65ad" alpha="255" label="42.19%"/>
          <item value="42.19" color="#3e65ad" alpha="255" label="42.19%"/>
          <item value="42.58" color="#3e66ae" alpha="255" label="42.58%"/>
          <item value="42.58" color="#3e66ae" alpha="255" label="42.58%"/>
          <item value="42.970000000000006" color="#3e67af" alpha="255" label="42.97%"/>
          <item value="42.970000000000006" color="#3e67af" alpha="255" label="42.97%"/>
          <item value="43.36" color="#3e68af" alpha="255" label="43.36%"/>
          <item value="43.36" color="#3e68af" alpha="255" label="43.36%"/>
          <item value="43.75" color="#3e69b0" alpha="255" label="43.75%"/>
          <item value="43.75" color="#3e69b0" alpha="255" label="43.75%"/>
          <item value="44.14" color="#3e6ab0" alpha="255" label="44.14%"/>
          <item value="44.14" color="#3e6ab0" alpha="255" label="44.14%"/>
          <item value="44.529999999999994" color="#3f6bb1" alpha="255" label="44.53%"/>
          <item value="44.529999999999994" color="#3f6bb1" alpha="255" label="44.53%"/>
          <item value="44.92" color="#3f6cb2" alpha="255" label="44.92%"/>
          <item value="44.92" color="#3f6cb2" alpha="255" label="44.92%"/>
          <item value="45.31" color="#3f6eb2" alpha="255" label="45.31%"/>
          <item value="45.31" color="#3f6eb2" alpha="255" label="45.31%"/>
          <item value="45.7" color="#3f6fb3" alpha="255" label="45.70%"/>
          <item value="45.7" color="#3f6fb3" alpha="255" label="45.70%"/>
          <item value="46.089999999999996" color="#3f70b3" alpha="255" label="46.09%"/>
          <item value="46.089999999999996" color="#3f70b3" alpha="255" label="46.09%"/>
          <item value="46.48" color="#3f71b4" alpha="255" label="46.48%"/>
          <item value="46.48" color="#3f71b4" alpha="255" label="46.48%"/>
          <item value="46.88" color="#4072b4" alpha="255" label="46.88%"/>
          <item value="46.88" color="#4072b4" alpha="255" label="46.88%"/>
          <item value="47.27" color="#4073b4" alpha="255" label="47.27%"/>
          <item value="47.27" color="#4073b4" alpha="255" label="47.27%"/>
          <item value="47.660000000000004" color="#4074b5" alpha="255" label="47.66%"/>
          <item value="47.660000000000004" color="#4074b5" alpha="255" label="47.66%"/>
          <item value="48.05" color="#4075b5" alpha="255" label="48.05%"/>
          <item value="48.05" color="#4075b5" alpha="255" label="48.05%"/>
          <item value="48.44" color="#4176b6" alpha="255" label="48.44%"/>
          <item value="48.44" color="#4176b6" alpha="255" label="48.44%"/>
          <item value="48.83" color="#4178b6" alpha="255" label="48.83%"/>
          <item value="48.83" color="#4178b6" alpha="255" label="48.83%"/>
          <item value="49.220000000000006" color="#4279b7" alpha="255" label="49.22%"/>
          <item value="49.220000000000006" color="#4279b7" alpha="255" label="49.22%"/>
          <item value="49.61" color="#427ab7" alpha="255" label="49.61%"/>
          <item value="49.61" color="#427ab7" alpha="255" label="49.61%"/>
          <item value="50" color="#427bb7" alpha="255" label="50.00%"/>
          <item value="50" color="#427bb7" alpha="255" label="50.00%"/>
          <item value="50.39" color="#437cb8" alpha="255" label="50.39%"/>
          <item value="50.39" color="#437cb8" alpha="255" label="50.39%"/>
          <item value="50.78" color="#437db8" alpha="255" label="50.78%"/>
          <item value="50.78" color="#437db8" alpha="255" label="50.78%"/>
          <item value="51.17" color="#447eb9" alpha="255" label="51.17%"/>
          <item value="51.17" color="#447eb9" alpha="255" label="51.17%"/>
          <item value="51.559999999999995" color="#447fb9" alpha="255" label="51.56%"/>
          <item value="51.559999999999995" color="#447fb9" alpha="255" label="51.56%"/>
          <item value="51.949999999999996" color="#4580b9" alpha="255" label="51.95%"/>
          <item value="51.949999999999996" color="#4580b9" alpha="255" label="51.95%"/>
          <item value="52.339999999999996" color="#4581ba" alpha="255" label="52.34%"/>
          <item value="52.339999999999996" color="#4581ba" alpha="255" label="52.34%"/>
          <item value="52.73" color="#4682ba" alpha="255" label="52.73%"/>
          <item value="52.73" color="#4682ba" alpha="255" label="52.73%"/>
          <item value="53.12" color="#4684bb" alpha="255" label="53.12%"/>
          <item value="53.12" color="#4684bb" alpha="255" label="53.12%"/>
          <item value="53.52" color="#4785bb" alpha="255" label="53.52%"/>
          <item value="53.52" color="#4785bb" alpha="255" label="53.52%"/>
          <item value="53.910000000000004" color="#4786bb" alpha="255" label="53.91%"/>
          <item value="53.910000000000004" color="#4786bb" alpha="255" label="53.91%"/>
          <item value="54.300000000000004" color="#4887bc" alpha="255" label="54.30%"/>
          <item value="54.300000000000004" color="#4887bc" alpha="255" label="54.30%"/>
          <item value="54.690000000000005" color="#4988bc" alpha="255" label="54.69%"/>
          <item value="54.690000000000005" color="#4988bc" alpha="255" label="54.69%"/>
          <item value="55.08" color="#4989bc" alpha="255" label="55.08%"/>
          <item value="55.08" color="#4989bc" alpha="255" label="55.08%"/>
          <item value="55.47" color="#4a8abd" alpha="255" label="55.47%"/>
          <item value="55.47" color="#4a8abd" alpha="255" label="55.47%"/>
          <item value="55.86" color="#4b8bbd" alpha="255" label="55.86%"/>
          <item value="55.86" color="#4b8bbd" alpha="255" label="55.86%"/>
          <item value="56.25" color="#4b8cbd" alpha="255" label="56.25%"/>
          <item value="56.25" color="#4b8cbd" alpha="255" label="56.25%"/>
          <item value="56.64" color="#4c8dbe" alpha="255" label="56.64%"/>
          <item value="56.64" color="#4c8dbe" alpha="255" label="56.64%"/>
          <item value="57.03" color="#4d8ebe" alpha="255" label="57.03%"/>
          <item value="57.03" color="#4d8ebe" alpha="255" label="57.03%"/>
          <item value="57.42" color="#4e8fbf" alpha="255" label="57.42%"/>
          <item value="57.42" color="#4e8fbf" alpha="255" label="57.42%"/>
          <item value="57.809999999999995" color="#4e90bf" alpha="255" label="57.81%"/>
          <item value="57.809999999999995" color="#4e90bf" alpha="255" label="57.81%"/>
          <item value="58.199999999999996" color="#4f91bf" alpha="255" label="58.20%"/>
          <item value="58.199999999999996" color="#4f91bf" alpha="255" label="58.20%"/>
          <item value="58.589999999999996" color="#5092c0" alpha="255" label="58.59%"/>
          <item value="58.589999999999996" color="#5092c0" alpha="255" label="58.59%"/>
          <item value="58.98" color="#5194c0" alpha="255" label="58.98%"/>
          <item value="58.98" color="#5194c0" alpha="255" label="58.98%"/>
          <item value="59.38" color="#5195c0" alpha="255" label="59.38%"/>
          <item value="59.38" color="#5195c0" alpha="255" label="59.38%"/>
          <item value="59.77" color="#5296c1" alpha="255" label="59.77%"/>
          <item value="59.77" color="#5296c1" alpha="255" label="59.77%"/>
          <item value="60.160000000000004" color="#5397c1" alpha="255" label="60.16%"/>
          <item value="60.160000000000004" color="#5397c1" alpha="255" label="60.16%"/>
          <item value="60.550000000000004" color="#5498c2" alpha="255" label="60.55%"/>
          <item value="60.550000000000004" color="#5498c2" alpha="255" label="60.55%"/>
          <item value="60.940000000000005" color="#5599c2" alpha="255" label="60.94%"/>
          <item value="60.940000000000005" color="#5599c2" alpha="255" label="60.94%"/>
          <item value="61.33" color="#559ac2" alpha="255" label="61.33%"/>
          <item value="61.33" color="#559ac2" alpha="255" label="61.33%"/>
          <item value="61.72" color="#569bc3" alpha="255" label="61.72%"/>
          <item value="61.72" color="#569bc3" alpha="255" label="61.72%"/>
          <item value="62.11" color="#579cc3" alpha="255" label="62.11%"/>
          <item value="62.11" color="#579cc3" alpha="255" label="62.11%"/>
          <item value="62.5" color="#589dc3" alpha="255" label="62.50%"/>
          <item value="62.5" color="#589dc3" alpha="255" label="62.50%"/>
          <item value="62.89" color="#599ec4" alpha="255" label="62.89%"/>
          <item value="62.89" color="#599ec4" alpha="255" label="62.89%"/>
          <item value="63.28" color="#5a9fc4" alpha="255" label="63.28%"/>
          <item value="63.28" color="#5a9fc4" alpha="255" label="63.28%"/>
          <item value="63.67" color="#5ba0c5" alpha="255" label="63.67%"/>
          <item value="63.67" color="#5ba0c5" alpha="255" label="63.67%"/>
          <item value="64.05999999999999" color="#5ca1c5" alpha="255" label="64.06%"/>
          <item value="64.05999999999999" color="#5ca1c5" alpha="255" label="64.06%"/>
          <item value="64.45" color="#5da2c5" alpha="255" label="64.45%"/>
          <item value="64.45" color="#5da2c5" alpha="255" label="64.45%"/>
          <item value="64.84" color="#5ea3c6" alpha="255" label="64.84%"/>
          <item value="64.84" color="#5ea3c6" alpha="255" label="64.84%"/>
          <item value="65.23" color="#5fa4c6" alpha="255" label="65.23%"/>
          <item value="65.23" color="#5fa4c6" alpha="255" label="65.23%"/>
          <item value="65.62" color="#5fa6c7" alpha="255" label="65.62%"/>
          <item value="65.62" color="#5fa6c7" alpha="255" label="65.62%"/>
          <item value="66.02" color="#60a7c7" alpha="255" label="66.02%"/>
          <item value="66.02" color="#60a7c7" alpha="255" label="66.02%"/>
          <item value="66.41" color="#61a8c7" alpha="255" label="66.41%"/>
          <item value="66.41" color="#61a8c7" alpha="255" label="66.41%"/>
          <item value="66.8" color="#62a9c8" alpha="255" label="66.80%"/>
          <item value="66.8" color="#62a9c8" alpha="255" label="66.80%"/>
          <item value="67.19000000000001" color="#63aac8" alpha="255" label="67.19%"/>
          <item value="67.19000000000001" color="#63aac8" alpha="255" label="67.19%"/>
          <item value="67.58" color="#64abc9" alpha="255" label="67.58%"/>
          <item value="67.58" color="#64abc9" alpha="255" label="67.58%"/>
          <item value="67.97" color="#65acc9" alpha="255" label="67.97%"/>
          <item value="67.97" color="#65acc9" alpha="255" label="67.97%"/>
          <item value="68.36" color="#67adc9" alpha="255" label="68.36%"/>
          <item value="68.36" color="#67adc9" alpha="255" label="68.36%"/>
          <item value="68.75" color="#68aeca" alpha="255" label="68.75%"/>
          <item value="68.75" color="#68aeca" alpha="255" label="68.75%"/>
          <item value="69.14" color="#69afca" alpha="255" label="69.14%"/>
          <item value="69.14" color="#69afca" alpha="255" label="69.14%"/>
          <item value="69.53" color="#6ab0cb" alpha="255" label="69.53%"/>
          <item value="69.53" color="#6ab0cb" alpha="255" label="69.53%"/>
          <item value="69.92" color="#6bb1cb" alpha="255" label="69.92%"/>
          <item value="69.92" color="#6bb1cb" alpha="255" label="69.92%"/>
          <item value="70.30999999999999" color="#6cb2cb" alpha="255" label="70.31%"/>
          <item value="70.30999999999999" color="#6cb2cb" alpha="255" label="70.31%"/>
          <item value="70.7" color="#6db3cc" alpha="255" label="70.70%"/>
          <item value="70.7" color="#6db3cc" alpha="255" label="70.70%"/>
          <item value="71.09" color="#6eb4cc" alpha="255" label="71.09%"/>
          <item value="71.09" color="#6eb4cc" alpha="255" label="71.09%"/>
          <item value="71.48" color="#6fb5cd" alpha="255" label="71.48%"/>
          <item value="71.48" color="#6fb5cd" alpha="255" label="71.48%"/>
          <item value="71.88" color="#71b6cd" alpha="255" label="71.88%"/>
          <item value="71.88" color="#71b6cd" alpha="255" label="71.88%"/>
          <item value="72.27" color="#72b8ce" alpha="255" label="72.27%"/>
          <item value="72.27" color="#72b8ce" alpha="255" label="72.27%"/>
          <item value="72.66" color="#73b9ce" alpha="255" label="72.66%"/>
          <item value="72.66" color="#73b9ce" alpha="255" label="72.66%"/>
          <item value="73.05" color="#74bace" alpha="255" label="73.05%"/>
          <item value="73.05" color="#74bace" alpha="255" label="73.05%"/>
          <item value="73.44000000000001" color="#75bbcf" alpha="255" label="73.44%"/>
          <item value="73.44000000000001" color="#75bbcf" alpha="255" label="73.44%"/>
          <item value="73.83" color="#77bccf" alpha="255" label="73.83%"/>
          <item value="73.83" color="#77bccf" alpha="255" label="73.83%"/>
          <item value="74.22" color="#78bdd0" alpha="255" label="74.22%"/>
          <item value="74.22" color="#78bdd0" alpha="255" label="74.22%"/>
          <item value="74.61" color="#79bed0" alpha="255" label="74.61%"/>
          <item value="74.61" color="#79bed0" alpha="255" label="74.61%"/>
          <item value="75" color="#7bbfd0" alpha="255" label="75.00%"/>
          <item value="75" color="#7bbfd0" alpha="255" label="75.00%"/>
          <item value="75.39" color="#7cc0d1" alpha="255" label="75.39%"/>
          <item value="75.39" color="#7cc0d1" alpha="255" label="75.39%"/>
          <item value="75.78" color="#7dc1d1" alpha="255" label="75.78%"/>
          <item value="75.78" color="#7dc1d1" alpha="255" label="75.78%"/>
          <item value="76.17" color="#7fc2d2" alpha="255" label="76.17%"/>
          <item value="76.17" color="#7fc2d2" alpha="255" label="76.17%"/>
          <item value="76.55999999999999" color="#80c3d2" alpha="255" label="76.56%"/>
          <item value="76.55999999999999" color="#80c3d2" alpha="255" label="76.56%"/>
          <item value="76.95" color="#82c4d3" alpha="255" label="76.95%"/>
          <item value="76.95" color="#82c4d3" alpha="255" label="76.95%"/>
          <item value="77.34" color="#83c5d3" alpha="255" label="77.34%"/>
          <item value="77.34" color="#83c5d3" alpha="255" label="77.34%"/>
          <item value="77.73" color="#85c6d3" alpha="255" label="77.73%"/>
          <item value="77.73" color="#85c6d3" alpha="255" label="77.73%"/>
          <item value="78.12" color="#86c7d4" alpha="255" label="78.12%"/>
          <item value="78.12" color="#86c7d4" alpha="255" label="78.12%"/>
          <item value="78.52" color="#88c8d4" alpha="255" label="78.52%"/>
          <item value="78.52" color="#88c8d4" alpha="255" label="78.52%"/>
          <item value="78.91" color="#89c9d5" alpha="255" label="78.91%"/>
          <item value="78.91" color="#89c9d5" alpha="255" label="78.91%"/>
          <item value="79.3" color="#8bcad5" alpha="255" label="79.30%"/>
          <item value="79.3" color="#8bcad5" alpha="255" label="79.30%"/>
          <item value="79.69000000000001" color="#8ccbd6" alpha="255" label="79.69%"/>
          <item value="79.69000000000001" color="#8ccbd6" alpha="255" label="79.69%"/>
          <item value="80.08" color="#8eccd6" alpha="255" label="80.08%"/>
          <item value="80.08" color="#8eccd6" alpha="255" label="80.08%"/>
          <item value="80.47" color="#90cdd7" alpha="255" label="80.47%"/>
          <item value="80.47" color="#90cdd7" alpha="255" label="80.47%"/>
          <item value="80.86" color="#92ced7" alpha="255" label="80.86%"/>
          <item value="80.86" color="#92ced7" alpha="255" label="80.86%"/>
          <item value="81.25" color="#93cfd8" alpha="255" label="81.25%"/>
          <item value="81.25" color="#93cfd8" alpha="255" label="81.25%"/>
          <item value="81.64" color="#95d0d8" alpha="255" label="81.64%"/>
          <item value="81.64" color="#95d0d8" alpha="255" label="81.64%"/>
          <item value="82.03" color="#97d1d9" alpha="255" label="82.03%"/>
          <item value="82.03" color="#97d1d9" alpha="255" label="82.03%"/>
          <item value="82.42" color="#99d2d9" alpha="255" label="82.42%"/>
          <item value="82.42" color="#99d2d9" alpha="255" label="82.42%"/>
          <item value="82.80999999999999" color="#9ad3da" alpha="255" label="82.81%"/>
          <item value="82.80999999999999" color="#9ad3da" alpha="255" label="82.81%"/>
          <item value="83.2" color="#9cd4da" alpha="255" label="83.20%"/>
          <item value="83.2" color="#9cd4da" alpha="255" label="83.20%"/>
          <item value="83.59" color="#9ed5db" alpha="255" label="83.59%"/>
          <item value="83.59" color="#9ed5db" alpha="255" label="83.59%"/>
          <item value="83.98" color="#a0d6dc" alpha="255" label="83.98%"/>
          <item value="83.98" color="#a0d6dc" alpha="255" label="83.98%"/>
          <item value="84.38" color="#a2d6dc" alpha="255" label="84.38%"/>
          <item value="84.38" color="#a2d6dc" alpha="255" label="84.38%"/>
          <item value="84.77" color="#a4d7dd" alpha="255" label="84.77%"/>
          <item value="84.77" color="#a4d7dd" alpha="255" label="84.77%"/>
          <item value="85.16" color="#a6d8de" alpha="255" label="85.16%"/>
          <item value="85.16" color="#a6d8de" alpha="255" label="85.16%"/>
          <item value="85.55" color="#a8d9de" alpha="255" label="85.55%"/>
          <item value="85.55" color="#a8d9de" alpha="255" label="85.55%"/>
          <item value="85.94000000000001" color="#a9dadf" alpha="255" label="85.94%"/>
          <item value="85.94000000000001" color="#a9dadf" alpha="255" label="85.94%"/>
          <item value="86.33" color="#abdbe0" alpha="255" label="86.33%"/>
          <item value="86.33" color="#abdbe0" alpha="255" label="86.33%"/>
          <item value="86.72" color="#addce0" alpha="255" label="86.72%"/>
          <item value="86.72" color="#addce0" alpha="255" label="86.72%"/>
          <item value="87.11" color="#afdde1" alpha="255" label="87.11%"/>
          <item value="87.11" color="#afdde1" alpha="255" label="87.11%"/>
          <item value="87.5" color="#b1dee2" alpha="255" label="87.50%"/>
          <item value="87.5" color="#b1dee2" alpha="255" label="87.50%"/>
          <item value="87.89" color="#b3dfe3" alpha="255" label="87.89%"/>
          <item value="87.89" color="#b3dfe3" alpha="255" label="87.89%"/>
          <item value="88.28" color="#b5e0e3" alpha="255" label="88.28%"/>
          <item value="88.28" color="#b5e0e3" alpha="255" label="88.28%"/>
          <item value="88.67" color="#b7e1e4" alpha="255" label="88.67%"/>
          <item value="88.67" color="#b7e1e4" alpha="255" label="88.67%"/>
          <item value="89.05999999999999" color="#b9e2e5" alpha="255" label="89.06%"/>
          <item value="89.05999999999999" color="#b9e2e5" alpha="255" label="89.06%"/>
          <item value="89.45" color="#bae3e6" alpha="255" label="89.45%"/>
          <item value="89.45" color="#bae3e6" alpha="255" label="89.45%"/>
          <item value="89.84" color="#bce4e7" alpha="255" label="89.84%"/>
          <item value="89.84" color="#bce4e7" alpha="255" label="89.84%"/>
          <item value="90.23" color="#bee5e7" alpha="255" label="90.23%"/>
          <item value="90.23" color="#bee5e7" alpha="255" label="90.23%"/>
          <item value="90.62" color="#c0e6e8" alpha="255" label="90.62%"/>
          <item value="90.62" color="#c0e6e8" alpha="255" label="90.62%"/>
          <item value="91.02" color="#c2e6e9" alpha="255" label="91.02%"/>
          <item value="91.02" color="#c2e6e9" alpha="255" label="91.02%"/>
          <item value="91.41" color="#c4e7ea" alpha="255" label="91.41%"/>
          <item value="91.41" color="#c4e7ea" alpha="255" label="91.41%"/>
          <item value="91.8" color="#c6e8eb" alpha="255" label="91.80%"/>
          <item value="91.8" color="#c6e8eb" alpha="255" label="91.80%"/>
          <item value="92.19000000000001" color="#c8e9ec" alpha="255" label="92.19%"/>
          <item value="92.19000000000001" color="#c8e9ec" alpha="255" label="92.19%"/>
          <item value="92.58" color="#c9eaed" alpha="255" label="92.58%"/>
          <item value="92.58" color="#c9eaed" alpha="255" label="92.58%"/>
          <item value="92.97" color="#cbebee" alpha="255" label="92.97%"/>
          <item value="92.97" color="#cbebee" alpha="255" label="92.97%"/>
          <item value="93.36" color="#cdecef" alpha="255" label="93.36%"/>
          <item value="93.36" color="#cdecef" alpha="255" label="93.36%"/>
          <item value="93.75" color="#cfedef" alpha="255" label="93.75%"/>
          <item value="93.75" color="#cfedef" alpha="255" label="93.75%"/>
          <item value="94.14" color="#d1eef0" alpha="255" label="94.14%"/>
          <item value="94.14" color="#d1eef0" alpha="255" label="94.14%"/>
          <item value="94.53" color="#d3eff1" alpha="255" label="94.53%"/>
          <item value="94.53" color="#d3eff1" alpha="255" label="94.53%"/>
          <item value="94.92" color="#d5f0f2" alpha="255" label="94.92%"/>
          <item value="94.92" color="#d5f0f2" alpha="255" label="94.92%"/>
          <item value="95.30999999999999" color="#d6f1f3" alpha="255" label="95.31%"/>
          <item value="95.30999999999999" color="#d6f1f3" alpha="255" label="95.31%"/>
          <item value="95.7" color="#d8f2f4" alpha="255" label="95.70%"/>
          <item value="95.7" color="#d8f2f4" alpha="255" label="95.70%"/>
          <item value="96.09" color="#daf3f5" alpha="255" label="96.09%"/>
          <item value="96.09" color="#daf3f5" alpha="255" label="96.09%"/>
          <item value="96.48" color="#dcf4f6" alpha="255" label="96.48%"/>
          <item value="96.48" color="#dcf4f6" alpha="255" label="96.48%"/>
          <item value="96.88" color="#def5f7" alpha="255" label="96.88%"/>
          <item value="96.88" color="#def5f7" alpha="255" label="96.88%"/>
          <item value="97.27" color="#e0f6f8" alpha="255" label="97.27%"/>
          <item value="97.27" color="#e0f6f8" alpha="255" label="97.27%"/>
          <item value="97.66" color="#e1f7f9" alpha="255" label="97.66%"/>
          <item value="97.66" color="#e1f7f9" alpha="255" label="97.66%"/>
          <item value="98.05" color="#e3f9fa" alpha="255" label="98.05%"/>
          <item value="98.05" color="#e3f9fa" alpha="255" label="98.05%"/>
          <item value="98.44000000000001" color="#e5fafb" alpha="255" label="98.44%"/>
          <item value="98.44000000000001" color="#e5fafb" alpha="255" label="98.44%"/>
          <item value="98.83" color="#e7fbfb" alpha="255" label="98.83%"/>
          <item value="98.83" color="#e7fbfb" alpha="255" label="98.83%"/>
          <item value="99.22" color="#e8fcfc" alpha="255" label="99.22%"/>
          <item value="99.22" color="#e8fcfc" alpha="255" label="99.22%"/>
          <item value="99.61" color="#eafdfd" alpha="255" label="99.61%"/>
          <item value="99.61" color="#eafdfd" alpha="255" label="99.61%"/>
          <item value="100" color="#eafdfd" alpha="255" label="100.00%"/>
          <rampLegendSettings minimumLabel="" prefix="" orientation="1" direction="0" maximumLabel="" useContinuousLegend="1" suffix="%">
            <numericFormat id="basic">
              <Option type="Map">
                <Option name="decimal_separator" type="invalid"/>
                <Option name="decimals" type="int" value="6"/>
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
    <brightnesscontrast contrast="0" brightness="0" gamma="1"/>
    <huesaturation colorizeStrength="100" colorizeGreen="128" invertColors="0" saturation="0" grayscaleMode="0" colorizeBlue="128" colorizeOn="0" colorizeRed="255"/>
    <rasterresampler maxOversampling="2"/>
    <resamplingStage>resamplingFilter</resamplingStage>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

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
    <rasterrenderer classificationMax="20" alphaBand="-1" band="1" nodataColor="" classificationMin="-20" type="singlebandpseudocolor" opacity="1">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Exact</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <rastershader>
        <colorrampshader maximumValue="20" colorRampType="INTERPOLATED" minimumValue="-20" classificationMode="2" clip="0" labelPrecision="0">
          <colorramp name="[source]" type="gradient">
            <Option type="Map">
              <Option name="color1" value="24,28,67,255" type="QString"/>
              <Option name="color2" value="60,9,18,255" type="QString"/>
              <Option name="direction" value="ccw" type="QString"/>
              <Option name="discrete" value="0" type="QString"/>
              <Option name="rampType" value="gradient" type="QString"/>
              <Option name="spec" value="rgb" type="QString"/>
              <Option name="stops" value="0.0039;24,28,67,255;rgb;ccw:0.0039;25,30,70,255;rgb;ccw:0.0078;25,30,70,255;rgb;ccw:0.0078;26,31,73,255;rgb;ccw:0.0117;26,31,73,255;rgb;ccw:0.0117;27,33,76,255;rgb;ccw:0.0156;27,33,76,255;rgb;ccw:0.0156;28,34,79,255;rgb;ccw:0.0195;28,34,79,255;rgb;ccw:0.0195;29,35,82,255;rgb;ccw:0.0234;29,35,82,255;rgb;ccw:0.0234;30,37,85,255;rgb;ccw:0.0273;30,37,85,255;rgb;ccw:0.0273;31,38,88,255;rgb;ccw:0.0312;31,38,88,255;rgb;ccw:0.0312;32,39,91,255;rgb;ccw:0.0352;32,39,91,255;rgb;ccw:0.0352;33,41,95,255;rgb;ccw:0.0391;33,41,95,255;rgb;ccw:0.0391;33,42,98,255;rgb;ccw:0.043;33,42,98,255;rgb;ccw:0.043;34,43,101,255;rgb;ccw:0.0469;34,43,101,255;rgb;ccw:0.0469;35,45,105,255;rgb;ccw:0.0508;35,45,105,255;rgb;ccw:0.0508;36,46,108,255;rgb;ccw:0.0547;36,46,108,255;rgb;ccw:0.0547;37,47,111,255;rgb;ccw:0.0586;37,47,111,255;rgb;ccw:0.0586;37,48,115,255;rgb;ccw:0.0625;37,48,115,255;rgb;ccw:0.0625;38,50,118,255;rgb;ccw:0.0664;38,50,118,255;rgb;ccw:0.0664;39,51,122,255;rgb;ccw:0.0703;39,51,122,255;rgb;ccw:0.0703;39,52,125,255;rgb;ccw:0.0742;39,52,125,255;rgb;ccw:0.0742;40,54,129,255;rgb;ccw:0.0781;40,54,129,255;rgb;ccw:0.0781;40,55,132,255;rgb;ccw:0.082;40,55,132,255;rgb;ccw:0.082;41,56,136,255;rgb;ccw:0.0859;41,56,136,255;rgb;ccw:0.0859;41,58,140,255;rgb;ccw:0.0898;41,58,140,255;rgb;ccw:0.0898;41,59,143,255;rgb;ccw:0.0938;41,59,143,255;rgb;ccw:0.0938;41,60,147,255;rgb;ccw:0.0977;41,60,147,255;rgb;ccw:0.0977;41,62,151,255;rgb;ccw:0.1016;41,62,151,255;rgb;ccw:0.1016;41,63,154,255;rgb;ccw:0.1055;41,63,154,255;rgb;ccw:0.1055;41,64,158,255;rgb;ccw:0.1094;41,64,158,255;rgb;ccw:0.1094;41,66,162,255;rgb;ccw:0.1133;41,66,162,255;rgb;ccw:0.1133;40,67,165,255;rgb;ccw:0.1172;40,67,165,255;rgb;ccw:0.1172;39,69,169,255;rgb;ccw:0.1211;39,69,169,255;rgb;ccw:0.1211;38,71,172,255;rgb;ccw:0.125;38,71,172,255;rgb;ccw:0.125;37,72,176,255;rgb;ccw:0.1289;37,72,176,255;rgb;ccw:0.1289;35,74,179,255;rgb;ccw:0.1328;35,74,179,255;rgb;ccw:0.1328;33,76,182,255;rgb;ccw:0.1367;33,76,182,255;rgb;ccw:0.1367;31,78,184,255;rgb;ccw:0.1406;31,78,184,255;rgb;ccw:0.1406;28,80,186,255;rgb;ccw:0.1445;28,80,186,255;rgb;ccw:0.1445;25,82,188,255;rgb;ccw:0.1484;25,82,188,255;rgb;ccw:0.1484;22,85,189,255;rgb;ccw:0.1523;22,85,189,255;rgb;ccw:0.1523;19,87,190,255;rgb;ccw:0.1562;19,87,190,255;rgb;ccw:0.1562;16,89,190,255;rgb;ccw:0.1602;16,89,190,255;rgb;ccw:0.1602;13,91,190,255;rgb;ccw:0.1641;13,91,190,255;rgb;ccw:0.1641;12,94,190,255;rgb;ccw:0.168;12,94,190,255;rgb;ccw:0.168;10,96,190,255;rgb;ccw:0.1719;10,96,190,255;rgb;ccw:0.1719;10,98,190,255;rgb;ccw:0.1758;10,98,190,255;rgb;ccw:0.1758;10,100,190,255;rgb;ccw:0.1797;10,100,190,255;rgb;ccw:0.1797;11,102,189,255;rgb;ccw:0.1836;11,102,189,255;rgb;ccw:0.1836;13,104,189,255;rgb;ccw:0.1875;13,104,189,255;rgb;ccw:0.1875;15,106,189,255;rgb;ccw:0.1914;15,106,189,255;rgb;ccw:0.1914;17,108,188,255;rgb;ccw:0.1953;17,108,188,255;rgb;ccw:0.1953;19,110,188,255;rgb;ccw:0.1992;19,110,188,255;rgb;ccw:0.1992;22,112,188,255;rgb;ccw:0.2031;22,112,188,255;rgb;ccw:0.2031;25,114,187,255;rgb;ccw:0.207;25,114,187,255;rgb;ccw:0.207;27,116,187,255;rgb;ccw:0.2109;27,116,187,255;rgb;ccw:0.2109;30,118,187,255;rgb;ccw:0.2148;30,118,187,255;rgb;ccw:0.2148;33,120,187,255;rgb;ccw:0.2188;33,120,187,255;rgb;ccw:0.2188;35,122,186,255;rgb;ccw:0.2227;35,122,186,255;rgb;ccw:0.2227;38,123,186,255;rgb;ccw:0.2266;38,123,186,255;rgb;ccw:0.2266;41,125,186,255;rgb;ccw:0.2305;41,125,186,255;rgb;ccw:0.2305;43,127,186,255;rgb;ccw:0.2344;43,127,186,255;rgb;ccw:0.2344;46,129,186,255;rgb;ccw:0.2383;46,129,186,255;rgb;ccw:0.2383;48,131,186,255;rgb;ccw:0.2422;48,131,186,255;rgb;ccw:0.2422;51,132,186,255;rgb;ccw:0.2461;51,132,186,255;rgb;ccw:0.2461;54,134,186,255;rgb;ccw:0.25;54,134,186,255;rgb;ccw:0.25;56,136,186,255;rgb;ccw:0.2539;56,136,186,255;rgb;ccw:0.2539;59,137,186,255;rgb;ccw:0.2578;59,137,186,255;rgb;ccw:0.2578;62,139,186,255;rgb;ccw:0.2617;62,139,186,255;rgb;ccw:0.2617;64,141,186,255;rgb;ccw:0.2656;64,141,186,255;rgb;ccw:0.2656;67,143,186,255;rgb;ccw:0.2695;67,143,186,255;rgb;ccw:0.2695;70,144,186,255;rgb;ccw:0.2734;70,144,186,255;rgb;ccw:0.2734;72,146,186,255;rgb;ccw:0.2773;72,146,186,255;rgb;ccw:0.2773;75,148,186,255;rgb;ccw:0.2812;75,148,186,255;rgb;ccw:0.2812;78,149,186,255;rgb;ccw:0.2852;78,149,186,255;rgb;ccw:0.2852;81,151,186,255;rgb;ccw:0.2891;81,151,186,255;rgb;ccw:0.2891;83,153,186,255;rgb;ccw:0.293;83,153,186,255;rgb;ccw:0.293;86,154,187,255;rgb;ccw:0.2969;86,154,187,255;rgb;ccw:0.2969;89,156,187,255;rgb;ccw:0.3008;89,156,187,255;rgb;ccw:0.3008;92,157,187,255;rgb;ccw:0.3047;92,157,187,255;rgb;ccw:0.3047;95,159,187,255;rgb;ccw:0.3086;95,159,187,255;rgb;ccw:0.3086;98,160,187,255;rgb;ccw:0.3125;98,160,187,255;rgb;ccw:0.3125;101,162,188,255;rgb;ccw:0.3164;101,162,188,255;rgb;ccw:0.3164;104,164,188,255;rgb;ccw:0.3203;104,164,188,255;rgb;ccw:0.3203;107,165,188,255;rgb;ccw:0.3242;107,165,188,255;rgb;ccw:0.3242;110,167,189,255;rgb;ccw:0.3281;110,167,189,255;rgb;ccw:0.3281;113,168,189,255;rgb;ccw:0.332;113,168,189,255;rgb;ccw:0.332;117,170,190,255;rgb;ccw:0.3359;117,170,190,255;rgb;ccw:0.3359;120,171,190,255;rgb;ccw:0.3398;120,171,190,255;rgb;ccw:0.3398;123,172,191,255;rgb;ccw:0.3438;123,172,191,255;rgb;ccw:0.3438;126,174,191,255;rgb;ccw:0.3477;126,174,191,255;rgb;ccw:0.3477;129,175,192,255;rgb;ccw:0.3516;129,175,192,255;rgb;ccw:0.3516;133,177,192,255;rgb;ccw:0.3555;133,177,192,255;rgb;ccw:0.3555;136,178,193,255;rgb;ccw:0.3594;136,178,193,255;rgb;ccw:0.3594;139,180,194,255;rgb;ccw:0.3633;139,180,194,255;rgb;ccw:0.3633;142,181,195,255;rgb;ccw:0.3672;142,181,195,255;rgb;ccw:0.3672;145,183,195,255;rgb;ccw:0.3711;145,183,195,255;rgb;ccw:0.3711;148,184,196,255;rgb;ccw:0.375;148,184,196,255;rgb;ccw:0.375;152,186,197,255;rgb;ccw:0.3789;152,186,197,255;rgb;ccw:0.3789;155,187,198,255;rgb;ccw:0.3828;155,187,198,255;rgb;ccw:0.3828;158,188,199,255;rgb;ccw:0.3867;158,188,199,255;rgb;ccw:0.3867;161,190,200,255;rgb;ccw:0.3906;161,190,200,255;rgb;ccw:0.3906;164,191,201,255;rgb;ccw:0.3945;164,191,201,255;rgb;ccw:0.3945;167,193,202,255;rgb;ccw:0.3984;167,193,202,255;rgb;ccw:0.3984;170,194,203,255;rgb;ccw:0.4023;170,194,203,255;rgb;ccw:0.4023;173,196,204,255;rgb;ccw:0.4062;173,196,204,255;rgb;ccw:0.4062;176,197,205,255;rgb;ccw:0.4102;176,197,205,255;rgb;ccw:0.4102;179,199,206,255;rgb;ccw:0.4141;179,199,206,255;rgb;ccw:0.4141;182,201,207,255;rgb;ccw:0.418;182,201,207,255;rgb;ccw:0.418;185,202,208,255;rgb;ccw:0.4219;185,202,208,255;rgb;ccw:0.4219;188,204,210,255;rgb;ccw:0.4258;188,204,210,255;rgb;ccw:0.4258;191,205,211,255;rgb;ccw:0.4297;191,205,211,255;rgb;ccw:0.4297;193,207,212,255;rgb;ccw:0.4336;193,207,212,255;rgb;ccw:0.4336;196,208,213,255;rgb;ccw:0.4375;196,208,213,255;rgb;ccw:0.4375;199,210,215,255;rgb;ccw:0.4414;199,210,215,255;rgb;ccw:0.4414;202,212,216,255;rgb;ccw:0.4453;202,212,216,255;rgb;ccw:0.4453;205,213,217,255;rgb;ccw:0.4492;205,213,217,255;rgb;ccw:0.4492;208,215,218,255;rgb;ccw:0.4531;208,215,218,255;rgb;ccw:0.4531;211,217,220,255;rgb;ccw:0.457;211,217,220,255;rgb;ccw:0.457;213,218,221,255;rgb;ccw:0.4609;213,218,221,255;rgb;ccw:0.4609;216,220,222,255;rgb;ccw:0.4648;216,220,222,255;rgb;ccw:0.4648;219,222,224,255;rgb;ccw:0.4688;219,222,224,255;rgb;ccw:0.4688;222,224,225,255;rgb;ccw:0.4727;222,224,225,255;rgb;ccw:0.4727;225,225,227,255;rgb;ccw:0.4766;225,225,227,255;rgb;ccw:0.4766;227,227,228,255;rgb;ccw:0.4805;227,227,228,255;rgb;ccw:0.4805;230,229,230,255;rgb;ccw:0.4844;230,229,230,255;rgb;ccw:0.4844;233,231,231,255;rgb;ccw:0.4883;233,231,231,255;rgb;ccw:0.4883;235,233,233,255;rgb;ccw:0.4922;235,233,233,255;rgb;ccw:0.4922;238,234,234,255;rgb;ccw:0.4961;238,234,234,255;rgb;ccw:0.4961;241,236,236,255;rgb;ccw:0.5;241,236,236,255;rgb;ccw:0.5;241,236,235,255;rgb;ccw:0.5039;241,236,235,255;rgb;ccw:0.5039;240,234,233,255;rgb;ccw:0.5078;240,234,233,255;rgb;ccw:0.5078;239,232,230,255;rgb;ccw:0.5117;239,232,230,255;rgb;ccw:0.5117;238,229,227,255;rgb;ccw:0.5156;238,229,227,255;rgb;ccw:0.5156;237,227,224,255;rgb;ccw:0.5195;237,227,224,255;rgb;ccw:0.5195;236,224,222,255;rgb;ccw:0.5234;236,224,222,255;rgb;ccw:0.5234;235,222,219,255;rgb;ccw:0.5273;235,222,219,255;rgb;ccw:0.5273;234,220,216,255;rgb;ccw:0.5312;234,220,216,255;rgb;ccw:0.5312;233,217,213,255;rgb;ccw:0.5352;233,217,213,255;rgb;ccw:0.5352;232,215,210,255;rgb;ccw:0.5391;232,215,210,255;rgb;ccw:0.5391;231,213,207,255;rgb;ccw:0.543;231,213,207,255;rgb;ccw:0.543;230,210,205,255;rgb;ccw:0.5469;230,210,205,255;rgb;ccw:0.5469;229,208,202,255;rgb;ccw:0.5508;229,208,202,255;rgb;ccw:0.5508;229,206,199,255;rgb;ccw:0.5547;229,206,199,255;rgb;ccw:0.5547;228,203,196,255;rgb;ccw:0.5586;228,203,196,255;rgb;ccw:0.5586;227,201,193,255;rgb;ccw:0.5625;227,201,193,255;rgb;ccw:0.5625;226,199,190,255;rgb;ccw:0.5664;226,199,190,255;rgb;ccw:0.5664;225,196,187,255;rgb;ccw:0.5703;225,196,187,255;rgb;ccw:0.5703;225,194,184,255;rgb;ccw:0.5742;225,194,184,255;rgb;ccw:0.5742;224,192,181,255;rgb;ccw:0.5781;224,192,181,255;rgb;ccw:0.5781;223,189,178,255;rgb;ccw:0.582;223,189,178,255;rgb;ccw:0.582;223,187,176,255;rgb;ccw:0.5859;223,187,176,255;rgb;ccw:0.5859;222,185,173,255;rgb;ccw:0.5898;222,185,173,255;rgb;ccw:0.5898;221,182,170,255;rgb;ccw:0.5938;221,182,170,255;rgb;ccw:0.5938;220,180,167,255;rgb;ccw:0.5977;220,180,167,255;rgb;ccw:0.5977;220,178,164,255;rgb;ccw:0.6016;220,178,164,255;rgb;ccw:0.6016;219,175,161,255;rgb;ccw:0.6055;219,175,161,255;rgb;ccw:0.6055;218,173,158,255;rgb;ccw:0.6094;218,173,158,255;rgb;ccw:0.6094;218,171,155,255;rgb;ccw:0.6133;218,171,155,255;rgb;ccw:0.6133;217,169,152,255;rgb;ccw:0.6172;217,169,152,255;rgb;ccw:0.6172;216,166,150,255;rgb;ccw:0.6211;216,166,150,255;rgb;ccw:0.6211;216,164,147,255;rgb;ccw:0.625;216,164,147,255;rgb;ccw:0.625;215,162,144,255;rgb;ccw:0.6289;215,162,144,255;rgb;ccw:0.6289;214,159,141,255;rgb;ccw:0.6328;214,159,141,255;rgb;ccw:0.6328;214,157,138,255;rgb;ccw:0.6367;214,157,138,255;rgb;ccw:0.6367;213,155,135,255;rgb;ccw:0.6406;213,155,135,255;rgb;ccw:0.6406;212,153,132,255;rgb;ccw:0.6445;212,153,132,255;rgb;ccw:0.6445;211,150,129,255;rgb;ccw:0.6484;211,150,129,255;rgb;ccw:0.6484;211,148,127,255;rgb;ccw:0.6523;211,148,127,255;rgb;ccw:0.6523;210,146,124,255;rgb;ccw:0.6562;210,146,124,255;rgb;ccw:0.6562;209,143,121,255;rgb;ccw:0.6602;209,143,121,255;rgb;ccw:0.6602;209,141,118,255;rgb;ccw:0.6641;209,141,118,255;rgb;ccw:0.6641;208,139,115,255;rgb;ccw:0.668;208,139,115,255;rgb;ccw:0.668;207,137,112,255;rgb;ccw:0.6719;207,137,112,255;rgb;ccw:0.6719;207,134,110,255;rgb;ccw:0.6758;207,134,110,255;rgb;ccw:0.6758;206,132,107,255;rgb;ccw:0.6797;206,132,107,255;rgb;ccw:0.6797;205,130,104,255;rgb;ccw:0.6836;205,130,104,255;rgb;ccw:0.6836;205,127,101,255;rgb;ccw:0.6875;205,127,101,255;rgb;ccw:0.6875;204,125,99,255;rgb;ccw:0.6914;204,125,99,255;rgb;ccw:0.6914;203,123,96,255;rgb;ccw:0.6953;203,123,96,255;rgb;ccw:0.6953;202,121,93,255;rgb;ccw:0.6992;202,121,93,255;rgb;ccw:0.6992;202,118,91,255;rgb;ccw:0.7031;202,118,91,255;rgb;ccw:0.7031;201,116,88,255;rgb;ccw:0.707;201,116,88,255;rgb;ccw:0.707;200,114,85,255;rgb;ccw:0.7109;200,114,85,255;rgb;ccw:0.7109;199,111,83,255;rgb;ccw:0.7148;199,111,83,255;rgb;ccw:0.7148;199,109,80,255;rgb;ccw:0.7188;199,109,80,255;rgb;ccw:0.7188;198,107,77,255;rgb;ccw:0.7227;198,107,77,255;rgb;ccw:0.7227;197,104,75,255;rgb;ccw:0.7266;197,104,75,255;rgb;ccw:0.7266;196,102,72,255;rgb;ccw:0.7305;196,102,72,255;rgb;ccw:0.7305;195,99,70,255;rgb;ccw:0.7344;195,99,70,255;rgb;ccw:0.7344;195,97,67,255;rgb;ccw:0.7383;195,97,67,255;rgb;ccw:0.7383;194,95,65,255;rgb;ccw:0.7422;194,95,65,255;rgb;ccw:0.7422;193,92,63,255;rgb;ccw:0.7461;193,92,63,255;rgb;ccw:0.7461;192,90,60,255;rgb;ccw:0.75;192,90,60,255;rgb;ccw:0.75;191,87,58,255;rgb;ccw:0.7539;191,87,58,255;rgb;ccw:0.7539;190,85,56,255;rgb;ccw:0.7578;190,85,56,255;rgb;ccw:0.7578;190,82,54,255;rgb;ccw:0.7617;190,82,54,255;rgb;ccw:0.7617;189,80,52,255;rgb;ccw:0.7656;189,80,52,255;rgb;ccw:0.7656;188,77,50,255;rgb;ccw:0.7695;188,77,50,255;rgb;ccw:0.7695;187,75,48,255;rgb;ccw:0.7734;187,75,48,255;rgb;ccw:0.7734;186,72,46,255;rgb;ccw:0.7773;186,72,46,255;rgb;ccw:0.7773;185,69,44,255;rgb;ccw:0.7812;185,69,44,255;rgb;ccw:0.7812;184,67,43,255;rgb;ccw:0.7852;184,67,43,255;rgb;ccw:0.7852;183,64,41,255;rgb;ccw:0.7891;183,64,41,255;rgb;ccw:0.7891;182,61,40,255;rgb;ccw:0.793;182,61,40,255;rgb;ccw:0.793;180,59,39,255;rgb;ccw:0.7969;180,59,39,255;rgb;ccw:0.7969;179,56,38,255;rgb;ccw:0.8008;179,56,38,255;rgb;ccw:0.8008;178,53,37,255;rgb;ccw:0.8047;178,53,37,255;rgb;ccw:0.8047;177,51,37,255;rgb;ccw:0.8086;177,51,37,255;rgb;ccw:0.8086;175,48,36,255;rgb;ccw:0.8125;175,48,36,255;rgb;ccw:0.8125;174,46,36,255;rgb;ccw:0.8164;174,46,36,255;rgb;ccw:0.8164;172,43,36,255;rgb;ccw:0.8203;172,43,36,255;rgb;ccw:0.8203;171,41,36,255;rgb;ccw:0.8242;171,41,36,255;rgb;ccw:0.8242;169,38,36,255;rgb;ccw:0.8281;169,38,36,255;rgb;ccw:0.8281;167,36,36,255;rgb;ccw:0.832;167,36,36,255;rgb;ccw:0.832;165,33,37,255;rgb;ccw:0.8359;165,33,37,255;rgb;ccw:0.8359;163,31,37,255;rgb;ccw:0.8398;163,31,37,255;rgb;ccw:0.8398;161,29,37,255;rgb;ccw:0.8438;161,29,37,255;rgb;ccw:0.8438;159,27,38,255;rgb;ccw:0.8477;159,27,38,255;rgb;ccw:0.8477;157,25,38,255;rgb;ccw:0.8516;157,25,38,255;rgb;ccw:0.8516;155,23,39,255;rgb;ccw:0.8555;155,23,39,255;rgb;ccw:0.8555;153,22,39,255;rgb;ccw:0.8594;153,22,39,255;rgb;ccw:0.8594;151,20,40,255;rgb;ccw:0.8633;151,20,40,255;rgb;ccw:0.8633;148,19,40,255;rgb;ccw:0.8672;148,19,40,255;rgb;ccw:0.8672;146,18,40,255;rgb;ccw:0.8711;146,18,40,255;rgb;ccw:0.8711;144,16,41,255;rgb;ccw:0.875;144,16,41,255;rgb;ccw:0.875;141,16,41,255;rgb;ccw:0.8789;141,16,41,255;rgb;ccw:0.8789;139,15,41,255;rgb;ccw:0.8828;139,15,41,255;rgb;ccw:0.8828;136,15,41,255;rgb;ccw:0.8867;136,15,41,255;rgb;ccw:0.8867;134,14,41,255;rgb;ccw:0.8906;134,14,41,255;rgb;ccw:0.8906;131,14,41,255;rgb;ccw:0.8945;131,14,41,255;rgb;ccw:0.8945;128,14,41,255;rgb;ccw:0.8984;128,14,41,255;rgb;ccw:0.8984;126,14,41,255;rgb;ccw:0.9023;126,14,41,255;rgb;ccw:0.9023;123,14,41,255;rgb;ccw:0.9062;123,14,41,255;rgb;ccw:0.9062;120,14,40,255;rgb;ccw:0.9102;120,14,40,255;rgb;ccw:0.9102;118,14,40,255;rgb;ccw:0.9141;118,14,40,255;rgb;ccw:0.9141;115,14,39,255;rgb;ccw:0.918;115,14,39,255;rgb;ccw:0.918;112,14,39,255;rgb;ccw:0.9219;112,14,39,255;rgb;ccw:0.9219;109,14,38,255;rgb;ccw:0.9258;109,14,38,255;rgb;ccw:0.9258;107,15,37,255;rgb;ccw:0.9297;107,15,37,255;rgb;ccw:0.9297;104,15,37,255;rgb;ccw:0.9336;104,15,37,255;rgb;ccw:0.9336;101,15,36,255;rgb;ccw:0.9375;101,15,36,255;rgb;ccw:0.9375;99,14,35,255;rgb;ccw:0.9414;99,14,35,255;rgb;ccw:0.9414;96,14,34,255;rgb;ccw:0.9453;96,14,34,255;rgb;ccw:0.9453;94,14,33,255;rgb;ccw:0.9492;94,14,33,255;rgb;ccw:0.9492;91,14,32,255;rgb;ccw:0.9531;91,14,32,255;rgb;ccw:0.9531;88,14,31,255;rgb;ccw:0.957;88,14,31,255;rgb;ccw:0.957;86,14,30,255;rgb;ccw:0.9609;86,14,30,255;rgb;ccw:0.9609;83,13,29,255;rgb;ccw:0.9648;83,13,29,255;rgb;ccw:0.9648;81,13,28,255;rgb;ccw:0.9688;81,13,28,255;rgb;ccw:0.9688;78,13,27,255;rgb;ccw:0.9727;78,13,27,255;rgb;ccw:0.9727;75,12,25,255;rgb;ccw:0.9766;75,12,25,255;rgb;ccw:0.9766;73,12,24,255;rgb;ccw:0.9805;73,12,24,255;rgb;ccw:0.9805;70,11,23,255;rgb;ccw:0.9844;70,11,23,255;rgb;ccw:0.9844;68,11,22,255;rgb;ccw:0.9883;68,11,22,255;rgb;ccw:0.9883;65,10,20,255;rgb;ccw:0.9922;65,10,20,255;rgb;ccw:0.9922;63,10,19,255;rgb;ccw:0.9961;63,10,19,255;rgb;ccw:0.9961;60,9,18,255;rgb;ccw" type="QString"/>
            </Option>
          </colorramp>
          <item alpha="255" color="#181c43" label="-20°C" value="-20"/>
          <item alpha="255" color="#293e97" label="-16°C" value="-16"/>
          <item alpha="255" color="#1670bc" label="-12°C" value="-12"/>
          <item alpha="255" color="#599cbb" label="-8°C" value="-8"/>
          <item alpha="255" color="#aac2cb" label="-4°C" value="-4"/>
          <item alpha="255" color="#f1eceb" label="0°C" value="0"/>
          <item alpha="255" color="#dcb2a4" label="4°C" value="4"/>
          <item alpha="255" color="#ca765b" label="8°C" value="8"/>
          <item alpha="255" color="#b33826" label="12°C" value="12"/>
          <item alpha="255" color="#7e0e29" label="16°C" value="16"/>
          <item alpha="255" color="#3c0912" label="20°C" value="20"/>
          <rampLegendSettings prefix="" useContinuousLegend="1" direction="0" minimumLabel="" suffix="°C" orientation="1" maximumLabel="">
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

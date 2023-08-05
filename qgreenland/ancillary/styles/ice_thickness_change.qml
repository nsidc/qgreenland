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
            <Option type="QString" name="line_color" value="164,113,88,255"/>
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
            <Option type="QString" name="color" value="164,113,88,255"/>
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
    <rasterrenderer classificationMax="2" type="singlebandpseudocolor" nodataColor="" band="1" opacity="1" alphaBand="-1" classificationMin="-2">
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
        <colorrampshader colorRampType="INTERPOLATED" classificationMode="1" labelPrecision="5" maximumValue="2" clip="0" minimumValue="-2">
          <colorramp type="gradient" name="[source]">
            <Option type="Map">
              <Option type="QString" name="color1" value="60,9,18,255"/>
              <Option type="QString" name="color2" value="24,28,67,255"/>
              <Option type="QString" name="direction" value="ccw"/>
              <Option type="QString" name="discrete" value="0"/>
              <Option type="QString" name="rampType" value="gradient"/>
              <Option type="QString" name="spec" value="rgb"/>
              <Option type="QString" name="stops" value="0.0039;60,9,18,255;rgb;ccw:0.0039;63,10,19,255;rgb;ccw:0.0078;63,10,19,255;rgb;ccw:0.0078;65,10,20,255;rgb;ccw:0.0117;65,10,20,255;rgb;ccw:0.0117;68,11,22,255;rgb;ccw:0.0156;68,11,22,255;rgb;ccw:0.0156;70,11,23,255;rgb;ccw:0.0195;70,11,23,255;rgb;ccw:0.0195;73,12,24,255;rgb;ccw:0.0234;73,12,24,255;rgb;ccw:0.0234;75,12,25,255;rgb;ccw:0.0273;75,12,25,255;rgb;ccw:0.0273;78,13,27,255;rgb;ccw:0.0312;78,13,27,255;rgb;ccw:0.0312;81,13,28,255;rgb;ccw:0.0352;81,13,28,255;rgb;ccw:0.0352;83,13,29,255;rgb;ccw:0.0391;83,13,29,255;rgb;ccw:0.0391;86,14,30,255;rgb;ccw:0.043;86,14,30,255;rgb;ccw:0.043;88,14,31,255;rgb;ccw:0.0469;88,14,31,255;rgb;ccw:0.0469;91,14,32,255;rgb;ccw:0.0508;91,14,32,255;rgb;ccw:0.0508;94,14,33,255;rgb;ccw:0.0547;94,14,33,255;rgb;ccw:0.0547;96,14,34,255;rgb;ccw:0.0586;96,14,34,255;rgb;ccw:0.0586;99,14,35,255;rgb;ccw:0.0625;99,14,35,255;rgb;ccw:0.0625;101,15,36,255;rgb;ccw:0.0664;101,15,36,255;rgb;ccw:0.0664;104,15,37,255;rgb;ccw:0.0703;104,15,37,255;rgb;ccw:0.0703;107,15,37,255;rgb;ccw:0.0742;107,15,37,255;rgb;ccw:0.0742;109,14,38,255;rgb;ccw:0.0781;109,14,38,255;rgb;ccw:0.0781;112,14,39,255;rgb;ccw:0.082;112,14,39,255;rgb;ccw:0.082;115,14,39,255;rgb;ccw:0.0859;115,14,39,255;rgb;ccw:0.0859;118,14,40,255;rgb;ccw:0.0898;118,14,40,255;rgb;ccw:0.0898;120,14,40,255;rgb;ccw:0.0938;120,14,40,255;rgb;ccw:0.0938;123,14,41,255;rgb;ccw:0.0977;123,14,41,255;rgb;ccw:0.0977;126,14,41,255;rgb;ccw:0.1016;126,14,41,255;rgb;ccw:0.1016;128,14,41,255;rgb;ccw:0.1055;128,14,41,255;rgb;ccw:0.1055;131,14,41,255;rgb;ccw:0.1094;131,14,41,255;rgb;ccw:0.1094;134,14,41,255;rgb;ccw:0.1133;134,14,41,255;rgb;ccw:0.1133;136,15,41,255;rgb;ccw:0.1172;136,15,41,255;rgb;ccw:0.1172;139,15,41,255;rgb;ccw:0.1211;139,15,41,255;rgb;ccw:0.1211;141,16,41,255;rgb;ccw:0.125;141,16,41,255;rgb;ccw:0.125;144,16,41,255;rgb;ccw:0.1289;144,16,41,255;rgb;ccw:0.1289;146,18,40,255;rgb;ccw:0.1328;146,18,40,255;rgb;ccw:0.1328;148,19,40,255;rgb;ccw:0.1367;148,19,40,255;rgb;ccw:0.1367;151,20,40,255;rgb;ccw:0.1406;151,20,40,255;rgb;ccw:0.1406;153,22,39,255;rgb;ccw:0.1445;153,22,39,255;rgb;ccw:0.1445;155,23,39,255;rgb;ccw:0.1484;155,23,39,255;rgb;ccw:0.1484;157,25,38,255;rgb;ccw:0.1523;157,25,38,255;rgb;ccw:0.1523;159,27,38,255;rgb;ccw:0.1562;159,27,38,255;rgb;ccw:0.1562;161,29,37,255;rgb;ccw:0.1602;161,29,37,255;rgb;ccw:0.1602;163,31,37,255;rgb;ccw:0.1641;163,31,37,255;rgb;ccw:0.1641;165,33,37,255;rgb;ccw:0.168;165,33,37,255;rgb;ccw:0.168;167,36,36,255;rgb;ccw:0.1719;167,36,36,255;rgb;ccw:0.1719;169,38,36,255;rgb;ccw:0.1758;169,38,36,255;rgb;ccw:0.1758;171,41,36,255;rgb;ccw:0.1797;171,41,36,255;rgb;ccw:0.1797;172,43,36,255;rgb;ccw:0.1836;172,43,36,255;rgb;ccw:0.1836;174,46,36,255;rgb;ccw:0.1875;174,46,36,255;rgb;ccw:0.1875;175,48,36,255;rgb;ccw:0.1914;175,48,36,255;rgb;ccw:0.1914;177,51,37,255;rgb;ccw:0.1953;177,51,37,255;rgb;ccw:0.1953;178,53,37,255;rgb;ccw:0.1992;178,53,37,255;rgb;ccw:0.1992;179,56,38,255;rgb;ccw:0.2031;179,56,38,255;rgb;ccw:0.2031;180,59,39,255;rgb;ccw:0.207;180,59,39,255;rgb;ccw:0.207;182,61,40,255;rgb;ccw:0.2109;182,61,40,255;rgb;ccw:0.2109;183,64,41,255;rgb;ccw:0.2148;183,64,41,255;rgb;ccw:0.2148;184,67,43,255;rgb;ccw:0.2188;184,67,43,255;rgb;ccw:0.2188;185,69,44,255;rgb;ccw:0.2227;185,69,44,255;rgb;ccw:0.2227;186,72,46,255;rgb;ccw:0.2266;186,72,46,255;rgb;ccw:0.2266;187,75,48,255;rgb;ccw:0.2305;187,75,48,255;rgb;ccw:0.2305;188,77,50,255;rgb;ccw:0.2344;188,77,50,255;rgb;ccw:0.2344;189,80,52,255;rgb;ccw:0.2383;189,80,52,255;rgb;ccw:0.2383;190,82,54,255;rgb;ccw:0.2422;190,82,54,255;rgb;ccw:0.2422;190,85,56,255;rgb;ccw:0.2461;190,85,56,255;rgb;ccw:0.2461;191,87,58,255;rgb;ccw:0.25;191,87,58,255;rgb;ccw:0.25;192,90,60,255;rgb;ccw:0.2539;192,90,60,255;rgb;ccw:0.2539;193,92,63,255;rgb;ccw:0.2578;193,92,63,255;rgb;ccw:0.2578;194,95,65,255;rgb;ccw:0.2617;194,95,65,255;rgb;ccw:0.2617;195,97,67,255;rgb;ccw:0.2656;195,97,67,255;rgb;ccw:0.2656;195,99,70,255;rgb;ccw:0.2695;195,99,70,255;rgb;ccw:0.2695;196,102,72,255;rgb;ccw:0.2734;196,102,72,255;rgb;ccw:0.2734;197,104,75,255;rgb;ccw:0.2773;197,104,75,255;rgb;ccw:0.2773;198,107,77,255;rgb;ccw:0.2812;198,107,77,255;rgb;ccw:0.2812;199,109,80,255;rgb;ccw:0.2852;199,109,80,255;rgb;ccw:0.2852;199,111,83,255;rgb;ccw:0.2891;199,111,83,255;rgb;ccw:0.2891;200,114,85,255;rgb;ccw:0.293;200,114,85,255;rgb;ccw:0.293;201,116,88,255;rgb;ccw:0.2969;201,116,88,255;rgb;ccw:0.2969;202,118,91,255;rgb;ccw:0.3008;202,118,91,255;rgb;ccw:0.3008;202,121,93,255;rgb;ccw:0.3047;202,121,93,255;rgb;ccw:0.3047;203,123,96,255;rgb;ccw:0.3086;203,123,96,255;rgb;ccw:0.3086;204,125,99,255;rgb;ccw:0.3125;204,125,99,255;rgb;ccw:0.3125;205,127,101,255;rgb;ccw:0.3164;205,127,101,255;rgb;ccw:0.3164;205,130,104,255;rgb;ccw:0.3203;205,130,104,255;rgb;ccw:0.3203;206,132,107,255;rgb;ccw:0.3242;206,132,107,255;rgb;ccw:0.3242;207,134,110,255;rgb;ccw:0.3281;207,134,110,255;rgb;ccw:0.3281;207,137,112,255;rgb;ccw:0.332;207,137,112,255;rgb;ccw:0.332;208,139,115,255;rgb;ccw:0.3359;208,139,115,255;rgb;ccw:0.3359;209,141,118,255;rgb;ccw:0.3398;209,141,118,255;rgb;ccw:0.3398;209,143,121,255;rgb;ccw:0.3438;209,143,121,255;rgb;ccw:0.3438;210,146,124,255;rgb;ccw:0.3477;210,146,124,255;rgb;ccw:0.3477;211,148,127,255;rgb;ccw:0.3516;211,148,127,255;rgb;ccw:0.3516;211,150,129,255;rgb;ccw:0.3555;211,150,129,255;rgb;ccw:0.3555;212,153,132,255;rgb;ccw:0.3594;212,153,132,255;rgb;ccw:0.3594;213,155,135,255;rgb;ccw:0.3633;213,155,135,255;rgb;ccw:0.3633;214,157,138,255;rgb;ccw:0.3672;214,157,138,255;rgb;ccw:0.3672;214,159,141,255;rgb;ccw:0.3711;214,159,141,255;rgb;ccw:0.3711;215,162,144,255;rgb;ccw:0.375;215,162,144,255;rgb;ccw:0.375;216,164,147,255;rgb;ccw:0.3789;216,164,147,255;rgb;ccw:0.3789;216,166,150,255;rgb;ccw:0.3828;216,166,150,255;rgb;ccw:0.3828;217,169,152,255;rgb;ccw:0.3867;217,169,152,255;rgb;ccw:0.3867;218,171,155,255;rgb;ccw:0.3906;218,171,155,255;rgb;ccw:0.3906;218,173,158,255;rgb;ccw:0.3945;218,173,158,255;rgb;ccw:0.3945;219,175,161,255;rgb;ccw:0.3984;219,175,161,255;rgb;ccw:0.3984;220,178,164,255;rgb;ccw:0.4023;220,178,164,255;rgb;ccw:0.4023;220,180,167,255;rgb;ccw:0.4062;220,180,167,255;rgb;ccw:0.4062;221,182,170,255;rgb;ccw:0.4102;221,182,170,255;rgb;ccw:0.4102;222,185,173,255;rgb;ccw:0.4141;222,185,173,255;rgb;ccw:0.4141;223,187,176,255;rgb;ccw:0.418;223,187,176,255;rgb;ccw:0.418;223,189,178,255;rgb;ccw:0.4219;223,189,178,255;rgb;ccw:0.4219;224,192,181,255;rgb;ccw:0.4258;224,192,181,255;rgb;ccw:0.4258;225,194,184,255;rgb;ccw:0.4297;225,194,184,255;rgb;ccw:0.4297;225,196,187,255;rgb;ccw:0.4336;225,196,187,255;rgb;ccw:0.4336;226,199,190,255;rgb;ccw:0.4375;226,199,190,255;rgb;ccw:0.4375;227,201,193,255;rgb;ccw:0.4414;227,201,193,255;rgb;ccw:0.4414;228,203,196,255;rgb;ccw:0.4453;228,203,196,255;rgb;ccw:0.4453;229,206,199,255;rgb;ccw:0.4492;229,206,199,255;rgb;ccw:0.4492;229,208,202,255;rgb;ccw:0.4531;229,208,202,255;rgb;ccw:0.4531;230,210,205,255;rgb;ccw:0.457;230,210,205,255;rgb;ccw:0.457;231,213,207,255;rgb;ccw:0.4609;231,213,207,255;rgb;ccw:0.4609;232,215,210,255;rgb;ccw:0.4648;232,215,210,255;rgb;ccw:0.4648;233,217,213,255;rgb;ccw:0.4688;233,217,213,255;rgb;ccw:0.4688;234,220,216,255;rgb;ccw:0.4727;234,220,216,255;rgb;ccw:0.4727;235,222,219,255;rgb;ccw:0.4766;235,222,219,255;rgb;ccw:0.4766;236,224,222,255;rgb;ccw:0.4805;236,224,222,255;rgb;ccw:0.4805;237,227,224,255;rgb;ccw:0.4844;237,227,224,255;rgb;ccw:0.4844;238,229,227,255;rgb;ccw:0.4883;238,229,227,255;rgb;ccw:0.4883;239,232,230,255;rgb;ccw:0.4922;239,232,230,255;rgb;ccw:0.4922;240,234,233,255;rgb;ccw:0.4961;240,234,233,255;rgb;ccw:0.4961;241,236,235,255;rgb;ccw:0.5;241,236,235,255;rgb;ccw:0.5;241,236,236,255;rgb;ccw:0.5039;241,236,236,255;rgb;ccw:0.5039;238,234,234,255;rgb;ccw:0.5078;238,234,234,255;rgb;ccw:0.5078;235,233,233,255;rgb;ccw:0.5117;235,233,233,255;rgb;ccw:0.5117;233,231,231,255;rgb;ccw:0.5156;233,231,231,255;rgb;ccw:0.5156;230,229,230,255;rgb;ccw:0.5195;230,229,230,255;rgb;ccw:0.5195;227,227,228,255;rgb;ccw:0.5234;227,227,228,255;rgb;ccw:0.5234;225,225,227,255;rgb;ccw:0.5273;225,225,227,255;rgb;ccw:0.5273;222,224,225,255;rgb;ccw:0.5312;222,224,225,255;rgb;ccw:0.5312;219,222,224,255;rgb;ccw:0.5352;219,222,224,255;rgb;ccw:0.5352;216,220,222,255;rgb;ccw:0.5391;216,220,222,255;rgb;ccw:0.5391;213,218,221,255;rgb;ccw:0.543;213,218,221,255;rgb;ccw:0.543;211,217,220,255;rgb;ccw:0.5469;211,217,220,255;rgb;ccw:0.5469;208,215,218,255;rgb;ccw:0.5508;208,215,218,255;rgb;ccw:0.5508;205,213,217,255;rgb;ccw:0.5547;205,213,217,255;rgb;ccw:0.5547;202,212,216,255;rgb;ccw:0.5586;202,212,216,255;rgb;ccw:0.5586;199,210,215,255;rgb;ccw:0.5625;199,210,215,255;rgb;ccw:0.5625;196,208,213,255;rgb;ccw:0.5664;196,208,213,255;rgb;ccw:0.5664;193,207,212,255;rgb;ccw:0.5703;193,207,212,255;rgb;ccw:0.5703;191,205,211,255;rgb;ccw:0.5742;191,205,211,255;rgb;ccw:0.5742;188,204,210,255;rgb;ccw:0.5781;188,204,210,255;rgb;ccw:0.5781;185,202,208,255;rgb;ccw:0.582;185,202,208,255;rgb;ccw:0.582;182,201,207,255;rgb;ccw:0.5859;182,201,207,255;rgb;ccw:0.5859;179,199,206,255;rgb;ccw:0.5898;179,199,206,255;rgb;ccw:0.5898;176,197,205,255;rgb;ccw:0.5938;176,197,205,255;rgb;ccw:0.5938;173,196,204,255;rgb;ccw:0.5977;173,196,204,255;rgb;ccw:0.5977;170,194,203,255;rgb;ccw:0.6016;170,194,203,255;rgb;ccw:0.6016;167,193,202,255;rgb;ccw:0.6055;167,193,202,255;rgb;ccw:0.6055;164,191,201,255;rgb;ccw:0.6094;164,191,201,255;rgb;ccw:0.6094;161,190,200,255;rgb;ccw:0.6133;161,190,200,255;rgb;ccw:0.6133;158,188,199,255;rgb;ccw:0.6172;158,188,199,255;rgb;ccw:0.6172;155,187,198,255;rgb;ccw:0.6211;155,187,198,255;rgb;ccw:0.6211;152,186,197,255;rgb;ccw:0.625;152,186,197,255;rgb;ccw:0.625;148,184,196,255;rgb;ccw:0.6289;148,184,196,255;rgb;ccw:0.6289;145,183,195,255;rgb;ccw:0.6328;145,183,195,255;rgb;ccw:0.6328;142,181,195,255;rgb;ccw:0.6367;142,181,195,255;rgb;ccw:0.6367;139,180,194,255;rgb;ccw:0.6406;139,180,194,255;rgb;ccw:0.6406;136,178,193,255;rgb;ccw:0.6445;136,178,193,255;rgb;ccw:0.6445;133,177,192,255;rgb;ccw:0.6484;133,177,192,255;rgb;ccw:0.6484;129,175,192,255;rgb;ccw:0.6523;129,175,192,255;rgb;ccw:0.6523;126,174,191,255;rgb;ccw:0.6562;126,174,191,255;rgb;ccw:0.6562;123,172,191,255;rgb;ccw:0.6602;123,172,191,255;rgb;ccw:0.6602;120,171,190,255;rgb;ccw:0.6641;120,171,190,255;rgb;ccw:0.6641;117,170,190,255;rgb;ccw:0.668;117,170,190,255;rgb;ccw:0.668;113,168,189,255;rgb;ccw:0.6719;113,168,189,255;rgb;ccw:0.6719;110,167,189,255;rgb;ccw:0.6758;110,167,189,255;rgb;ccw:0.6758;107,165,188,255;rgb;ccw:0.6797;107,165,188,255;rgb;ccw:0.6797;104,164,188,255;rgb;ccw:0.6836;104,164,188,255;rgb;ccw:0.6836;101,162,188,255;rgb;ccw:0.6875;101,162,188,255;rgb;ccw:0.6875;98,160,187,255;rgb;ccw:0.6914;98,160,187,255;rgb;ccw:0.6914;95,159,187,255;rgb;ccw:0.6953;95,159,187,255;rgb;ccw:0.6953;92,157,187,255;rgb;ccw:0.6992;92,157,187,255;rgb;ccw:0.6992;89,156,187,255;rgb;ccw:0.7031;89,156,187,255;rgb;ccw:0.7031;86,154,187,255;rgb;ccw:0.707;86,154,187,255;rgb;ccw:0.707;83,153,186,255;rgb;ccw:0.7109;83,153,186,255;rgb;ccw:0.7109;81,151,186,255;rgb;ccw:0.7148;81,151,186,255;rgb;ccw:0.7148;78,149,186,255;rgb;ccw:0.7188;78,149,186,255;rgb;ccw:0.7188;75,148,186,255;rgb;ccw:0.7227;75,148,186,255;rgb;ccw:0.7227;72,146,186,255;rgb;ccw:0.7266;72,146,186,255;rgb;ccw:0.7266;70,144,186,255;rgb;ccw:0.7305;70,144,186,255;rgb;ccw:0.7305;67,143,186,255;rgb;ccw:0.7344;67,143,186,255;rgb;ccw:0.7344;64,141,186,255;rgb;ccw:0.7383;64,141,186,255;rgb;ccw:0.7383;62,139,186,255;rgb;ccw:0.7422;62,139,186,255;rgb;ccw:0.7422;59,137,186,255;rgb;ccw:0.7461;59,137,186,255;rgb;ccw:0.7461;56,136,186,255;rgb;ccw:0.75;56,136,186,255;rgb;ccw:0.75;54,134,186,255;rgb;ccw:0.7539;54,134,186,255;rgb;ccw:0.7539;51,132,186,255;rgb;ccw:0.7578;51,132,186,255;rgb;ccw:0.7578;48,131,186,255;rgb;ccw:0.7617;48,131,186,255;rgb;ccw:0.7617;46,129,186,255;rgb;ccw:0.7656;46,129,186,255;rgb;ccw:0.7656;43,127,186,255;rgb;ccw:0.7695;43,127,186,255;rgb;ccw:0.7695;41,125,186,255;rgb;ccw:0.7734;41,125,186,255;rgb;ccw:0.7734;38,123,186,255;rgb;ccw:0.7773;38,123,186,255;rgb;ccw:0.7773;35,122,186,255;rgb;ccw:0.7812;35,122,186,255;rgb;ccw:0.7812;33,120,187,255;rgb;ccw:0.7852;33,120,187,255;rgb;ccw:0.7852;30,118,187,255;rgb;ccw:0.7891;30,118,187,255;rgb;ccw:0.7891;27,116,187,255;rgb;ccw:0.793;27,116,187,255;rgb;ccw:0.793;25,114,187,255;rgb;ccw:0.7969;25,114,187,255;rgb;ccw:0.7969;22,112,188,255;rgb;ccw:0.8008;22,112,188,255;rgb;ccw:0.8008;19,110,188,255;rgb;ccw:0.8047;19,110,188,255;rgb;ccw:0.8047;17,108,188,255;rgb;ccw:0.8086;17,108,188,255;rgb;ccw:0.8086;15,106,189,255;rgb;ccw:0.8125;15,106,189,255;rgb;ccw:0.8125;13,104,189,255;rgb;ccw:0.8164;13,104,189,255;rgb;ccw:0.8164;11,102,189,255;rgb;ccw:0.8203;11,102,189,255;rgb;ccw:0.8203;10,100,190,255;rgb;ccw:0.8242;10,100,190,255;rgb;ccw:0.8242;10,98,190,255;rgb;ccw:0.8281;10,98,190,255;rgb;ccw:0.8281;10,96,190,255;rgb;ccw:0.832;10,96,190,255;rgb;ccw:0.832;12,94,190,255;rgb;ccw:0.8359;12,94,190,255;rgb;ccw:0.8359;13,91,190,255;rgb;ccw:0.8398;13,91,190,255;rgb;ccw:0.8398;16,89,190,255;rgb;ccw:0.8438;16,89,190,255;rgb;ccw:0.8438;19,87,190,255;rgb;ccw:0.8477;19,87,190,255;rgb;ccw:0.8477;22,85,189,255;rgb;ccw:0.8516;22,85,189,255;rgb;ccw:0.8516;25,82,188,255;rgb;ccw:0.8555;25,82,188,255;rgb;ccw:0.8555;28,80,186,255;rgb;ccw:0.8594;28,80,186,255;rgb;ccw:0.8594;31,78,184,255;rgb;ccw:0.8633;31,78,184,255;rgb;ccw:0.8633;33,76,182,255;rgb;ccw:0.8672;33,76,182,255;rgb;ccw:0.8672;35,74,179,255;rgb;ccw:0.8711;35,74,179,255;rgb;ccw:0.8711;37,72,176,255;rgb;ccw:0.875;37,72,176,255;rgb;ccw:0.875;38,71,172,255;rgb;ccw:0.8789;38,71,172,255;rgb;ccw:0.8789;39,69,169,255;rgb;ccw:0.8828;39,69,169,255;rgb;ccw:0.8828;40,67,165,255;rgb;ccw:0.8867;40,67,165,255;rgb;ccw:0.8867;41,66,162,255;rgb;ccw:0.8906;41,66,162,255;rgb;ccw:0.8906;41,64,158,255;rgb;ccw:0.8945;41,64,158,255;rgb;ccw:0.8945;41,63,154,255;rgb;ccw:0.8984;41,63,154,255;rgb;ccw:0.8984;41,62,151,255;rgb;ccw:0.9023;41,62,151,255;rgb;ccw:0.9023;41,60,147,255;rgb;ccw:0.9062;41,60,147,255;rgb;ccw:0.9062;41,59,143,255;rgb;ccw:0.9102;41,59,143,255;rgb;ccw:0.9102;41,58,140,255;rgb;ccw:0.9141;41,58,140,255;rgb;ccw:0.9141;41,56,136,255;rgb;ccw:0.918;41,56,136,255;rgb;ccw:0.918;40,55,132,255;rgb;ccw:0.9219;40,55,132,255;rgb;ccw:0.9219;40,54,129,255;rgb;ccw:0.9258;40,54,129,255;rgb;ccw:0.9258;39,52,125,255;rgb;ccw:0.9297;39,52,125,255;rgb;ccw:0.9297;39,51,122,255;rgb;ccw:0.9336;39,51,122,255;rgb;ccw:0.9336;38,50,118,255;rgb;ccw:0.9375;38,50,118,255;rgb;ccw:0.9375;37,48,115,255;rgb;ccw:0.9414;37,48,115,255;rgb;ccw:0.9414;37,47,111,255;rgb;ccw:0.9453;37,47,111,255;rgb;ccw:0.9453;36,46,108,255;rgb;ccw:0.9492;36,46,108,255;rgb;ccw:0.9492;35,45,105,255;rgb;ccw:0.9531;35,45,105,255;rgb;ccw:0.9531;34,43,101,255;rgb;ccw:0.957;34,43,101,255;rgb;ccw:0.957;33,42,98,255;rgb;ccw:0.9609;33,42,98,255;rgb;ccw:0.9609;33,41,95,255;rgb;ccw:0.9648;33,41,95,255;rgb;ccw:0.9648;32,39,91,255;rgb;ccw:0.9688;32,39,91,255;rgb;ccw:0.9688;31,38,88,255;rgb;ccw:0.9727;31,38,88,255;rgb;ccw:0.9727;30,37,85,255;rgb;ccw:0.9766;30,37,85,255;rgb;ccw:0.9766;29,35,82,255;rgb;ccw:0.9805;29,35,82,255;rgb;ccw:0.9805;28,34,79,255;rgb;ccw:0.9844;28,34,79,255;rgb;ccw:0.9844;27,33,76,255;rgb;ccw:0.9883;27,33,76,255;rgb;ccw:0.9883;26,31,73,255;rgb;ccw:0.9922;26,31,73,255;rgb;ccw:0.9922;25,30,70,255;rgb;ccw:0.9961;25,30,70,255;rgb;ccw:0.9961;24,28,67,255;rgb;ccw"/>
            </Option>
          </colorramp>
          <item color="#3c0912" label="-2.00000 m/y" alpha="255" value="-2"/>
          <item color="#3f0a13" label="-1.98440 m/y" alpha="255" value="-1.9844"/>
          <item color="#3f0a13" label="-1.98440 m/y" alpha="255" value="-1.9844"/>
          <item color="#410a14" label="-1.96880 m/y" alpha="255" value="-1.9688"/>
          <item color="#410a14" label="-1.96880 m/y" alpha="255" value="-1.9688"/>
          <item color="#440b16" label="-1.95320 m/y" alpha="255" value="-1.9532"/>
          <item color="#440b16" label="-1.95320 m/y" alpha="255" value="-1.9532"/>
          <item color="#460b17" label="-1.93760 m/y" alpha="255" value="-1.9376"/>
          <item color="#460b17" label="-1.93760 m/y" alpha="255" value="-1.9376"/>
          <item color="#490c18" label="-1.92200 m/y" alpha="255" value="-1.922"/>
          <item color="#490c18" label="-1.92200 m/y" alpha="255" value="-1.922"/>
          <item color="#4b0c19" label="-1.90640 m/y" alpha="255" value="-1.9064"/>
          <item color="#4b0c19" label="-1.90640 m/y" alpha="255" value="-1.9064"/>
          <item color="#4e0d1b" label="-1.89080 m/y" alpha="255" value="-1.8908"/>
          <item color="#4e0d1b" label="-1.89080 m/y" alpha="255" value="-1.8908"/>
          <item color="#510d1c" label="-1.87520 m/y" alpha="255" value="-1.8752"/>
          <item color="#510d1c" label="-1.87520 m/y" alpha="255" value="-1.8752"/>
          <item color="#530d1d" label="-1.85920 m/y" alpha="255" value="-1.8592"/>
          <item color="#530d1d" label="-1.85920 m/y" alpha="255" value="-1.8592"/>
          <item color="#560e1e" label="-1.84360 m/y" alpha="255" value="-1.8436"/>
          <item color="#560e1e" label="-1.84360 m/y" alpha="255" value="-1.8436"/>
          <item color="#580e1f" label="-1.82800 m/y" alpha="255" value="-1.828"/>
          <item color="#580e1f" label="-1.82800 m/y" alpha="255" value="-1.828"/>
          <item color="#5b0e20" label="-1.81240 m/y" alpha="255" value="-1.8124"/>
          <item color="#5b0e20" label="-1.81240 m/y" alpha="255" value="-1.8124"/>
          <item color="#5e0e21" label="-1.79680 m/y" alpha="255" value="-1.7968"/>
          <item color="#5e0e21" label="-1.79680 m/y" alpha="255" value="-1.7968"/>
          <item color="#600e22" label="-1.78120 m/y" alpha="255" value="-1.7812"/>
          <item color="#600e22" label="-1.78120 m/y" alpha="255" value="-1.7812"/>
          <item color="#630e23" label="-1.76560 m/y" alpha="255" value="-1.7656"/>
          <item color="#630e23" label="-1.76560 m/y" alpha="255" value="-1.7656"/>
          <item color="#650f24" label="-1.75000 m/y" alpha="255" value="-1.75"/>
          <item color="#650f24" label="-1.75000 m/y" alpha="255" value="-1.75"/>
          <item color="#680f25" label="-1.73440 m/y" alpha="255" value="-1.7344"/>
          <item color="#680f25" label="-1.73440 m/y" alpha="255" value="-1.7344"/>
          <item color="#6b0f25" label="-1.71880 m/y" alpha="255" value="-1.7188"/>
          <item color="#6b0f25" label="-1.71880 m/y" alpha="255" value="-1.7188"/>
          <item color="#6d0e26" label="-1.70320 m/y" alpha="255" value="-1.7032"/>
          <item color="#6d0e26" label="-1.70320 m/y" alpha="255" value="-1.7032"/>
          <item color="#700e27" label="-1.68760 m/y" alpha="255" value="-1.6876"/>
          <item color="#700e27" label="-1.68760 m/y" alpha="255" value="-1.6876"/>
          <item color="#730e27" label="-1.67200 m/y" alpha="255" value="-1.672"/>
          <item color="#730e27" label="-1.67200 m/y" alpha="255" value="-1.672"/>
          <item color="#760e28" label="-1.65640 m/y" alpha="255" value="-1.6564"/>
          <item color="#760e28" label="-1.65640 m/y" alpha="255" value="-1.6564"/>
          <item color="#780e28" label="-1.64080 m/y" alpha="255" value="-1.6408"/>
          <item color="#780e28" label="-1.64080 m/y" alpha="255" value="-1.6408"/>
          <item color="#7b0e29" label="-1.62480 m/y" alpha="255" value="-1.6248"/>
          <item color="#7b0e29" label="-1.62480 m/y" alpha="255" value="-1.6248"/>
          <item color="#7e0e29" label="-1.60920 m/y" alpha="255" value="-1.6092"/>
          <item color="#7e0e29" label="-1.60920 m/y" alpha="255" value="-1.6092"/>
          <item color="#800e29" label="-1.59360 m/y" alpha="255" value="-1.5936"/>
          <item color="#800e29" label="-1.59360 m/y" alpha="255" value="-1.5936"/>
          <item color="#830e29" label="-1.57800 m/y" alpha="255" value="-1.578"/>
          <item color="#830e29" label="-1.57800 m/y" alpha="255" value="-1.578"/>
          <item color="#860e29" label="-1.56240 m/y" alpha="255" value="-1.5624"/>
          <item color="#860e29" label="-1.56240 m/y" alpha="255" value="-1.5624"/>
          <item color="#880f29" label="-1.54680 m/y" alpha="255" value="-1.5468"/>
          <item color="#880f29" label="-1.54680 m/y" alpha="255" value="-1.5468"/>
          <item color="#8b0f29" label="-1.53120 m/y" alpha="255" value="-1.5312"/>
          <item color="#8b0f29" label="-1.53120 m/y" alpha="255" value="-1.5312"/>
          <item color="#8d1029" label="-1.51560 m/y" alpha="255" value="-1.5156"/>
          <item color="#8d1029" label="-1.51560 m/y" alpha="255" value="-1.5156"/>
          <item color="#901029" label="-1.50000 m/y" alpha="255" value="-1.5"/>
          <item color="#901029" label="-1.50000 m/y" alpha="255" value="-1.5"/>
          <item color="#921228" label="-1.48440 m/y" alpha="255" value="-1.4844"/>
          <item color="#921228" label="-1.48440 m/y" alpha="255" value="-1.4844"/>
          <item color="#941328" label="-1.46880 m/y" alpha="255" value="-1.4688"/>
          <item color="#941328" label="-1.46880 m/y" alpha="255" value="-1.4688"/>
          <item color="#971428" label="-1.45320 m/y" alpha="255" value="-1.4532"/>
          <item color="#971428" label="-1.45320 m/y" alpha="255" value="-1.4532"/>
          <item color="#991627" label="-1.43760 m/y" alpha="255" value="-1.4376"/>
          <item color="#991627" label="-1.43760 m/y" alpha="255" value="-1.4376"/>
          <item color="#9b1727" label="-1.42200 m/y" alpha="255" value="-1.422"/>
          <item color="#9b1727" label="-1.42200 m/y" alpha="255" value="-1.422"/>
          <item color="#9d1926" label="-1.40640 m/y" alpha="255" value="-1.4064"/>
          <item color="#9d1926" label="-1.40640 m/y" alpha="255" value="-1.4064"/>
          <item color="#9f1b26" label="-1.39080 m/y" alpha="255" value="-1.3908"/>
          <item color="#9f1b26" label="-1.39080 m/y" alpha="255" value="-1.3908"/>
          <item color="#a11d25" label="-1.37520 m/y" alpha="255" value="-1.3752"/>
          <item color="#a11d25" label="-1.37520 m/y" alpha="255" value="-1.3752"/>
          <item color="#a31f25" label="-1.35920 m/y" alpha="255" value="-1.3592"/>
          <item color="#a31f25" label="-1.35920 m/y" alpha="255" value="-1.3592"/>
          <item color="#a52125" label="-1.34360 m/y" alpha="255" value="-1.3436"/>
          <item color="#a52125" label="-1.34360 m/y" alpha="255" value="-1.3436"/>
          <item color="#a72424" label="-1.32800 m/y" alpha="255" value="-1.328"/>
          <item color="#a72424" label="-1.32800 m/y" alpha="255" value="-1.328"/>
          <item color="#a92624" label="-1.31240 m/y" alpha="255" value="-1.3124"/>
          <item color="#a92624" label="-1.31240 m/y" alpha="255" value="-1.3124"/>
          <item color="#ab2924" label="-1.29680 m/y" alpha="255" value="-1.2968"/>
          <item color="#ab2924" label="-1.29680 m/y" alpha="255" value="-1.2968"/>
          <item color="#ac2b24" label="-1.28120 m/y" alpha="255" value="-1.2812"/>
          <item color="#ac2b24" label="-1.28120 m/y" alpha="255" value="-1.2812"/>
          <item color="#ae2e24" label="-1.26560 m/y" alpha="255" value="-1.2656"/>
          <item color="#ae2e24" label="-1.26560 m/y" alpha="255" value="-1.2656"/>
          <item color="#af3024" label="-1.25000 m/y" alpha="255" value="-1.25"/>
          <item color="#af3024" label="-1.25000 m/y" alpha="255" value="-1.25"/>
          <item color="#b13325" label="-1.23440 m/y" alpha="255" value="-1.2344"/>
          <item color="#b13325" label="-1.23440 m/y" alpha="255" value="-1.2344"/>
          <item color="#b23525" label="-1.21880 m/y" alpha="255" value="-1.2188"/>
          <item color="#b23525" label="-1.21880 m/y" alpha="255" value="-1.2188"/>
          <item color="#b33826" label="-1.20320 m/y" alpha="255" value="-1.2032"/>
          <item color="#b33826" label="-1.20320 m/y" alpha="255" value="-1.2032"/>
          <item color="#b43b27" label="-1.18760 m/y" alpha="255" value="-1.1876"/>
          <item color="#b43b27" label="-1.18760 m/y" alpha="255" value="-1.1876"/>
          <item color="#b63d28" label="-1.17200 m/y" alpha="255" value="-1.172"/>
          <item color="#b63d28" label="-1.17200 m/y" alpha="255" value="-1.172"/>
          <item color="#b74029" label="-1.15640 m/y" alpha="255" value="-1.1564"/>
          <item color="#b74029" label="-1.15640 m/y" alpha="255" value="-1.1564"/>
          <item color="#b8432b" label="-1.14080 m/y" alpha="255" value="-1.1408"/>
          <item color="#b8432b" label="-1.14080 m/y" alpha="255" value="-1.1408"/>
          <item color="#b9452c" label="-1.12480 m/y" alpha="255" value="-1.1248"/>
          <item color="#b9452c" label="-1.12480 m/y" alpha="255" value="-1.1248"/>
          <item color="#ba482e" label="-1.10920 m/y" alpha="255" value="-1.1092"/>
          <item color="#ba482e" label="-1.10920 m/y" alpha="255" value="-1.1092"/>
          <item color="#bb4b30" label="-1.09360 m/y" alpha="255" value="-1.0936"/>
          <item color="#bb4b30" label="-1.09360 m/y" alpha="255" value="-1.0936"/>
          <item color="#bc4d32" label="-1.07800 m/y" alpha="255" value="-1.078"/>
          <item color="#bc4d32" label="-1.07800 m/y" alpha="255" value="-1.078"/>
          <item color="#bd5034" label="-1.06240 m/y" alpha="255" value="-1.0624"/>
          <item color="#bd5034" label="-1.06240 m/y" alpha="255" value="-1.0624"/>
          <item color="#be5236" label="-1.04680 m/y" alpha="255" value="-1.0468"/>
          <item color="#be5236" label="-1.04680 m/y" alpha="255" value="-1.0468"/>
          <item color="#be5538" label="-1.03120 m/y" alpha="255" value="-1.0312"/>
          <item color="#be5538" label="-1.03120 m/y" alpha="255" value="-1.0312"/>
          <item color="#bf573a" label="-1.01560 m/y" alpha="255" value="-1.0156"/>
          <item color="#bf573a" label="-1.01560 m/y" alpha="255" value="-1.0156"/>
          <item color="#c05a3c" label="-1.00000 m/y" alpha="255" value="-1"/>
          <item color="#c05a3c" label="-1.00000 m/y" alpha="255" value="-1"/>
          <item color="#c15c3f" label="-0.98440 m/y" alpha="255" value="-0.9844"/>
          <item color="#c15c3f" label="-0.98440 m/y" alpha="255" value="-0.9844"/>
          <item color="#c25f41" label="-0.96880 m/y" alpha="255" value="-0.9688"/>
          <item color="#c25f41" label="-0.96880 m/y" alpha="255" value="-0.9688"/>
          <item color="#c36143" label="-0.95320 m/y" alpha="255" value="-0.9532"/>
          <item color="#c36143" label="-0.95320 m/y" alpha="255" value="-0.9532"/>
          <item color="#c36346" label="-0.93760 m/y" alpha="255" value="-0.9376"/>
          <item color="#c36346" label="-0.93760 m/y" alpha="255" value="-0.9376"/>
          <item color="#c46648" label="-0.92200 m/y" alpha="255" value="-0.922"/>
          <item color="#c46648" label="-0.92200 m/y" alpha="255" value="-0.922"/>
          <item color="#c5684b" label="-0.90640 m/y" alpha="255" value="-0.9064"/>
          <item color="#c5684b" label="-0.90640 m/y" alpha="255" value="-0.9064"/>
          <item color="#c66b4d" label="-0.89080 m/y" alpha="255" value="-0.8908"/>
          <item color="#c66b4d" label="-0.89080 m/y" alpha="255" value="-0.8908"/>
          <item color="#c76d50" label="-0.87520 m/y" alpha="255" value="-0.8752"/>
          <item color="#c76d50" label="-0.87520 m/y" alpha="255" value="-0.8752"/>
          <item color="#c76f53" label="-0.85920 m/y" alpha="255" value="-0.8592"/>
          <item color="#c76f53" label="-0.85920 m/y" alpha="255" value="-0.8592"/>
          <item color="#c87255" label="-0.84360 m/y" alpha="255" value="-0.8436"/>
          <item color="#c87255" label="-0.84360 m/y" alpha="255" value="-0.8436"/>
          <item color="#c97458" label="-0.82800 m/y" alpha="255" value="-0.828"/>
          <item color="#c97458" label="-0.82800 m/y" alpha="255" value="-0.828"/>
          <item color="#ca765b" label="-0.81240 m/y" alpha="255" value="-0.8124"/>
          <item color="#ca765b" label="-0.81240 m/y" alpha="255" value="-0.8124"/>
          <item color="#ca795d" label="-0.79680 m/y" alpha="255" value="-0.7968"/>
          <item color="#ca795d" label="-0.79680 m/y" alpha="255" value="-0.7968"/>
          <item color="#cb7b60" label="-0.78120 m/y" alpha="255" value="-0.7812"/>
          <item color="#cb7b60" label="-0.78120 m/y" alpha="255" value="-0.7812"/>
          <item color="#cc7d63" label="-0.76560 m/y" alpha="255" value="-0.7656"/>
          <item color="#cc7d63" label="-0.76560 m/y" alpha="255" value="-0.7656"/>
          <item color="#cd7f65" label="-0.75000 m/y" alpha="255" value="-0.75"/>
          <item color="#cd7f65" label="-0.75000 m/y" alpha="255" value="-0.75"/>
          <item color="#cd8268" label="-0.73440 m/y" alpha="255" value="-0.7344"/>
          <item color="#cd8268" label="-0.73440 m/y" alpha="255" value="-0.7344"/>
          <item color="#ce846b" label="-0.71880 m/y" alpha="255" value="-0.7188"/>
          <item color="#ce846b" label="-0.71880 m/y" alpha="255" value="-0.7188"/>
          <item color="#cf866e" label="-0.70320 m/y" alpha="255" value="-0.7032"/>
          <item color="#cf866e" label="-0.70320 m/y" alpha="255" value="-0.7032"/>
          <item color="#cf8970" label="-0.68760 m/y" alpha="255" value="-0.6876"/>
          <item color="#cf8970" label="-0.68760 m/y" alpha="255" value="-0.6876"/>
          <item color="#d08b73" label="-0.67200 m/y" alpha="255" value="-0.672"/>
          <item color="#d08b73" label="-0.67200 m/y" alpha="255" value="-0.672"/>
          <item color="#d18d76" label="-0.65640 m/y" alpha="255" value="-0.6564"/>
          <item color="#d18d76" label="-0.65640 m/y" alpha="255" value="-0.6564"/>
          <item color="#d18f79" label="-0.64080 m/y" alpha="255" value="-0.6408"/>
          <item color="#d18f79" label="-0.64080 m/y" alpha="255" value="-0.6408"/>
          <item color="#d2927c" label="-0.62480 m/y" alpha="255" value="-0.6248"/>
          <item color="#d2927c" label="-0.62480 m/y" alpha="255" value="-0.6248"/>
          <item color="#d3947f" label="-0.60920 m/y" alpha="255" value="-0.6092"/>
          <item color="#d3947f" label="-0.60920 m/y" alpha="255" value="-0.6092"/>
          <item color="#d39681" label="-0.59360 m/y" alpha="255" value="-0.5936"/>
          <item color="#d39681" label="-0.59360 m/y" alpha="255" value="-0.5936"/>
          <item color="#d49984" label="-0.57800 m/y" alpha="255" value="-0.578"/>
          <item color="#d49984" label="-0.57800 m/y" alpha="255" value="-0.578"/>
          <item color="#d59b87" label="-0.56240 m/y" alpha="255" value="-0.5624"/>
          <item color="#d59b87" label="-0.56240 m/y" alpha="255" value="-0.5624"/>
          <item color="#d69d8a" label="-0.54680 m/y" alpha="255" value="-0.5468"/>
          <item color="#d69d8a" label="-0.54680 m/y" alpha="255" value="-0.5468"/>
          <item color="#d69f8d" label="-0.53120 m/y" alpha="255" value="-0.5312"/>
          <item color="#d69f8d" label="-0.53120 m/y" alpha="255" value="-0.5312"/>
          <item color="#d7a290" label="-0.51560 m/y" alpha="255" value="-0.5156"/>
          <item color="#d7a290" label="-0.51560 m/y" alpha="255" value="-0.5156"/>
          <item color="#d8a493" label="-0.50000 m/y" alpha="255" value="-0.5"/>
          <item color="#d8a493" label="-0.50000 m/y" alpha="255" value="-0.5"/>
          <item color="#d8a696" label="-0.48440 m/y" alpha="255" value="-0.4844"/>
          <item color="#d8a696" label="-0.48440 m/y" alpha="255" value="-0.4844"/>
          <item color="#d9a998" label="-0.46880 m/y" alpha="255" value="-0.4688"/>
          <item color="#d9a998" label="-0.46880 m/y" alpha="255" value="-0.4688"/>
          <item color="#daab9b" label="-0.45320 m/y" alpha="255" value="-0.4532"/>
          <item color="#daab9b" label="-0.45320 m/y" alpha="255" value="-0.4532"/>
          <item color="#daad9e" label="-0.43760 m/y" alpha="255" value="-0.4376"/>
          <item color="#daad9e" label="-0.43760 m/y" alpha="255" value="-0.4376"/>
          <item color="#dbafa1" label="-0.42200 m/y" alpha="255" value="-0.422"/>
          <item color="#dbafa1" label="-0.42200 m/y" alpha="255" value="-0.422"/>
          <item color="#dcb2a4" label="-0.40640 m/y" alpha="255" value="-0.4064"/>
          <item color="#dcb2a4" label="-0.40640 m/y" alpha="255" value="-0.4064"/>
          <item color="#dcb4a7" label="-0.39080 m/y" alpha="255" value="-0.3908"/>
          <item color="#dcb4a7" label="-0.39080 m/y" alpha="255" value="-0.3908"/>
          <item color="#ddb6aa" label="-0.37520 m/y" alpha="255" value="-0.3752"/>
          <item color="#ddb6aa" label="-0.37520 m/y" alpha="255" value="-0.3752"/>
          <item color="#deb9ad" label="-0.35920 m/y" alpha="255" value="-0.3592"/>
          <item color="#deb9ad" label="-0.35920 m/y" alpha="255" value="-0.3592"/>
          <item color="#dfbbb0" label="-0.34360 m/y" alpha="255" value="-0.3436"/>
          <item color="#dfbbb0" label="-0.34360 m/y" alpha="255" value="-0.3436"/>
          <item color="#dfbdb2" label="-0.32800 m/y" alpha="255" value="-0.328"/>
          <item color="#dfbdb2" label="-0.32800 m/y" alpha="255" value="-0.328"/>
          <item color="#e0c0b5" label="-0.31240 m/y" alpha="255" value="-0.3124"/>
          <item color="#e0c0b5" label="-0.31240 m/y" alpha="255" value="-0.3124"/>
          <item color="#e1c2b8" label="-0.29680 m/y" alpha="255" value="-0.2968"/>
          <item color="#e1c2b8" label="-0.29680 m/y" alpha="255" value="-0.2968"/>
          <item color="#e1c4bb" label="-0.28120 m/y" alpha="255" value="-0.2812"/>
          <item color="#e1c4bb" label="-0.28120 m/y" alpha="255" value="-0.2812"/>
          <item color="#e2c7be" label="-0.26560 m/y" alpha="255" value="-0.2656"/>
          <item color="#e2c7be" label="-0.26560 m/y" alpha="255" value="-0.2656"/>
          <item color="#e3c9c1" label="-0.25000 m/y" alpha="255" value="-0.25"/>
          <item color="#e3c9c1" label="-0.25000 m/y" alpha="255" value="-0.25"/>
          <item color="#e4cbc4" label="-0.23440 m/y" alpha="255" value="-0.2344"/>
          <item color="#e4cbc4" label="-0.23440 m/y" alpha="255" value="-0.2344"/>
          <item color="#e5cec7" label="-0.21880 m/y" alpha="255" value="-0.2188"/>
          <item color="#e5cec7" label="-0.21880 m/y" alpha="255" value="-0.2188"/>
          <item color="#e5d0ca" label="-0.20320 m/y" alpha="255" value="-0.2032"/>
          <item color="#e5d0ca" label="-0.20320 m/y" alpha="255" value="-0.2032"/>
          <item color="#e6d2cd" label="-0.18760 m/y" alpha="255" value="-0.1876"/>
          <item color="#e6d2cd" label="-0.18760 m/y" alpha="255" value="-0.1876"/>
          <item color="#e7d5cf" label="-0.17200 m/y" alpha="255" value="-0.172"/>
          <item color="#e7d5cf" label="-0.17200 m/y" alpha="255" value="-0.172"/>
          <item color="#e8d7d2" label="-0.15640 m/y" alpha="255" value="-0.1564"/>
          <item color="#e8d7d2" label="-0.15640 m/y" alpha="255" value="-0.1564"/>
          <item color="#e9d9d5" label="-0.14080 m/y" alpha="255" value="-0.1408"/>
          <item color="#e9d9d5" label="-0.14080 m/y" alpha="255" value="-0.1408"/>
          <item color="#eadcd8" label="-0.12480 m/y" alpha="255" value="-0.1248"/>
          <item color="#eadcd8" label="-0.12480 m/y" alpha="255" value="-0.1248"/>
          <item color="#ebdedb" label="-0.10920 m/y" alpha="255" value="-0.1092"/>
          <item color="#ebdedb" label="-0.10920 m/y" alpha="255" value="-0.1092"/>
          <item color="#ece0de" label="-0.09360 m/y" alpha="255" value="-0.0935999999999999"/>
          <item color="#ece0de" label="-0.09360 m/y" alpha="255" value="-0.0935999999999999"/>
          <item color="#ede3e0" label="-0.07800 m/y" alpha="255" value="-0.0780000000000001"/>
          <item color="#ede3e0" label="-0.07800 m/y" alpha="255" value="-0.0780000000000001"/>
          <item color="#eee5e3" label="-0.06240 m/y" alpha="255" value="-0.0624"/>
          <item color="#eee5e3" label="-0.06240 m/y" alpha="255" value="-0.0624"/>
          <item color="#efe8e6" label="-0.04680 m/y" alpha="255" value="-0.0468"/>
          <item color="#efe8e6" label="-0.04680 m/y" alpha="255" value="-0.0468"/>
          <item color="#f0eae9" label="-0.03120 m/y" alpha="255" value="-0.0311999999999999"/>
          <item color="#f0eae9" label="-0.03120 m/y" alpha="255" value="-0.0311999999999999"/>
          <item color="#f1eceb" label="-0.01560 m/y" alpha="255" value="-0.0156000000000001"/>
          <item color="#f1eceb" label="-0.01560 m/y" alpha="255" value="-0.0156000000000001"/>
          <item color="#f1ecec" label="0.00000 m/y" alpha="255" value="0"/>
          <item color="#f1ecec" label="0.00000 m/y" alpha="255" value="0"/>
          <item color="#eeeaea" label="0.01560 m/y" alpha="255" value="0.0156000000000001"/>
          <item color="#eeeaea" label="0.01560 m/y" alpha="255" value="0.0156000000000001"/>
          <item color="#ebe9e9" label="0.03120 m/y" alpha="255" value="0.0312000000000001"/>
          <item color="#ebe9e9" label="0.03120 m/y" alpha="255" value="0.0312000000000001"/>
          <item color="#e9e7e7" label="0.04680 m/y" alpha="255" value="0.0468000000000002"/>
          <item color="#e9e7e7" label="0.04680 m/y" alpha="255" value="0.0468000000000002"/>
          <item color="#e6e5e6" label="0.06240 m/y" alpha="255" value="0.0623999999999998"/>
          <item color="#e6e5e6" label="0.06240 m/y" alpha="255" value="0.0623999999999998"/>
          <item color="#e3e3e4" label="0.07800 m/y" alpha="255" value="0.0779999999999998"/>
          <item color="#e3e3e4" label="0.07800 m/y" alpha="255" value="0.0779999999999998"/>
          <item color="#e1e1e3" label="0.09360 m/y" alpha="255" value="0.0935999999999999"/>
          <item color="#e1e1e3" label="0.09360 m/y" alpha="255" value="0.0935999999999999"/>
          <item color="#dee0e1" label="0.10920 m/y" alpha="255" value="0.1092"/>
          <item color="#dee0e1" label="0.10920 m/y" alpha="255" value="0.1092"/>
          <item color="#dbdee0" label="0.12480 m/y" alpha="255" value="0.1248"/>
          <item color="#dbdee0" label="0.12480 m/y" alpha="255" value="0.1248"/>
          <item color="#d8dcde" label="0.14080 m/y" alpha="255" value="0.1408"/>
          <item color="#d8dcde" label="0.14080 m/y" alpha="255" value="0.1408"/>
          <item color="#d5dadd" label="0.15640 m/y" alpha="255" value="0.1564"/>
          <item color="#d5dadd" label="0.15640 m/y" alpha="255" value="0.1564"/>
          <item color="#d3d9dc" label="0.17200 m/y" alpha="255" value="0.172"/>
          <item color="#d3d9dc" label="0.17200 m/y" alpha="255" value="0.172"/>
          <item color="#d0d7da" label="0.18760 m/y" alpha="255" value="0.1876"/>
          <item color="#d0d7da" label="0.18760 m/y" alpha="255" value="0.1876"/>
          <item color="#cdd5d9" label="0.20320 m/y" alpha="255" value="0.2032"/>
          <item color="#cdd5d9" label="0.20320 m/y" alpha="255" value="0.2032"/>
          <item color="#cad4d8" label="0.21880 m/y" alpha="255" value="0.2188"/>
          <item color="#cad4d8" label="0.21880 m/y" alpha="255" value="0.2188"/>
          <item color="#c7d2d7" label="0.23440 m/y" alpha="255" value="0.2344"/>
          <item color="#c7d2d7" label="0.23440 m/y" alpha="255" value="0.2344"/>
          <item color="#c4d0d5" label="0.25000 m/y" alpha="255" value="0.25"/>
          <item color="#c4d0d5" label="0.25000 m/y" alpha="255" value="0.25"/>
          <item color="#c1cfd4" label="0.26560 m/y" alpha="255" value="0.2656"/>
          <item color="#c1cfd4" label="0.26560 m/y" alpha="255" value="0.2656"/>
          <item color="#bfcdd3" label="0.28120 m/y" alpha="255" value="0.2812"/>
          <item color="#bfcdd3" label="0.28120 m/y" alpha="255" value="0.2812"/>
          <item color="#bcccd2" label="0.29680 m/y" alpha="255" value="0.2968"/>
          <item color="#bcccd2" label="0.29680 m/y" alpha="255" value="0.2968"/>
          <item color="#b9cad0" label="0.31240 m/y" alpha="255" value="0.3124"/>
          <item color="#b9cad0" label="0.31240 m/y" alpha="255" value="0.3124"/>
          <item color="#b6c9cf" label="0.32800 m/y" alpha="255" value="0.328"/>
          <item color="#b6c9cf" label="0.32800 m/y" alpha="255" value="0.328"/>
          <item color="#b3c7ce" label="0.34360 m/y" alpha="255" value="0.3436"/>
          <item color="#b3c7ce" label="0.34360 m/y" alpha="255" value="0.3436"/>
          <item color="#b0c5cd" label="0.35920 m/y" alpha="255" value="0.3592"/>
          <item color="#b0c5cd" label="0.35920 m/y" alpha="255" value="0.3592"/>
          <item color="#adc4cc" label="0.37520 m/y" alpha="255" value="0.3752"/>
          <item color="#adc4cc" label="0.37520 m/y" alpha="255" value="0.3752"/>
          <item color="#aac2cb" label="0.39080 m/y" alpha="255" value="0.3908"/>
          <item color="#aac2cb" label="0.39080 m/y" alpha="255" value="0.3908"/>
          <item color="#a7c1ca" label="0.40640 m/y" alpha="255" value="0.4064"/>
          <item color="#a7c1ca" label="0.40640 m/y" alpha="255" value="0.4064"/>
          <item color="#a4bfc9" label="0.42200 m/y" alpha="255" value="0.422"/>
          <item color="#a4bfc9" label="0.42200 m/y" alpha="255" value="0.422"/>
          <item color="#a1bec8" label="0.43760 m/y" alpha="255" value="0.4376"/>
          <item color="#a1bec8" label="0.43760 m/y" alpha="255" value="0.4376"/>
          <item color="#9ebcc7" label="0.45320 m/y" alpha="255" value="0.4532"/>
          <item color="#9ebcc7" label="0.45320 m/y" alpha="255" value="0.4532"/>
          <item color="#9bbbc6" label="0.46880 m/y" alpha="255" value="0.4688"/>
          <item color="#9bbbc6" label="0.46880 m/y" alpha="255" value="0.4688"/>
          <item color="#98bac5" label="0.48440 m/y" alpha="255" value="0.4844"/>
          <item color="#98bac5" label="0.48440 m/y" alpha="255" value="0.4844"/>
          <item color="#94b8c4" label="0.50000 m/y" alpha="255" value="0.5"/>
          <item color="#94b8c4" label="0.50000 m/y" alpha="255" value="0.5"/>
          <item color="#91b7c3" label="0.51560 m/y" alpha="255" value="0.5156"/>
          <item color="#91b7c3" label="0.51560 m/y" alpha="255" value="0.5156"/>
          <item color="#8eb5c3" label="0.53120 m/y" alpha="255" value="0.5312"/>
          <item color="#8eb5c3" label="0.53120 m/y" alpha="255" value="0.5312"/>
          <item color="#8bb4c2" label="0.54680 m/y" alpha="255" value="0.5468"/>
          <item color="#8bb4c2" label="0.54680 m/y" alpha="255" value="0.5468"/>
          <item color="#88b2c1" label="0.56240 m/y" alpha="255" value="0.5624"/>
          <item color="#88b2c1" label="0.56240 m/y" alpha="255" value="0.5624"/>
          <item color="#85b1c0" label="0.57800 m/y" alpha="255" value="0.578"/>
          <item color="#85b1c0" label="0.57800 m/y" alpha="255" value="0.578"/>
          <item color="#81afc0" label="0.59360 m/y" alpha="255" value="0.5936"/>
          <item color="#81afc0" label="0.59360 m/y" alpha="255" value="0.5936"/>
          <item color="#7eaebf" label="0.60920 m/y" alpha="255" value="0.6092"/>
          <item color="#7eaebf" label="0.60920 m/y" alpha="255" value="0.6092"/>
          <item color="#7bacbf" label="0.62480 m/y" alpha="255" value="0.6248"/>
          <item color="#7bacbf" label="0.62480 m/y" alpha="255" value="0.6248"/>
          <item color="#78abbe" label="0.64080 m/y" alpha="255" value="0.6408"/>
          <item color="#78abbe" label="0.64080 m/y" alpha="255" value="0.6408"/>
          <item color="#75aabe" label="0.65640 m/y" alpha="255" value="0.6564"/>
          <item color="#75aabe" label="0.65640 m/y" alpha="255" value="0.6564"/>
          <item color="#71a8bd" label="0.67200 m/y" alpha="255" value="0.672"/>
          <item color="#71a8bd" label="0.67200 m/y" alpha="255" value="0.672"/>
          <item color="#6ea7bd" label="0.68760 m/y" alpha="255" value="0.6876"/>
          <item color="#6ea7bd" label="0.68760 m/y" alpha="255" value="0.6876"/>
          <item color="#6ba5bc" label="0.70320 m/y" alpha="255" value="0.7032"/>
          <item color="#6ba5bc" label="0.70320 m/y" alpha="255" value="0.7032"/>
          <item color="#68a4bc" label="0.71880 m/y" alpha="255" value="0.7188"/>
          <item color="#68a4bc" label="0.71880 m/y" alpha="255" value="0.7188"/>
          <item color="#65a2bc" label="0.73440 m/y" alpha="255" value="0.7344"/>
          <item color="#65a2bc" label="0.73440 m/y" alpha="255" value="0.7344"/>
          <item color="#62a0bb" label="0.75000 m/y" alpha="255" value="0.75"/>
          <item color="#62a0bb" label="0.75000 m/y" alpha="255" value="0.75"/>
          <item color="#5f9fbb" label="0.76560 m/y" alpha="255" value="0.7656"/>
          <item color="#5f9fbb" label="0.76560 m/y" alpha="255" value="0.7656"/>
          <item color="#5c9dbb" label="0.78120 m/y" alpha="255" value="0.7812"/>
          <item color="#5c9dbb" label="0.78120 m/y" alpha="255" value="0.7812"/>
          <item color="#599cbb" label="0.79680 m/y" alpha="255" value="0.7968"/>
          <item color="#599cbb" label="0.79680 m/y" alpha="255" value="0.7968"/>
          <item color="#569abb" label="0.81240 m/y" alpha="255" value="0.8124"/>
          <item color="#569abb" label="0.81240 m/y" alpha="255" value="0.8124"/>
          <item color="#5399ba" label="0.82800 m/y" alpha="255" value="0.828"/>
          <item color="#5399ba" label="0.82800 m/y" alpha="255" value="0.828"/>
          <item color="#5197ba" label="0.84360 m/y" alpha="255" value="0.8436"/>
          <item color="#5197ba" label="0.84360 m/y" alpha="255" value="0.8436"/>
          <item color="#4e95ba" label="0.85920 m/y" alpha="255" value="0.8592"/>
          <item color="#4e95ba" label="0.85920 m/y" alpha="255" value="0.8592"/>
          <item color="#4b94ba" label="0.87520 m/y" alpha="255" value="0.8752"/>
          <item color="#4b94ba" label="0.87520 m/y" alpha="255" value="0.8752"/>
          <item color="#4892ba" label="0.89080 m/y" alpha="255" value="0.8908"/>
          <item color="#4892ba" label="0.89080 m/y" alpha="255" value="0.8908"/>
          <item color="#4690ba" label="0.90640 m/y" alpha="255" value="0.9064"/>
          <item color="#4690ba" label="0.90640 m/y" alpha="255" value="0.9064"/>
          <item color="#438fba" label="0.92200 m/y" alpha="255" value="0.922"/>
          <item color="#438fba" label="0.92200 m/y" alpha="255" value="0.922"/>
          <item color="#408dba" label="0.93760 m/y" alpha="255" value="0.9376"/>
          <item color="#408dba" label="0.93760 m/y" alpha="255" value="0.9376"/>
          <item color="#3e8bba" label="0.95320 m/y" alpha="255" value="0.9532"/>
          <item color="#3e8bba" label="0.95320 m/y" alpha="255" value="0.9532"/>
          <item color="#3b89ba" label="0.96880 m/y" alpha="255" value="0.9688"/>
          <item color="#3b89ba" label="0.96880 m/y" alpha="255" value="0.9688"/>
          <item color="#3888ba" label="0.98440 m/y" alpha="255" value="0.9844"/>
          <item color="#3888ba" label="0.98440 m/y" alpha="255" value="0.9844"/>
          <item color="#3686ba" label="1.00000 m/y" alpha="255" value="1"/>
          <item color="#3686ba" label="1.00000 m/y" alpha="255" value="1"/>
          <item color="#3384ba" label="1.01560 m/y" alpha="255" value="1.0156"/>
          <item color="#3384ba" label="1.01560 m/y" alpha="255" value="1.0156"/>
          <item color="#3083ba" label="1.03120 m/y" alpha="255" value="1.0312"/>
          <item color="#3083ba" label="1.03120 m/y" alpha="255" value="1.0312"/>
          <item color="#2e81ba" label="1.04680 m/y" alpha="255" value="1.0468"/>
          <item color="#2e81ba" label="1.04680 m/y" alpha="255" value="1.0468"/>
          <item color="#2b7fba" label="1.06240 m/y" alpha="255" value="1.0624"/>
          <item color="#2b7fba" label="1.06240 m/y" alpha="255" value="1.0624"/>
          <item color="#297dba" label="1.07800 m/y" alpha="255" value="1.078"/>
          <item color="#297dba" label="1.07800 m/y" alpha="255" value="1.078"/>
          <item color="#267bba" label="1.09360 m/y" alpha="255" value="1.0936"/>
          <item color="#267bba" label="1.09360 m/y" alpha="255" value="1.0936"/>
          <item color="#237aba" label="1.10920 m/y" alpha="255" value="1.1092"/>
          <item color="#237aba" label="1.10920 m/y" alpha="255" value="1.1092"/>
          <item color="#2178bb" label="1.12480 m/y" alpha="255" value="1.1248"/>
          <item color="#2178bb" label="1.12480 m/y" alpha="255" value="1.1248"/>
          <item color="#1e76bb" label="1.14080 m/y" alpha="255" value="1.1408"/>
          <item color="#1e76bb" label="1.14080 m/y" alpha="255" value="1.1408"/>
          <item color="#1b74bb" label="1.15640 m/y" alpha="255" value="1.1564"/>
          <item color="#1b74bb" label="1.15640 m/y" alpha="255" value="1.1564"/>
          <item color="#1972bb" label="1.17200 m/y" alpha="255" value="1.172"/>
          <item color="#1972bb" label="1.17200 m/y" alpha="255" value="1.172"/>
          <item color="#1670bc" label="1.18760 m/y" alpha="255" value="1.1876"/>
          <item color="#1670bc" label="1.18760 m/y" alpha="255" value="1.1876"/>
          <item color="#136ebc" label="1.20320 m/y" alpha="255" value="1.2032"/>
          <item color="#136ebc" label="1.20320 m/y" alpha="255" value="1.2032"/>
          <item color="#116cbc" label="1.21880 m/y" alpha="255" value="1.2188"/>
          <item color="#116cbc" label="1.21880 m/y" alpha="255" value="1.2188"/>
          <item color="#0f6abd" label="1.23440 m/y" alpha="255" value="1.2344"/>
          <item color="#0f6abd" label="1.23440 m/y" alpha="255" value="1.2344"/>
          <item color="#0d68bd" label="1.25000 m/y" alpha="255" value="1.25"/>
          <item color="#0d68bd" label="1.25000 m/y" alpha="255" value="1.25"/>
          <item color="#0b66bd" label="1.26560 m/y" alpha="255" value="1.2656"/>
          <item color="#0b66bd" label="1.26560 m/y" alpha="255" value="1.2656"/>
          <item color="#0a64be" label="1.28120 m/y" alpha="255" value="1.2812"/>
          <item color="#0a64be" label="1.28120 m/y" alpha="255" value="1.2812"/>
          <item color="#0a62be" label="1.29680 m/y" alpha="255" value="1.2968"/>
          <item color="#0a62be" label="1.29680 m/y" alpha="255" value="1.2968"/>
          <item color="#0a60be" label="1.31240 m/y" alpha="255" value="1.3124"/>
          <item color="#0a60be" label="1.31240 m/y" alpha="255" value="1.3124"/>
          <item color="#0c5ebe" label="1.32800 m/y" alpha="255" value="1.328"/>
          <item color="#0c5ebe" label="1.32800 m/y" alpha="255" value="1.328"/>
          <item color="#0d5bbe" label="1.34360 m/y" alpha="255" value="1.3436"/>
          <item color="#0d5bbe" label="1.34360 m/y" alpha="255" value="1.3436"/>
          <item color="#1059be" label="1.35920 m/y" alpha="255" value="1.3592"/>
          <item color="#1059be" label="1.35920 m/y" alpha="255" value="1.3592"/>
          <item color="#1357be" label="1.37520 m/y" alpha="255" value="1.3752"/>
          <item color="#1357be" label="1.37520 m/y" alpha="255" value="1.3752"/>
          <item color="#1655bd" label="1.39080 m/y" alpha="255" value="1.3908"/>
          <item color="#1655bd" label="1.39080 m/y" alpha="255" value="1.3908"/>
          <item color="#1952bc" label="1.40640 m/y" alpha="255" value="1.4064"/>
          <item color="#1952bc" label="1.40640 m/y" alpha="255" value="1.4064"/>
          <item color="#1c50ba" label="1.42200 m/y" alpha="255" value="1.422"/>
          <item color="#1c50ba" label="1.42200 m/y" alpha="255" value="1.422"/>
          <item color="#1f4eb8" label="1.43760 m/y" alpha="255" value="1.4376"/>
          <item color="#1f4eb8" label="1.43760 m/y" alpha="255" value="1.4376"/>
          <item color="#214cb6" label="1.45320 m/y" alpha="255" value="1.4532"/>
          <item color="#214cb6" label="1.45320 m/y" alpha="255" value="1.4532"/>
          <item color="#234ab3" label="1.46880 m/y" alpha="255" value="1.4688"/>
          <item color="#234ab3" label="1.46880 m/y" alpha="255" value="1.4688"/>
          <item color="#2548b0" label="1.48440 m/y" alpha="255" value="1.4844"/>
          <item color="#2548b0" label="1.48440 m/y" alpha="255" value="1.4844"/>
          <item color="#2647ac" label="1.50000 m/y" alpha="255" value="1.5"/>
          <item color="#2647ac" label="1.50000 m/y" alpha="255" value="1.5"/>
          <item color="#2745a9" label="1.51560 m/y" alpha="255" value="1.5156"/>
          <item color="#2745a9" label="1.51560 m/y" alpha="255" value="1.5156"/>
          <item color="#2843a5" label="1.53120 m/y" alpha="255" value="1.5312"/>
          <item color="#2843a5" label="1.53120 m/y" alpha="255" value="1.5312"/>
          <item color="#2942a2" label="1.54680 m/y" alpha="255" value="1.5468"/>
          <item color="#2942a2" label="1.54680 m/y" alpha="255" value="1.5468"/>
          <item color="#29409e" label="1.56240 m/y" alpha="255" value="1.5624"/>
          <item color="#29409e" label="1.56240 m/y" alpha="255" value="1.5624"/>
          <item color="#293f9a" label="1.57800 m/y" alpha="255" value="1.578"/>
          <item color="#293f9a" label="1.57800 m/y" alpha="255" value="1.578"/>
          <item color="#293e97" label="1.59360 m/y" alpha="255" value="1.5936"/>
          <item color="#293e97" label="1.59360 m/y" alpha="255" value="1.5936"/>
          <item color="#293c93" label="1.60920 m/y" alpha="255" value="1.6092"/>
          <item color="#293c93" label="1.60920 m/y" alpha="255" value="1.6092"/>
          <item color="#293b8f" label="1.62480 m/y" alpha="255" value="1.6248"/>
          <item color="#293b8f" label="1.62480 m/y" alpha="255" value="1.6248"/>
          <item color="#293a8c" label="1.64080 m/y" alpha="255" value="1.6408"/>
          <item color="#293a8c" label="1.64080 m/y" alpha="255" value="1.6408"/>
          <item color="#293888" label="1.65640 m/y" alpha="255" value="1.6564"/>
          <item color="#293888" label="1.65640 m/y" alpha="255" value="1.6564"/>
          <item color="#283784" label="1.67200 m/y" alpha="255" value="1.672"/>
          <item color="#283784" label="1.67200 m/y" alpha="255" value="1.672"/>
          <item color="#283681" label="1.68760 m/y" alpha="255" value="1.6876"/>
          <item color="#283681" label="1.68760 m/y" alpha="255" value="1.6876"/>
          <item color="#27347d" label="1.70320 m/y" alpha="255" value="1.7032"/>
          <item color="#27347d" label="1.70320 m/y" alpha="255" value="1.7032"/>
          <item color="#27337a" label="1.71880 m/y" alpha="255" value="1.7188"/>
          <item color="#27337a" label="1.71880 m/y" alpha="255" value="1.7188"/>
          <item color="#263276" label="1.73440 m/y" alpha="255" value="1.7344"/>
          <item color="#263276" label="1.73440 m/y" alpha="255" value="1.7344"/>
          <item color="#253073" label="1.75000 m/y" alpha="255" value="1.75"/>
          <item color="#253073" label="1.75000 m/y" alpha="255" value="1.75"/>
          <item color="#252f6f" label="1.76560 m/y" alpha="255" value="1.7656"/>
          <item color="#252f6f" label="1.76560 m/y" alpha="255" value="1.7656"/>
          <item color="#242e6c" label="1.78120 m/y" alpha="255" value="1.7812"/>
          <item color="#242e6c" label="1.78120 m/y" alpha="255" value="1.7812"/>
          <item color="#232d69" label="1.79680 m/y" alpha="255" value="1.7968"/>
          <item color="#232d69" label="1.79680 m/y" alpha="255" value="1.7968"/>
          <item color="#222b65" label="1.81240 m/y" alpha="255" value="1.8124"/>
          <item color="#222b65" label="1.81240 m/y" alpha="255" value="1.8124"/>
          <item color="#212a62" label="1.82800 m/y" alpha="255" value="1.828"/>
          <item color="#212a62" label="1.82800 m/y" alpha="255" value="1.828"/>
          <item color="#21295f" label="1.84360 m/y" alpha="255" value="1.8436"/>
          <item color="#21295f" label="1.84360 m/y" alpha="255" value="1.8436"/>
          <item color="#20275b" label="1.85920 m/y" alpha="255" value="1.8592"/>
          <item color="#20275b" label="1.85920 m/y" alpha="255" value="1.8592"/>
          <item color="#1f2658" label="1.87520 m/y" alpha="255" value="1.8752"/>
          <item color="#1f2658" label="1.87520 m/y" alpha="255" value="1.8752"/>
          <item color="#1e2555" label="1.89080 m/y" alpha="255" value="1.8908"/>
          <item color="#1e2555" label="1.89080 m/y" alpha="255" value="1.8908"/>
          <item color="#1d2352" label="1.90640 m/y" alpha="255" value="1.9064"/>
          <item color="#1d2352" label="1.90640 m/y" alpha="255" value="1.9064"/>
          <item color="#1c224f" label="1.92200 m/y" alpha="255" value="1.922"/>
          <item color="#1c224f" label="1.92200 m/y" alpha="255" value="1.922"/>
          <item color="#1b214c" label="1.93760 m/y" alpha="255" value="1.9376"/>
          <item color="#1b214c" label="1.93760 m/y" alpha="255" value="1.9376"/>
          <item color="#1a1f49" label="1.95320 m/y" alpha="255" value="1.9532"/>
          <item color="#1a1f49" label="1.95320 m/y" alpha="255" value="1.9532"/>
          <item color="#191e46" label="1.96880 m/y" alpha="255" value="1.9688"/>
          <item color="#191e46" label="1.96880 m/y" alpha="255" value="1.9688"/>
          <item color="#181c43" label="1.98440 m/y" alpha="255" value="1.9844"/>
          <item color="#181c43" label="1.98440 m/y" alpha="255" value="1.9844"/>
          <item color="#181c43" label="2.00000 m/y" alpha="255" value="2"/>
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

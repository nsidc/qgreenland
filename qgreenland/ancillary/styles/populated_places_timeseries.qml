<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="Symbology|Labeling|Rendering|Temporal" simplifyDrawingTol="1" simplifyDrawingHints="0" autoRefreshMode="Disabled" labelsEnabled="1" simplifyAlgorithm="0" minScale="100000000" hasScaleBasedVisibilityFlag="0" version="3.44.7-Solothurn" simplifyMaxScale="1" symbologyReferenceScale="-1" simplifyLocal="1" autoRefreshTime="0" maxScale="0">
  <temporal endField="end_date" startField="start_date" mode="2" accumulate="0" limitMode="1" enabled="1" endExpression="" fixedDuration="0" startExpression="" durationField="fid" durationUnit="min">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <renderer-v2 graduatedMethod="GraduatedColor" attr="population" enableorderby="0" symbollevels="0" referencescale="-1" type="graduatedSymbol" forceraster="0">
    <ranges>
      <range upper="133.000000000000000" uuid="{0dec995e-cdac-4265-9fa0-8a5c1b94fb65}" lower="0.000000000000000" render="true" symbol="0" label="0 - 133"/>
      <range upper="343.000000000000000" uuid="{c228f03e-7037-4924-9015-5f95c52c7797}" lower="133.000000000000000" render="true" symbol="1" label="133 - 343"/>
      <range upper="802.000000000000000" uuid="{afc3060a-7566-41c4-ba31-c7511156a265}" lower="343.000000000000000" render="true" symbol="2" label="343 - 802"/>
      <range upper="1464.000000000000000" uuid="{4f843859-9373-4937-8fa2-80d1e2636183}" lower="802.000000000000000" render="true" symbol="3" label="802 - 1464"/>
      <range upper="2384.000000000000000" uuid="{19890b2a-612c-41f4-acdb-def1e12c26f7}" lower="1464.000000000000000" render="true" symbol="4" label="1464 - 2384"/>
      <range upper="3572.000000000000000" uuid="{bb50a31f-acc0-4ae1-9828-382d6bd4b770}" lower="2384.000000000000000" render="true" symbol="5" label="2384 - 3572"/>
      <range upper="4737.000000000000000" uuid="{dbe7b5ef-6e28-41b8-bdb9-5643626b2d25}" lower="3572.000000000000000" render="true" symbol="6" label="3572 - 4737"/>
      <range upper="5598.000000000000000" uuid="{2dd52cb8-ff17-4c67-8777-749e54b6bdf4}" lower="4737.000000000000000" render="true" symbol="7" label="4737 - 5598"/>
      <range upper="10972.000000000000000" uuid="{5970a80f-6d10-4d4c-98f9-0049e3fda1ac}" lower="5598.000000000000000" render="true" symbol="8" label="5598 - 10972"/>
      <range upper="13884.000000000000000" uuid="{4e0006d5-920f-4a7d-80ac-cad9dcee7c2f}" lower="10972.000000000000000" render="true" symbol="9" label="10972 - 13884"/>
      <range upper="16992.000000000000000" uuid="{d1576f9e-d36f-4549-a9d5-8de7296954e9}" lower="13884.000000000000000" render="true" symbol="10" label="13884 - 16992"/>
      <range upper="20298.000000000000000" uuid="{b690b7bf-9733-45c7-bcc4-ba8f0709648a}" lower="16992.000000000000000" render="true" symbol="11" label="16992 - 20298"/>
    </ranges>
    <symbols>
      <symbol alpha="1" name="0" clip_to_extent="1" frame_rate="10" force_rhr="0" is_animated="0" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer enabled="1" id="{50ff14a4-b40c-4fae-bd7e-5fc6ff425834}" pass="0" locked="0" class="SimpleMarker">
          <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="square" name="cap_style" type="QString"/>
            <Option value="68,1,84,255,rgb:0.2666667,0.0039216,0.3294118,1" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="circle" name="name" type="QString"/>
            <Option value="0,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="MM" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="2" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="MM" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="size" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="population" name="field" type="QString"/>
                  <Option name="transformer" type="Map">
                    <Option name="d" type="Map">
                      <Option value="0.57" name="exponent" type="double"/>
                      <Option value="10" name="maxSize" type="double"/>
                      <Option value="20298" name="maxValue" type="double"/>
                      <Option value="1" name="minSize" type="double"/>
                      <Option value="0" name="minValue" type="double"/>
                      <Option value="0" name="nullSize" type="double"/>
                      <Option value="2" name="scaleType" type="int"/>
                    </Option>
                    <Option value="1" name="t" type="int"/>
                  </Option>
                  <Option value="2" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" name="1" clip_to_extent="1" frame_rate="10" force_rhr="0" is_animated="0" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer enabled="1" id="{50ff14a4-b40c-4fae-bd7e-5fc6ff425834}" pass="0" locked="0" class="SimpleMarker">
          <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="square" name="cap_style" type="QString"/>
            <Option value="72,33,115,255,rgb:0.2823529,0.1311971,0.4502632,1" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="circle" name="name" type="QString"/>
            <Option value="0,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="MM" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="2" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="MM" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="size" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="population" name="field" type="QString"/>
                  <Option name="transformer" type="Map">
                    <Option name="d" type="Map">
                      <Option value="0.57" name="exponent" type="double"/>
                      <Option value="10" name="maxSize" type="double"/>
                      <Option value="20298" name="maxValue" type="double"/>
                      <Option value="1" name="minSize" type="double"/>
                      <Option value="0" name="minValue" type="double"/>
                      <Option value="0" name="nullSize" type="double"/>
                      <Option value="2" name="scaleType" type="int"/>
                    </Option>
                    <Option value="1" name="t" type="int"/>
                  </Option>
                  <Option value="2" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" name="10" clip_to_extent="1" frame_rate="10" force_rhr="0" is_animated="0" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer enabled="1" id="{50ff14a4-b40c-4fae-bd7e-5fc6ff425834}" pass="0" locked="0" class="SimpleMarker">
          <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="square" name="cap_style" type="QString"/>
            <Option value="194,224,35,255,rgb:0.7597162,0.8773632,0.1390402,1" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="circle" name="name" type="QString"/>
            <Option value="0,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="MM" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="2" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="MM" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="size" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="population" name="field" type="QString"/>
                  <Option name="transformer" type="Map">
                    <Option name="d" type="Map">
                      <Option value="0.57" name="exponent" type="double"/>
                      <Option value="10" name="maxSize" type="double"/>
                      <Option value="20298" name="maxValue" type="double"/>
                      <Option value="1" name="minSize" type="double"/>
                      <Option value="0" name="minValue" type="double"/>
                      <Option value="0" name="nullSize" type="double"/>
                      <Option value="2" name="scaleType" type="int"/>
                    </Option>
                    <Option value="1" name="t" type="int"/>
                  </Option>
                  <Option value="2" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" name="11" clip_to_extent="1" frame_rate="10" force_rhr="0" is_animated="0" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer enabled="1" id="{50ff14a4-b40c-4fae-bd7e-5fc6ff425834}" pass="0" locked="0" class="SimpleMarker">
          <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="square" name="cap_style" type="QString"/>
            <Option value="253,231,37,255,rgb:0.9921569,0.9058824,0.145098,1" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="circle" name="name" type="QString"/>
            <Option value="0,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="MM" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="2" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="MM" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="size" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="population" name="field" type="QString"/>
                  <Option name="transformer" type="Map">
                    <Option name="d" type="Map">
                      <Option value="0.57" name="exponent" type="double"/>
                      <Option value="10" name="maxSize" type="double"/>
                      <Option value="20298" name="maxValue" type="double"/>
                      <Option value="1" name="minSize" type="double"/>
                      <Option value="0" name="minValue" type="double"/>
                      <Option value="0" name="nullSize" type="double"/>
                      <Option value="2" name="scaleType" type="int"/>
                    </Option>
                    <Option value="1" name="t" type="int"/>
                  </Option>
                  <Option value="2" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" name="2" clip_to_extent="1" frame_rate="10" force_rhr="0" is_animated="0" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer enabled="1" id="{50ff14a4-b40c-4fae-bd7e-5fc6ff425834}" pass="0" locked="0" class="SimpleMarker">
          <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="square" name="cap_style" type="QString"/>
            <Option value="66,62,133,255,rgb:0.2606088,0.2445563,0.5208515,1" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="circle" name="name" type="QString"/>
            <Option value="0,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="MM" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="2" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="MM" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="size" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="population" name="field" type="QString"/>
                  <Option name="transformer" type="Map">
                    <Option name="d" type="Map">
                      <Option value="0.57" name="exponent" type="double"/>
                      <Option value="10" name="maxSize" type="double"/>
                      <Option value="20298" name="maxValue" type="double"/>
                      <Option value="1" name="minSize" type="double"/>
                      <Option value="0" name="minValue" type="double"/>
                      <Option value="0" name="nullSize" type="double"/>
                      <Option value="2" name="scaleType" type="int"/>
                    </Option>
                    <Option value="1" name="t" type="int"/>
                  </Option>
                  <Option value="2" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" name="3" clip_to_extent="1" frame_rate="10" force_rhr="0" is_animated="0" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer enabled="1" id="{50ff14a4-b40c-4fae-bd7e-5fc6ff425834}" pass="0" locked="0" class="SimpleMarker">
          <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="square" name="cap_style" type="QString"/>
            <Option value="56,88,140,255,rgb:0.220325,0.3468833,0.5486687,1" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="circle" name="name" type="QString"/>
            <Option value="0,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="MM" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="2" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="MM" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="size" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="population" name="field" type="QString"/>
                  <Option name="transformer" type="Map">
                    <Option name="d" type="Map">
                      <Option value="0.57" name="exponent" type="double"/>
                      <Option value="10" name="maxSize" type="double"/>
                      <Option value="20298" name="maxValue" type="double"/>
                      <Option value="1" name="minSize" type="double"/>
                      <Option value="0" name="minValue" type="double"/>
                      <Option value="0" name="nullSize" type="double"/>
                      <Option value="2" name="scaleType" type="int"/>
                    </Option>
                    <Option value="1" name="t" type="int"/>
                  </Option>
                  <Option value="2" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" name="4" clip_to_extent="1" frame_rate="10" force_rhr="0" is_animated="0" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer enabled="1" id="{50ff14a4-b40c-4fae-bd7e-5fc6ff425834}" pass="0" locked="0" class="SimpleMarker">
          <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="square" name="cap_style" type="QString"/>
            <Option value="45,111,142,255,rgb:0.1761196,0.4360113,0.5568627,1" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="circle" name="name" type="QString"/>
            <Option value="0,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="MM" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="2" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="MM" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="size" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="population" name="field" type="QString"/>
                  <Option name="transformer" type="Map">
                    <Option name="d" type="Map">
                      <Option value="0.57" name="exponent" type="double"/>
                      <Option value="10" name="maxSize" type="double"/>
                      <Option value="20298" name="maxValue" type="double"/>
                      <Option value="1" name="minSize" type="double"/>
                      <Option value="0" name="minValue" type="double"/>
                      <Option value="0" name="nullSize" type="double"/>
                      <Option value="2" name="scaleType" type="int"/>
                    </Option>
                    <Option value="1" name="t" type="int"/>
                  </Option>
                  <Option value="2" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" name="5" clip_to_extent="1" frame_rate="10" force_rhr="0" is_animated="0" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer enabled="1" id="{50ff14a4-b40c-4fae-bd7e-5fc6ff425834}" pass="0" locked="0" class="SimpleMarker">
          <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="square" name="cap_style" type="QString"/>
            <Option value="37,133,142,255,rgb:0.143679,0.5212177,0.5568627,1" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="circle" name="name" type="QString"/>
            <Option value="0,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="MM" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="2" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="MM" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="size" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="population" name="field" type="QString"/>
                  <Option name="transformer" type="Map">
                    <Option name="d" type="Map">
                      <Option value="0.57" name="exponent" type="double"/>
                      <Option value="10" name="maxSize" type="double"/>
                      <Option value="20298" name="maxValue" type="double"/>
                      <Option value="1" name="minSize" type="double"/>
                      <Option value="0" name="minValue" type="double"/>
                      <Option value="0" name="nullSize" type="double"/>
                      <Option value="2" name="scaleType" type="int"/>
                    </Option>
                    <Option value="1" name="t" type="int"/>
                  </Option>
                  <Option value="2" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" name="6" clip_to_extent="1" frame_rate="10" force_rhr="0" is_animated="0" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer enabled="1" id="{50ff14a4-b40c-4fae-bd7e-5fc6ff425834}" pass="0" locked="0" class="SimpleMarker">
          <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="square" name="cap_style" type="QString"/>
            <Option value="30,155,137,255,rgb:0.1183642,0.6081941,0.538674,1" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="circle" name="name" type="QString"/>
            <Option value="0,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="MM" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="2" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="MM" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="size" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="population" name="field" type="QString"/>
                  <Option name="transformer" type="Map">
                    <Option name="d" type="Map">
                      <Option value="0.57" name="exponent" type="double"/>
                      <Option value="10" name="maxSize" type="double"/>
                      <Option value="20298" name="maxValue" type="double"/>
                      <Option value="1" name="minSize" type="double"/>
                      <Option value="0" name="minValue" type="double"/>
                      <Option value="0" name="nullSize" type="double"/>
                      <Option value="2" name="scaleType" type="int"/>
                    </Option>
                    <Option value="1" name="t" type="int"/>
                  </Option>
                  <Option value="2" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" name="7" clip_to_extent="1" frame_rate="10" force_rhr="0" is_animated="0" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer enabled="1" id="{50ff14a4-b40c-4fae-bd7e-5fc6ff425834}" pass="0" locked="0" class="SimpleMarker">
          <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="square" name="cap_style" type="QString"/>
            <Option value="43,176,126,255,rgb:0.1675593,0.6912642,0.4948348,1" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="circle" name="name" type="QString"/>
            <Option value="0,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="MM" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="2" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="MM" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="size" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="population" name="field" type="QString"/>
                  <Option name="transformer" type="Map">
                    <Option name="d" type="Map">
                      <Option value="0.57" name="exponent" type="double"/>
                      <Option value="10" name="maxSize" type="double"/>
                      <Option value="20298" name="maxValue" type="double"/>
                      <Option value="1" name="minSize" type="double"/>
                      <Option value="0" name="minValue" type="double"/>
                      <Option value="0" name="nullSize" type="double"/>
                      <Option value="2" name="scaleType" type="int"/>
                    </Option>
                    <Option value="1" name="t" type="int"/>
                  </Option>
                  <Option value="2" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" name="8" clip_to_extent="1" frame_rate="10" force_rhr="0" is_animated="0" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer enabled="1" id="{50ff14a4-b40c-4fae-bd7e-5fc6ff425834}" pass="0" locked="0" class="SimpleMarker">
          <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="square" name="cap_style" type="QString"/>
            <Option value="81,196,105,255,rgb:0.3172961,0.7700465,0.41355,1" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="circle" name="name" type="QString"/>
            <Option value="0,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="MM" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="2" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="MM" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="size" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="population" name="field" type="QString"/>
                  <Option name="transformer" type="Map">
                    <Option name="d" type="Map">
                      <Option value="0.57" name="exponent" type="double"/>
                      <Option value="10" name="maxSize" type="double"/>
                      <Option value="20298" name="maxValue" type="double"/>
                      <Option value="1" name="minSize" type="double"/>
                      <Option value="0" name="minValue" type="double"/>
                      <Option value="0" name="nullSize" type="double"/>
                      <Option value="2" name="scaleType" type="int"/>
                    </Option>
                    <Option value="1" name="t" type="int"/>
                  </Option>
                  <Option value="2" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" name="9" clip_to_extent="1" frame_rate="10" force_rhr="0" is_animated="0" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer enabled="1" id="{50ff14a4-b40c-4fae-bd7e-5fc6ff425834}" pass="0" locked="0" class="SimpleMarker">
          <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="square" name="cap_style" type="QString"/>
            <Option value="133,212,74,255,rgb:0.5233539,0.8320897,0.2909133,1" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="circle" name="name" type="QString"/>
            <Option value="0,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="MM" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="2" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="MM" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="size" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="population" name="field" type="QString"/>
                  <Option name="transformer" type="Map">
                    <Option name="d" type="Map">
                      <Option value="0.57" name="exponent" type="double"/>
                      <Option value="10" name="maxSize" type="double"/>
                      <Option value="20298" name="maxValue" type="double"/>
                      <Option value="1" name="minSize" type="double"/>
                      <Option value="0" name="minValue" type="double"/>
                      <Option value="0" name="nullSize" type="double"/>
                      <Option value="2" name="scaleType" type="int"/>
                    </Option>
                    <Option value="1" name="t" type="int"/>
                  </Option>
                  <Option value="2" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <source-symbol>
      <symbol alpha="1" name="0" clip_to_extent="1" frame_rate="10" force_rhr="0" is_animated="0" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer enabled="1" id="{50ff14a4-b40c-4fae-bd7e-5fc6ff425834}" pass="0" locked="0" class="SimpleMarker">
          <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="square" name="cap_style" type="QString"/>
            <Option value="68,1,84,255,rgb:0.2666667,0.0039216,0.3294118,1" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="circle" name="name" type="QString"/>
            <Option value="0,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="MM" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="2" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="MM" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties" type="Map">
                <Option name="size" type="Map">
                  <Option value="true" name="active" type="bool"/>
                  <Option value="population" name="field" type="QString"/>
                  <Option name="transformer" type="Map">
                    <Option name="d" type="Map">
                      <Option value="0.57" name="exponent" type="double"/>
                      <Option value="10" name="maxSize" type="double"/>
                      <Option value="20298" name="maxValue" type="double"/>
                      <Option value="1" name="minSize" type="double"/>
                      <Option value="0" name="minValue" type="double"/>
                      <Option value="0" name="nullSize" type="double"/>
                      <Option value="2" name="scaleType" type="int"/>
                    </Option>
                    <Option value="1" name="t" type="int"/>
                  </Option>
                  <Option value="2" name="type" type="int"/>
                </Option>
              </Option>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </source-symbol>
    <colorramp name="[source]" type="gradient">
      <Option type="Map">
        <Option value="68,1,84,255,rgb:0.2666667,0.0039216,0.3294118,1" name="color1" type="QString"/>
        <Option value="253,231,37,255,rgb:0.9921569,0.9058824,0.145098,1" name="color2" type="QString"/>
        <Option value="ccw" name="direction" type="QString"/>
        <Option value="0" name="discrete" type="QString"/>
        <Option value="gradient" name="rampType" type="QString"/>
        <Option value="rgb" name="spec" type="QString"/>
        <Option value="0.0196078;70,8,92,255,rgb:0.2745098,0.0313725,0.3607843,1;rgb;ccw:0.0392157;71,16,99,255,rgb:0.2784314,0.0627451,0.3882353,1;rgb;ccw:0.0588235;72,23,105,255,rgb:0.2823529,0.0901961,0.4117647,1;rgb;ccw:0.0784314;72,29,111,255,rgb:0.2823529,0.1137255,0.4352941,1;rgb;ccw:0.0980392;72,36,117,255,rgb:0.2823529,0.1411765,0.4588235,1;rgb;ccw:0.117647;71,42,122,255,rgb:0.2784314,0.1647059,0.4784314,1;rgb;ccw:0.137255;70,48,126,255,rgb:0.2745098,0.1882353,0.4941176,1;rgb;ccw:0.156863;69,55,129,255,rgb:0.2705882,0.2156863,0.5058824,1;rgb;ccw:0.176471;67,61,132,255,rgb:0.2627451,0.2392157,0.5176471,1;rgb;ccw:0.196078;65,66,135,255,rgb:0.254902,0.2588235,0.5294118,1;rgb;ccw:0.215686;63,72,137,255,rgb:0.2470588,0.2823529,0.5372549,1;rgb;ccw:0.235294;61,78,138,255,rgb:0.2392157,0.3058824,0.5411765,1;rgb;ccw:0.254902;58,83,139,255,rgb:0.227451,0.3254902,0.545098,1;rgb;ccw:0.27451;56,89,140,255,rgb:0.2196078,0.3490196,0.5490196,1;rgb;ccw:0.294118;53,94,141,255,rgb:0.2078431,0.3686275,0.5529412,1;rgb;ccw:0.313725;51,99,141,255,rgb:0.2,0.3882353,0.5529412,1;rgb;ccw:0.333333;49,104,142,255,rgb:0.1921569,0.4078431,0.5568627,1;rgb;ccw:0.352941;46,109,142,255,rgb:0.1803922,0.427451,0.5568627,1;rgb;ccw:0.372549;44,113,142,255,rgb:0.172549,0.4431373,0.5568627,1;rgb;ccw:0.392157;42,118,142,255,rgb:0.1647059,0.4627451,0.5568627,1;rgb;ccw:0.411765;41,123,142,255,rgb:0.1607843,0.4823529,0.5568627,1;rgb;ccw:0.431373;39,128,142,255,rgb:0.1529412,0.5019608,0.5568627,1;rgb;ccw:0.45098;37,132,142,255,rgb:0.145098,0.5176471,0.5568627,1;rgb;ccw:0.470588;35,137,142,255,rgb:0.1372549,0.5372549,0.5568627,1;rgb;ccw:0.490196;33,142,141,255,rgb:0.1294118,0.5568627,0.5529412,1;rgb;ccw:0.509804;32,146,140,255,rgb:0.1254902,0.572549,0.5490196,1;rgb;ccw:0.529412;31,151,139,255,rgb:0.1215686,0.5921569,0.545098,1;rgb;ccw:0.54902;30,156,137,255,rgb:0.1176471,0.6117647,0.5372549,1;rgb;ccw:0.568627;31,161,136,255,rgb:0.1215686,0.6313725,0.5333333,1;rgb;ccw:0.588235;33,165,133,255,rgb:0.1294118,0.6470588,0.5215686,1;rgb;ccw:0.607843;36,170,131,255,rgb:0.1411765,0.6666667,0.5137255,1;rgb;ccw:0.627451;40,174,128,255,rgb:0.1568627,0.6823529,0.5019608,1;rgb;ccw:0.647059;46,179,124,255,rgb:0.1803922,0.7019608,0.4862745,1;rgb;ccw:0.666667;53,183,121,255,rgb:0.2078431,0.7176471,0.4745098,1;rgb;ccw:0.686275;61,188,116,255,rgb:0.2392157,0.7372549,0.454902,1;rgb;ccw:0.705882;70,192,111,255,rgb:0.2745098,0.7529412,0.4352941,1;rgb;ccw:0.72549;80,196,106,255,rgb:0.3137255,0.7686275,0.4156863,1;rgb;ccw:0.745098;90,200,100,255,rgb:0.3529412,0.7843137,0.3921569,1;rgb;ccw:0.764706;101,203,94,255,rgb:0.3960784,0.7960784,0.3686275,1;rgb;ccw:0.784314;112,207,87,255,rgb:0.4392157,0.8117647,0.3411765,1;rgb;ccw:0.803922;124,210,80,255,rgb:0.4862745,0.8235294,0.3137255,1;rgb;ccw:0.823529;137,213,72,255,rgb:0.5372549,0.8352941,0.2823529,1;rgb;ccw:0.843137;149,216,64,255,rgb:0.5843137,0.8470588,0.2509804,1;rgb;ccw:0.862745;162,218,55,255,rgb:0.6352941,0.854902,0.2156863,1;rgb;ccw:0.882353;176,221,47,255,rgb:0.6901961,0.8666667,0.1843137,1;rgb;ccw:0.901961;189,223,38,255,rgb:0.7411765,0.8745098,0.1490196,1;rgb;ccw:0.921569;202,225,31,255,rgb:0.7921569,0.8823529,0.1215686,1;rgb;ccw:0.941176;216,226,25,255,rgb:0.8470588,0.8862745,0.0980392,1;rgb;ccw:0.960784;229,228,25,255,rgb:0.8980392,0.8941176,0.0980392,1;rgb;ccw:0.980392;241,229,29,255,rgb:0.945098,0.8980392,0.1137255,1;rgb;ccw" name="stops" type="QString"/>
      </Option>
    </colorramp>
    <classificationMethod id="Jenks">
      <symmetricMode astride="0" enabled="0" symmetrypoint="0"/>
      <labelFormat trimtrailingzeroes="1" labelprecision="0" format="%1 - %2"/>
      <parameters>
        <Option/>
      </parameters>
      <extraInformation/>
    </classificationMethod>
    <rotation/>
    <sizescale/>
    <data-defined-properties>
      <Option type="Map">
        <Option value="" name="name" type="QString"/>
        <Option name="properties"/>
        <Option value="collection" name="type" type="QString"/>
      </Option>
    </data-defined-properties>
  </renderer-v2>
  <selection mode="Default">
    <selectionColor invalid="1"/>
    <selectionSymbol>
      <symbol alpha="1" name="" clip_to_extent="1" frame_rate="10" force_rhr="0" is_animated="0" type="marker">
        <data_defined_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </data_defined_properties>
        <layer enabled="1" id="{6d98bd60-e654-4d82-a695-e212fe418234}" pass="0" locked="0" class="SimpleMarker">
          <Option type="Map">
            <Option value="0" name="angle" type="QString"/>
            <Option value="square" name="cap_style" type="QString"/>
            <Option value="255,0,0,255,rgb:1,0,0,1" name="color" type="QString"/>
            <Option value="1" name="horizontal_anchor_point" type="QString"/>
            <Option value="bevel" name="joinstyle" type="QString"/>
            <Option value="circle" name="name" type="QString"/>
            <Option value="0,0" name="offset" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
            <Option value="MM" name="offset_unit" type="QString"/>
            <Option value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" name="outline_color" type="QString"/>
            <Option value="solid" name="outline_style" type="QString"/>
            <Option value="0" name="outline_width" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
            <Option value="MM" name="outline_width_unit" type="QString"/>
            <Option value="diameter" name="scale_method" type="QString"/>
            <Option value="2" name="size" type="QString"/>
            <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
            <Option value="MM" name="size_unit" type="QString"/>
            <Option value="1" name="vertical_anchor_point" type="QString"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option value="" name="name" type="QString"/>
              <Option name="properties"/>
              <Option value="collection" name="type" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </selectionSymbol>
  </selection>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style fontLetterSpacing="0" blendMode="0" fontStrikeout="0" tabStopDistanceMapUnitScale="3x:0,0,0,0,0,0" namedStyle="Regular" fontKerning="1" previewBkgrdColor="255,255,255,255,rgb:1,1,1,1" forcedBold="0" fontFamily="Open Sans" multilineHeight="1" tabStopDistanceUnit="Point" useSubstitutions="0" fieldName="&quot;label&quot; || ':' || &quot;population&quot;" fontItalic="0" textOpacity="1" fontWordSpacing="0" forcedItalic="0" textColor="50,50,50,255,rgb:0.1960784,0.1960784,0.1960784,1" fontWeight="50" multilineHeightUnit="Percentage" capitalization="0" allowHtml="0" isExpression="1" fontSizeUnit="Point" legendString="Aa" fontUnderline="0" fontSize="10" fontSizeMapUnitScale="3x:0,0,0,0,0,0" tabStopDistance="80" textOrientation="horizontal">
        <families/>
        <text-buffer bufferDraw="0" bufferSizeUnits="MM" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferOpacity="1" bufferJoinStyle="128" bufferSize="1" bufferColor="250,250,250,255,rgb:0.9803922,0.9803922,0.9803922,1" bufferBlendMode="0" bufferNoFill="1"/>
        <text-mask maskSizeUnits="MM" maskJoinStyle="128" maskSize2="1.5" maskSizeMapUnitScale="3x:0,0,0,0,0,0" maskEnabled="0" maskedSymbolLayers="" maskType="0" maskSize="1.5" maskOpacity="1"/>
        <background shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetX="0" shapeRadiiUnit="Point" shapeSVGFile="" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSizeX="0" shapeSizeType="0" shapeSizeUnit="Point" shapeRotationType="0" shapeJoinStyle="64" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeType="0" shapeRadiiX="0" shapeBorderWidth="0" shapeSizeY="0" shapeRadiiY="0" shapeBorderWidthUnit="Point" shapeOffsetUnit="Point" shapeRotation="0" shapeFillColor="255,255,255,255,rgb:1,1,1,1" shapeDraw="0" shapeOpacity="1" shapeOffsetY="0" shapeBorderColor="128,128,128,255,rgb:0.5019608,0.5019608,0.5019608,1">
          <symbol alpha="1" name="markerSymbol" clip_to_extent="1" frame_rate="10" force_rhr="0" is_animated="0" type="marker">
            <data_defined_properties>
              <Option type="Map">
                <Option value="" name="name" type="QString"/>
                <Option name="properties"/>
                <Option value="collection" name="type" type="QString"/>
              </Option>
            </data_defined_properties>
            <layer enabled="1" id="" pass="0" locked="0" class="SimpleMarker">
              <Option type="Map">
                <Option value="0" name="angle" type="QString"/>
                <Option value="square" name="cap_style" type="QString"/>
                <Option value="114,155,111,255,rgb:0.4470588,0.6078431,0.4352941,1" name="color" type="QString"/>
                <Option value="1" name="horizontal_anchor_point" type="QString"/>
                <Option value="bevel" name="joinstyle" type="QString"/>
                <Option value="circle" name="name" type="QString"/>
                <Option value="0,0" name="offset" type="QString"/>
                <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
                <Option value="MM" name="offset_unit" type="QString"/>
                <Option value="35,35,35,255,rgb:0.1372549,0.1372549,0.1372549,1" name="outline_color" type="QString"/>
                <Option value="solid" name="outline_style" type="QString"/>
                <Option value="0" name="outline_width" type="QString"/>
                <Option value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale" type="QString"/>
                <Option value="MM" name="outline_width_unit" type="QString"/>
                <Option value="diameter" name="scale_method" type="QString"/>
                <Option value="2" name="size" type="QString"/>
                <Option value="3x:0,0,0,0,0,0" name="size_map_unit_scale" type="QString"/>
                <Option value="MM" name="size_unit" type="QString"/>
                <Option value="1" name="vertical_anchor_point" type="QString"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
          <symbol alpha="1" name="fillSymbol" clip_to_extent="1" frame_rate="10" force_rhr="0" is_animated="0" type="fill">
            <data_defined_properties>
              <Option type="Map">
                <Option value="" name="name" type="QString"/>
                <Option name="properties"/>
                <Option value="collection" name="type" type="QString"/>
              </Option>
            </data_defined_properties>
            <layer enabled="1" id="" pass="0" locked="0" class="SimpleFill">
              <Option type="Map">
                <Option value="3x:0,0,0,0,0,0" name="border_width_map_unit_scale" type="QString"/>
                <Option value="255,255,255,255,rgb:1,1,1,1" name="color" type="QString"/>
                <Option value="bevel" name="joinstyle" type="QString"/>
                <Option value="0,0" name="offset" type="QString"/>
                <Option value="3x:0,0,0,0,0,0" name="offset_map_unit_scale" type="QString"/>
                <Option value="MM" name="offset_unit" type="QString"/>
                <Option value="128,128,128,255,rgb:0.5019608,0.5019608,0.5019608,1" name="outline_color" type="QString"/>
                <Option value="no" name="outline_style" type="QString"/>
                <Option value="0" name="outline_width" type="QString"/>
                <Option value="Point" name="outline_width_unit" type="QString"/>
                <Option value="solid" name="style" type="QString"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option value="" name="name" type="QString"/>
                  <Option name="properties"/>
                  <Option value="collection" name="type" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </background>
        <shadow shadowDraw="0" shadowScale="100" shadowRadiusUnit="MM" shadowOffsetGlobal="1" shadowOffsetDist="1" shadowOffsetAngle="135" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowRadius="1.5" shadowBlendMode="6" shadowOpacity="0.69999999999999996" shadowRadiusAlphaOnly="0" shadowUnder="0" shadowOffsetUnit="MM" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowColor="0,0,0,255,rgb:0,0,0,1"/>
        <dd_properties>
          <Option type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format autoWrapLength="0" rightDirectionSymbol=">" wrapChar="" useMaxLineLengthForAutoWrap="1" addDirectionSymbol="0" formatNumbers="0" decimals="3" placeDirectionSymbol="0" plussign="0" reverseDirectionSymbol="0" multilineAlign="3" leftDirectionSymbol="&lt;"/>
      <placement xOffset="0" dist="0" fitInPolygonOnly="0" overrunDistance="0" geometryGeneratorEnabled="0" offsetType="1" preserveRotation="1" geometryGenerator="" repeatDistanceUnits="MM" yOffset="0" layerType="PointGeometry" priority="5" quadOffset="4" placement="6" overrunDistanceUnit="MM" geometryGeneratorType="PointGeometry" maxCurvedCharAngleOut="-25" lineAnchorTextPoint="FollowPlacement" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" lineAnchorClipping="0" distUnits="MM" distMapUnitScale="3x:0,0,0,0,0,0" repeatDistance="0" centroidInside="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" lineAnchorPercent="0.5" overlapHandling="PreventOverlap" maximumDistance="0" maximumDistanceMapUnitScale="3x:0,0,0,0,0,0" polygonPlacementFlags="2" rotationUnit="AngleDegrees" centroidWhole="0" maxCurvedCharAngleIn="25" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" placementFlags="10" lineAnchorType="0" allowDegraded="0" prioritization="PreferCloser" rotationAngle="0" offsetUnits="MM" maximumDistanceUnit="MM"/>
      <rendering fontMaxPixelSize="10000" mergeLines="0" zIndex="0" fontLimitPixelSize="0" drawLabels="1" scaleMin="0" fontMinPixelSize="3" minFeatureSize="0" maxNumLabels="2000" obstacleType="1" unplacedVisibility="0" limitNumLabels="0" upsidedownLabels="0" obstacle="1" scaleVisibility="0" obstacleFactor="1" scaleMax="0" labelPerPart="0"/>
      <dd_properties>
        <Option type="Map">
          <Option value="" name="name" type="QString"/>
          <Option name="properties"/>
          <Option value="collection" name="type" type="QString"/>
        </Option>
      </dd_properties>
      <callout type="simple">
        <Option type="Map">
          <Option value="pole_of_inaccessibility" name="anchorPoint" type="QString"/>
          <Option value="0" name="blendMode" type="int"/>
          <Option name="ddProperties" type="Map">
            <Option value="" name="name" type="QString"/>
            <Option name="properties"/>
            <Option value="collection" name="type" type="QString"/>
          </Option>
          <Option value="false" name="drawToAllParts" type="bool"/>
          <Option value="0" name="enabled" type="QString"/>
          <Option value="point_on_exterior" name="labelAnchorPoint" type="QString"/>
          <Option value="&lt;symbol alpha=&quot;1&quot; name=&quot;symbol&quot; clip_to_extent=&quot;1&quot; frame_rate=&quot;10&quot; force_rhr=&quot;0&quot; is_animated=&quot;0&quot; type=&quot;line&quot;>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;&quot; name=&quot;name&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option value=&quot;collection&quot; name=&quot;type&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;layer enabled=&quot;1&quot; id=&quot;{706ea95e-ced3-48be-8078-b7bdfb88e47a}&quot; pass=&quot;0&quot; locked=&quot;0&quot; class=&quot;SimpleLine&quot;>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;0&quot; name=&quot;align_dash_pattern&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;square&quot; name=&quot;capstyle&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;5;2&quot; name=&quot;customdash&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;customdash_map_unit_scale&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;MM&quot; name=&quot;customdash_unit&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;dash_pattern_offset&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;dash_pattern_offset_map_unit_scale&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;MM&quot; name=&quot;dash_pattern_offset_unit&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;draw_inside_polygon&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;bevel&quot; name=&quot;joinstyle&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;60,60,60,255,rgb:0.2352941,0.2352941,0.2352941,1&quot; name=&quot;line_color&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;solid&quot; name=&quot;line_style&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0.3&quot; name=&quot;line_width&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;MM&quot; name=&quot;line_width_unit&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;offset&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;offset_map_unit_scale&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;MM&quot; name=&quot;offset_unit&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;ring_filter&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;trim_distance_end&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;trim_distance_end_map_unit_scale&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;MM&quot; name=&quot;trim_distance_end_unit&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;trim_distance_start&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;trim_distance_start_map_unit_scale&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;MM&quot; name=&quot;trim_distance_start_unit&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;tweak_dash_pattern_on_corners&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;0&quot; name=&quot;use_custom_dash&quot; type=&quot;QString&quot;/>&lt;Option value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;width_map_unit_scale&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option value=&quot;&quot; name=&quot;name&quot; type=&quot;QString&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option value=&quot;collection&quot; name=&quot;type&quot; type=&quot;QString&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" name="lineSymbol" type="QString"/>
          <Option value="0" name="minLength" type="double"/>
          <Option value="3x:0,0,0,0,0,0" name="minLengthMapUnitScale" type="QString"/>
          <Option value="MM" name="minLengthUnit" type="QString"/>
          <Option value="0" name="offsetFromAnchor" type="double"/>
          <Option value="3x:0,0,0,0,0,0" name="offsetFromAnchorMapUnitScale" type="QString"/>
          <Option value="MM" name="offsetFromAnchorUnit" type="QString"/>
          <Option value="0" name="offsetFromLabel" type="double"/>
          <Option value="3x:0,0,0,0,0,0" name="offsetFromLabelMapUnitScale" type="QString"/>
          <Option value="MM" name="offsetFromLabelUnit" type="QString"/>
        </Option>
      </callout>
    </settings>
  </labeling>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <layerGeometryType>0</layerGeometryType>
</qgis>

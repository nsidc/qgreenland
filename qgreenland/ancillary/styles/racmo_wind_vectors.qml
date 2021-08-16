<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis labelsEnabled="0" maxScale="0" styleCategories="Symbology|Labeling|Rendering" hasScaleBasedVisibilityFlag="0" simplifyMaxScale="1" simplifyAlgorithm="0" version="3.10.4-A Coruña" minScale="1e+08" simplifyDrawingHints="0" simplifyDrawingTol="1" simplifyLocal="1">
  <renderer-v2 graduatedMethod="GraduatedColor" attr="magnitude" type="graduatedSymbol" enableorderby="0" forceraster="0" symbollevels="0">
    <ranges>
      <range symbol="0" lower="0.003448811673259" label="0 - 1.33 m/s" upper="1.332404872014141" render="true"/>
      <range symbol="1" lower="1.332404872014141" label="1.33 - 2.02 m/s" upper="2.020839150910295" render="true"/>
      <range symbol="2" lower="2.020839150910295" label="2.02 - 2.69 m/s" upper="2.689467394799844" render="true"/>
      <range symbol="3" lower="2.689467394799844" label="2.69 - 4.43 m/s" upper="4.425605157703052" render="true"/>
      <range symbol="4" lower="4.425605157703052" label="4.43 - 9.94 m/s" upper="9.936010947590397" render="true"/>
    </ranges>
    <symbols>
      <symbol force_rhr="0" type="marker" alpha="1" name="0" clip_to_extent="1">
        <layer enabled="1" pass="0" locked="0" class="VectorField">
          <prop k="angle_orientation" v="1"/>
          <prop k="angle_units" v="0"/>
          <prop k="distance_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="distance_unit" v="MapUnit"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="scale" v="500"/>
          <prop k="size" v="0"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vector_field_type" v="0"/>
          <prop k="x_attribute" v="eastward_component"/>
          <prop k="y_attribute" v="northward_component"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" type="line" alpha="1" name="@0@0" clip_to_extent="1">
            <layer enabled="1" pass="0" locked="0" class="SimpleLine">
              <prop k="capstyle" v="square"/>
              <prop k="customdash" v="5;2"/>
              <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="customdash_unit" v="MM"/>
              <prop k="draw_inside_polygon" v="0"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="line_color" v="253,231,37,255"/>
              <prop k="line_style" v="solid"/>
              <prop k="line_width" v="0"/>
              <prop k="line_width_unit" v="Pixel"/>
              <prop k="offset" v="0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="ring_filter" v="0"/>
              <prop k="use_custom_dash" v="0"/>
              <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option type="Map" name="properties">
                    <Option type="Map" name="outlineWidth">
                      <Option type="bool" value="true" name="active"/>
                      <Option type="QString" value="1 + (sqrt((&quot;vx&quot; ^ 2)+(&quot;vy&quot; ^ 2)))/1000" name="expression"/>
                      <Option type="int" value="3" name="type"/>
                    </Option>
                  </Option>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
            <layer enabled="1" pass="0" locked="0" class="MarkerLine">
              <prop k="average_angle_length" v="4"/>
              <prop k="average_angle_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="average_angle_unit" v="MM"/>
              <prop k="interval" v="3"/>
              <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="interval_unit" v="MM"/>
              <prop k="offset" v="0"/>
              <prop k="offset_along_line" v="0"/>
              <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_along_line_unit" v="MM"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="placement" v="lastvertex"/>
              <prop k="ring_filter" v="0"/>
              <prop k="rotate" v="1"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
              <symbol force_rhr="0" type="marker" alpha="1" name="@@0@0@1" clip_to_extent="1">
                <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
                  <prop k="angle" v="0"/>
                  <prop k="color" v="255,0,0,255"/>
                  <prop k="horizontal_anchor_point" v="1"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="name" v="arrowhead"/>
                  <prop k="offset" v="0,0"/>
                  <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="outline_color" v="253,231,37,255"/>
                  <prop k="outline_style" v="solid"/>
                  <prop k="outline_width" v="0"/>
                  <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="outline_width_unit" v="Pixel"/>
                  <prop k="scale_method" v="diameter"/>
                  <prop k="size" v="1"/>
                  <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="size_unit" v="MM"/>
                  <prop k="vertical_anchor_point" v="1"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option type="QString" value="" name="name"/>
                      <Option type="Map" name="properties">
                        <Option type="Map" name="outlineWidth">
                          <Option type="bool" value="true" name="active"/>
                          <Option type="QString" value="1 + (sqrt((&quot;vx&quot; ^ 2)+(&quot;vy&quot; ^ 2)))/1000" name="expression"/>
                          <Option type="int" value="3" name="type"/>
                        </Option>
                        <Option type="Map" name="size">
                          <Option type="bool" value="true" name="active"/>
                          <Option type="QString" value="1 + (sqrt((&quot;vx&quot; ^ 2)+(&quot;vy&quot; ^ 2)))/1000" name="expression"/>
                          <Option type="int" value="3" name="type"/>
                        </Option>
                      </Option>
                      <Option type="QString" value="collection" name="type"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="marker" alpha="1" name="1" clip_to_extent="1">
        <layer enabled="1" pass="0" locked="0" class="VectorField">
          <prop k="angle_orientation" v="1"/>
          <prop k="angle_units" v="0"/>
          <prop k="distance_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="distance_unit" v="MapUnit"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="scale" v="500"/>
          <prop k="size" v="0"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vector_field_type" v="0"/>
          <prop k="x_attribute" v="eastward_component"/>
          <prop k="y_attribute" v="northward_component"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" type="line" alpha="1" name="@1@0" clip_to_extent="1">
            <layer enabled="1" pass="0" locked="0" class="SimpleLine">
              <prop k="capstyle" v="square"/>
              <prop k="customdash" v="5;2"/>
              <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="customdash_unit" v="MM"/>
              <prop k="draw_inside_polygon" v="0"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="line_color" v="93,201,98,255"/>
              <prop k="line_style" v="solid"/>
              <prop k="line_width" v="0"/>
              <prop k="line_width_unit" v="Pixel"/>
              <prop k="offset" v="0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="ring_filter" v="0"/>
              <prop k="use_custom_dash" v="0"/>
              <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option type="Map" name="properties">
                    <Option type="Map" name="outlineWidth">
                      <Option type="bool" value="true" name="active"/>
                      <Option type="QString" value="1 + (sqrt((&quot;vx&quot; ^ 2)+(&quot;vy&quot; ^ 2)))/1000" name="expression"/>
                      <Option type="int" value="3" name="type"/>
                    </Option>
                  </Option>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
            <layer enabled="1" pass="0" locked="0" class="MarkerLine">
              <prop k="average_angle_length" v="4"/>
              <prop k="average_angle_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="average_angle_unit" v="MM"/>
              <prop k="interval" v="3"/>
              <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="interval_unit" v="MM"/>
              <prop k="offset" v="0"/>
              <prop k="offset_along_line" v="0"/>
              <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_along_line_unit" v="MM"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="placement" v="lastvertex"/>
              <prop k="ring_filter" v="0"/>
              <prop k="rotate" v="1"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
              <symbol force_rhr="0" type="marker" alpha="1" name="@@1@0@1" clip_to_extent="1">
                <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
                  <prop k="angle" v="0"/>
                  <prop k="color" v="255,0,0,255"/>
                  <prop k="horizontal_anchor_point" v="1"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="name" v="arrowhead"/>
                  <prop k="offset" v="0,0"/>
                  <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="outline_color" v="93,201,98,255"/>
                  <prop k="outline_style" v="solid"/>
                  <prop k="outline_width" v="0"/>
                  <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="outline_width_unit" v="Pixel"/>
                  <prop k="scale_method" v="diameter"/>
                  <prop k="size" v="1"/>
                  <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="size_unit" v="MM"/>
                  <prop k="vertical_anchor_point" v="1"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option type="QString" value="" name="name"/>
                      <Option type="Map" name="properties">
                        <Option type="Map" name="outlineWidth">
                          <Option type="bool" value="true" name="active"/>
                          <Option type="QString" value="1 + (sqrt((&quot;vx&quot; ^ 2)+(&quot;vy&quot; ^ 2)))/1000" name="expression"/>
                          <Option type="int" value="3" name="type"/>
                        </Option>
                        <Option type="Map" name="size">
                          <Option type="bool" value="true" name="active"/>
                          <Option type="QString" value="1 + (sqrt((&quot;vx&quot; ^ 2)+(&quot;vy&quot; ^ 2)))/1000" name="expression"/>
                          <Option type="int" value="3" name="type"/>
                        </Option>
                      </Option>
                      <Option type="QString" value="collection" name="type"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="marker" alpha="1" name="2" clip_to_extent="1">
        <layer enabled="1" pass="0" locked="0" class="VectorField">
          <prop k="angle_orientation" v="1"/>
          <prop k="angle_units" v="0"/>
          <prop k="distance_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="distance_unit" v="MapUnit"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="scale" v="500"/>
          <prop k="size" v="0"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vector_field_type" v="0"/>
          <prop k="x_attribute" v="eastward_component"/>
          <prop k="y_attribute" v="northward_component"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" type="line" alpha="1" name="@2@0" clip_to_extent="1">
            <layer enabled="1" pass="0" locked="0" class="SimpleLine">
              <prop k="capstyle" v="square"/>
              <prop k="customdash" v="5;2"/>
              <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="customdash_unit" v="MM"/>
              <prop k="draw_inside_polygon" v="0"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="line_color" v="32,144,141,255"/>
              <prop k="line_style" v="solid"/>
              <prop k="line_width" v="0"/>
              <prop k="line_width_unit" v="Pixel"/>
              <prop k="offset" v="0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="ring_filter" v="0"/>
              <prop k="use_custom_dash" v="0"/>
              <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option type="Map" name="properties">
                    <Option type="Map" name="outlineWidth">
                      <Option type="bool" value="true" name="active"/>
                      <Option type="QString" value="1 + (sqrt((&quot;vx&quot; ^ 2)+(&quot;vy&quot; ^ 2)))/1000" name="expression"/>
                      <Option type="int" value="3" name="type"/>
                    </Option>
                  </Option>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
            <layer enabled="1" pass="0" locked="0" class="MarkerLine">
              <prop k="average_angle_length" v="4"/>
              <prop k="average_angle_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="average_angle_unit" v="MM"/>
              <prop k="interval" v="3"/>
              <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="interval_unit" v="MM"/>
              <prop k="offset" v="0"/>
              <prop k="offset_along_line" v="0"/>
              <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_along_line_unit" v="MM"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="placement" v="lastvertex"/>
              <prop k="ring_filter" v="0"/>
              <prop k="rotate" v="1"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
              <symbol force_rhr="0" type="marker" alpha="1" name="@@2@0@1" clip_to_extent="1">
                <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
                  <prop k="angle" v="0"/>
                  <prop k="color" v="255,0,0,255"/>
                  <prop k="horizontal_anchor_point" v="1"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="name" v="arrowhead"/>
                  <prop k="offset" v="0,0"/>
                  <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="outline_color" v="32,144,141,255"/>
                  <prop k="outline_style" v="solid"/>
                  <prop k="outline_width" v="0"/>
                  <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="outline_width_unit" v="Pixel"/>
                  <prop k="scale_method" v="diameter"/>
                  <prop k="size" v="1"/>
                  <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="size_unit" v="MM"/>
                  <prop k="vertical_anchor_point" v="1"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option type="QString" value="" name="name"/>
                      <Option type="Map" name="properties">
                        <Option type="Map" name="outlineWidth">
                          <Option type="bool" value="true" name="active"/>
                          <Option type="QString" value="1 + (sqrt((&quot;vx&quot; ^ 2)+(&quot;vy&quot; ^ 2)))/1000" name="expression"/>
                          <Option type="int" value="3" name="type"/>
                        </Option>
                        <Option type="Map" name="size">
                          <Option type="bool" value="true" name="active"/>
                          <Option type="QString" value="1 + (sqrt((&quot;vx&quot; ^ 2)+(&quot;vy&quot; ^ 2)))/1000" name="expression"/>
                          <Option type="int" value="3" name="type"/>
                        </Option>
                      </Option>
                      <Option type="QString" value="collection" name="type"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="marker" alpha="1" name="3" clip_to_extent="1">
        <layer enabled="1" pass="0" locked="0" class="VectorField">
          <prop k="angle_orientation" v="1"/>
          <prop k="angle_units" v="0"/>
          <prop k="distance_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="distance_unit" v="MapUnit"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="scale" v="500"/>
          <prop k="size" v="0"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vector_field_type" v="0"/>
          <prop k="x_attribute" v="eastward_component"/>
          <prop k="y_attribute" v="northward_component"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" type="line" alpha="1" name="@3@0" clip_to_extent="1">
            <layer enabled="1" pass="0" locked="0" class="SimpleLine">
              <prop k="capstyle" v="square"/>
              <prop k="customdash" v="5;2"/>
              <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="customdash_unit" v="MM"/>
              <prop k="draw_inside_polygon" v="0"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="line_color" v="58,82,139,255"/>
              <prop k="line_style" v="solid"/>
              <prop k="line_width" v="0"/>
              <prop k="line_width_unit" v="Pixel"/>
              <prop k="offset" v="0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="ring_filter" v="0"/>
              <prop k="use_custom_dash" v="0"/>
              <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option type="Map" name="properties">
                    <Option type="Map" name="outlineWidth">
                      <Option type="bool" value="true" name="active"/>
                      <Option type="QString" value="1 + (sqrt((&quot;vx&quot; ^ 2)+(&quot;vy&quot; ^ 2)))/1000" name="expression"/>
                      <Option type="int" value="3" name="type"/>
                    </Option>
                  </Option>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
            <layer enabled="1" pass="0" locked="0" class="MarkerLine">
              <prop k="average_angle_length" v="4"/>
              <prop k="average_angle_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="average_angle_unit" v="MM"/>
              <prop k="interval" v="3"/>
              <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="interval_unit" v="MM"/>
              <prop k="offset" v="0"/>
              <prop k="offset_along_line" v="0"/>
              <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_along_line_unit" v="MM"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="placement" v="lastvertex"/>
              <prop k="ring_filter" v="0"/>
              <prop k="rotate" v="1"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
              <symbol force_rhr="0" type="marker" alpha="1" name="@@3@0@1" clip_to_extent="1">
                <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
                  <prop k="angle" v="0"/>
                  <prop k="color" v="255,0,0,255"/>
                  <prop k="horizontal_anchor_point" v="1"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="name" v="arrowhead"/>
                  <prop k="offset" v="0,0"/>
                  <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="outline_color" v="58,82,139,255"/>
                  <prop k="outline_style" v="solid"/>
                  <prop k="outline_width" v="0"/>
                  <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="outline_width_unit" v="Pixel"/>
                  <prop k="scale_method" v="diameter"/>
                  <prop k="size" v="1"/>
                  <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="size_unit" v="MM"/>
                  <prop k="vertical_anchor_point" v="1"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option type="QString" value="" name="name"/>
                      <Option type="Map" name="properties">
                        <Option type="Map" name="outlineWidth">
                          <Option type="bool" value="true" name="active"/>
                          <Option type="QString" value="1 + (sqrt((&quot;vx&quot; ^ 2)+(&quot;vy&quot; ^ 2)))/1000" name="expression"/>
                          <Option type="int" value="3" name="type"/>
                        </Option>
                        <Option type="Map" name="size">
                          <Option type="bool" value="true" name="active"/>
                          <Option type="QString" value="1 + (sqrt((&quot;vx&quot; ^ 2)+(&quot;vy&quot; ^ 2)))/1000" name="expression"/>
                          <Option type="int" value="3" name="type"/>
                        </Option>
                      </Option>
                      <Option type="QString" value="collection" name="type"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol force_rhr="0" type="marker" alpha="1" name="4" clip_to_extent="1">
        <layer enabled="1" pass="0" locked="0" class="VectorField">
          <prop k="angle_orientation" v="1"/>
          <prop k="angle_units" v="0"/>
          <prop k="distance_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="distance_unit" v="MapUnit"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="scale" v="500"/>
          <prop k="size" v="0"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vector_field_type" v="0"/>
          <prop k="x_attribute" v="eastward_component"/>
          <prop k="y_attribute" v="northward_component"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" type="line" alpha="1" name="@4@0" clip_to_extent="1">
            <layer enabled="1" pass="0" locked="0" class="SimpleLine">
              <prop k="capstyle" v="square"/>
              <prop k="customdash" v="5;2"/>
              <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="customdash_unit" v="MM"/>
              <prop k="draw_inside_polygon" v="0"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="line_color" v="68,1,84,255"/>
              <prop k="line_style" v="solid"/>
              <prop k="line_width" v="0"/>
              <prop k="line_width_unit" v="Pixel"/>
              <prop k="offset" v="0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="ring_filter" v="0"/>
              <prop k="use_custom_dash" v="0"/>
              <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option type="Map" name="properties">
                    <Option type="Map" name="outlineWidth">
                      <Option type="bool" value="true" name="active"/>
                      <Option type="QString" value="1 + (sqrt((&quot;vx&quot; ^ 2)+(&quot;vy&quot; ^ 2)))/1000" name="expression"/>
                      <Option type="int" value="3" name="type"/>
                    </Option>
                  </Option>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
            <layer enabled="1" pass="0" locked="0" class="MarkerLine">
              <prop k="average_angle_length" v="4"/>
              <prop k="average_angle_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="average_angle_unit" v="MM"/>
              <prop k="interval" v="3"/>
              <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="interval_unit" v="MM"/>
              <prop k="offset" v="0"/>
              <prop k="offset_along_line" v="0"/>
              <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_along_line_unit" v="MM"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="placement" v="lastvertex"/>
              <prop k="ring_filter" v="0"/>
              <prop k="rotate" v="1"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
              <symbol force_rhr="0" type="marker" alpha="1" name="@@4@0@1" clip_to_extent="1">
                <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
                  <prop k="angle" v="0"/>
                  <prop k="color" v="255,0,0,255"/>
                  <prop k="horizontal_anchor_point" v="1"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="name" v="arrowhead"/>
                  <prop k="offset" v="0,0"/>
                  <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="outline_color" v="68,1,84,255"/>
                  <prop k="outline_style" v="solid"/>
                  <prop k="outline_width" v="0"/>
                  <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="outline_width_unit" v="Pixel"/>
                  <prop k="scale_method" v="diameter"/>
                  <prop k="size" v="1"/>
                  <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="size_unit" v="MM"/>
                  <prop k="vertical_anchor_point" v="1"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option type="QString" value="" name="name"/>
                      <Option type="Map" name="properties">
                        <Option type="Map" name="outlineWidth">
                          <Option type="bool" value="true" name="active"/>
                          <Option type="QString" value="1 + (sqrt((&quot;vx&quot; ^ 2)+(&quot;vy&quot; ^ 2)))/1000" name="expression"/>
                          <Option type="int" value="3" name="type"/>
                        </Option>
                        <Option type="Map" name="size">
                          <Option type="bool" value="true" name="active"/>
                          <Option type="QString" value="1 + (sqrt((&quot;vx&quot; ^ 2)+(&quot;vy&quot; ^ 2)))/1000" name="expression"/>
                          <Option type="int" value="3" name="type"/>
                        </Option>
                      </Option>
                      <Option type="QString" value="collection" name="type"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </layer>
          </symbol>
        </layer>
      </symbol>
    </symbols>
    <source-symbol>
      <symbol force_rhr="0" type="marker" alpha="1" name="0" clip_to_extent="1">
        <layer enabled="1" pass="0" locked="0" class="VectorField">
          <prop k="angle_orientation" v="1"/>
          <prop k="angle_units" v="0"/>
          <prop k="distance_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="distance_unit" v="MapUnit"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="scale" v="500"/>
          <prop k="size" v="0"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vector_field_type" v="0"/>
          <prop k="x_attribute" v="eastward_component"/>
          <prop k="y_attribute" v="northward_component"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
          <symbol force_rhr="0" type="line" alpha="1" name="@0@0" clip_to_extent="1">
            <layer enabled="1" pass="0" locked="0" class="SimpleLine">
              <prop k="capstyle" v="square"/>
              <prop k="customdash" v="5;2"/>
              <prop k="customdash_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="customdash_unit" v="MM"/>
              <prop k="draw_inside_polygon" v="0"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="line_color" v="0,0,0,255"/>
              <prop k="line_style" v="solid"/>
              <prop k="line_width" v="0"/>
              <prop k="line_width_unit" v="Pixel"/>
              <prop k="offset" v="0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="ring_filter" v="0"/>
              <prop k="use_custom_dash" v="0"/>
              <prop k="width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option type="Map" name="properties">
                    <Option type="Map" name="outlineWidth">
                      <Option type="bool" value="true" name="active"/>
                      <Option type="QString" value="1 + (sqrt((&quot;vx&quot; ^ 2)+(&quot;vy&quot; ^ 2)))/1000" name="expression"/>
                      <Option type="int" value="3" name="type"/>
                    </Option>
                  </Option>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
            <layer enabled="1" pass="0" locked="0" class="MarkerLine">
              <prop k="average_angle_length" v="4"/>
              <prop k="average_angle_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="average_angle_unit" v="MM"/>
              <prop k="interval" v="3"/>
              <prop k="interval_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="interval_unit" v="MM"/>
              <prop k="offset" v="0"/>
              <prop k="offset_along_line" v="0"/>
              <prop k="offset_along_line_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_along_line_unit" v="MM"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="placement" v="lastvertex"/>
              <prop k="ring_filter" v="0"/>
              <prop k="rotate" v="1"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
              <symbol force_rhr="0" type="marker" alpha="1" name="@@0@0@1" clip_to_extent="1">
                <layer enabled="1" pass="0" locked="0" class="SimpleMarker">
                  <prop k="angle" v="0"/>
                  <prop k="color" v="255,0,0,255"/>
                  <prop k="horizontal_anchor_point" v="1"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="name" v="arrowhead"/>
                  <prop k="offset" v="0,0"/>
                  <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="outline_color" v="0,0,0,255"/>
                  <prop k="outline_style" v="solid"/>
                  <prop k="outline_width" v="0"/>
                  <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="outline_width_unit" v="Pixel"/>
                  <prop k="scale_method" v="diameter"/>
                  <prop k="size" v="1"/>
                  <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="size_unit" v="MM"/>
                  <prop k="vertical_anchor_point" v="1"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option type="QString" value="" name="name"/>
                      <Option type="Map" name="properties">
                        <Option type="Map" name="outlineWidth">
                          <Option type="bool" value="true" name="active"/>
                          <Option type="QString" value="1 + (sqrt((&quot;vx&quot; ^ 2)+(&quot;vy&quot; ^ 2)))/1000" name="expression"/>
                          <Option type="int" value="3" name="type"/>
                        </Option>
                        <Option type="Map" name="size">
                          <Option type="bool" value="true" name="active"/>
                          <Option type="QString" value="1 + (sqrt((&quot;vx&quot; ^ 2)+(&quot;vy&quot; ^ 2)))/1000" name="expression"/>
                          <Option type="int" value="3" name="type"/>
                        </Option>
                      </Option>
                      <Option type="QString" value="collection" name="type"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </layer>
          </symbol>
        </layer>
      </symbol>
    </source-symbol>
    <colorramp type="gradient" name="[source]">
      <prop k="color1" v="253,231,37,255"/>
      <prop k="color2" v="68,1,84,255"/>
      <prop k="discrete" v="0"/>
      <prop k="rampType" v="gradient"/>
      <prop k="stops" v="0.019608;241,229,29,255:0.039216;229,228,25,255:0.058824;216,226,25,255:0.078431;202,225,31,255:0.098039;189,223,38,255:0.117647;176,221,47,255:0.137255;162,218,55,255:0.156863;149,216,64,255:0.176471;137,213,72,255:0.196078;124,210,80,255:0.215686;112,207,87,255:0.235294;101,203,94,255:0.254902;90,200,100,255:0.27451;80,196,106,255:0.294118;70,192,111,255:0.313725;61,188,116,255:0.333333;53,183,121,255:0.352941;46,179,124,255:0.372549;40,174,128,255:0.392157;36,170,131,255:0.411765;33,165,133,255:0.431373;31,161,136,255:0.45098;30,156,137,255:0.470588;31,151,139,255:0.490196;32,146,140,255:0.509804;33,142,141,255:0.529412;35,137,142,255:0.54902;37,132,142,255:0.568627;39,128,142,255:0.588235;41,123,142,255:0.607843;42,118,142,255:0.627451;44,113,142,255:0.647059;46,109,142,255:0.666667;49,104,142,255:0.686275;51,99,141,255:0.705882;53,94,141,255:0.72549;56,89,140,255:0.745098;58,83,139,255:0.764706;61,78,138,255:0.784314;63,72,137,255:0.803922;65,66,135,255:0.823529;67,61,132,255:0.843137;69,55,129,255:0.862745;70,48,126,255:0.882353;71,42,122,255:0.901961;72,36,117,255:0.921569;72,29,111,255:0.941176;72,23,105,255:0.960784;71,16,99,255:0.980392;70,8,92,255"/>
    </colorramp>
    <classificationMethod id="Quantile">
      <symmetricMode symmetrypoint="0" astride="0" enabled="0"/>
      <labelFormat labelprecision="4" format="%1 - %2 " trimtrailingzeroes="1"/>
      <extraInformation/>
    </classificationMethod>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <layerGeometryType>0</layerGeometryType>
</qgis>

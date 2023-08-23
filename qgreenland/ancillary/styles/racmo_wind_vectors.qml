<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" minScale="100000000" simplifyDrawingTol="1" styleCategories="Symbology|Labeling|Rendering" symbologyReferenceScale="-1" labelsEnabled="0" simplifyLocal="1" simplifyAlgorithm="0" simplifyMaxScale="1" hasScaleBasedVisibilityFlag="0" simplifyDrawingHints="0" version="3.28.7-Firenze">
  <renderer-v2 referencescale="-1" enableorderby="0" type="singleSymbol" symbollevels="0" forceraster="0">
    <symbols>
      <symbol frame_rate="10" alpha="1" is_animated="0" name="0" type="marker" clip_to_extent="1" force_rhr="0">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer class="VectorField" pass="0" enabled="1" locked="0">
          <Option type="Map">
            <Option name="angle_orientation" type="QString" value="1"/>
            <Option name="angle_units" type="QString" value="0"/>
            <Option name="distance_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="distance_unit" type="QString" value="MapUnit"/>
            <Option name="offset" type="QString" value="0,0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="scale" type="QString" value="500"/>
            <Option name="size" type="QString" value="0"/>
            <Option name="size_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="size_unit" type="QString" value="MM"/>
            <Option name="vector_field_type" type="QString" value="0"/>
            <Option name="x_attribute" type="QString" value="eastward_component"/>
            <Option name="y_attribute" type="QString" value="northward_component"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol frame_rate="10" alpha="1" is_animated="0" name="@0@0" type="line" clip_to_extent="1" force_rhr="0">
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </data_defined_properties>
            <layer class="SimpleLine" pass="0" enabled="1" locked="0">
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
                <Option name="line_color" type="QString" value="0,0,0,255"/>
                <Option name="line_style" type="QString" value="solid"/>
                <Option name="line_width" type="QString" value="0"/>
                <Option name="line_width_unit" type="QString" value="Pixel"/>
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
                  <Option name="properties" type="Map">
                    <Option name="outlineWidth" type="Map">
                      <Option name="active" type="bool" value="true"/>
                      <Option name="expression" type="QString" value="1 + (sqrt((&quot;vx&quot; ^ 2)+(&quot;vy&quot; ^ 2)))/1000"/>
                      <Option name="type" type="int" value="3"/>
                    </Option>
                  </Option>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
            <layer class="MarkerLine" pass="0" enabled="1" locked="0">
              <Option type="Map">
                <Option name="average_angle_length" type="QString" value="4"/>
                <Option name="average_angle_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="average_angle_unit" type="QString" value="MM"/>
                <Option name="interval" type="QString" value="3"/>
                <Option name="interval_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="interval_unit" type="QString" value="MM"/>
                <Option name="offset" type="QString" value="0"/>
                <Option name="offset_along_line" type="QString" value="0"/>
                <Option name="offset_along_line_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="offset_along_line_unit" type="QString" value="MM"/>
                <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="offset_unit" type="QString" value="MM"/>
                <Option name="place_on_every_part" type="bool" value="true"/>
                <Option name="placements" type="QString" value="LastVertex"/>
                <Option name="ring_filter" type="QString" value="0"/>
                <Option name="rotate" type="QString" value="1"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
              <symbol frame_rate="10" alpha="1" is_animated="0" name="@@0@0@1" type="marker" clip_to_extent="1" force_rhr="0">
                <data_defined_properties>
                  <Option type="Map">
                    <Option name="name" type="QString" value=""/>
                    <Option name="properties"/>
                    <Option name="type" type="QString" value="collection"/>
                  </Option>
                </data_defined_properties>
                <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
                  <Option type="Map">
                    <Option name="angle" type="QString" value="0"/>
                    <Option name="cap_style" type="QString" value="square"/>
                    <Option name="color" type="QString" value="255,0,0,255"/>
                    <Option name="horizontal_anchor_point" type="QString" value="1"/>
                    <Option name="joinstyle" type="QString" value="bevel"/>
                    <Option name="name" type="QString" value="arrowhead"/>
                    <Option name="offset" type="QString" value="0,0"/>
                    <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                    <Option name="offset_unit" type="QString" value="MM"/>
                    <Option name="outline_color" type="QString" value="0,0,0,255"/>
                    <Option name="outline_style" type="QString" value="solid"/>
                    <Option name="outline_width" type="QString" value="0"/>
                    <Option name="outline_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                    <Option name="outline_width_unit" type="QString" value="Pixel"/>
                    <Option name="scale_method" type="QString" value="diameter"/>
                    <Option name="size" type="QString" value="1"/>
                    <Option name="size_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                    <Option name="size_unit" type="QString" value="MM"/>
                    <Option name="vertical_anchor_point" type="QString" value="1"/>
                  </Option>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option name="name" type="QString" value=""/>
                      <Option name="properties" type="Map">
                        <Option name="outlineWidth" type="Map">
                          <Option name="active" type="bool" value="true"/>
                          <Option name="expression" type="QString" value="1 + (sqrt((&quot;vx&quot; ^ 2)+(&quot;vy&quot; ^ 2)))/1000"/>
                          <Option name="type" type="int" value="3"/>
                        </Option>
                        <Option name="size" type="Map">
                          <Option name="active" type="bool" value="true"/>
                          <Option name="expression" type="QString" value="1 + (sqrt((&quot;vx&quot; ^ 2)+(&quot;vy&quot; ^ 2)))/1000"/>
                          <Option name="type" type="int" value="3"/>
                        </Option>
                      </Option>
                      <Option name="type" type="QString" value="collection"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </layer>
          </symbol>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <layerGeometryType>0</layerGeometryType>
</qgis>

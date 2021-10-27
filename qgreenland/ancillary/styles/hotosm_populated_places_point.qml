<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="3.10.4-A Coruña" simplifyDrawingHints="0" styleCategories="Symbology|Labeling|Rendering" hasScaleBasedVisibilityFlag="0" maxScale="0" simplifyDrawingTol="1" simplifyLocal="1" simplifyMaxScale="1" labelsEnabled="1" simplifyAlgorithm="0" minScale="1e+08">
  <renderer-v2 type="RuleRenderer" symbollevels="0" forceraster="0" enableorderby="0">
    <rules key="{54bac836-3bdb-4243-b0bb-84e8bd1186ca}">
      <rule key="{48825e81-e7d8-4689-847a-9310d4c81c41}" filter="&quot;place&quot; = 'city'" symbol="0" label="Cities"/>
      <rule key="{ff41f546-9acf-490e-ac12-8450898dd7a9}" filter="&quot;place&quot; = 'town' or &quot;place&quot; = 'village'" symbol="1" label="Towns, villages"/>
      <rule key="{d74d65d0-5220-4299-b575-299c330bee85}" filter="ELSE" symbol="2" label="Everything else"/>
    </rules>
    <symbols>
      <symbol alpha="1" type="marker" clip_to_extent="1" force_rhr="0" name="0">
        <layer enabled="1" class="SimpleMarker" pass="0" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="232,239,241,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="3.5"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="1" type="marker" clip_to_extent="1" force_rhr="0" name="1">
        <layer enabled="1" class="SimpleMarker" pass="0" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="232,239,241,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="2"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol alpha="0.97" type="marker" clip_to_extent="1" force_rhr="0" name="2">
        <layer enabled="1" class="SimpleMarker" pass="0" locked="0">
          <prop k="angle" v="0"/>
          <prop k="color" v="232,239,241,255"/>
          <prop k="horizontal_anchor_point" v="1"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="name" v="circle"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="35,35,35,255"/>
          <prop k="outline_style" v="solid"/>
          <prop k="outline_width" v="0"/>
          <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="scale_method" v="diameter"/>
          <prop k="size" v="1.5"/>
          <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="size_unit" v="MM"/>
          <prop k="vertical_anchor_point" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <labeling type="rule-based">
    <rules key="{5a457255-0cbc-4815-96d6-d8acd4a53225}">
      <rule description="Cities" key="{68118414-7f41-46f0-84e3-5ab586bd8394}" filter="&quot;place&quot; = 'city'">
        <settings calloutType="simple">
          <text-style isExpression="0" fontSizeUnit="Point" fontWeight="50" fontKerning="1" namedStyle="" fontItalic="0" fontUnderline="0" multilineHeight="1" textOpacity="1" fontFamily="Cantarell" useSubstitutions="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontStrikeout="0" fontSize="10" fontLetterSpacing="0" textColor="0,0,0,255" fontWordSpacing="0" textOrientation="horizontal" previewBkgrdColor="255,255,255,255" blendMode="0" fieldName="name" fontCapitals="0">
            <text-buffer bufferColor="255,255,255,255" bufferBlendMode="0" bufferOpacity="1" bufferDraw="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferSize="1" bufferSizeUnits="MM" bufferNoFill="1" bufferJoinStyle="128"/>
            <background shapeBlendMode="0" shapeOffsetY="0" shapeRadiiX="0" shapeDraw="0" shapeRadiiY="0" shapeType="0" shapeRotationType="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeBorderColor="128,128,128,255" shapeOffsetX="0" shapeSizeY="0" shapeOffsetUnit="MM" shapeSizeType="0" shapeRadiiUnit="MM" shapeBorderWidthUnit="MM" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeFillColor="255,255,255,255" shapeJoinStyle="64" shapeRotation="0" shapeSizeUnit="MM" shapeSVGFile="" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSizeX="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidth="0" shapeOpacity="1">
              <symbol alpha="1" type="marker" clip_to_extent="1" force_rhr="0" name="markerSymbol">
                <layer enabled="1" class="SimpleMarker" pass="0" locked="0">
                  <prop k="angle" v="0"/>
                  <prop k="color" v="133,182,111,255"/>
                  <prop k="horizontal_anchor_point" v="1"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="name" v="circle"/>
                  <prop k="offset" v="0,0"/>
                  <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="outline_color" v="35,35,35,255"/>
                  <prop k="outline_style" v="solid"/>
                  <prop k="outline_width" v="0"/>
                  <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="outline_width_unit" v="MM"/>
                  <prop k="scale_method" v="diameter"/>
                  <prop k="size" v="2"/>
                  <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="size_unit" v="MM"/>
                  <prop k="vertical_anchor_point" v="1"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option type="QString" value="" name="name"/>
                      <Option name="properties"/>
                      <Option type="QString" value="collection" name="type"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </background>
            <shadow shadowScale="100" shadowRadiusUnit="MM" shadowBlendMode="6" shadowOffsetUnit="MM" shadowOffsetGlobal="1" shadowColor="0,0,0,255" shadowOffsetAngle="135" shadowOpacity="0.7" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusAlphaOnly="0" shadowUnder="0" shadowDraw="0" shadowOffsetDist="1" shadowRadius="1.5"/>
            <dd_properties>
              <Option type="Map">
                <Option type="QString" value="" name="name"/>
                <Option name="properties"/>
                <Option type="QString" value="collection" name="type"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format wrapChar="" rightDirectionSymbol=">" addDirectionSymbol="0" plussign="0" reverseDirectionSymbol="0" multilineAlign="3" leftDirectionSymbol="&lt;" formatNumbers="0" autoWrapLength="0" decimals="3" placeDirectionSymbol="0" useMaxLineLengthForAutoWrap="1"/>
          <placement xOffset="0" preserveRotation="1" centroidWhole="0" maxCurvedCharAngleOut="-25" fitInPolygonOnly="0" offsetUnits="MM" placement="0" overrunDistance="0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" layerType="PointGeometry" quadOffset="4" centroidInside="0" priority="5" rotationAngle="0" maxCurvedCharAngleIn="25" overrunDistanceUnit="MM" repeatDistance="0" geometryGeneratorEnabled="0" distUnits="MM" distMapUnitScale="3x:0,0,0,0,0,0" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" placementFlags="10" repeatDistanceUnits="MM" yOffset="0" offsetType="0" geometryGeneratorType="PointGeometry" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" dist="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" geometryGenerator=""/>
          <rendering fontMaxPixelSize="10000" obstacleFactor="1" obstacle="1" drawLabels="1" scaleMax="28500000" fontMinPixelSize="3" displayAll="0" zIndex="0" obstacleType="0" labelPerPart="0" minFeatureSize="0" scaleMin="0" upsidedownLabels="0" fontLimitPixelSize="0" scaleVisibility="1" mergeLines="0" limitNumLabels="0" maxNumLabels="2000"/>
          <dd_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </dd_properties>
          <callout type="simple">
            <Option type="Map">
              <Option type="QString" value="pole_of_inaccessibility" name="anchorPoint"/>
              <Option type="Map" name="ddProperties">
                <Option type="QString" value="" name="name"/>
                <Option name="properties"/>
                <Option type="QString" value="collection" name="type"/>
              </Option>
              <Option type="bool" value="false" name="drawToAllParts"/>
              <Option type="QString" value="0" name="enabled"/>
              <Option type="QString" value="&lt;symbol alpha=&quot;1&quot; type=&quot;line&quot; clip_to_extent=&quot;1&quot; force_rhr=&quot;0&quot; name=&quot;symbol&quot;>&lt;layer enabled=&quot;1&quot; class=&quot;SimpleLine&quot; pass=&quot;0&quot; locked=&quot;0&quot;>&lt;prop k=&quot;capstyle&quot; v=&quot;square&quot;/>&lt;prop k=&quot;customdash&quot; v=&quot;5;2&quot;/>&lt;prop k=&quot;customdash_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;customdash_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;draw_inside_polygon&quot; v=&quot;0&quot;/>&lt;prop k=&quot;joinstyle&quot; v=&quot;bevel&quot;/>&lt;prop k=&quot;line_color&quot; v=&quot;60,60,60,255&quot;/>&lt;prop k=&quot;line_style&quot; v=&quot;solid&quot;/>&lt;prop k=&quot;line_width&quot; v=&quot;0.3&quot;/>&lt;prop k=&quot;line_width_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;ring_filter&quot; v=&quot;0&quot;/>&lt;prop k=&quot;use_custom_dash&quot; v=&quot;0&quot;/>&lt;prop k=&quot;width_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; value=&quot;&quot; name=&quot;name&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;collection&quot; name=&quot;type&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" name="lineSymbol"/>
              <Option type="double" value="0" name="minLength"/>
              <Option type="QString" value="3x:0,0,0,0,0,0" name="minLengthMapUnitScale"/>
              <Option type="QString" value="MM" name="minLengthUnit"/>
              <Option type="double" value="0" name="offsetFromAnchor"/>
              <Option type="QString" value="3x:0,0,0,0,0,0" name="offsetFromAnchorMapUnitScale"/>
              <Option type="QString" value="MM" name="offsetFromAnchorUnit"/>
              <Option type="double" value="0" name="offsetFromLabel"/>
              <Option type="QString" value="3x:0,0,0,0,0,0" name="offsetFromLabelMapUnitScale"/>
              <Option type="QString" value="MM" name="offsetFromLabelUnit"/>
            </Option>
          </callout>
        </settings>
      </rule>
      <rule description="Towns, villages" key="{4d271f21-c6a6-42b8-a865-e4e0c5f7867d}" filter="&quot;place&quot; = 'town' or &quot;place&quot; = 'village'">
        <settings calloutType="simple">
          <text-style isExpression="0" fontSizeUnit="Point" fontWeight="50" fontKerning="1" namedStyle="" fontItalic="0" fontUnderline="0" multilineHeight="1" textOpacity="1" fontFamily="Cantarell" useSubstitutions="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontStrikeout="0" fontSize="10" fontLetterSpacing="0" textColor="0,0,0,255" fontWordSpacing="0" textOrientation="horizontal" previewBkgrdColor="255,255,255,255" blendMode="0" fieldName="name" fontCapitals="0">
            <text-buffer bufferColor="255,255,255,255" bufferBlendMode="0" bufferOpacity="1" bufferDraw="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferSize="1" bufferSizeUnits="MM" bufferNoFill="1" bufferJoinStyle="128"/>
            <background shapeBlendMode="0" shapeOffsetY="0" shapeRadiiX="0" shapeDraw="0" shapeRadiiY="0" shapeType="0" shapeRotationType="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeBorderColor="128,128,128,255" shapeOffsetX="0" shapeSizeY="0" shapeOffsetUnit="MM" shapeSizeType="0" shapeRadiiUnit="MM" shapeBorderWidthUnit="MM" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeFillColor="255,255,255,255" shapeJoinStyle="64" shapeRotation="0" shapeSizeUnit="MM" shapeSVGFile="" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSizeX="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidth="0" shapeOpacity="1">
              <symbol alpha="1" type="marker" clip_to_extent="1" force_rhr="0" name="markerSymbol">
                <layer enabled="1" class="SimpleMarker" pass="0" locked="0">
                  <prop k="angle" v="0"/>
                  <prop k="color" v="225,89,137,255"/>
                  <prop k="horizontal_anchor_point" v="1"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="name" v="circle"/>
                  <prop k="offset" v="0,0"/>
                  <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="outline_color" v="35,35,35,255"/>
                  <prop k="outline_style" v="solid"/>
                  <prop k="outline_width" v="0"/>
                  <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="outline_width_unit" v="MM"/>
                  <prop k="scale_method" v="diameter"/>
                  <prop k="size" v="2"/>
                  <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="size_unit" v="MM"/>
                  <prop k="vertical_anchor_point" v="1"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option type="QString" value="" name="name"/>
                      <Option name="properties"/>
                      <Option type="QString" value="collection" name="type"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </background>
            <shadow shadowScale="100" shadowRadiusUnit="MM" shadowBlendMode="6" shadowOffsetUnit="MM" shadowOffsetGlobal="1" shadowColor="0,0,0,255" shadowOffsetAngle="135" shadowOpacity="0.7" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusAlphaOnly="0" shadowUnder="0" shadowDraw="0" shadowOffsetDist="1" shadowRadius="1.5"/>
            <dd_properties>
              <Option type="Map">
                <Option type="QString" value="" name="name"/>
                <Option name="properties"/>
                <Option type="QString" value="collection" name="type"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format wrapChar="" rightDirectionSymbol=">" addDirectionSymbol="0" plussign="0" reverseDirectionSymbol="0" multilineAlign="3" leftDirectionSymbol="&lt;" formatNumbers="0" autoWrapLength="0" decimals="3" placeDirectionSymbol="0" useMaxLineLengthForAutoWrap="1"/>
          <placement xOffset="0" preserveRotation="1" centroidWhole="0" maxCurvedCharAngleOut="-25" fitInPolygonOnly="0" offsetUnits="MM" placement="0" overrunDistance="0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" layerType="PointGeometry" quadOffset="4" centroidInside="0" priority="5" rotationAngle="0" maxCurvedCharAngleIn="25" overrunDistanceUnit="MM" repeatDistance="0" geometryGeneratorEnabled="0" distUnits="MM" distMapUnitScale="3x:0,0,0,0,0,0" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" placementFlags="10" repeatDistanceUnits="MM" yOffset="0" offsetType="0" geometryGeneratorType="PointGeometry" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" dist="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" geometryGenerator=""/>
          <rendering fontMaxPixelSize="10000" obstacleFactor="1" obstacle="1" drawLabels="1" scaleMax="3515511" fontMinPixelSize="3" displayAll="0" zIndex="0" obstacleType="0" labelPerPart="0" minFeatureSize="0" scaleMin="0" upsidedownLabels="0" fontLimitPixelSize="0" scaleVisibility="1" mergeLines="0" limitNumLabels="0" maxNumLabels="2000"/>
          <dd_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </dd_properties>
          <callout type="simple">
            <Option type="Map">
              <Option type="QString" value="pole_of_inaccessibility" name="anchorPoint"/>
              <Option type="Map" name="ddProperties">
                <Option type="QString" value="" name="name"/>
                <Option name="properties"/>
                <Option type="QString" value="collection" name="type"/>
              </Option>
              <Option type="bool" value="false" name="drawToAllParts"/>
              <Option type="QString" value="0" name="enabled"/>
              <Option type="QString" value="&lt;symbol alpha=&quot;1&quot; type=&quot;line&quot; clip_to_extent=&quot;1&quot; force_rhr=&quot;0&quot; name=&quot;symbol&quot;>&lt;layer enabled=&quot;1&quot; class=&quot;SimpleLine&quot; pass=&quot;0&quot; locked=&quot;0&quot;>&lt;prop k=&quot;capstyle&quot; v=&quot;square&quot;/>&lt;prop k=&quot;customdash&quot; v=&quot;5;2&quot;/>&lt;prop k=&quot;customdash_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;customdash_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;draw_inside_polygon&quot; v=&quot;0&quot;/>&lt;prop k=&quot;joinstyle&quot; v=&quot;bevel&quot;/>&lt;prop k=&quot;line_color&quot; v=&quot;60,60,60,255&quot;/>&lt;prop k=&quot;line_style&quot; v=&quot;solid&quot;/>&lt;prop k=&quot;line_width&quot; v=&quot;0.3&quot;/>&lt;prop k=&quot;line_width_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;ring_filter&quot; v=&quot;0&quot;/>&lt;prop k=&quot;use_custom_dash&quot; v=&quot;0&quot;/>&lt;prop k=&quot;width_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; value=&quot;&quot; name=&quot;name&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;collection&quot; name=&quot;type&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" name="lineSymbol"/>
              <Option type="double" value="0" name="minLength"/>
              <Option type="QString" value="3x:0,0,0,0,0,0" name="minLengthMapUnitScale"/>
              <Option type="QString" value="MM" name="minLengthUnit"/>
              <Option type="double" value="0" name="offsetFromAnchor"/>
              <Option type="QString" value="3x:0,0,0,0,0,0" name="offsetFromAnchorMapUnitScale"/>
              <Option type="QString" value="MM" name="offsetFromAnchorUnit"/>
              <Option type="double" value="0" name="offsetFromLabel"/>
              <Option type="QString" value="3x:0,0,0,0,0,0" name="offsetFromLabelMapUnitScale"/>
              <Option type="QString" value="MM" name="offsetFromLabelUnit"/>
            </Option>
          </callout>
        </settings>
      </rule>
      <rule description="Everything else" key="{a1ab1771-294d-4f3f-80b3-6c3834236705}" filter="ELSE">
        <settings calloutType="simple">
          <text-style isExpression="0" fontSizeUnit="Point" fontWeight="50" fontKerning="1" namedStyle="" fontItalic="0" fontUnderline="0" multilineHeight="1" textOpacity="1" fontFamily="Cantarell" useSubstitutions="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontStrikeout="0" fontSize="10" fontLetterSpacing="0" textColor="0,0,0,255" fontWordSpacing="0" textOrientation="horizontal" previewBkgrdColor="255,255,255,255" blendMode="0" fieldName="name" fontCapitals="0">
            <text-buffer bufferColor="255,255,255,255" bufferBlendMode="0" bufferOpacity="1" bufferDraw="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferSize="1" bufferSizeUnits="MM" bufferNoFill="1" bufferJoinStyle="128"/>
            <background shapeBlendMode="0" shapeOffsetY="0" shapeRadiiX="0" shapeDraw="0" shapeRadiiY="0" shapeType="0" shapeRotationType="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeBorderColor="128,128,128,255" shapeOffsetX="0" shapeSizeY="0" shapeOffsetUnit="MM" shapeSizeType="0" shapeRadiiUnit="MM" shapeBorderWidthUnit="MM" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeFillColor="255,255,255,255" shapeJoinStyle="64" shapeRotation="0" shapeSizeUnit="MM" shapeSVGFile="" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSizeX="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidth="0" shapeOpacity="1">
              <symbol alpha="1" type="marker" clip_to_extent="1" force_rhr="0" name="markerSymbol">
                <layer enabled="1" class="SimpleMarker" pass="0" locked="0">
                  <prop k="angle" v="0"/>
                  <prop k="color" v="196,60,57,255"/>
                  <prop k="horizontal_anchor_point" v="1"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="name" v="circle"/>
                  <prop k="offset" v="0,0"/>
                  <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="outline_color" v="35,35,35,255"/>
                  <prop k="outline_style" v="solid"/>
                  <prop k="outline_width" v="0"/>
                  <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="outline_width_unit" v="MM"/>
                  <prop k="scale_method" v="diameter"/>
                  <prop k="size" v="2"/>
                  <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="size_unit" v="MM"/>
                  <prop k="vertical_anchor_point" v="1"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option type="QString" value="" name="name"/>
                      <Option name="properties"/>
                      <Option type="QString" value="collection" name="type"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </background>
            <shadow shadowScale="100" shadowRadiusUnit="MM" shadowBlendMode="6" shadowOffsetUnit="MM" shadowOffsetGlobal="1" shadowColor="0,0,0,255" shadowOffsetAngle="135" shadowOpacity="0.7" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusAlphaOnly="0" shadowUnder="0" shadowDraw="0" shadowOffsetDist="1" shadowRadius="1.5"/>
            <dd_properties>
              <Option type="Map">
                <Option type="QString" value="" name="name"/>
                <Option name="properties"/>
                <Option type="QString" value="collection" name="type"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format wrapChar="" rightDirectionSymbol=">" addDirectionSymbol="0" plussign="0" reverseDirectionSymbol="0" multilineAlign="3" leftDirectionSymbol="&lt;" formatNumbers="0" autoWrapLength="0" decimals="3" placeDirectionSymbol="0" useMaxLineLengthForAutoWrap="1"/>
          <placement xOffset="0" preserveRotation="1" centroidWhole="0" maxCurvedCharAngleOut="-25" fitInPolygonOnly="0" offsetUnits="MM" placement="0" overrunDistance="0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" layerType="PointGeometry" quadOffset="4" centroidInside="0" priority="5" rotationAngle="0" maxCurvedCharAngleIn="25" overrunDistanceUnit="MM" repeatDistance="0" geometryGeneratorEnabled="0" distUnits="MM" distMapUnitScale="3x:0,0,0,0,0,0" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" placementFlags="10" repeatDistanceUnits="MM" yOffset="0" offsetType="0" geometryGeneratorType="PointGeometry" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" dist="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" geometryGenerator=""/>
          <rendering fontMaxPixelSize="10000" obstacleFactor="1" obstacle="1" drawLabels="1" scaleMax="439439" fontMinPixelSize="3" displayAll="0" zIndex="0" obstacleType="0" labelPerPart="0" minFeatureSize="0" scaleMin="0" upsidedownLabels="0" fontLimitPixelSize="0" scaleVisibility="1" mergeLines="0" limitNumLabels="0" maxNumLabels="2000"/>
          <dd_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </dd_properties>
          <callout type="simple">
            <Option type="Map">
              <Option type="QString" value="pole_of_inaccessibility" name="anchorPoint"/>
              <Option type="Map" name="ddProperties">
                <Option type="QString" value="" name="name"/>
                <Option name="properties"/>
                <Option type="QString" value="collection" name="type"/>
              </Option>
              <Option type="bool" value="false" name="drawToAllParts"/>
              <Option type="QString" value="0" name="enabled"/>
              <Option type="QString" value="&lt;symbol alpha=&quot;1&quot; type=&quot;line&quot; clip_to_extent=&quot;1&quot; force_rhr=&quot;0&quot; name=&quot;symbol&quot;>&lt;layer enabled=&quot;1&quot; class=&quot;SimpleLine&quot; pass=&quot;0&quot; locked=&quot;0&quot;>&lt;prop k=&quot;capstyle&quot; v=&quot;square&quot;/>&lt;prop k=&quot;customdash&quot; v=&quot;5;2&quot;/>&lt;prop k=&quot;customdash_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;customdash_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;draw_inside_polygon&quot; v=&quot;0&quot;/>&lt;prop k=&quot;joinstyle&quot; v=&quot;bevel&quot;/>&lt;prop k=&quot;line_color&quot; v=&quot;60,60,60,255&quot;/>&lt;prop k=&quot;line_style&quot; v=&quot;solid&quot;/>&lt;prop k=&quot;line_width&quot; v=&quot;0.3&quot;/>&lt;prop k=&quot;line_width_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;ring_filter&quot; v=&quot;0&quot;/>&lt;prop k=&quot;use_custom_dash&quot; v=&quot;0&quot;/>&lt;prop k=&quot;width_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; value=&quot;&quot; name=&quot;name&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;collection&quot; name=&quot;type&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" name="lineSymbol"/>
              <Option type="double" value="0" name="minLength"/>
              <Option type="QString" value="3x:0,0,0,0,0,0" name="minLengthMapUnitScale"/>
              <Option type="QString" value="MM" name="minLengthUnit"/>
              <Option type="double" value="0" name="offsetFromAnchor"/>
              <Option type="QString" value="3x:0,0,0,0,0,0" name="offsetFromAnchorMapUnitScale"/>
              <Option type="QString" value="MM" name="offsetFromAnchorUnit"/>
              <Option type="double" value="0" name="offsetFromLabel"/>
              <Option type="QString" value="3x:0,0,0,0,0,0" name="offsetFromLabelMapUnitScale"/>
              <Option type="QString" value="MM" name="offsetFromLabelUnit"/>
            </Option>
          </callout>
        </settings>
      </rule>
    </rules>
  </labeling>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <layerGeometryType>0</layerGeometryType>
</qgis>

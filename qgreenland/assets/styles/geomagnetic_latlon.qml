<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis hasScaleBasedVisibilityFlag="0" maxScale="0" simplifyLocal="1" minScale="1e+08" styleCategories="Symbology|Labeling|Rendering" simplifyDrawingHints="1" simplifyAlgorithm="0" simplifyMaxScale="1" version="3.10.4-A Coruña" labelsEnabled="1" simplifyDrawingTol="1">
  <renderer-v2 forceraster="0" symbollevels="0" type="singleSymbol" enableorderby="0">
    <symbols>
      <symbol alpha="1" force_rhr="0" type="line" name="0" clip_to_extent="1">
        <layer enabled="1" locked="0" pass="0" class="SimpleLine">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0,0,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.26" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
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
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style fontSizeUnit="Point" fontWeight="50" fontLetterSpacing="0" namedStyle="Normal" fieldName="to_string(Contour) || '°'" textOrientation="horizontal" fontKerning="1" fontUnderline="0" blendMode="0" fontFamily="Sans Serif" multilineHeight="1" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontWordSpacing="0" fontStrikeout="0" textOpacity="1" textColor="0,0,0,255" fontItalic="0" fontCapitals="0" isExpression="1" previewBkgrdColor="255,255,255,255" fontSize="10" useSubstitutions="0">
        <text-buffer bufferDraw="0" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferColor="255,255,255,255" bufferOpacity="1" bufferJoinStyle="128" bufferSizeUnits="MM" bufferBlendMode="0" bufferNoFill="1" bufferSize="1"/>
        <background shapeType="0" shapeOffsetY="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBlendMode="0" shapeRotation="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeSizeY="0" shapeOpacity="1" shapeOffsetX="0" shapeRotationType="0" shapeDraw="0" shapeRadiiY="0" shapeSizeX="0" shapeSizeUnit="MM" shapeBorderWidthUnit="MM" shapeBorderColor="128,128,128,255" shapeBorderWidth="0" shapeSVGFile="" shapeRadiiX="0" shapeFillColor="255,255,255,255" shapeJoinStyle="64" shapeSizeType="0" shapeOffsetUnit="MM" shapeRadiiUnit="MM" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0">
          <symbol alpha="1" force_rhr="0" type="marker" name="markerSymbol" clip_to_extent="1">
            <layer enabled="1" locked="0" pass="0" class="SimpleMarker">
              <prop v="0" k="angle"/>
              <prop v="183,72,75,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="circle" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="35,35,35,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="2" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
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
        <shadow shadowDraw="0" shadowOffsetDist="1" shadowOffsetGlobal="1" shadowRadius="1.5" shadowOpacity="0.7" shadowRadiusAlphaOnly="0" shadowOffsetAngle="135" shadowOffsetUnit="MM" shadowRadiusUnit="MM" shadowBlendMode="6" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowUnder="0" shadowColor="0,0,0,255" shadowScale="100"/>
        <dd_properties>
          <Option type="Map">
            <Option type="QString" value="" name="name"/>
            <Option name="properties"/>
            <Option type="QString" value="collection" name="type"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format leftDirectionSymbol="&lt;" placeDirectionSymbol="0" reverseDirectionSymbol="0" decimals="3" plussign="0" useMaxLineLengthForAutoWrap="1" formatNumbers="0" wrapChar="" multilineAlign="0" addDirectionSymbol="0" rightDirectionSymbol=">" autoWrapLength="0"/>
      <placement geometryGenerator="" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" quadOffset="4" geometryGeneratorEnabled="0" fitInPolygonOnly="0" maxCurvedCharAngleIn="25" offsetType="0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" centroidWhole="0" overrunDistance="0" yOffset="0" preserveRotation="1" geometryGeneratorType="PointGeometry" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" repeatDistanceUnits="MM" xOffset="0" distMapUnitScale="3x:0,0,0,0,0,0" dist="0" offsetUnits="MM" placementFlags="10" priority="5" layerType="LineGeometry" centroidInside="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" placement="2" overrunDistanceUnit="MM" rotationAngle="0" repeatDistance="0" distUnits="MM" maxCurvedCharAngleOut="-25"/>
      <rendering fontMinPixelSize="3" scaleMin="0" obstacleFactor="1" displayAll="0" limitNumLabels="0" maxNumLabels="2000" scaleMax="0" fontLimitPixelSize="0" zIndex="0" obstacle="1" mergeLines="0" labelPerPart="0" obstacleType="0" minFeatureSize="0" fontMaxPixelSize="10000" drawLabels="1" upsidedownLabels="0" scaleVisibility="0"/>
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
          <Option type="QString" value="&lt;symbol alpha=&quot;1&quot; force_rhr=&quot;0&quot; type=&quot;line&quot; name=&quot;symbol&quot; clip_to_extent=&quot;1&quot;>&lt;layer enabled=&quot;1&quot; locked=&quot;0&quot; pass=&quot;0&quot; class=&quot;SimpleLine&quot;>&lt;prop v=&quot;square&quot; k=&quot;capstyle&quot;/>&lt;prop v=&quot;5;2&quot; k=&quot;customdash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;customdash_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;customdash_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;draw_inside_polygon&quot;/>&lt;prop v=&quot;bevel&quot; k=&quot;joinstyle&quot;/>&lt;prop v=&quot;60,60,60,255&quot; k=&quot;line_color&quot;/>&lt;prop v=&quot;solid&quot; k=&quot;line_style&quot;/>&lt;prop v=&quot;0.3&quot; k=&quot;line_width&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;line_width_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;ring_filter&quot;/>&lt;prop v=&quot;0&quot; k=&quot;use_custom_dash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;width_map_unit_scale&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; value=&quot;&quot; name=&quot;name&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;collection&quot; name=&quot;type&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" name="lineSymbol"/>
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
  </labeling>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <layerGeometryType>1</layerGeometryType>
</qgis>

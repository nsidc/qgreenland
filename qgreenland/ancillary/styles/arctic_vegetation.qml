<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis hasScaleBasedVisibilityFlag="0" version="3.28.7-Firenze" maxScale="0" minScale="1e+08" styleCategories="AllStyleCategories">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
    <Private>0</Private>
  </flags>
  <temporal fetchMode="0" mode="0" enabled="0">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <elevation symbology="Line" zoffset="0" band="1" enabled="0" zscale="1">
    <data-defined-properties>
      <Option type="Map">
        <Option type="QString" value="" name="name"/>
        <Option name="properties"/>
        <Option type="QString" value="collection" name="type"/>
      </Option>
    </data-defined-properties>
    <profileLineSymbol>
      <symbol alpha="1" frame_rate="10" is_animated="0" type="line" clip_to_extent="1" force_rhr="0" name="">
        <data_defined_properties>
          <Option type="Map">
            <Option type="QString" value="" name="name"/>
            <Option name="properties"/>
            <Option type="QString" value="collection" name="type"/>
          </Option>
        </data_defined_properties>
        <layer pass="0" class="SimpleLine" locked="0" enabled="1">
          <Option type="Map">
            <Option type="QString" value="0" name="align_dash_pattern"/>
            <Option type="QString" value="square" name="capstyle"/>
            <Option type="QString" value="5;2" name="customdash"/>
            <Option type="QString" value="3x:0,0,0,0,0,0" name="customdash_map_unit_scale"/>
            <Option type="QString" value="MM" name="customdash_unit"/>
            <Option type="QString" value="0" name="dash_pattern_offset"/>
            <Option type="QString" value="3x:0,0,0,0,0,0" name="dash_pattern_offset_map_unit_scale"/>
            <Option type="QString" value="MM" name="dash_pattern_offset_unit"/>
            <Option type="QString" value="0" name="draw_inside_polygon"/>
            <Option type="QString" value="bevel" name="joinstyle"/>
            <Option type="QString" value="114,155,111,255" name="line_color"/>
            <Option type="QString" value="solid" name="line_style"/>
            <Option type="QString" value="0.6" name="line_width"/>
            <Option type="QString" value="MM" name="line_width_unit"/>
            <Option type="QString" value="0" name="offset"/>
            <Option type="QString" value="3x:0,0,0,0,0,0" name="offset_map_unit_scale"/>
            <Option type="QString" value="MM" name="offset_unit"/>
            <Option type="QString" value="0" name="ring_filter"/>
            <Option type="QString" value="0" name="trim_distance_end"/>
            <Option type="QString" value="3x:0,0,0,0,0,0" name="trim_distance_end_map_unit_scale"/>
            <Option type="QString" value="MM" name="trim_distance_end_unit"/>
            <Option type="QString" value="0" name="trim_distance_start"/>
            <Option type="QString" value="3x:0,0,0,0,0,0" name="trim_distance_start_map_unit_scale"/>
            <Option type="QString" value="MM" name="trim_distance_start_unit"/>
            <Option type="QString" value="0" name="tweak_dash_pattern_on_corners"/>
            <Option type="QString" value="0" name="use_custom_dash"/>
            <Option type="QString" value="3x:0,0,0,0,0,0" name="width_map_unit_scale"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </profileLineSymbol>
    <profileFillSymbol>
      <symbol alpha="1" frame_rate="10" is_animated="0" type="fill" clip_to_extent="1" force_rhr="0" name="">
        <data_defined_properties>
          <Option type="Map">
            <Option type="QString" value="" name="name"/>
            <Option name="properties"/>
            <Option type="QString" value="collection" name="type"/>
          </Option>
        </data_defined_properties>
        <layer pass="0" class="SimpleFill" locked="0" enabled="1">
          <Option type="Map">
            <Option type="QString" value="3x:0,0,0,0,0,0" name="border_width_map_unit_scale"/>
            <Option type="QString" value="114,155,111,255" name="color"/>
            <Option type="QString" value="bevel" name="joinstyle"/>
            <Option type="QString" value="0,0" name="offset"/>
            <Option type="QString" value="3x:0,0,0,0,0,0" name="offset_map_unit_scale"/>
            <Option type="QString" value="MM" name="offset_unit"/>
            <Option type="QString" value="35,35,35,255" name="outline_color"/>
            <Option type="QString" value="no" name="outline_style"/>
            <Option type="QString" value="0.26" name="outline_width"/>
            <Option type="QString" value="MM" name="outline_width_unit"/>
            <Option type="QString" value="solid" name="style"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </profileFillSymbol>
  </elevation>
  <customproperties>
    <Option type="Map">
      <Option type="bool" value="false" name="WMSBackgroundLayer"/>
      <Option type="bool" value="false" name="WMSPublishDataSourceUrl"/>
      <Option type="int" value="0" name="embeddedWidgets/count"/>
      <Option type="QString" value="Value" name="identify/format"/>
    </Option>
  </customproperties>
  <pipe-data-defined-properties>
    <Option type="Map">
      <Option type="QString" value="" name="name"/>
      <Option name="properties"/>
      <Option type="QString" value="collection" name="type"/>
    </Option>
  </pipe-data-defined-properties>
  <pipe>
    <provider>
      <resampling zoomedInResamplingMethod="nearestNeighbour" zoomedOutResamplingMethod="nearestNeighbour" maxOversampling="2" enabled="false"/>
    </provider>
    <rasterrenderer opacity="1" alphaBand="-1" type="paletted" band="1" nodataColor="">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <colorPalette>
        <paletteEntry alpha="255" label="B1 - Cryptogam, herb barren" color="#cdcfa8" value="1"/>
        <paletteEntry alpha="255" label="B2a - Cryptogam, barren complex" color="#939a33" value="2"/>
        <paletteEntry alpha="255" label="B3 - Non-carbonate mountain complex" color="#896f70" value="3"/>
        <paletteEntry alpha="255" label="B4 - Carbonate mountain complex" color="#706d8c" value="4"/>
        <paletteEntry alpha="255" label="B2b - Cryptogam, barren, dwarf-shrub complex" color="#a9b259" value="5"/>
        <paletteEntry alpha="255" label="G1 - Graminoid, forb, cryptogam tundra" color="#f5e8a2" value="21"/>
        <paletteEntry alpha="255" label="G2 - Graminoid, prostrate dwarf-shrub, forb, moss tundra" color="#eccc75" value="22"/>
        <paletteEntry alpha="255" label="G3 - Non-tussock sedge, dwarf-shrub, moss tundra" color="#c6b62f" value="23"/>
        <paletteEntry alpha="255" label="G4 - Tussock-sedge, dwarf-shrub, moss tundra" color="#ecec32" value="24"/>
        <paletteEntry alpha="255" label="P1 - Prostrate dwarf-shrub, herb, lichen tundra" color="#c5a1a1" value="31"/>
        <paletteEntry alpha="255" label="P2 - Prostrate/hemi-prostrate dwarf-shrub, lichen tundra" color="#ba828d" value="32"/>
        <paletteEntry alpha="255" label="S1 - Erect dwarf-shrub, moss tundra" color="#9ac339" value="33"/>
        <paletteEntry alpha="255" label="S2 - Low-shrub, moss tundra" color="#599a3e" value="34"/>
        <paletteEntry alpha="255" label="W1 - Sedge/grass, moss wetland complex" color="#aacea8" value="41"/>
        <paletteEntry alpha="255" label="W2 - Sedge, moss, dwarf-shrub wetland complex" color="#9ac8bd" value="42"/>
        <paletteEntry alpha="255" label="W3 - Sedge, moss, low-shrub wetland complex" color="#74b289" value="43"/>
        <paletteEntry alpha="255" label="FW - Fresh water" color="#4656a3" value="91"/>
        <paletteEntry alpha="255" label="SW - Saline water" color="#bbc4e5" value="92"/>
        <paletteEntry alpha="255" label="GL - Glacier" color="#ffffff" value="93"/>
        <paletteEntry alpha="255" label="NA - Non-Arctic" color="#f6e9b5" value="99"/>
      </colorPalette>
      <colorramp type="gradient" name="[source]">
        <Option type="Map">
          <Option type="QString" value="215,25,28,255" name="color1"/>
          <Option type="QString" value="43,131,186,255" name="color2"/>
          <Option type="QString" value="ccw" name="direction"/>
          <Option type="QString" value="0" name="discrete"/>
          <Option type="QString" value="gradient" name="rampType"/>
          <Option type="QString" value="rgb" name="spec"/>
          <Option type="QString" value="0.25;253,174,97,255;rgb;ccw:0.5;255,255,191,255;rgb;ccw:0.75;171,221,164,255;rgb;ccw" name="stops"/>
        </Option>
      </colorramp>
    </rasterrenderer>
    <brightnesscontrast contrast="0" gamma="1" brightness="0"/>
    <huesaturation colorizeOn="0" colorizeStrength="100" saturation="0" colorizeBlue="128" colorizeGreen="128" invertColors="0" colorizeRed="255" grayscaleMode="0"/>
    <rasterresampler maxOversampling="2"/>
    <resamplingStage>resamplingFilter</resamplingStage>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

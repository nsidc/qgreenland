<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="3.10.7-A Coruña" maxScale="0" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" minScale="1e+08">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <customproperties>
    <property value="false" key="WMSBackgroundLayer"/>
    <property value="false" key="WMSPublishDataSourceUrl"/>
    <property value="0" key="embeddedWidgets/count"/>
    <property value="Value" key="identify/format"/>
  </customproperties>
  <pipe>
    <rasterrenderer band="1" alphaBand="-1" type="paletted" opacity="1">
      <rasterTransparency>
        <singleValuePixelList>
          <pixelListEntry percentTransparent="100" min="23" max="25"/>
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
      <colorPalette>
        <paletteEntry alpha="255" value="1" color="#b15928" label="Continuous permafrost extent with high ground ice content and thick overburden"/>
        <paletteEntry alpha="255" value="5" color="#ffff99" label="Continuous permafrost extent with medium ground ice content and thick overburden"/>
        <paletteEntry alpha="255" value="13" color="#6a3d9a" label="Continuous permafrost extent with high ground ice content and thin overburden and exposed bedrock"/>
        <paletteEntry alpha="255" value="15" color="#ff7f00" label="Sporadic permafrost extent with high ground ice content and thin overburden and exposed bedrock"/>
        <paletteEntry alpha="255" value="17" color="#fdbf6f" label="Continuous permafrost extent with low ground ice content and thin overburden and exposed bedrock"/>
        <paletteEntry alpha="255" value="18" color="#e31a1c" label="Discontinuous permafrost extent with low ground ice content and thin overburden and exposed bedrock"/>
        <paletteEntry alpha="255" value="20" color="#33a02c" label="Isolated patches of permafrost extent with low ground ice content and thin overburden and exposed bedrock"/>
        <paletteEntry alpha="255" value="21" color="#b2df8a" label="Glaciers"/>
        <paletteEntry alpha="255" value="24" color="#1f78b4" label="Ocean/inland seas"/>
        <paletteEntry alpha="255" value="25" color="#a6cee3" label="Land"/>
      </colorPalette>
      <colorramp name="[source]" type="colorbrewer">
        <prop k="colors" v="12"/>
        <prop k="inverted" v="1"/>
        <prop k="rampType" v="colorbrewer"/>
        <prop k="schemeName" v="Paired"/>
      </colorramp>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0"/>
    <huesaturation saturation="0" colorizeRed="255" grayscaleMode="0" colorizeOn="0" colorizeStrength="100" colorizeGreen="128" colorizeBlue="128"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

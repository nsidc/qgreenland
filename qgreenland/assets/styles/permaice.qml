<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="1e+08" version="3.10.7-A Coruña" maxScale="0" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0">
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
    <rasterrenderer type="paletted" alphaBand="-1" band="1" opacity="1">
      <rasterTransparency>
        <singleValuePixelList>
          <pixelListEntry min="23" max="25" percentTransparent="100"/>
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
        <paletteEntry color="#66c8d7" label="Continuous permafrost extent with high ground ice content and thick overburden" alpha="255" value="1"/>
        <paletteEntry color="#c7db7e" label="Discontinuous permafrost extent with high ground ice content and thick overburden" alpha="255" value="2"/>
        <paletteEntry color="#cac71f" label="Sporadic permafrost extent with high ground ice content and thick overburden" alpha="255" value="3"/>
        <paletteEntry color="#63c88d" label="Isolated patches of permafrost extent with high ground ice content and thick overburden" alpha="255" value="4"/>
        <paletteEntry color="#b717de" label="Continuous permafrost extent with medium ground ice content and thick overburden" alpha="255" value="5"/>
        <paletteEntry color="#37e22b" label="Discontinuous permafrost extent with medium ground ice content and thick overburden" alpha="255" value="6"/>
        <paletteEntry color="#304adc" label="Sporadic permafrost extent with medium ground ice content and thick overburden" alpha="255" value="7"/>
        <paletteEntry color="#56aee1" label="Isolated patches of permafrost extent with medium ground ice content and thick overburden" alpha="255" value="8"/>
        <paletteEntry color="#a766d8" label="Continuous permafrost extent with low ground ice content and thick overburden" alpha="255" value="9"/>
        <paletteEntry color="#db7c7b" label="Discontinuous permafrost extent with low ground ice content and thick overburden" alpha="255" value="10"/>
        <paletteEntry color="#98e835" label="Sporadic permafrost extent with low ground ice content and thick overburden" alpha="255" value="11"/>
        <paletteEntry color="#cf2c78" label="Isolated patches of permafrost extent with low ground ice content and thick overburden" alpha="255" value="12"/>
        <paletteEntry color="#91eee5" label="Continuous permafrost extent with high ground ice content and thin overburden and exposed bedrock" alpha="255" value="13"/>
        <paletteEntry color="#5a4de1" label="Discontinuous permafrost extent with high ground ice content and thin overburden and exposed bedrock" alpha="255" value="14"/>
        <paletteEntry color="#e40ea4" label="Sporadic permafrost extent with high ground ice content and thin overburden and exposed bedrock" alpha="255" value="15"/>
        <paletteEntry color="#78d2b3" label="Isolated patches of permafrost extent with high ground ice content and thin overburden and exposed bedrock" alpha="255" value="16"/>
        <paletteEntry color="#e3b943" label="Continuous permafrost extent with low ground ice content and thin overburden and exposed bedrock" alpha="255" value="17"/>
        <paletteEntry color="#5c1fd4" label="Discontinuous permafrost extent with low ground ice content and thin overburden and exposed bedrock" alpha="255" value="18"/>
        <paletteEntry color="#df8c6d" label="Sporadic permafrost extent with low ground ice content and thin overburden and exposed bedrock" alpha="255" value="19"/>
        <paletteEntry color="#e54ede" label="Isolated patches of permafrost extent with low ground ice content and thin overburden and exposed bedrock" alpha="255" value="20"/>
        <paletteEntry color="#e29b54" label="Glaciers" alpha="255" value="21"/>
        <paletteEntry color="#68cf3c" label="Relict permafrost" alpha="255" value="22"/>
        <paletteEntry color="#5ae771" label="Inland lakes" alpha="255" value="23"/>
        <paletteEntry color="#367ae7" label="Ocean/inland seas" alpha="255" value="24"/>
        <paletteEntry color="#ca4764" label="Land" alpha="255" value="25"/>
      </colorPalette>
      <colorramp type="randomcolors" name="[source]"/>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0"/>
    <huesaturation colorizeGreen="128" colorizeStrength="100" colorizeBlue="128" saturation="0" colorizeOn="0" grayscaleMode="0" colorizeRed="255"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

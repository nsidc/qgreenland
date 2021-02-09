<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="1e+08" version="3.10.4-A Coruña" hasScaleBasedVisibilityFlag="0" maxScale="0" styleCategories="AllStyleCategories">
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
    <rasterrenderer band="1" type="paletted" opacity="1" alphaBand="-1">
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
        <paletteEntry label="0" value="0" color="#2b83ba" alpha="255"/>
        <paletteEntry label="1" value="1" color="#abdda4" alpha="255"/>
        <paletteEntry label="2" value="2" color="#fdae61" alpha="255"/>
        <paletteEntry label="3" value="3" color="#d7191c" alpha="255"/>
      </colorPalette>
      <colorramp name="[source]" type="colorbrewer">
        <prop k="colors" v="5"/>
        <prop k="inverted" v="1"/>
        <prop k="rampType" v="colorbrewer"/>
        <prop k="schemeName" v="Spectral"/>
      </colorramp>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0"/>
    <huesaturation colorizeOn="0" colorizeStrength="100" saturation="0" colorizeRed="255" colorizeBlue="128" colorizeGreen="128" grayscaleMode="0"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>

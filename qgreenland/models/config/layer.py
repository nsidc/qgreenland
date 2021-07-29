class ConfigLayer:
    id: str

    # The layer name in QGIS layers panel:
    title: str

    # Descriptive text:
    description: str

    hierarchy: List[str]
    # in_package: bool


    # Is this layer initially "checked" as visible in QGIS?:
    show: bool

    # Which style (.qml) file to use for this layer?
    style: str
    
    input: ConfigLayerInput

    steps: List[ConfigLayerStep]


class ConfigLayerInput:
    # TODO: De-reference?
    # Reference
    dataset: str
    # Reference
    asset: str

# Require a _subtype_ of ConfigDatasetAsset
VariableAsset = TypeVar('VariableAsset', bound=ConfigDatasetAsset)


class ConfigDataset:
    id: str
    assets: List[VariableAsset]
    metadata: ConfigDatasetMetadata


class ConfigDatasetMetadata:
    title: str
    abstract: str
    citation: ConfigDatasetCitation


class ConfigDatasetCitation:
    text: str
    url: str


class ConfigDatasetAsset:
    id: str


class ConfigDatasetHttpAsset(ConfigDatasetAsset):
    urls: List[str]

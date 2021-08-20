package Datasets

#Citation: {
  text: string
  url: string
}
#DatasetMetadata: {
  title: string
  abstract: string
  citation: #Citation
}
// What's wrong with this? Looks like this represents a struct like:
// { foo: { id: ... }, bar: { id: ... }, }
// But how do we extract the inner struct into a template?
#DatasetAsset: {
  id: string
  ...
}
#HttpDatasetAsset: #DatasetAsset & {
  type: "http"
  urls: [...string]
}
#Dataset: {
  id: string
  assets: [AssetId=_]: #DatasetAsset & {
    id: AssetId
  }
  metadata: #DatasetMetadata
}

datasets: [DatasetId=_]: #Dataset & {
  id: DatasetId
}

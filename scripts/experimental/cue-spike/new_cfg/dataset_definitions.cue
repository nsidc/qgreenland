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
#DatasetAsset: [Id=_]: {
  id: Id
  ...
}
#HttpDatasetAsset: #DatasetAsset & {
  type: "http"
  urls: [...string]
}
#Dataset: {
  id: string
  assets: #DatasetAsset
  metadata: #DatasetMetadata
}

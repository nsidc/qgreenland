package Layers

import "nsidc.org/qgreenland:Datasets"

#Step: {
  ...
}
#CommandStep: #Step & {
  args: [...string]
}
#Input: {
  dataset: Datasets.#Dataset
  asset: Datasets.#DatasetAsset
}
#Layer: {
  id: string
  title: string
  hierarchy: [...string]
  description: string
  show: bool
  style?: string
  input: #Input
  steps: [...#Step]

}
layers: [LayerId=_]: #Layer & {
  id: LayerId
}

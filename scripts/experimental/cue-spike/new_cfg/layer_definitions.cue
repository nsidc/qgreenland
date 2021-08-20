package Layers

import (
  "nsidc.org/qgreenland:Datasets"
  "nsidc.org/qgreenland:Steps"
)

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
  steps: [...Steps.#Step]

}
layers: [LayerId=_]: #Layer & {
  id: LayerId
}

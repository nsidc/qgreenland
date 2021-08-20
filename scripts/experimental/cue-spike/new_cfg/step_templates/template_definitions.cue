package Templates

import "nsidc.org/qgreenland:Steps"

// TODO: Move input file and output file to "#Step"?
#Template: {
  inputFile: string
  outputFile: string
  ...

  steps: [...Steps.#Step]
}
#templates: [TemplateId=_]: #Template & {
  id: TemplateId
}

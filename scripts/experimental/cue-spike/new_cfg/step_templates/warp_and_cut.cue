package Templates

import "nsidc.org/qgreenland:Steps"

#templates: {
  warp_and_cut: #Template & {
    crs: string
    targetExtent: string
    cutFilePath: string
    inputFile: string
    outputFile: string

    steps: [
      Steps.#CommandStep & {
        args: [
          "gdalwarp",
          "-t_srs",
          crs,
          "-tr",
          "500",
          "500",
          "-te",
          targetExtent,
          "-dstnodata",
          "0",
          "-wo",
          "SOURCE_EXTRA=100",
          "-wo",
          "SAMPLE_GRID=YES",
          inputFile,
          "{output_dir}/warped.tif",
        ]
      },
      Steps.#CommandStep & {
        args: [
          "gdalwarp",
          "-cutline",
          cutFilePath,
          "-crop_to_cutline",
          "-co",
          "COMPRESS=DEFLATE",
          "{input_dir}/warped.tif",
          outputFile,
        ]
      },
    ]
  },
}

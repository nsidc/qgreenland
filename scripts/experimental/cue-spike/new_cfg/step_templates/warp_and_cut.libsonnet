local steps = import '../steps.libsonnet';

{
  warpAndCut: {
    inputFile:: error 'Must override "inputFile"',
    outputFile:: error 'Must override "outputFile"',
    crs:: error 'Must override "crs"',
    targetExtent:: error 'must override "targetExtent"',
    cutFilePath:: error 'must oevrride "cutFilePath"',

    local template = self,

    steps: [
      steps.CommandStep {
        args: [ 
          "gdalwarp",
          "-t_srs",
          template.crs,
          "-tr",
          "500",
          "500",
          "-te",
          template.targetExtent,
          "-dstnodata",
          "0",
          "-wo",
          "SOURCE_EXTRA=100",
          "-wo",
          "SAMPLE_GRID=YES",
          template.inputFile,
          "{output_dir}/warped.tif",
        ],
      },
      steps.CommandStep {
        args: [ 
          "gdalwarp",
          "-cutline",
          template.cutFilePath,
          "-crop_to_cutline",
          "-co",
          "COMPRESS=DEFLATE",
          "{input_dir}/warped.tif",
          template.outputFile,
        ],
      },
    ],
  },
}

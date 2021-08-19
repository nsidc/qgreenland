local datasets = (import 'datasets.jsonnet').datasets;
local steps = import 'steps.libsonnet';

{
  datasets: datasets,
  layers: {
    background: {
      id: 'background',
      title: 'Background (500m)',
      hierarchy: ['Basemaps'],
      description: "Stylized shaded-relief map for providing a general sense of geography.",
      show: true,
      style: null,
      input: {
        dataset: datasets.background,
        asset: datasets.background.assets.high_res,
      },
      steps: [
        steps.CommandStep {
          args: [ 
            "unzip",
            "{input_dir}/*.zip",
            "-d",
            "{output_dir}",
          ],
        },
        steps.CommandStep {
          args: [ 
            "gdalwarp",
            "-t_srs",
            "EPSG:3413",
            "-tr",
            "500",
            "500",
            "-te",
            "-5774572.727595 -5774572.727595 5774572.727595 5774572.727595",
            "-dstnodata",
            "0",
            "-wo",
            "SOURCE_EXTRA=100",
            "-wo",
            "SAMPLE_GRID=YES",
            "{input_dir}/NE2_HR_LC_SR_W/NE2_HR_LC_SR_W.tif",
            "{output_dir}/warped.tif",
          ],
        },
        steps.CommandStep {
          args: [ 
            "gdalwarp",
            "-cutline",
            "{assets_dir}/latitude_shape_40_degrees.geojson",
            "-crop_to_cutline",
            "-co",
            "COMPRESS=DEFLATE",
            "{input_dir}/warped.tif",
            "{output_dir}/warped_and_cut.tif",
          ],
        },
        steps.CommandStep {
          args: [ 
            "cp",
            "{input_dir}/warped_and_cut.tif",
            "{output_dir}/overviews.tif",
            "&&",
            "gdaladdo",
            "-r",
            "average",
            "{output_dir}/overviews.tif",
            "2",
            "4",
            "8",
            "16",
          ],
        },
      ],
    },
  },
}

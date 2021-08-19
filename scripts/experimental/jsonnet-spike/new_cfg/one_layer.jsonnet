local datasets = (import 'datasets.jsonnet').datasets;

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
      },
   },
}

local datasets = (import 'datasets.jsonnet').datasets;

{
  'datasets': datasets,
  'layers': {
      'background': {
        'id': 'background',
        'title': 'Background (500)m',
        'input': {
          'dataset': datasets.background,
          'asset': datasets.background.assets.high_res,
        },
      },
   },
}

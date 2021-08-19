local asset_types = {
  http: 'http',
  cmr: 'cmr',
  # ...
};

{
  datasets: {
    background: {
      id: 'background',
      assets: {
        high_res: {
          id: 'high_res',
          type: asset_types.http,
          urls: [
            'https://naciscdn.org/naturalearth/10m/raster/NE2_HR_LC_SR_W.zip',
          ],
        },
        low_res: {
          id: 'low_res',
          type: asset_types.http,
          urls: [
            'https://naciscdn.org/naturalearth/10m/raster/NE2_LR_LC_SR_W.zip',
          ],
        },
      },
      metadata: {
        title: "Natural Earth II with Shaded Relief and Water (1:10m)",
        abstract: "Natural Earth II (Public Domain)",
        citation: {
          text: "Made with Natural Earth",
          url: "https://github.com/nvkelso/natural-earth-vector/blob/master/LICENSE.md",
        },
      },
    },
  },
}

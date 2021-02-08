from qgreenland.tasks.common.fetch import FetchLocalDataFiles
from qgreenland.tasks.common.raster import BuildRasterOverviews
from qgreenland.util.luigi import LayerPipeline


class DmsGtkTopo(LayerPipeline):
    """Topo map from the Danish Agency for Map Supply and Efficiency.

    This dataset uses an internal colormap with the `byte` data type. Using a
    typical raster processing pipeline with gdal warp prduces a raster the size
    of the cutline, and yields out of extent values that cannot be easily masked
    (made transparent). Just get the source as-is and use it in qgreenland. This
    is in a slightly different projection, but it looks much better than warping
    to EPSG:3413. We could convert this into an RGBA raster, but that brings the
    filesize from 54M to 16G.
    """

    def requires(self):
        fetch = FetchLocalDataFiles(
            source_cfg=self.cfg['source'],
            dataset_cfg=self.cfg['dataset']
        )  # ->
        return BuildRasterOverviews(
            requires_task=fetch,
            layer_id=self.layer_id
        )

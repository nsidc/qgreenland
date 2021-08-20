from functools import cached_property
from typing import Dict

from pydantic import FilePath, validator
import fiona

from qgreenland.models.base_model import QgrBaseModel


class BoundingBox(QgrBaseModel):
    min_x: float
    min_y: float
    max_x: float
    max_y: float


class ConfigBoundariesInfo(QgrBaseModel):
    fp: FilePath
    bbox: BoundingBox = None

    @validator('bbox', pre=True, always=True)
    def calculate_bbox(cls, value, values) -> BoundingBox:
        if 'fp' not in values or not values['fp']:
            raise RuntimeError('No u gotta')

        fp = values['fp']

        with fiona.open(fp) as ifile:
            features = list(ifile)
            meta = ifile.meta
            bbox = ifile.bounds

        if (feature_count := len(features)) != 1:
            raise exc.QgrInvalidConfigError(
                f'Configured boundary {boundary_name} contains the wrong'
                f' number of features. Expected 1, got {feature_count}.',
            )

        # TODO: fix.
        # if (boundary_crs := meta['crs']['init'].lower()) \
        #    != (project_crs := cfg['project']['crs'].lower()):
        #     raise exc.QgrInvalidConfigError(
        #         f'Expected CRS of boundary file {fp} ({boundary_crs}) to'
        #         f' match project CRS ({project_crs}).',
        #     )

        return BoundingBox(
            min_x=bbox[0],
            min_y=bbox[1],
            max_x=bbox[2],
            max_y=bbox[3],
        )


class ConfigProject(QgrBaseModel):
    crs: str
    boundaries: Dict[str, ConfigBoundariesInfo]

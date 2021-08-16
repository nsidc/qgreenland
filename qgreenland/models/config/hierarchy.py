from typing import List

from pydantic import validator

from qgreenland.models.base_model import QgrBaseModel


# TODO: maybe hierarchy config should just be a list of Hierarchy settings?
class HierarchySettings(QgrBaseModel):
    path: List[str]
    show: bool = False
    expand: bool = False

    @validator('path', pre=True)
    @classmethod
    # TODO: Remove classmethod decorator?
    # https://github.com/samuelcolvin/pydantic/issues/1415#issuecomment-617809543
    def path_str_to_list(cls, value):
        return value.split('/')


# class ConfigHierarchy(BaseModel):
#     # TODO : How to represent unknown keys? This is a mapping between paths and
#     # settings. Maybe it makes most sense to leave this as a dict of HierarchySettings?
#     __root__: Dict[str, HierarchySettings]
#
#     def __getitem__(self, item):
#         return self.__root__[item]

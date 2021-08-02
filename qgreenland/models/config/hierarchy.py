from typing import Dict

from pydantic import BaseModel


# TODO: maybe hierarchy config should just be a list of Hierarchy settings?
class HierarchySettings(BaseModel):
    path: str
    show: bool
    expand: bool


# class ConfigHierarchy(BaseModel):
#     # TODO : How to represent unknown keys? This is a mapping between paths and
#     # settings. Maybe it makes most sense to leave this as a dict of HierarchySettings?
#     __root__: Dict[str, HierarchySettings]
#
#     def __getitem__(self, item):
#         return self.__root__[item]

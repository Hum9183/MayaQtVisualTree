# -*- coding: utf-8 -*-
from maya import cmds

from .utils.readonly_meta import ReadonlyMeta


class Const(metaclass=ReadonlyMeta):
    TOOL_NAME: str = 'QtVisualTree'
    TOOL_TITLE: str = 'Qt Visual Tree'
    TOOL_VERSION: str = '0.1.0'

    maya_major_ver = int(cmds.about(version=True))

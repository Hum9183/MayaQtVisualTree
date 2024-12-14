# -*- coding: utf-8 -*-
import traceback
from textwrap import dedent

from maya import cmds


def __register_qtvisualtree_startup():
    # TODO: Py2の場合は「Not Supported」みたいなmenuitemを追加するようにする
    cmd = dedent(
        """
        import qtvisualtree.startup
        qtvisualtree.startup.main()
        """)
    cmds.evalDeferred(cmd)


if __name__ == '__main__':
    try:
        __register_qtvisualtree_startup()

    except Exception:
        traceback.print_exc()

# -*- coding: utf-8 -*-
from maya import OpenMayaUI as omui
from maya import cmds

try:
    from PySide6.QtWidgets import QApplication, QWidget
    from shiboken6 import wrapInstance
except ImportError:
    from PySide2.QtWidgets import QApplication, QWidget
    from shiboken2 import wrapInstance

from .window import generate, QtVisualTreeMainWindow


def restart() -> None:
    """開発用(再起動用)"""
    if omui.MQtUtil.findControl(QtVisualTreeMainWindow.name):
        cmds.deleteUI(QtVisualTreeMainWindow.workspace_control, control=True)
    window = generate()
    window.show()


def restore() -> None:
    ptr = omui.MQtUtil.findControl(QtVisualTreeMainWindow.name)
    if ptr is None:
        _ = generate(keep_instance=True)
        ptr = omui.MQtUtil.findControl(QtVisualTreeMainWindow.name)
    restored_control = omui.MQtUtil.findControl(QtVisualTreeMainWindow.workspace_control)
    omui.MQtUtil.addWidgetToMayaLayout(int(ptr), int(restored_control))


def start() -> None:
    ptr = omui.MQtUtil.findControl(QtVisualTreeMainWindow.name)
    if ptr is None:
        window = generate()
        window.show()
    else:
        window = wrapInstance(int(ptr), QtVisualTreeMainWindow)
        if window.isVisible() is False:
            window.setVisible(True)
        cmds.setFocus(QtVisualTreeMainWindow.name)

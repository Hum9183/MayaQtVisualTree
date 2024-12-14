# -*- coding: utf-8 -*-
import inspect
from textwrap import dedent

from maya import cmds, mel

from .const import Const
from .run_scripts import start


def main():
    mel.eval('''
    buildViewMenu MayaWindow|mainWindowMenu;
    setParent -menu "MayaWindow|mainWindowMenu";
    ''')

    cmds.menuItem(divider=True)

    start_script_str = inspect.getsource(start)
    cmds.menuItem(
        Const.TOOL_NAME,
        label=Const.TOOL_NAME,
        annotation='Run {}'.format(Const.TOOL_NAME),
        echoCommand=True,
        command=dedent(start_script_str))

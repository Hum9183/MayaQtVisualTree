# -*- coding: utf-8 -*-
from maya import cmds


# TODO: Window内に出したい
def show(message):
    highlighted_msg: any = u'<hl>{}</hl>'.format(message)
    cmds.inViewMessage(amg=highlighted_msg, pos='botCenter', fade=True)

# -*- coding: utf-8 -*-


def restart_qtvisualtree():
    from qtvisualtree import run, module_reloader
    module_reloader.deep_reload(run, 'qtvisualtree')
    run.restart()


if __name__ == '__main__':
    restart_qtvisualtree()

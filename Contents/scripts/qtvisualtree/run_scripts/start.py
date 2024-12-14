# -*- coding: utf-8 -*-


def start_qtvisualtree():
    # WARNING:
    # startではreloadは行わない。
    # reloadしたい場合は「Dev」=>「Restart」を実行する
    from qtvisualtree import run
    run.start()


if __name__ == '__main__':
    start_qtvisualtree()

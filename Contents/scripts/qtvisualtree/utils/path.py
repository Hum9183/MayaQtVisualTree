# -*- coding: utf-8 -*-
import os


def combine(paths):
    """パスのlistを結合し、パスを返す。

    Args:
        paths (list[str]): パスのlist

    Returns:
        str: \で結合したパス。
    """
    return '/'.join(paths)


def create_directory(path):
    """ディレクトリを作成する。中間ディレクトリもすべて作成する。

    Args:
        path (str): 作成するディレクトリのパス
    """
    if os.path.isdir(path):
        return

    folder_names = path.split('/')

    # すべてのディレクトリパスのリストを作成
    folder_paths = []
    for _ in range(len(folder_names)):
        folder_path = combine(folder_names)
        folder_paths.append(folder_path)
        del folder_names[-1]

    # ディレクトリ作成
    for _folder_path in reversed(folder_paths):
        if os.path.isdir(_folder_path) is False:
            os.mkdir(_folder_path)

# -*- coding: utf-8 -*-
from typing import Tuple, Any


def try_get_item(list_, index) -> Tuple[Any, bool]:
    """listへのgetitemを試みる。IndexErrorがraiseされた場合はFalseが返る

    Args:
        list_ (list[any]): リスト
        index (int): getitemしたいインデックス

    Returns:
        element, success (any, bool): 要素、getitemが成功したかどうか
    """
    if list_ is False:
        return None, False

    try:
        return list_[index], True
    except IndexError:
        return None, False

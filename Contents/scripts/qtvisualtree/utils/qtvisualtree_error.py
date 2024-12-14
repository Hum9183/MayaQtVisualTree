# -*- coding: utf-8 -*-
import functools

from . import inview_message
from .log import Log


class QtVisualTreeError(Exception):
    @staticmethod
    def catch(function):
        """QtVisualTreeErrorを検知するデコレータ"""

        @functools.wraps(function)
        def wrapper(*args, **keywords):
            try:
                return_value = function(*args, **keywords)
            except QtVisualTreeError as e:
                e.__log()
                return
            return return_value

        return wrapper

    def __log(self):
        Log.log(self)
        inview_message.show(self)

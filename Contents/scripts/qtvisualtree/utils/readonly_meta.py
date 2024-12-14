# -*- coding: utf-8 -*-
import inspect
from textwrap import dedent


class ReadonlyMeta(type):
    def __setattr__(self, name, value):
        if name in self.__dict__.keys():
            file_name = inspect.stack()[1].filename
            func_name = inspect.stack()[1].function
            raise RebindError(get_waring_str(
                file_name, func_name, name, value))
        else:
            self.__dict__[name] = value


def get_waring_str(file_name, func_name, attr_name, attr_value):
    return u'Rebind Error' + dedent(
        u"""
            # Rebind Error: Classes inheriting from ReadonlyMeta cannot rebind attribute.
            # Info:
            #   File...'{}' 
            #   Function...'{}' 
            #   Attribute...'{}' 
            #   Value...'{}'
            ////////////////////////// Rebind Error ///////////////////////////
            // Classes inheriting from ReadonlyMeta cannot rebind attribute. //
            ///////////////////////////////////////////////////////////////////
        """.format(file_name, func_name, attr_name, attr_value))


class RebindError(Exception):
    pass

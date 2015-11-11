# -*- coding: utf-8 -*-
import importlib


def load(_str):
    module_name, class_name = _str.rsplit(".", 1)
    return getattr(importlib.import_module(module_name), class_name, None)()

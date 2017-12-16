#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: manager.py
@time: 2017/12/16
"""
import importlib
import logging

from tornado_middleware.config import MIDDLEWARE_CLASSES


class MiddlewareManager(object):
    def __init__(self, handler):
        self.handler = handler
        self.request_middlewares = []
        self.response_middlewares = []
        for middleware_class in MIDDLEWARE_CLASSES:
            module_name, class_name = self.get_module_class_name(middleware_class)
            try:
                mod = importlib.import_module(module_name)
            except Exception as e:
                logging.error('module import error: {}'.format(e), exc_info=True)
                continue

            try:
                cls = getattr(mod, class_name)
                inst = cls(self.handler)
                if hasattr(inst, 'request_hook'):
                    self.request_middlewares.append(inst)
                if hasattr(inst, 'response_hook'):
                    self.response_middlewares.append(inst)
            except AttributeError as e:
                logging.warn("class instance error: {0}".format(e), exc_info=1)

    def run_request_hooks(self):
        for middleware in self.request_middlewares:
            try:
                middleware.request_hook()
            except Exception as e:
                logging.warn(e, exc_info=True)

    def run_response_hooks(self, chunk):
        for middleware in self.response_middlewares:
            try:
                middleware.response_hook(chunk)
            except Exception as e:
                logging.warn(e, exc_info=True)

    def get_module_class_name(self, class_path):
        try:
            pos = class_path.rindex('.')
        except ValueError:
            raise Exception('%s is invalid' % class_path)
        return class_path[:pos], class_path[pos + 1:]

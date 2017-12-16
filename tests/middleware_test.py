#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: middleware_test.py
@time: 2017/12/16
"""

from tornado_middleware.middleware.manager import MiddlewareManager

if __name__ == '__main__':
    middleware_manager = MiddlewareManager('test')
    middleware_manager.run_request_hooks()

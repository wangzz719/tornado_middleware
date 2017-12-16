#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: helloworld.py
@time: 2017/12/16
"""
import time
from tornado_middleware.handlers.base import BaseHandler


class HelloWorldHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.write(dict(hello=int(time.time())))

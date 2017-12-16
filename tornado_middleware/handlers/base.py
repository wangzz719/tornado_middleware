#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: base.py
@time: 2017/12/16
"""

from tornado.web import RequestHandler
from tornado_middleware.middleware.manager import MiddlewareManager


class BaseHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        RequestHandler.__init__(self, application, request, **kwargs)
        # add middleware
        self.middleware_manager = MiddlewareManager(self)

    def prepare(self):
        self.middleware_manager.run_request_hooks()

    def finish(self, chunk=None):
        self._chunk = chunk
        self.middleware_manager.run_response_hooks(self._chunk)
        rtn_content = b''.join(self._write_buffer)
        if chunk is not None:
            rtn_content += str(chunk)
        self.set_header("Content-Type", "application/json; charset=utf-8")
        if self._auto_finish and not self._finished:
            RequestHandler.finish(self, self._chunk)

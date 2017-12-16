#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: log.py
@time: 2017/12/16
"""
import json
import logging


class LogMiddleware(object):
    def __init__(self, handler):
        self.handler = handler

    def request_hook(self):
        logging.info('header: {}'.format(self.handler.request.headers))

    def response_hook(self, chunk):
        rtn_content = b''.join(self.handler._write_buffer)
        logging.info('return_content: {}'.format(rtn_content) )
        rtn_content = json.loads(rtn_content)
        rtn_content['path'] = self.handler.request.path
        self.handler._write_buffer = [json.dumps(rtn_content)]
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: app.py
@time: 2017/12/16
"""
import logging
import tornado.ioloop
import tornado.web

from tornado_middleware.handlers.helloworld import HelloWorldHandler

FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

def make_app():
    handlers = [
        (r"/hello", HelloWorldHandler),
    ]
    return tornado.web.Application(handlers)

def run():
    app = make_app()
    app.listen(19090)
    tornado.ioloop.IOLoop.current().start()
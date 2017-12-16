#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: wangzhizhao
@contact: wzhizhao@gmail.com
@file: setup.py.py
@time: 2017/12/16
"""

from setuptools import find_packages, setup

setup(name='tornado_middleware',
      version='0.0.1',
      author='wangzhizhao',
      author_email='wzhizhao@gmail.com',
      description='',
      license='PRIVATE',
      packages=find_packages(),
      install_requires=[
          'tornado',
      ],
      entry_points={
          'console_scripts': [
              'middleware_web = tornado_middleware.app:run'
          ],
      })

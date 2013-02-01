#!/usr/bin/env python
#-*- coding:utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='doiclient',
      version='0.1',
      description='Python API to resolve DOI®',
      author='Jonathan Barnoud',
      author_email='jonathan@barnoud.net',
      packages=['doiclient'],
      install_requires=['requests'],
     )

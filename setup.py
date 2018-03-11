#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4 colorcolumn=80 expandtab

from setuptools import setup

setup(
    name='gitpath',
    version='0.1',
    description='After import this module, you can import library etc.',
    author='Zhuo Yin',
    author_email='zhuoyin@gmail.com',
    packages=['gitpath'],
    install_requires=['gitpython'],
)

# -*- coding: utf-8 -*-

name = 'pyblish_lite'

version = '0.8.13'

description = \
    """
    Lightweight graphical user interface to Pyblish
    """

authors = ['Abstract Factory and Contributors marcus@abstractfactory.com']

requires = ['python-3+<4']


def commands():
    env.PYTHONPATH.append('{root}')

help = [['Home Page', 'https://github.com/pyblish/pyblish-lite']]

# -*- coding: utf-8 -*-
# This file was auto-generated by pysh.
# Don't edit this by hand.
import pysh.shell.runner






filename = "for_test"


f = open("setup.py","w")

str = """
##### setup.py

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension('""" + filename + """', ['""" + filename + """.pyx'])]   #assign new.pyx module in setup.py.

setup(name        = '""" + filename + """ app',cmdclass    = {'build_ext':build_ext},ext_modules = ext_modules)

##### end
"""
for i in xrange(2):
    pass
print(str, file="setup.py")





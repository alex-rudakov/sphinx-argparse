from distutils.version import StrictVersion
import os
from setuptools import setup
# from tests import PyTest
import sys

deps = ["sphinx"]

# argparse was added to python stdlib since 2.7
if StrictVersion(sys.version.split(' ')[0]) < StrictVersion('2.7.0'):
    deps.append('argparse')

setup(
    name='sphinx-argparse',
    version='0.1.7',
    packages=[
        'sphinxarg',
    ],

    url='',
    license='MIT',
    author='Aleksandr Rudakov',
    author_email='ribozz@gmail.com',
    description='Sphinx extension that automatically document argparse commands and options',
    long_description='',
    install_requires=deps,

    extras_require={
        'dev': ['pytest'],
    }
)

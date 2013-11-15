import os
from setuptools import setup
# from tests import PyTest

setup(
    name='sphinx-argparse',
    version='0.1.4',
    packages=[
        'sphinxarg',
    ],

    url='',
    license='MIT',
    author='Aleksandr Rudakov',
    author_email='ribozz@gmail.com',
    description='Sphinx extension that automatically document argparse commands and options',
    long_description='',
    install_requires=[
        "argparse", "sphinx"
    ],
)

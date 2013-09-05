import os
from setuptools import setup
# from tests import PyTest

setup(
    name='sphinx-argparse',
    version='0.5.12',
    packages=[
        'sphinxarg',
    ],

    url='',
    license='MIT',
    author='Aleksandr Rudakov',
    author_email='ribozz@gmail.com',
    description='Sphinx extension that automatically document argparse commands and options',
    long_description=open('README.md').read(),
    install_requires=[
        "argparse", "sphinx"
    ],
)

from setuptools import setup

setup(
    name='sphinx_argparse',
    version='0.2.0',
    packages=[
        'sphinxarg',
    ],
    url='',
    license='MIT',
    author='Aleksandr Rudakov and Devon Ryan',
    author_email='ribozz@gmail.com',
    description='Sphinx extension that automatically documents argparse commands and options',
    long_description='',
    install_requires=[
        'sphinx',
        'CommonMark>=0.5.6'
    ],
    extras_require={
        'dev': ['pytest', 'sphinx_rtd_theme'],
    }
)

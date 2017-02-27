from setuptools import setup

deps = ["sphinx"]

setup(
    name='sphinx_argparse',
    version='0.1.17',
    packages=[
        'sphinxarg',
    ],

    url='',
    license='MIT',
    author='Aleksandr Rudakov and Devon Ryan',
    author_email='ribozz@gmail.com',
    description='Sphinx extension that automatically documents argparse commands and options',
    long_description='',
    install_requires=deps,

    extras_require={
        'dev': ['pytest', 'sphinx_rtd_theme', 'sphinx'],
    }
)

from setuptools import setup


def getVersion():
    f = open("sphinxarg/__init__.py")
    _ = f.read()
    ver = _.split("'")[1]
    f.close()
    return ver


setup(
    name='sphinx-argparse',
    version=getVersion(),
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
        'dev': ['pytest', 'sphinx_rtd_theme']
    }
)

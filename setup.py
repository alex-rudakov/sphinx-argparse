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
    url='https://github.com/ribozz/sphinx-argparse',
    license='MIT',
    author='Aleksandr Rudakov and Devon Ryan',
    author_email='ribozz@gmail.com',
    description='A sphinx extension that automatically documents argparse commands and options',
    long_description="""A sphinx extension that automatically documents argparse commands and options.

For installation and usage details, see the `documentation <http://sphinx-argparse.readthedocs.org/en/latest/>`_.""",
    install_requires=[
        'sphinx>=1.2.0',
        'CommonMark>=0.5.6'
    ],
    extras_require={
        'dev': ['pytest', 'sphinx_rtd_theme']
    }
)

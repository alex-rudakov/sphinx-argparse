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
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Documentation'
    ],
    install_requires=[
        'sphinx>=1.2.0'
    ],
    extras_require={
        'dev': ['pytest', 'sphinx_rtd_theme'],
        'markdown': ['CommonMark>=0.5.6']
    }
)

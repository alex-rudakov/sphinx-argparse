from setuptools import setup

MARKDOWN_REQUIREMENTS = ['CommonMark>=0.5.6']
LINT_REQUIREMENTS = ['flake8']
TEST_REQUIREMENTS = ['pytest', 'tox']
DEV_REQUIREMENTS = ['sphinx_rtd_theme==0.4.3'] + \
    TEST_REQUIREMENTS + \
    LINT_REQUIREMENTS + \
    MARKDOWN_REQUIREMENTS


def get_version():
    f = open('sphinxarg/__init__.py')
    _ = f.read()
    ver = _.split('\'')[1]
    f.close()
    return ver


def get_long_description():
    f = open('README.md')
    long_desc = f.read()
    f.close()
    return long_desc


setup(
    name='sphinx-argparse',
    version=get_version(),
    packages=[
        'sphinxarg',
    ],
    url='https://github.com/alex-rudakov/sphinx-argparse',
    license='MIT',
    data_files=[("", ["LICENSE"])],
    author='Aleksandr Rudakov and Devon Ryan',
    author_email='ribozz@gmail.com',
    description='A sphinx extension that automatically documents' +
                ' argparse commands and options',
    long_description=get_long_description(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Documentation'
    ],
    install_requires=[
        'sphinx>=1.2.0'
    ],
    extras_require={
        'dev': DEV_REQUIREMENTS,
        'lint': LINT_REQUIREMENTS,
        'test': TEST_REQUIREMENTS,
        'markdown': MARKDOWN_REQUIREMENTS
    }
)

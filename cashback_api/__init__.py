# -*- coding: utf-8 -*-
from os import getenv

from setuptools import find_packages, setup

__version__ = getenv("APP_VERSION")
__description__ = getenv("APP_DESCRIPTION")
__long_description__ = getenv("APP_LONG_DESCRIPTION")

__author__ = getenv("APP_AUTHOR")
__author_email__ = getenv("APP_AUTHOR_EMAIL")

setup(
    name='Api',
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    packages=find_packages(),
    license='MIT',
    description=__description__,
    long_description=__long_description__,
    url='https://github.com/lexgalante/cashback',
    keywords='Cashback',
    include_package_data=True,
    zip_safe=False,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    extras_require={
        'testing': [
            'pytest',
            'pytest-cov',
        ],
    },
)

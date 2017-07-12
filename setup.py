#!/usr/bin/env python

from setuptools import find_packages, setup


VERSION = '1.0.0'
REPO_URL = 'https://github.com/drongo-framework/drongo-nest'
DOWNLOAD_URL = REPO_URL + '/archive/v{version}.tar.gz'.format(version=VERSION)

setup(
    name='drongo-nest',
    version=VERSION,
    description='High performance server for drongo.',
    author='Sattvik Chakravarthy, Sagar Chakravarthy',
    author_email='sattvik@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    packages=find_packages(),
    url=REPO_URL,
    download_url=DOWNLOAD_URL,
    include_package_data=True,
    install_requires=[
        'six'
    ],
    zip_safe=False,
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(

    name = 'python-kana-conversion',
    version = '0.1', 
    description = 'Convert ASCII characters (i.e. English) to and from Japanese Kana',
    long_description = 'Convert ASCII characters (i.e. English) to and from Japanese Kana',
    packages = find_packages(),
    author = 'Ian Wilson',
    url = 'https://github.com/ian-wilson/python-kana-conversion',
    author_email = 'tellme@emotionai.com',
    license = 'MIT',
    platforms = 'any',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

)

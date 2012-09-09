#!/usr/bin/env python
# Copyright (c) Paul Tagliamonte <paultag@debian.org> under the terms and
# conditions of the Expat license.

from setuptools import setup

long_description = open('README.md').read()

setup(
    name="loadavg",
    version="0.1",
    packages=['loadavg'],
    author="Paul Tagliamonte",
    author_email="paultag@debian.org",
    long_description=long_description,
    description='system load information',
    license="Expat",
    url="http://pault.ag",
    platforms=['linux']
)

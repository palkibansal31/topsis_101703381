#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 16:11:17 2020

@author: Palki
"""

import setuptools
with open("README.md", "r") as fh:
    README = fh.read()

setuptools.setup(
    name="Topsis_101703381", # Replace with your own username
    version="1.0.1",
    author="Palki",
    author_email="palkipb@gmail.com",
    description="A Python package to implement topsis function",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/palkibansal31/",
    packages=setuptools.find_packages(),
    licence="MIT" 
)
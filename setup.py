#!/usr/bin/env python

from setuptools import setup

setup(
  include_package_data=True,
  zip_safe=False,
  install_requires=['flask'],
  setup_requires=['pbr'],
  pbr=True,
)
#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages
import sys
import re


def find_version():
    return re.search(r"^__version__ = '(.*)'$",
                     open('cantools/version.py', 'r').read(),
                     re.MULTILINE).group(1)


def dependencies():
    deps = [
        'bitstruct>=8.15.1',
        'python-can>=3.3.4',
        'textparser>=0.21.1',
        'diskcache',
        'argparse_addons',
        'typing_extensions>=3.10.0.0',
        'crccheck',
    ]

    if sys.platform == 'win32':
        deps += [
            'windows-curses'
        ]

    return deps

setup(name='cantools',
      version=find_version(),
      description='CAN BUS tools.',
      long_description=open('README.rst', 'r').read(),
      long_description_content_type='text/x-rst',
      author='Erik Moqvist',
      author_email='erik.moqvist@gmail.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      keywords=['can', 'can bus', 'dbc', 'kcd', 'automotive'],
      url='https://github.com/eerimoq/cantools',
      packages=find_packages(exclude=['tests']),
      package_data={"cantools": ["py.typed"]},
      python_requires='>=3.6',
      install_requires=dependencies(),
      extras_require=dict(
          plot=['matplotlib'],
      ),
      test_suite="tests",
      entry_points={
          'console_scripts': ['cantools=cantools.__init__:_main']
      })

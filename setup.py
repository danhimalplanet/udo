#!/usr/bin/env python

from __future__ import print_function
from setuptools import setup, find_packages
import io
import codecs
import os
import sys

import udo

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = """
Udo (Unemployed DevOps) is a friendly command-line tool to manage clusters of Amazon Elastic Compute instances using autoscaling groups.
If you use Amazon Web Services you probably want to be using Udo.
Read the README for more information: https://github.com/revmischa/udo/blob/master/README.md
"""

setup(
    name='udo',
    version='4.2.2',
    url='http://github.com/revmischa/udo',
    license='Anyone But RMS',
    author='Mischa Spiegelmock',
    tests_require=['pytest'],
    install_requires=[
        'boto3==1.2.3',
        'botocore==1.3.23',
        'docutils==0.12',
        'futures==3.0.4',
        'jmespath==0.9.0',
        'python-dateutil==2.4.2',
        'PyYAML==3.11',
        'six==1.10.0',
        'termcolor==1.1.0',
        'wheel==0.27.0',
    ],
    author_email='revmischa@cpan.org',
    description='Automate AWS Orchestration and Deployments',
    long_description=long_description,
    packages=['udo'],
    include_package_data=True,
    platforms='any',
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'udo = udo.main:invoke_console',
        ],
    },
    keywords='devops aws amazon autoscaling orchestration',
    classifiers=[
        'Programming Language :: Python',
        'Topic :: System :: Systems Administration'
    ]
)

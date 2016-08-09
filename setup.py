#!/usr/bin/env python
import os
import sys

from setuptools import setup, find_packages

version = '1.0.2'

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    os.system("git tag -a %s -m 'v%s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

with open('README.rst') as readme_file:
    readme = readme_file.read()

if sys.argv[-1] == 'readme':
    print(readme)
    sys.exit()

requirements = ['requests']

setup(
    name='spamcheck',
    version=version,
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,

    # metadata for upload to PyPI
    author='Tesorio',
    author_email='hello@tesorio.com',
    description="A simple Python wrapper for Postmark's Spamcheck API",
    long_description=readme,
    license='MIT License',
    keywords='postmark spam spamcheck',
    url='https://github.com/Tesorio/spamcheck-python',
)

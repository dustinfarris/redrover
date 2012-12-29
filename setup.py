#!/usr/bin/env python
"""
RedRover
========

RedRover is a testing utility suite for Django.  It wraps other powerful
tools such as Nose and Selinium into an easy to use and read syntax.

At its core, RedRover borrows from other python projects and provides
an interface with custom syntax sugar inspired by the RSpec and Capybara
projects that are used widely with Ruby on Rails.

:copyright: (c) 2012 by Dustin Farris
:license: BSD, see LICENSE for more details.

"""

from setuptools import setup, find_packages


# Hack to prevent stupid "TypeError: 'NoneType' object is not callable" error
# in multiprocessing/util.py _exit_function when running `python
# setup.py test` (see
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
for m in ('multiprocessing', 'billiard'):
    try:
        __import__(m)
    except ImportError:
        pass

tests_require = [
  'pytest',
  'pytest-django']

install_requires = [
  'Django>=1.4',
  'django_nose',
  'rednose==0.3.3',
  'splinter']

setup(
  name='redrover',
  version='0.3.0',
  author='Dustin Farris',
  author_email='dustin@dustinfarris.com',
  url='https://github.com/dustinfarris/redrover',
  description='A testing utility suite for Django.',
  long_description=__doc__,
  package_dir={'': 'src'},
  packages=find_packages('src'),
  zip_safe=False,
  install_requires=install_requires,
  tests_require=tests_require,
  test_suite='runtests.runtests',
  license='BSD',
  include_package_data=True,
  classifiers=[
    'Framework :: Django',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Operating System :: OS Independent',
    'Topic :: Software Development'])
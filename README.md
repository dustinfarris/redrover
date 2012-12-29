RedRover
========

[![Build Status](https://travis-ci.org/dustinfarris/redrover.png?branch=master)](https://travis-ci.org/dustinfarris/redrover)

RedRover is a testing utility suite for Django.  It wraps other powerful
tools such as Nose and Selinium into an easy to use and read syntax.

At its core, RedRover borrows from other python projects and provides
an interface with custom syntax sugar inspired by the RSpec and Capybara
projects that are used widely with Ruby on Rails.

Requirements
------------
* Python 2.7+ (Django is on the fast-track to 3.0 and so am I)
* Django 1.4+ (tested with all micro-releases of 1.4)

Installation
------------
Install via pip.

    pip install redrover

Dependencies
------------
These will be automatically installed for you.

* django_nose
* rednose
* splinter

Configuration
-------------
Add ``'redrover'`` to the bottom of your ``INSTALLED_APPS``.  Also add
the following configuration to your settings.py:

    TEST_RUNNER = 'redrover.RedRoverRunner'

Usage
-----
No big changes here:

    python manage.py test

Since RedRover wraps [nose][1] (via django_nose), you get all of its
testing options as well.  See their [documentation][2]  for details, or
just run ``python manage.py help test``.


[1]: https://github.com/nose-devs/nose
[2]: https://nose.readthedocs.org/en/latest/
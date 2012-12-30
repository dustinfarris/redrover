RedRover
========

UNDER DEVELOPMENT - RedRover is not ready for production use and is
made available for the curious only.

[![Build Status](https://travis-ci.org/dustinfarris/redrover.png?branch=master)](https://travis-ci.org/dustinfarris/redrover)

RedRover is a behavior-driven testing utility suite for Django.  It
wraps other powerful tools such as Nose and Selinium into a clean
readable syntax that is easy to use.

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

```sh
$ pip install redrover
```

Dependencies
------------
These will be automatically installed for you.

* django_nose
* rednose
* splinter

It is also highly recommended that you install and use [FactoryBoy][1].
While not strictly required to run RedRover, it is a very nice
compliment to RedRover's operation and is used in many of the examples.

Configuration
-------------
Add ``'redrover'`` to the bottom of your ``INSTALLED_APPS``.  Also add
the following configuration to your settings.py:

```python
TEST_RUNNER = 'redrover.RedRoverRunner'
```

Usage
-----
No big changes here:

```sh
$ python manage.py test
```

Since RedRover wraps [nose][2] (via django_nose), you get all of its
testing options as well.  See their [documentation][3]  for details, or
just run ``python manage.py help test``.

Writing Tests
-------------
The idea of writing RedRover tests is to identify a particular "thing"
and describe how it should behave.  Every thing gets a class where it
becomes the 'subject,' and every class has one or more tests that
evaluate the subject's behavior by referring to "it."

In the simplest form, suppose we want to show that the number 5 can be
attained by adding the numbers 2 and 3.  Our test would look like this:

```python
from redrover import *


class NumberFiveTest(RedRoverTest):

  subject = 5

  def test_addition(self):
    it.should(equal, 2 + 3)
```

Running ``./manage.py test`` should result in some nice looking output
that informs you all tests have passed.

You are not completely restricted to writing tests in this way.  The
standard unittest library and assertions work as good as ever; and
they may be preferable in some cases.  Where RedRover really shines
is in behavior-driven developement.

[1]: https://github.com/dnerdy/factory_boy
[2]: https://github.com/nose-devs/nose
[3]: https://nose.readthedocs.org/en/latest/
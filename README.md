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

To accomplish this, we declare a subject in the class description, and
further define it in the setUp method.

Model Tests
-----------

Suppose we decide to describe the behavior of a "Person" Django model.
One of the qualities of Person might be that it has a first_name, or in
other words, that it responds to a first_name attribute inquiry.  Here
is what this sort of "behavior-driven" test might look like when using
RedRover:

```python
from redrover import *

from people.models import Person


class PersonTest(RedRoverTest):

  subject = 'person'

  def setUp(self):
    self.person = Person()

  @describe
  def attributes(self):
    it.should(respond_to, 'first_name')

```

Running ``./manage.py test`` should result in some nice looking output
that informs you all tests have passed.

Now let's take it a step further.  Suppose you want to ensure that your
model instance properly validates when populated with correct
information -- and moreso, that it *doesn't* validate when populated
with incorrect information.   Assume the model Person looks something
like this:

```python
from django.db import models


class Person(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)

  @property
  def full_name(self):
    return '%s %s' % (self.first_name, self.last_name)

```

Using RedRover, we can fully test this model's behavior like so:

```python
from redrover import *

from people.models import Person


class PersonTest(RedRoverTest):

  subject = 'person'

  def setUp(self):
    self.person = Person(first_name='Bob', last_name='Smith')

  @describe
  def attributes(self):
    it.should(respond_to, 'first_name')
    it.should(respond_to, 'last_name')
    it.should(respond_to, 'full_name')
    its('full_name').should(equal, "Bob Smith")

    it.should(be_valid)

  @describe
  def when_first_name_is_blank(self):
    self.person.first_name = ""
    it.should_not(be_valid)

  @describe
  def when_last_name_is_blank(self):
    self.person.last_name = ""
    it.should_not(be_valid)

```

Page Tests
----------

A.k.a "view/template" tests, here we'll identify the "page" as the
subject and define how it should look/behave as we do things to it.
Here's an example:

```python
from redrover import *


class PagesTest(RedRoverTest):

  subject = page

  @before
  def setUp(self):
    visit('/')

  @describe
  def the_homepage(self):
    its('title').should(be, 'Homepage')
    it.should(have_text, 'Welcome')

  @describe
  def navigating_to_the_people_index(self):
    click_link('People')
    its('title').should(be, 'People')
    it.should(have_selector, 'h1', text='People')

```

You are not completely restricted to writing tests in this way.  The
standard unittest library and assertions work as good as ever; and
they may be preferable in some cases.  Where RedRover really shines
is in behavior-driven developement.

[1]: https://github.com/dnerdy/factory_boy
[2]: https://github.com/nose-devs/nose
[3]: https://nose.readthedocs.org/en/latest/
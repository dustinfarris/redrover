Quickstart
===========

Basic requirements to run RedRover:

* Python 2.7 (Working on 3.x but not quite there)
* Django 1.4+ (tested with all micro-releases of 1.4)

Dependencies
------------

These will be automatically installed for you:

* django_nose
* rednose
* splinter

It is also highly recommended that you install and use
`FactoryBoy <https://github.com/dnerdy/factory_boy>`_. While not
strictly required to run RedRover, it is a very nice compliment
to RedRover's operation and is used in many of the examples.

Install RedRover
----------------

Installing is easy via pip::

  pip install redrover

Configuration
-------------

Add ``'redrover'`` to the bottom of your ``'INSTALLED_APPS'``.  Also add
the following to your settings.py::

  TEST_RUNNER = 'redrover.RedRoverRunner'

Usage
-----

Run your tests the same as usual.  Django will use the custom test-
runner you specified in settings.py which gives RedRover the reigns.::

  python manage.py test

Test Discovery
--------------

RedRover will discover your tests be recursively detecting Python
modules and then looking for any sub-module(file) ending in "_test.py".
Because of this, it is recommended that you organize your tests in a
"tests" directory in your root project directory.

A sample Django project might look like this::

  myproject
    |
    |-- manage.py
    |
    |-- myapp
    |     |
    |     |-- __init__.py
    |     |-- models.py
    |     |-- views.py
    |     +-- urls.py
    |
    |-- myproject
    |     |
    |     |-- __init__.py
    |     |-- settings.py
    |     |-- urls.py
    |     +-- wsgi.py
    |
    +-- tests
          |
          |-- __init__.py
          |-- factories.py
          |
          |-- models
          |     |
          |     |-- __init__.py
          |     +-- myapp_mymodel_test.py
          |
          +-- requests
                |
                |-- __init__.py
                +-- myapp_pages_test.py

Within your 'test' Python files, you should import RedRover and subclass
the RedRoverTest or RedRoverLiveTest classes like this::

  # myapp_my_model_test.py

  from redrover import *

  from myapp.models import MyModel


  class MyModelTest(RedRoverTest):

When you use the RedRoverTest or RedRoverLiveTest superclass you are
provided the "describe" decorator.  When you decorate your individual
test cases with this decorator, they will be discovered by the test
runner regardless of whether the characters "test" appear in the method
name::

  class MyModelTest(RedRoverTest):

    @describe
    def addition(self):
      assert_equal(2, 1 + 1)

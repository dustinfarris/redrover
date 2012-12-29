from types import FunctionType

from django.test import TestCase


def do_decorate(attr, value):
  return (
    '__' not in attr and
    'setUp' is not attr and
    'setUpClass' is not attr and
    'tearDown' is not attr and
    'tearDownClass' is not attr and
    'run' is not attr and
    'skipTest' is not attr and
    'debug' is not attr and
    isinstance(value, FunctionType))


def decorate_all():

  class DecorateAll(type):

    def __new__(cls, name, bases, dct):
      for attr, value in dct.iteritems():
        if do_decorate(attr, value):
          value.__name__ = 'test_%s' % value.__name__
          value.__globals__.update({
            'it': Subject(dct['subject'])})
      return super(DecorateAll, cls).__new__(
        cls, name, bases, dct)

    def __setattr__(self, attr, value):
      if do_decorate(attr, value):
        value.__name__ = 'test_%s' % value.__name__
      super(DecorateAll, self).__setattr__(attr, value)

  return DecorateAll


class Subject(object):

  def __init__(self, subject):
    self.subject = subject

  def should(self, cls, *args, **kwargs):
    assertion = cls(self.get_subject, *args, **kwargs)
    if not assertion.passes:
      raise AssertionError(assertion.message)
    return True

  def should_not(self, cls, *args, **kwargs):
    assertion = cls(self.get_subject, *args, **kwargs)
    if assertion.passes:
      raise AssertionError(assertion.message)
    return True

  @property
  def get_subject(self):
    return self.subject


class RedRoverTest(TestCase):

  __metaclass__ = decorate_all()

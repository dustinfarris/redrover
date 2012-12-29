from types import FunctionType

from django.test import TestCase


def do_decorate(attr, value):
  protected = [
    'setUp', 'setUpClass', 'tearDown', 'tearDownClass',
    'run', 'skipTest', 'debug']
  return (
    '__' not in attr and
    attr not in protected and
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

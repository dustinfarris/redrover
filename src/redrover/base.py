import functools
from types import FunctionType

from django.test import LiveServerTestCase, TestCase
import splinter

from subject import _splinter_action, _subject


def describe(func):
  """
  This more or less is the "magic" of RedRover.  With the `describe`
  decorator, a test is equipped with the keywords 'it', 'its', and
  if applicable, 'visit'.

  """
  @functools.wraps(func)
  def test_func(instance, *args, **kwargs):
    subject_name = getattr(instance, 'subject', None)

    if subject_name:
      extra_context = {
        'it': _subject(instance)(subject_name),
        'its': _subject(instance, parent_name=subject_name)}

      if subject_name == 'page':
        extra_context.update({
          'visit': _splinter_action(instance, 'visit')})

      # Now do the actual "decorating"
      func.__globals__.update(extra_context)

    return func(instance, *args, **kwargs)

  return test_func


def _is_protected(item):
    """Filter out things we shouldn't be messing with."""
    return ('__' in item or item in dir(LiveServerTestCase))


def _redrover_klass():
  """
  Prefix test methods with 'test_' so they are discoverable by the
  test runner.

  """
  class DiscoverableTests(type):

    def __new__(cls, name, bases, dct):
      for attr, value in dct.iteritems():
        if not _is_protected(attr) and isinstance(value, FunctionType):
          value.__name__ = 'test_%s' % value.__name__
      return super(DiscoverableTests, cls).__new__(cls, name, bases, dct)

  return DiscoverableTests


class RedRoverTest(TestCase):

  __metaclass__ = _redrover_klass()


class RedRoverLiveTest(LiveServerTestCase):

  def __init__(self, *args, **kwargs):
    if getattr(self, 'subject', None) == 'page':
      self.page = splinter.Browser('zope.testbrowser')
      self.setUp.__globals__.update({'visit': _splinter_action(self, 'visit')})
    super(RedRoverLiveTest, self).__init__(*args, **kwargs)

  __metaclass__ = _redrover_klass()

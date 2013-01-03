import functools
from types import FunctionType

from django.test import LiveServerTestCase, TestCase
import splinter

from subject import get_splinter_actions, _subject, BROWSER


def _get_extra_context(instance, extra_context={}):
  subject_name = getattr(instance, 'subject', None)

  if subject_name:
    extra_context = {
      'it': _subject(instance)(subject_name),
      'its': _subject(instance, parent_name=subject_name)}

    if subject_name == BROWSER:
      extra_context.update(get_splinter_actions(instance))

  return extra_context


def before(func):
  """
  The only way to get `setUp` to behave the way we want is to decorate
  it.  So might as well make it look intentional :)

  """
  @functools.wraps(func)
  def setUp(instance, *args, **kwargs):
    func.__globals__.update(_get_extra_context(instance))
    return func(instance, *args, **kwargs)

  return setUp


def describe(func):
  """
  This more or less is the "magic" of RedRover.  With the `describe`
  decorator, a test is equipped with the keywords 'it', 'its', and
  if applicable, 'visit'.

  """
  @functools.wraps(func)
  def test_func(instance, *args, **kwargs):
    func.__globals__.update(_get_extra_context(instance))
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
    if getattr(self, 'subject', None) == BROWSER:
      setattr(self, BROWSER, splinter.Browser('zope.testbrowser'))
      self.setUp.__globals__.update(get_splinter_actions(self))
    super(RedRoverLiveTest, self).__init__(*args, **kwargs)

  __metaclass__ = _redrover_klass()

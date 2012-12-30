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
      subject = dct.get('subject')
      if subject:
        if subject in dct:
          raise NameError(
            'You cannot use "%s" as a subject name.' % subject)
        dct[subject] = None

      for attr, value in dct.iteritems():
        if do_decorate(attr, value):
          if isinstance(value, FunctionType):
            value.__name__ = 'test_%s' % value.__name__
      return super(DecorateAll, cls).__new__(
        cls, name, bases, dct)

  return DecorateAll


class RedRoverTest(TestCase):

  __metaclass__ = decorate_all()

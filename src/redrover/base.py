from types import FunctionType

from django.test import LiveServerTestCase, TestCase
import splinter

from subject import _splinter_action


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

        if subject == 'page':
          dct['page'] = splinter.Browser('zope.testbrowser')

      for attr, value in dct.iteritems():
        if do_decorate(attr, value):
          if isinstance(value, FunctionType):
            value.__name__ = 'test_%s' % value.__name__

      dct['_browser'] = splinter.Browser('zope.testbrowser')

      return super(DecorateAll, cls).__new__(
        cls, name, bases, dct)

  return DecorateAll


class RedRoverTest(TestCase):

  __metaclass__ = decorate_all()


class RedRoverLiveTest(LiveServerTestCase):

  def __init__(self, *args, **kwargs):
    self.setUp.__globals__.update({'visit': _splinter_action(self, 'visit')})
    super(RedRoverLiveTest, self).__init__(*args, **kwargs)

  __metaclass__ = decorate_all()

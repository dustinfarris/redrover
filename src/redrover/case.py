import logging
from types import FunctionType

from django.test import TestCase


logger = logging.getLogger(__name__)


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


class Equal(object):

  def __init__(self, subject, other):
    self.subject = subject
    self.other = other

  def process(self):
    return self.subject == self.other

  def __unicode__(self):
    if self.process():
      message = '{subject_type} {subject_value} equals {other}'
    else:
      message = '{subject_type} {subject_value} does not equal {other}'
    return message.format(
      subject_type=type(self.subject).__name__,
      subject_value=str(self.subject),
      other=str(self.other))


class Subject(object):

  def __init__(self, subject):
    self.subject = subject

  def should(self, cls, *args, **kwargs):
    klass = cls(self.get_subject, *args, **kwargs)
    if not klass.process():
      raise AssertionError(klass.__unicode__().capitalize())
    return True

  def should_not(self):
    return

  @property
  def get_subject(self):
    return self.subject


class RedRover(TestCase):

  __metaclass__ = decorate_all()


equal = Equal

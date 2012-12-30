import functools


def _subject(parent=None):

  class Subject(object):

    def __init__(self, value):
      if parent:
        self.value = getattr(parent, value)
      else:
        self.value = value

    def should(self, cls, *args, **kwargs):
      assertion = cls(self.value, *args, **kwargs)
      if not assertion.passes:
        raise AssertionError(assertion.message)
      return True

    def should_not(self, cls, *args, **kwargs):
      assertion = cls(self.value, *args, **kwargs)
      if assertion.passes:
        raise AssertionError(assertion.message)
      return True

  return Subject


def describe(func):
  @functools.wraps(func)
  def test_describe(instance, *args, **kwargs):
    subject_name = getattr(instance, 'subject', None)
    if subject_name:
      subject = getattr(instance, subject_name, None)
      if not subject:
        raise NameError(
          'You are trying to use a subject that has not been initialized ' +
          'in `setUp`.')
      It = _subject()
      Its = _subject(subject)
      func.__globals__.update({
        'it': It(subject),
        'its': Its})
    return func(instance, *args, **kwargs)
  return test_describe

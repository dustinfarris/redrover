import functools


def _splinter_action(_parent, _action):

  _browser = _parent.page

  def do_action(*args, **kwargs):
    if _action == 'visit':
      base_url = _parent.live_server_url
      url = args[0]
      return _browser.visit('%s%s' % (base_url, url))

    return getattr(_browser, _action)(*args, **kwargs)

  return do_action


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
    extra_context = {}

    if subject_name:
      subject = getattr(instance, subject_name, None)
      if not subject:
        raise NameError(
          'You are trying to use a subject that has not been initialized ' +
          'in `setUp`.')

      if subject_name == 'page':
        extra_context.update({
          'visit': _splinter_action(instance, 'visit')})

      extra_context.update({
        'it': _subject()(subject),
        'its': _subject(subject)})

      func.__globals__.update(extra_context)

    return func(instance, *args, **kwargs)

  return test_describe

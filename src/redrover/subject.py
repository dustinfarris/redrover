def _splinter_action(_parent, _action):

  _browser = _parent.page

  def do_action(*args, **kwargs):
    if _action == 'visit':
      base_url = _parent.live_server_url
      url = args[0]
      return _browser.visit('%s%s' % (base_url, url))

    return getattr(_browser, _action)(*args, **kwargs)

  return do_action


def _subject(instance, parent_name=None):

  class Subject(object):

    def __init__(self, name):
      self.name = name

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

    @property
    def value(self):
      if parent_name:
        parent = getattr(instance, parent_name)
        return getattr(parent, self.name)
      return getattr(instance, self.name)

  return Subject

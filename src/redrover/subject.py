from urlparse import urlparse


def _splinter_action(_parent, _action):
  """
  Hook to perform the specified action against the parent's
  `page` attriburte.

  """

  def do_action(*args, **kwargs):
    _browser = getattr(_parent, 'page')

    if _action == 'visit':
      url = args[0]
      if url.startswith('http'):
        return _browser.visit(url)
      base_url = getattr(_parent, 'live_server_url')
      return _browser.visit('%s%s' % (base_url, url))

    return getattr(_browser, _action)(*args, **kwargs)

  return do_action


def get_splinter_actions(instance):
  """
  A dictionary of all supported Splinter actions set up against the
  given test-class instance.

  """
  return {
    'visit': _splinter_action(instance, 'visit'),
    'current_path': _subject(
      instance.page, modifier=lambda url: urlparse(url).path)('url')}


def _subject(instance, parent_name=None, modifier=None):
  """
  The Subject object references a particular attribute and allows the
  developer to check it for various behaivors and conditions.

  """
  class Subject(object):

    def __init__(self, name):
      self.name = name
      self.instance = instance  # For debugging

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
        _value = getattr(parent, self.name)
      else:
        _value = getattr(instance, self.name)
      if modifier:
        _value = modifier(_value)
      return _value

    def __str__(self):
      return str(self.value)

    def __repr__(self):
      return self.__str__()

    def __lt__(self, other):
      return self.value < other

    def __le__(self, other):
      return self.value <= other

    def __eq__(self, other):
      return self.value == other

    def __ne__(self, other):
      return self.value != other

    def __gt__(self, other):
      return self.value > other

    def __ge__(self, other):
      return self.value >= other

  return Subject

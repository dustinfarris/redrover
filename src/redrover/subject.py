from urlparse import urlparse

from splinter.exceptions import ElementDoesNotExist


class ElementNotFound(ElementDoesNotExist):
  pass


def _splinter_action(_action, _parent):
  """
  All the various splinter actions we support.  (and a few others)

  """
  _browser = getattr(_parent, 'page')

  def visit(location):
    if location.startswith('http'):
      return _browser.visit(location)
    base_url = _parent.live_server_url
    return _browser.visit('%s%s' % (base_url, location))

  def click_link(locator):
    # First we'll try by text, then by CSS selector
    links = _browser.find_link_by_text(locator)
    if links:
      return links.first.click()
    links = _browser.find_by_css('a').find_by_css(locator)
    if links:
      return links.first.click()
    raise ElementNotFound()

  return locals().get(_action)


def get_splinter_actions(instance):
  """
  A dictionary of all supported Splinter actions plus a few of my own
  set up against the given test-class instance.

  """
  return {
    'click_link': _splinter_action('click_link', instance),
    'visit': _splinter_action('visit', instance),
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

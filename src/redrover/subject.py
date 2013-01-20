from httplib import InvalidURL
from urlparse import urlparse

from splinter.exceptions import ElementDoesNotExist
from zope.testbrowser.browser import Browser as ZopeTestBrowser
from utils import get_url


class ElementNotFound(AssertionError):
  pass


BROWSER = '_browser'


def _splinter_action(_action, _parent):
  """
  All the various splinter actions we support.  (and a few others)

  """
  _browser = getattr(_parent, BROWSER)

  # Finders

  def find_button(query):
    # Grab all buttons
    buttons = _browser.find_by_tag('button')
    # First try to find the right one matching text
    matching_text = filter(lambda e: e.text.strip() == query, buttons)
    if matching_text:
      return matching_text[0]
    # Try by CSS selector
    buttons = _browser.find_by_css(query)
    if buttons:
      return buttons.first
    raise ElementNotFound('Could not find a button matching "%s"' % query)

  def find_link(query):
    # First we'll try by text, then by CSS selector
    links = _browser.find_link_by_text(query)
    if links:
      return links.first
    links = _browser.find_by_css('a').find_by_css(query)
    if links:
      return links.first
    raise ElementNotFound('Could not find a link matching "%s"' % query)

  def find_input(query):
    #
    # NO LONGER USED
    #
    # Try by label text first
    labels = _browser.find_by_tag('label')
    matching_text = filter(lambda e: e.text == query, labels)
    if matching_text:
      input_id = matching_text[0]._element.for_element.attrib['id']
      try:
        return _browser.find_by_id(input_id).first
      except ElementDoesNotExist:
        raise ElementNotFound(
          'Found label "%s", but no matching input' % query)
    # Try by name
    try:
      inputs = _browser.find_by_name(query)
    except LookupError:
      # Zope Testbrowser throws this if the query is not a valid name.
      inputs = None
    if inputs:
      return inputs.first
    # Try by CSS selector
    inputs = _browser.find_by_css(query)
    if inputs:
      return inputs.first
    raise ElementNotFound('Could not find an input matching "%s"' % query)

  # Actions

  def fill_in(query, value):
    try:
      control = _browser._browser.getControl(query)
    except LookupError:
      try:
        control = _browser._browser.getControl(name=query)
      except LookupError:
        control = None

    if control:
      control.value = value
    else:
      input_field = find_input(query)
      input_field.fill(value)

  def click_on(query):
    try:
      # First try it the easy way (if the button is actually a
      # submit input).
      control = _browser._browser.getControl(query)
    except LookupError:
      button = find_button(query)
      try:
        control = _browser._browser.getControl(
          name=button._element.attrib['name'])
      except KeyError:
        raise KeyError(
          'Buttons must have a unique `name` attribute to be used.')
    return control.click()

  def select(query, option):
    try:
      control = _browser._browser.getControl(query)
    except LookupError:
      control = _browser._browser.getControl(name=query)
    control.value = [option]

  def visit(location, *args, **kwargs):
    try:
      url = get_url(location, *args, **kwargs)
      if url.startswith('/'):
        base_url = _parent.live_server_url
        return _browser.visit('%s%s' % (base_url, url))
      return _browser.visit(location)
    except:
      raise InvalidURL(
        'Could not determine a reliable URL from "%s"' % location)

  def click_link(*args, **kwargs):
    control = _browser._browser.getLink(*args, **kwargs)
    return control.click()

  return locals().get(_action)


def get_splinter_actions(instance):
  """
  A dictionary of all supported Splinter actions plus a few of my own
  set up against the given test-class instance.

  """
  finders = ['find_button', 'find_link', 'find_input']
  actions = ['click_link', 'click_on', 'fill_in', 'select', 'visit']

  all_actions = {k: _splinter_action(k, instance) for k in finders + actions}
  all_actions['current_path'] = _subject(
    instance._browser, modifier=lambda url: urlparse(url).path)('url')
  return all_actions


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
        if self.name == 'path':
          if isinstance(getattr(parent, BROWSER, None), ZopeTestBrowser):
            _value = urlparse(parent.url).path
        else:
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

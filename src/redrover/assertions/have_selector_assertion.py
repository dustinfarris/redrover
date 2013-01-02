from base import BaseAssertion


class HaveSelectorAssertion(BaseAssertion):
  """Determine if given selector exists in a splinter Browser document."""

  def __init__(self, browser, selector, **kwargs):
    if not hasattr(browser, 'html'):
      raise ValueError(
        '`have_selector` must be called on a page/Browser instance.')
    self.url = browser.url
    self.selector = selector
    self.extras = kwargs
    elements = browser.find_by_css(selector)
    # Special requests
    for k in kwargs:
      elements = [el for el in elements if getattr(el, k) == kwargs[k]]

    self.passes = bool(elements)

  @property
  def message(self):
    if self.passes:
      msg = '{selector} selector{extras} exists in {url}'
    else:
      msg = '{selector} selector{extras} does not exist in {url}'

    if self.extras:
      extras = ' with the %s' % ', and the '.join(
        ['%s "%s"' % (k, self.extras[k]) for k in self.extras])
    else:
      extras = ''

    return msg.format(
      selector=repr(self.selector),
      url=self.url,
      extras=extras)

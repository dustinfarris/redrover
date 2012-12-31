from base import BaseAssertion


class HaveTextAssertion(BaseAssertion):
  """Determine if given text appears in an splinter Browser document."""

  def __init__(self, browser, text):
    if not hasattr(browser, 'html'):
      raise ValueError(
        '`have_text` must be called on a page/Browser instance.')
    self.browser = browser
    self.text = text
    self.passes = text in browser.html

  @property
  def message(self):
    if self.passes:
      msg = '{text} appears in {url}'
    else:
      msg = '{text} does not appear in {url}'

    return msg.format(
      text=repr(self.text),
      url=self.browser.url)

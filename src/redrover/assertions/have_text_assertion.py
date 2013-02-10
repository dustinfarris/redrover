from urlparse import urlparse

from django.utils.encoding import smart_text

from base import BaseAssertion


class HaveTextAssertion(BaseAssertion):
    """
    Determine if given text appears in an splinter Browser document.

    """
    def __init__(self, browser, text):
        if not hasattr(browser, 'html'):
            raise ValueError(
                '`have_text` must be called on a page/Browser instance.')
        self.url = urlparse(browser.url).path
        self.text = text
        self.passes = smart_text(text) in smart_text(browser.html)

    @property
    def message(self):
        if self.passes:
            msg = '{text} appears in {url}'
        else:
            msg = '{text} does not appear in {url}'

        return msg.format(
            text=repr(self.text),
            url=self.url)

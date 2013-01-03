from django.test import LiveServerTestCase
import splinter

from redrover import have_selector, page
from redrover.subject import _subject


class AssertHaveSelectorTest(LiveServerTestCase):

  @classmethod
  def setUpClass(cls):

    class DummyTest():
      _browser = splinter.Browser('zope.testbrowser')
      subject = page

    cls.dummy_test = DummyTest()
    super(AssertHaveSelectorTest, cls).setUpClass()

  def setUp(self):
    getattr(self.dummy_test, page).visit('%s/people/' % self.live_server_url)
    subject = _subject(self.dummy_test)
    self.subject = subject(page)

  def test_should_passes(self):
    self.assertTrue(self.subject.should(have_selector, 'h1'))

  def test_should_fails(self):
    with self.assertRaises(AssertionError):
      self.subject.should(have_selector, 'audio')

  def test_should_not_passes(self):
    self.assertTrue(self.subject.should_not(have_selector, 'audio'))

  def test_should_not_fails(self):
    with self.assertRaises(AssertionError):
      self.subject.should_not(have_selector, 'h1')

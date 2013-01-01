from django.test import LiveServerTestCase
import splinter

from redrover import have_text
from redrover.subject import _subject


class AssertHaveTextTest(LiveServerTestCase):

  @classmethod
  def setUpClass(cls):

    class DummyTest():
      page = splinter.Browser('zope.testbrowser')
      subject = 'page'

    cls.dummy_test = DummyTest()
    super(AssertHaveTextTest, cls).setUpClass()

  def setUp(self):
    self.dummy_test.page.visit('%s/people/' % self.live_server_url)
    subject = _subject(self.dummy_test)
    self.subject = subject('page')

  def test_should_passes(self):
    self.assertTrue(self.subject.should(have_text, 'People'))

  def test_should_fails(self):
    with self.assertRaises(AssertionError):
      self.subject.should(have_text, 'bluedabadee')

  def test_should_not_passes(self):
    self.assertTrue(self.subject.should_not(have_text, 'bluedabadee'))

  def test_should_not_fails(self):
    with self.assertRaises(AssertionError):
      self.subject.should_not(have_text, 'People')

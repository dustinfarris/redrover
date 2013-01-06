from django.test import LiveServerTestCase
import splinter

from redrover.assertions import HaveSelectorAssertion


class HaveSelectorAssertionTest(LiveServerTestCase):

  @classmethod
  def setUpClass(cls):
    cls.browser = splinter.Browser('zope.testbrowser')
    super(HaveSelectorAssertionTest, cls).setUpClass()

  def setUp(self):
    self.browser.visit('%s/people/' % self.live_server_url)

  def test_assertion_passes(self):
    """It should pass if the given selector exists in the document."""
    assertion = HaveSelectorAssertion(self.browser, 'h1')
    self.assertTrue(assertion.passes)

  def test_assertion_fails(self):
    """It should fail if the given selector does not exist in the document."""
    assertion = HaveSelectorAssertion(self.browser, 'audio')
    self.assertFalse(assertion.passes)

  def test_pass_message(self):
    assertion = HaveSelectorAssertion(self.browser, 'h1')
    self.assertEqual(
      "'h1' selector exists in /people/",
      assertion.message)

  def test_fail_message(self):
    assertion = HaveSelectorAssertion(self.browser, 'audio')
    self.assertEqual(
      "'audio' selector does not exist in /people/",
      assertion.message)

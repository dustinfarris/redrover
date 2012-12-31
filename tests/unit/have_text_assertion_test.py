from django.test import LiveServerTestCase
import splinter

from redrover.assertions import HaveTextAssertion


class HaveTextAssertionTest(LiveServerTestCase):

  @classmethod
  def setUpClass(cls):
    cls.browser = splinter.Browser('zope.testbrowser')
    super(HaveTextAssertionTest, cls).setUpClass()

  def setUp(self):
    self.browser.visit('%s/people/' % self.live_server_url)

  def test_assertion_passes(self):
    """It should pass if given text appears in the document's HTML."""
    assertion = HaveTextAssertion(self.browser, 'People')
    self.assertTrue(assertion.passes)

  def test_assertion_fails(self):
    """It should fail if given text does not appear in the document's HTML."""
    assertion = HaveTextAssertion(self.browser, 'bluedabadee')
    self.assertFalse(assertion.passes)

  def test_pass_message(self):
    assertion = HaveTextAssertion(self.browser, 'People')
    self.assertEqual(
      "'People' appears in %s" % self.browser.url,
      assertion.message)

  def test_fail_message(self):
    assertion = HaveTextAssertion(self.browser, 'bluedabadee')
    self.assertEqual(
      "'bluedabadee' does not appear in %s" % self.browser.url,
      assertion.message)

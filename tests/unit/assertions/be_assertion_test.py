from unittest import TestCase

from redrover.assertions import BeAssertion


class BeAssertionTest(TestCase):

  def test_assertion_passes(self):
    """It should pass two objects that are identical."""
    assertion = BeAssertion(1, 1)
    self.assertTrue(assertion.passes)

  def test_assertion_failes(self):
    """It should reject two objects that are not identical."""
    assertion = BeAssertion(1, True)
    self.assertFalse(assertion.passes)

  def test_pass_message(self):
    assertion = BeAssertion(1, 1)
    self.assertEqual('1 is 1', assertion.message)

  def test_fail_message(self):
    assertion = BeAssertion(1, True)
    self.assertEqual('1 is not True', assertion.message)

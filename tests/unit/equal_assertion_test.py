from unittest import TestCase

from redrover.case import EqualAssertion


class EqualAssertionTest(TestCase):

  def test_assertion_passes(self):
    """It should pass two objects that are equal."""
    assertion = EqualAssertion(2, 1 + 1)
    self.assertTrue(assertion.passes)

  def test_assertion_fails(self):
    """It should reject two objects that are not equal."""
    assertion = EqualAssertion(0, 1 + 1)
    self.assertFalse(assertion.passes)

  def test_pass_message(self):
    assertion = EqualAssertion(2, 1 + 1)
    self.assertEqual('Int 2 equals 2', assertion.message)

  def test_fail_message(self):
    assertion = EqualAssertion(0, 1 + 1)
    self.assertEqual('Int 0 does not equal 2', assertion.message)

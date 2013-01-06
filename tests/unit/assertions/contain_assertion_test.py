from unittest import TestCase

from redrover.assertions import ContainAssertion


class ContainAssertionTest(TestCase):

  def test_assertion_passes(self):
    """It should pass if one object exists within another."""
    assertion = ContainAssertion([1, 2, 3], 2)
    self.assertTrue(assertion.passes)
    self.assertEqual('2 is in [1, 2, 3]', assertion.message)

  def test_assertion_fails(self):
    """It should fail if one object does not exist within another."""
    assertion = ContainAssertion([1, 2, 3], 7)
    self.assertFalse(assertion.passes)
    self.assertEqual('7 is not in [1, 2, 3]', assertion.message)

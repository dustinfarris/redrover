import unittest

from redrover.expectations.base import BaseExpectation


class BaseExpectationTest(unittest.TestCase):

  def test_message(self):
    """It should raise `NotImplemented`."""
    base_expectation = BaseExpectation()
    with self.assertRaises(NotImplementedError):
      base_expectation.message

  def test_passes(self):
    """It should be None."""
    base_expectation = BaseExpectation()
    self.assertEqual(None, base_expectation.passes)

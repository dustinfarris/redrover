from unittest import TestCase

from redrover.assertions.base import BaseAssertion


class BaseAssertionTest(TestCase):

    def test_message(self):
        """It should raise `NotImplemented`."""
        base_assertion = BaseAssertion()
        with self.assertRaises(NotImplementedError):
            base_assertion.message

    def test_passes(self):
        """It should be None."""
        base_assertion = BaseAssertion()
        self.assertEqual(None, base_assertion.passes)

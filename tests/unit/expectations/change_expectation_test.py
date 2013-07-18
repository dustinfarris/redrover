import unittest

from redrover.expectations import ChangeExpectation


class ChangeExpectationTest(unittest.TestCase):

    def test_expectation_passes(self):
        """It should pass a callable that changes."""
        expectation = ChangeExpectation(lambda: self.foo)
        self.foo = 1
        expectation.enter()
        self.foo = 2
        expectation.exit()
        self.assertTrue(expectation.passes)
        self.assertRegexpMatches(
            expectation.message,
            r"changed")

    def test_expectation_fails(self):
        """It should reject a callable that does not change."""
        expectation = ChangeExpectation(lambda: self.foo)
        self.foo = 1
        expectation.enter()
        self.foo = 1
        expectation.exit()
        self.assertFalse(expectation.passes)
        self.assertRegexpMatches(
            expectation.message,
            r"did not change")

    def test_expectation_passes_with_delta(self):
        expectation = ChangeExpectation(lambda: self.foo, by=5)
        self.foo = 5
        expectation.enter()
        self.foo = 10
        expectation.exit()
        self.assertTrue(expectation.passes)
        self.assertRegexpMatches(
            expectation.message,
            r"changed by 5")

    def test_expectation_fails_with_delta(self):
        expectation = ChangeExpectation(lambda: self.foo, by=5)
        self.foo = 5
        expectation.enter()
        self.foo = 40
        expectation.exit()
        self.assertFalse(expectation.passes)
        self.assertRegexpMatches(
            expectation.message,
            r"did not change by 5")

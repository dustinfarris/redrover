from django.test import TestCase

from redrover.assertions import RespondToAssertion
from tests.factories import PersonFactory


class RespondToAssertionTest(TestCase):

    def setUp(self):
        self.person = PersonFactory.build()

    def test_assertion_passes(self):
        """
        It should pass an item that is a valid attribute of self.person.

        """
        assertion = RespondToAssertion(self.person, 'first_name')
        self.assertTrue(assertion.passes)

    def test_assertion_fails(self):
        """
        It should reject an item that is not a valid attribute of
        self.person.

        """
        assertion = RespondToAssertion(self.person, 'bluedabadee')
        self.assertFalse(assertion.passes)

    def test_pass_message(self):
        assertion = RespondToAssertion(self.person, 'first_name')
        self.assertEqual(
            "<Person: Dustin Farris> responds to 'first_name'",
            assertion.message)

    def test_fail_message(self):
        assertion = RespondToAssertion(self.person, 'bluedabadee')
        self.assertEqual(
            "<Person: Dustin Farris> does not respond to 'bluedabadee'",
            assertion.message)

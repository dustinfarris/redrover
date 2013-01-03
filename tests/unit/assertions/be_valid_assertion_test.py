from django.test import TestCase

from redrover.assertions import BeValidAssertion
from tests.factories import PersonFactory


class BeValidAssertionTest(TestCase):

  def setUp(self):
    self.person = PersonFactory.build()

  def test_assertion_passes(self):
    """It should pass a Django Model that is valid."""
    assertion = BeValidAssertion(self.person)
    self.assertTrue(assertion.passes)

  def test_assertion_fails(self):
    """It should reject a Django Model that is not valid."""
    self.person.first_name = ""
    assertion = BeValidAssertion(self.person)
    self.assertFalse(assertion.passes)

  def test_pass_message(self):
    assertion = BeValidAssertion(self.person)
    self.assertEqual('<Person: Dustin Farris> is valid', assertion.message)

  def test_fail_message(self):
    self.person.gender = "X"
    assertion = BeValidAssertion(self.person)
    self.assertEqual((
      "<Person: Dustin Farris> is not valid.  "
      "\x1b[0mgender: Value 'X' is not a valid choice."), assertion.message)

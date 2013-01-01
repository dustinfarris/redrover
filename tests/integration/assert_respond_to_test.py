from django.test import TestCase

from redrover import respond_to
from redrover.subject import _subject
from tests.factories import PersonFactory


class AssertRespondToTest(TestCase):

  def setUp(self):
    subject = _subject(self)
    self.person = PersonFactory.build()
    self.subject = subject('person')

  def test_should_passes(self):
    self.assertTrue(self.subject.should(respond_to, 'first_name'))

  def test_should_fails(self):
    with self.assertRaises(AssertionError):
      self.subject.should(respond_to, 'bluedabadee')

  def test_should_not_passes(self):
    self.assertTrue(self.subject.should_not(respond_to, 'bluedabadee'))

  def test_should_not_failes(self):
    with self.assertRaises(AssertionError):
      self.subject.should_not(respond_to, 'first_name')

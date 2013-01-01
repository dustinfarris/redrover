from django.test import TestCase

from redrover import be_valid
from redrover.subject import _subject
from tests.factories import PersonFactory


class AssertBeValidTest(TestCase):

  def setUp(self):
    subject = _subject(self)
    self.person = PersonFactory.build()
    self.subject = subject('person')

  def test_should_passes(self):
    self.assertTrue(self.subject.should(be_valid))

  def test_should_fails(self):
    self.subject.value.first_name = ""
    with self.assertRaises(AssertionError):
      self.subject.should(be_valid)

  def test_should_not_passes(self):
    self.subject.value.first_name = ""
    self.assertTrue(self.subject.should_not(be_valid))

  def test_should_not_fails(self):
    with self.assertRaises(AssertionError):
      self.subject.should_not(be_valid)

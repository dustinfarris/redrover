from django.test import TestCase

from redrover import equal
from redrover.base import Subject


class AssertEqualTest(TestCase):

  @classmethod
  def setUpClass(cls):
    cls.subject = Subject(2)

  def test_should_passes(self):
    self.assertTrue(self.subject.should(equal, 1 + 1))

  def test_should_fails(self):
    with self.assertRaises(AssertionError):
      self.subject.should(equal, 0)

  def test_should_not_passes(self):
    self.assertTrue(self.subject.should_not(equal, 0))

  def test_should_not_fails(self):
    with self.assertRaises(AssertionError):
      self.subject.should_not(equal, 1 + 1)

from django.test import TestCase

from redrover import be
from redrover.subject import _subject


class AssertBeTest(TestCase):

  @classmethod
  def setUpClass(cls):
    subject = _subject()
    cls.subject = subject(1)

  def test_should_passes(self):
    self.assertTrue(self.subject.should(be, 1))

  def test_should_fails(self):
    with self.assertRaises(AssertionError):
      self.subject.should(be, True)

  def test_should_not_passes(self):
    self.assertTrue(self.subject.should_not(be, '1'))

  def test_should_not_fails(self):
    with self.assertRaises(AssertionError):
      self.subject.should_not(be, 1)

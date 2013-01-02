from django.test import TestCase

from redrover import be_exactly
from redrover.subject import _subject


class AssertBeTest(TestCase):

  @classmethod
  def setUpClass(cls):
    subject = _subject(cls)
    cls.number = 1
    cls.subject = subject('number')

  def test_should_passes(self):
    self.assertTrue(self.subject.should(be_exactly, 1))

  def test_should_fails(self):
    with self.assertRaises(AssertionError):
      self.subject.should(be_exactly, True)

  def test_should_not_passes(self):
    self.assertTrue(self.subject.should_not(be_exactly, '1'))

  def test_should_not_fails(self):
    with self.assertRaises(AssertionError):
      self.subject.should_not(be_exactly, 1)

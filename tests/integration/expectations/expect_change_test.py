from django.test import TestCase

from redrover import expect, change
from redrover.expect import ExpectationError


class ExpectChangeTest(TestCase):

  def test_to_passes(self):
    self.foo = 4
    with expect.to(change, lambda: self.foo):
      self.foo = 6

  def test_to_fails(self):
    self.foo = 4
    with self.assertRaises(ExpectationError):
      with expect.to(change, lambda: self.foo):
        pass

  def test_not_to_passes(self):
    self.foo = 4
    with expect.not_to(change, lambda: self.foo):
      pass

  def test_not_to_fails(self):
    self.foo = 4
    with self.assertRaises(ExpectationError):
      with expect.not_to(change, lambda: self.foo):
        self.foo = 6

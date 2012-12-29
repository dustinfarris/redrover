from unittest import TestCase

from redrover.base import do_decorate


class DoDecorateTest(TestCase):

  def test_allow(self):
    """It should allow attributes that are tests."""
    sample_function = lambda a: a
    self.assertTrue(do_decorate('some_func', sample_function))

  def test_reject(self):
    """It should filter out attributes that are not tests."""
    sample_function = lambda a: a
    self.assertFalse(do_decorate('__class__', sample_function))
    self.assertFalse(do_decorate('setUp', sample_function))
    self.assertFalse(do_decorate('setUpClass', sample_function))
    self.assertFalse(do_decorate('tearDown', sample_function))
    self.assertFalse(do_decorate('tearDownClass', sample_function))
    self.assertFalse(do_decorate('would_work', 'except not a function'))

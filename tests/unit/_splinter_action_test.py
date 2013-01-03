from types import FunctionType
import unittest

from redrover.subject import _splinter_action


class SplinterActionTest(unittest.TestCase):

  @classmethod
  def setUpClass(cls):

    class Browser():
      pass

    class ParentClass():
      def __init__(self):
        self._browser = Browser()

    cls.ParentClass = ParentClass

  def setUp(self):
    self.parent_class = self.ParentClass()

  def test_splinter_action(self):
    """It should return an appropriate function."""
    func = _splinter_action('visit', self.parent_class)
    self.assertEqual(FunctionType, type(func))

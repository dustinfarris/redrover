import unittest

from redrover.subject import _splinter_action


class SplinterActionTest(unittest.TestCase):

  @classmethod
  def setUpClass(cls):

    class Browser():

      def get_hi(self):
        return "hi"

      def get_arg(self, arg):
        return arg

    class ParentClass():
      def __init__(self):
        self.page = Browser()

    cls.ParentClass = ParentClass

  def setUp(self):
    self.parent_class = self.ParentClass()

  def test_action_executes(self):
    """
    We should be able to create an 'action' function based on the parent
    class and a named method.

    """
    func = _splinter_action(self.parent_class, 'get_hi')
    self.assertEqual('hi', func())

  def test_action_accepts_arguments(self):
    func = _splinter_action(self.parent_class, 'get_arg')
    self.assertEqual('bluedabadee', func('bluedabadee'))

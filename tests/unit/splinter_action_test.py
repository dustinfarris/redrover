import unittest

import splinter

from redrover.subject import get_splinter_actions


class SplinterActionTest(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    cls.page = splinter.Browser('zope.testbrowser')

  def setUp(self):
    self.page.visit('http://dustinfarris.com/')
    self.splinter_actions = get_splinter_actions(self)

  def test_visit_action(self):
    """It should navigate to the desired page."""
    do_visit = self.splinter_actions['visit']
    do_visit('http://dustinfarris.com/about/')
    self.assertEqual('http://dustinfarris.com/about/', self.page.url)

  def test_current_path_action(self):
    """It should report the correct path."""
    do_current_path = self.splinter_actions['current_path']
    self.assertEqual('/', do_current_path)

from unittest import TestCase

import splinter

from redrover import RedRoverTest


class SubjectPageIsBrowserTest(TestCase):

  @classmethod
  def setUpClass(cls):

    class DummyTest(RedRoverTest):
      subject = 'page'

    cls.dummy_test = DummyTest

  def test_subject_is_browser(self):
    """
    The 'page' attribute of the RedRoverTest should be automatically
    assigned a splinter.Browser instance.

    """
    zope_testbrowser = splinter.Browser('zope.testbrowser')
    self.assertEqual(type(self.dummy_test.page), type(zope_testbrowser))
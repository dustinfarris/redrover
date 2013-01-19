from django.test import LiveServerTestCase
import splinter

from redrover import *
from redrover.subject import BROWSER


class VisitPeople(RedRoverHelper):

  def entry(self):
    visit('/people/')

  def exit(self):
    visit('/')


class HelperTest(LiveServerTestCase):

  @classmethod
  def setUpClass(cls):
    setattr(cls, BROWSER, splinter.Browser('zope.testbrowser'))
    setattr(cls, 'subject', BROWSER)
    super(HelperTest, cls).setUpClass()

  def test_helper(self):
    base_url = self.live_server_url
    getattr(self, BROWSER).visit('%s/' % base_url)
    self.assertEqual('%s/' % base_url, getattr(self, BROWSER).url)
    with VisitPeople(self):
      self.assertEqual('%s/people/' % base_url, getattr(self, BROWSER).url)
    self.assertEqual('%s/' % base_url, getattr(self, BROWSER).url)

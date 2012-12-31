from django.test import LiveServerTestCase
import splinter

from redrover.subject import _splinter_action


class SplinterIntegrationTest(LiveServerTestCase):

  @classmethod
  def setUpClass(cls):
    cls.page = splinter.Browser('zope.testbrowser')
    super(SplinterIntegrationTest, cls).setUpClass()

  def test_visit_action(self):
    do_visit = _splinter_action(self, 'visit')
    do_visit('/people/')
    self.assertIn('<h1>People</h1>', self.page.html)

from django.test import LiveServerTestCase
import splinter

from redrover.subject import get_splinter_actions


class SplinterIntegrationTest(LiveServerTestCase):

  @classmethod
  def setUpClass(cls):
    cls.page = splinter.Browser('zope.testbrowser')
    super(SplinterIntegrationTest, cls).setUpClass()

  def setUp(self):
    self.splinter_actions = get_splinter_actions(self)
    self.page.visit(self.live_server_url)

  def test_visit_action(self):
    do_visit = self.splinter_actions['visit']
    do_visit('/people/')
    self.assertIn('<h1>People</h1>', self.page.html)

  def test_current_path_action(self):
    do_current_path = self.splinter_actions['current_path']
    self.assertEqual('/', do_current_path)

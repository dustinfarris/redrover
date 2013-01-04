from django.test import LiveServerTestCase
import splinter

from redrover.subject import get_splinter_actions, BROWSER
from tests.factories import PersonFactory


class SplinterIntegrationTest(LiveServerTestCase):

  @classmethod
  def setUpClass(cls):
    setattr(cls, BROWSER, splinter.Browser('zope.testbrowser'))
    super(SplinterIntegrationTest, cls).setUpClass()

  def setUp(self):
    self.splinter_actions = get_splinter_actions(self)
    getattr(self, BROWSER).visit('%s/' % self.live_server_url)

  def test_visit_action(self):
    do_visit = self.splinter_actions['visit']
    do_visit('people:index')
    self.assertIn('<h1>People</h1>', getattr(self, BROWSER).html)

  def test_current_path_action(self):
    do_current_path = self.splinter_actions['current_path']
    self.assertEqual('/', do_current_path)

  def test_visit_complex_url_resolution(self):
    person = PersonFactory()
    do_visit = self.splinter_actions['visit']
    do_visit('people:detail', args=[str(person.id)])
    self.assertIn(person.first_name, getattr(self, BROWSER).html)

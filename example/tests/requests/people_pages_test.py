from redrover import *


class PeoplePagesTest(RedRoverLiveTest):

  subject = 'page'

  def setUp(self):
    visit('/people/')

  @describe
  def the_page_contents(self):
    it.should(have_text, 'People')

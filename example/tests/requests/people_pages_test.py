from redrover import *

from people.models import Person


class PeopleIndexTest(RedRoverLiveTest):

  subject = page

  @before
  def setUp(self):
    visit('/people/')

  @describe
  def the_page_contents(self):
    it.should(have_text, 'People')


class NewPersonPage(RedRoverLiveTest):

  subject = page

  @before
  def setUp(self):
    visit('people:new')

  @describe
  def the_new_person_page(self):
    it.should(have_selector, 'h1', text='New Person')
    its('title').should(be, 'New Person')


class NewPersonAction(RedRoverLiveTest):

  subject = page

  @before
  def setUp(self):
    visit('people:new')

  @describe
  def with_invalid_information(self):
    with expect.not_to(change, Person.objects.count, by=1):
      click_button('Submit')

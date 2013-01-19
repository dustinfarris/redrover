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
    its('path').should(be, '/people/new/')


class NewPersonAction(RedRoverLiveTest):

  subject = page

  @before
  def setUp(self):
    visit('people:new')

  @describe
  def with_invalid_information(self):
    with expect.not_to(change, Person.objects.count):
      click_on('Submit')
    it.should(have_text, "This field is required.")

  @describe
  def with_valid_information(self):
    with expect.to(change, Person.objects.count, by=1):
      fill_in("First name:", "Dustin")
      fill_in("Last name:", "Farris")
      fill_in("Age:", "28")
      select("Gender:", "M")
      click_on("Submit")


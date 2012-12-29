from redrover import *


@subject(page)
class PeoplePages(RedRoverTest):
  
  @before(PersonFactory())
  @before(PersonFactory())
  @before(PersonFactory())
  @before(visit('people:index'))
  def index_page():
    
    it.should (have_selector('h1', {text: 'People'}))
    it.should (have_selector('title', {text: 'People'}))
    
    @before(published_people = People.objects.filter(published=True))
    def published_people_should_be_listed():
      
      for person in published_people:
        page.should (have_link(person.name, {href: person}))
    
    @before(unpublished_people = People.objects.filter(published=False))
    def unpublished_people_should_not_be_listed():
    
      for person in unpublished_people:
        page.should_not (have_link(person.name, {href: person}))
      
    
      
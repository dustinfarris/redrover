import factory
from people.models import Person, Pet


class PersonFactory(factory.Factory):
  FACTORY_FOR = Person
  first_name = "Fyodor"
  last_name = "Dostoevsky"
  age = 90
  gender = 'M'

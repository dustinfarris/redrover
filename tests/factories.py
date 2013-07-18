import factory

from people.models import Person


class PersonFactory(factory.Factory):
    FACTORY_FOR = Person
    first_name = "Dustin"
    last_name = "Farris"
    age = 28
    gender = 'M'

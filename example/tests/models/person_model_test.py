from redrover import *

from tests.factories import *


class PersonTest(RedRoverTest):

    subject = 'person'

    def setUp(self):
        self.person = PersonFactory()

    @describe
    def fields(self):
        it.should(be, self.person)
        it.should(respond_to, 'first_name')
        it.should(respond_to, 'last_name')
        it.should(respond_to, 'full_name')
        it.should(respond_to, 'age')
        it.should(respond_to, 'gender')
        it.should(respond_to, 'pets')
        it.should(respond_to, 'is_owner_of')

        it.should(be_valid)

    @describe
    def when_first_name_is_not_present(self):
        self.person.first_name = ""
        it.should_not(be_valid)

    @describe
    def when_last_name_is_not_present(self):
        self.person.last_name = ""
        it.should_not(be_valid)

    @describe
    def when_age_is_not_present(self):
        self.person.age = None
        it.should_not(be_valid)

    @describe
    def when_gender_is_not_present(self):
        self.person.gender = ""
        it.should_not(be_valid)

    @describe
    def when_gender_is_invalid(self):
        self.person.gender = "X"
        it.should_not(be_valid)

    @describe
    def full_name(self):
        self.person.first_name = "Charles"
        self.person.last_name = "Dickens"
        its('full_name').should(equal, "Charles Dickens")

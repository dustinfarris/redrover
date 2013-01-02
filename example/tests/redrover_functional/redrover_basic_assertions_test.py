########################################################################
#
# The tests in this directory, tests/redrover_functional/, are not
# meant to represent tests that would normally appear in a Django
# project.  They are simply a comprehensive set of tests to make sure
# all of RedRover's components are functioning as they should. e.g. if
# one of these tests fail, it's because something is wrong with
# RedRover.
#
# During RedRover's own test suite, this Django project is fired up with
# manage.py test to make sure everything is working.
#
########################################################################

from redrover import *


class RedRoverBasicAssertions(RedRoverTest):

  subject = 'cities'

  def setUp(self):
    self.cities = ['New York', 'Springfield', 'Orlando']

  @describe
  def when_equal(self):
    it.should(equal, ['New York', 'Springfield', 'Orlando'])

  @describe
  def when_not_equal(self):
    it.should_not(equal, ['Springfield', 'Orlando', 'New York'])

  @describe
  def when_is(self):
    x = self.cities
    it.should(be_exactly, x)

  @describe
  def when_is_not(self):
    """
    This fails because the two objects are at different locations in
    memory -- which passes the test ala "should_not".

    """
    it.should_not(be_exactly, ['New York', 'Springfield', 'Orlando'])

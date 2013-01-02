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


class RedRoverSplinterActionsTest(RedRoverLiveTest):

  subject = 'page'

  @before
  def setUp(self):
    visit('/')

  @describe
  def when_i_visit_the_home_page(self):
    # Tests `visit` and `current_path`
    current_path.should(equal, '/')

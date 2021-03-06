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


class RedRoverSanityTest(RedRoverTest):

    def test_assertion(self):
        self.assertEquals(2, 1 + 1)

# Basic assertions to make sure redrover is working.  This file will be
# removed in the future in favor of more practical tests.
from redrover import *


class RedRoverAssertions(RedRoverTest):

  subject = 'number'

  def setUp(self):
    self.number = 12345

  @describe
  def when_equal(self):
    it.should(equal, 12345)

  @describe
  def when_not_equal(self):
    it.should_not(equal, 54321)

  @describe
  def when_is(self):
    x = self.number
    it.should(be, x)

  @describe
  def when_is_not(self):
    """
    This fails because the two objects are at different locations in
    memory -- which passes the test ala "should_not".

    """
    it.should_not(be, 12345)

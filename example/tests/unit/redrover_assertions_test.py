# Basic assertions to make sure redrover is working.  This file will be
# removed in the future in favor of more practical tests.
from redrover import *


class RedRoverAssertions(RedRoverTest):

  subject = 12345

  def test_equal(self):
    it.should(equal, 12345)

  def test_not_equal(self):
    it.should_not(equal, 54321)

  def test_is(self):
    x = self.subject
    it.should(be, x)

  def test_is_not(self):
    """
    This fails because the two objects are at different locations in memory.

    """
    it.should_not(be, 12345)

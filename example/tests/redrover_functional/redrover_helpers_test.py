from redrover import *


class MyNavHelper(RedRoverHelper):

  def entry(self):
    visit('people:index')

  def exit(self):
    visit('home')


class RedRoverHelperTest(RedRoverLiveTest):

  subject = page

  @describe
  def using_a_helper(self):
    with MyNavHelper(self):
      its('path').should(be, '/people/')
    its('path').should(be, '/')

from redrover import *


class VisitThePeoplePage(RedRoverHelper):

  def enter(self):
    visit('people:index')

  def exit(self):
    visit('people:index')

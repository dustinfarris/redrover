from redrover import *


@before(mymodel=PersonFactory())
@subject(mymodel)
class People(RedRoverTest):
  
  it.should (respond_to ( 'name' ))
  it.should (respond_to ( 'age' ))
  it.should (respond_to ( 'gender' ))
  it.should (respond_to ( 'friends' ))
  it.should (respond_to ( 'published' ))
  
  it.should (be_valid)
  
  @before(mymodel.name = " ")
  def when_name_is_not_present():
    it.should_not (be_valid)
  
  @before(mymodel.age = None)
  def when_age_is_not_present():
    it.should_not (be_valid)
  
  @before(mymodel.gender = " ")
  def when_gender_is_not_present():
    it.should_not (be_valid)
  
  @before(mymodel.name = "a" * 51)
  def when_name_is_too_long():
    it.should_not (be_valid)

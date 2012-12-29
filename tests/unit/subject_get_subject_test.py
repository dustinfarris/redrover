from unittest import TestCase

from redrover.base import Subject


class SubjectGetSubjectTest(TestCase):

  @classmethod
  def setUpClass(cls):
    cls.subject = Subject('abcdefg')

  def test_get_subject_property(self):
    self.assertEqual('abcdefg', self.subject.get_subject)

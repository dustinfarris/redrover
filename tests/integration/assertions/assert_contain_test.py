from django.test import TestCase

from redrover import contain
from redrover.subject import _subject


class AssertContainTest(TestCase):

    @classmethod
    def setUpClass(cls):
        subject = _subject(cls)
        cls.mylist = [1, 2, 3]
        cls.subject = subject('mylist')

    def test_should_passes(self):
        self.assertTrue(self.subject.should(contain, 2))

    def test_should_fails(self):
        with self.assertRaises(AssertionError):
            self.subject.should(contain, 7)

    def test_should_not_passes(self):
        self.assertTrue(self.subject.should_not(contain, 7))

    def test_should_not_fails(self):
        with self.assertRaises(AssertionError):
            self.subject.should_not(contain, 2)

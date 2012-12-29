from django.test import TestCase


class BasicAssertionTest(TestCase):

  def test_assertion(self):
    self.assertEquals(2, 1+1)
from unittest import TestCase

from redrover.base import _is_protected


class IsProtectedTest(TestCase):

    def test_allow(self):
        """It should allow attribute names that could be tests."""
        self.assertFalse(_is_protected('when_i_am_testing'))

    def test_reject(self):
        """It should reject names that are definitely not tests."""
        self.assertTrue(_is_protected('__class__'))
        self.assertTrue(_is_protected('setUp'))
        self.assertTrue(_is_protected('setUpClass'))
        self.assertTrue(_is_protected('tearDown'))
        self.assertTrue(_is_protected('tearDownClass'))
        self.assertTrue(_is_protected('live_server_url'))

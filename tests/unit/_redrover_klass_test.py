from unittest import TestCase

from redrover.base import _redrover_klass


class RedRoverKlassTest(TestCase):

    @classmethod
    def setUpClass(cls):

        class Dummy(object):

            def setUp(self):
                pass

            def i_am_a_test(self):
                pass

            __metaclass__ = _redrover_klass()

        cls.dummy_class = Dummy()

    def test_method_renaming(self):
        """
        It prepend certain methods with 'test_' and leave the
        rest alone.

        """
        self.assertEqual(
            'test_i_am_a_test',
            self.dummy_class.i_am_a_test.__name__)
        self.assertEqual(
            'setUp',
            self.dummy_class.setUp.__name__)

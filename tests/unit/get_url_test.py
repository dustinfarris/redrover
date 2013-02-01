import unittest

import pytest
from redrover.utils import get_url
from tests.factories import PersonFactory


class GetUrlTest(unittest.TestCase):

    def test_url_from_string(self):
        self.assertEqual('/people/', get_url('/people/'))

    @pytest.mark.django_db
    def test_url_from_model_instance(self):
        person = PersonFactory(id=987)
        self.assertEqual('/people/987/', get_url(person))

    def test_url_from_simple_reverse_query(self):
        self.assertEqual('/people/', get_url('people:index'))

    @pytest.mark.django_db
    def test_url_from_complex_reverse_query(self):
        person = PersonFactory(id=789)
        self.assertEqual(
            '/people/789/', get_url('people:detail', args=[person.id]))

    def test_bad_input_raises_runtime_error(self):
        with self.assertRaises(RuntimeError):
            get_url('a', 'b', 'c', 'd')

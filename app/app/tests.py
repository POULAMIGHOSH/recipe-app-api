'''
simple test
'''

from django.test import SimpleTestCase
from . import calc


class clacTests(SimpleTestCase):
    def test_should_return_added_value_when_two_numbers_are_given(self):
        res = calc.add(5, 4)

        self.assertEqual(res, 9)

    def test_should_return_subsracted_value_when_two_numbers_are_given(self):
        res = calc.sub(5, 4)

        self.assertEqual(res, 1)

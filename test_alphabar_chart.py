from unittest import TestCase
from alphabar_chart import parse_string_to_letter, make_dd_list


class TestParse(TestCase):
    def test_parse_string_to_letter(self):
        expect = {'a': 1, 'b': 1, 'c': 1}
        p_input = ''.join(expect.keys())
        # print(p_input)

        self.assertEqual(expect, parse_string_to_letter(p_input))

    def test_exclude_spaces(self):
        expect = {'a': 3, 'd': 3, 'e': 3, 'h': 1, 'i': 1, 'm': 3, 'o': 1, 'r': 1, 't': 3}
        p_input = 'madhatter made me do it'

        # print(parse_string_to_letter(p_input))
        self.assertEqual(expect, parse_string_to_letter(p_input))


class TestMakeDefDictList(TestCase):
    def test_simple_dd(self):
        p_input = {'a': 1, 'b': 1, 'c': 1}
        expected = {'a': ['a'], 'b': ['b'], 'c': ['c']}
        # print(p_input)

        self.assertEqual(expected, make_dd_list(p_input))

    def test_multiple_letters(self):
        p_input = {'a': 3, 'b': 1, 'c': 1}
        expected = {'a': ['a', 'a', 'a', ], 'b': ['b'], 'c': ['c']}
        # print(p_input)

        self.assertEqual(expected, make_dd_list(p_input))

from unittest import TestCase
from alphabar_chart import parse_string_to_letter


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



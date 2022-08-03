import unittest
from morse import Morse


class TestMorseInterpreter(unittest.TestCase):
    morse_code = None

    @classmethod
    def setUp(cls):
        cls.morse_code = Morse()

    def test_vowels(self):
        vowel_a = self.morse_code.get_morse_code('A')
        vowel_e = self.morse_code.get_morse_code('E')
        vowel_i = self.morse_code.get_morse_code('I')
        vowel_o = self.morse_code.get_morse_code('O')
        vowel_u = self.morse_code.get_morse_code('U')

        self.assertEqual(vowel_a, '._')
        self.assertEqual(vowel_e, '.')
        self.assertEqual(vowel_i, '..')
        self.assertEqual(vowel_o, '___')
        self.assertEqual(vowel_u, '.._')


if __name__ == '__main__':
    unittest.main()

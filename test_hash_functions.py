import unittest
import hash_functions as hf
import random
import string


class testHASCII(unittest.TestCase):
    def test_no_input_key(self):
        self.assertRaises(TypeError, hf.h_ascii, None, 100)

    def test_wrong_input_type_key(self):
        self.assertRaises(TypeError, hf.h_ascii, 1, 100)
        self.assertRaises(TypeError, hf.h_ascii, [10, 10, 10], 100)
        self.assertRaises(TypeError, hf.h_ascii, {}, 100)

    def test_no_input_N(self):
        self.assertRaises(TypeError, hf.h_ascii, 'text', None)

    def test_wrong_input_type_N(self):
        self.assertRaises(TypeError, hf.h_ascii, 'text', 'text')
        self.assertRaises(TypeError, hf.h_ascii, 'text',
                          ['text', 'text', 'text'])
        self.assertRaises(TypeError, hf.h_ascii, 'text', {})

    def test_return_int(self):
        self.assertTrue(isinstance(hf.h_ascii('text', 20), int))

    def test_output_fixed_input(self):
        self.assertEqual(hf.h_ascii('text', 50), 3)

    def test_output_random_input(self):
        for i in range(1000):
            random_hash = ''.join([random.choice(string.ascii_letters
                 + string.digits + string.punctuation) for n in range(32)])
            random_N = random.randint(1, 1000)
            self.assertLess(hf.h_ascii(random_hash, random_N), random_N)


class testHRolling(unittest.TestCase):
    def test_no_input_key(self):
        self.assertRaises(TypeError, hf.h_rolling, None, 100)

    def test_wrong_input_type_key(self):
        self.assertRaises(TypeError, hf.h_rolling, 1, 100)
        self.assertRaises(TypeError, hf.h_rolling, [10, 10, 10], 100)
        self.assertRaises(TypeError, hf.h_rolling, {}, 100)

    def test_no_input_N(self):
        self.assertRaises(TypeError, hf.h_rolling, 'text', None)

    def test_wrong_input_type_N(self):
        self.assertRaises(TypeError, hf.h_rolling, 'text', 'text')
        self.assertRaises(TypeError, hf.h_rolling, 'text',
                          ['text', 'text', 'text'])
        self.assertRaises(TypeError, hf.h_rolling, 'text', {})

    def test_return_int(self):
        self.assertTrue(isinstance(hf.h_rolling('text', 20), int))

    def test_output_fixed_input(self):
        self.assertEqual(hf.h_rolling('text', 50), 31)

    def test_output_random_input(self):
        for i in range(1000):
            random_hash = ''.join([random.choice(string.ascii_letters
                 + string.digits + string.punctuation) for n in range(32)])
            random_N = random.randint(1, 1000)
            self.assertLess(hf.h_rolling(random_hash, random_N), random_N)

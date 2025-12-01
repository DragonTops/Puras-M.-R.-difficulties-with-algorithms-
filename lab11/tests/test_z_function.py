import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from z_function import z_function


class TestZFunction(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(z_function(""), [])
    
    def test_single_character(self):
        self.assertEqual(z_function("a"), [0])
    
    def test_abacaba(self):
        s = "abacaba"
        expected = [0, 0, 1, 0, 3, 0, 1]
        self.assertEqual(z_function(s), expected)
    
    def test_aaa(self):
        s = "aaa"
        expected = [0, 2, 1]
        self.assertEqual(z_function(s), expected)
    
    def test_aabaac(self):
        s = "aabaac"
        expected = [0, 1, 0, 2, 1, 0]
        self.assertEqual(z_function(s), expected)


if __name__ == '__main__':
    unittest.main()
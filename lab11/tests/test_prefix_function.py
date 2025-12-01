import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from prefix_function import prefix_function


class TestPrefixFunction(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(prefix_function(""), [])
    
    def test_single_character(self):
        self.assertEqual(prefix_function("a"), [0])
    
    def test_ababaca(self):
        s = "ababaca"
        expected = [0, 0, 1, 2, 3, 0, 1]
        self.assertEqual(prefix_function(s), expected)
    
    def test_aaa(self):
        s = "aaa"
        expected = [0, 1, 2]
        self.assertEqual(prefix_function(s), expected)
    
    def test_abcabcd(self):
        s = "abcabcd"
        expected = [0, 0, 0, 1, 2, 3, 0]
        self.assertEqual(prefix_function(s), expected)


if __name__ == '__main__':
    unittest.main()
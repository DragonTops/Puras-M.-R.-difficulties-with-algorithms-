import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from kmp_search import kmp_search


class TestKMPSearch(unittest.TestCase):
    
    def test_empty_pattern(self):
        self.assertEqual(kmp_search("abc", ""), [])
    
    def test_pattern_longer_than_text(self):
        self.assertEqual(kmp_search("abc", "abcd"), [])
    
    def test_exact_match(self):
        self.assertEqual(kmp_search("abc", "abc"), [0])
    
    def test_multiple_occurrences(self):
        text = "abababa"
        pattern = "aba"
        expected = [0, 2, 4]
        self.assertEqual(kmp_search(text, pattern), expected)
    
    def test_no_occurrences(self):
        self.assertEqual(kmp_search("abc", "d"), [])
    
    def test_special_characters(self):
        text = "a!b@c#d$"
        pattern = "b@c"
        self.assertEqual(kmp_search(text, pattern), [2])


if __name__ == '__main__':
    unittest.main()
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from rabin_karp import rabin_karp_search


class TestRabinKarp(unittest.TestCase):
    
    def test_empty_pattern(self):
        self.assertEqual(rabin_karp_search("abc", ""), [])
    
    def test_pattern_longer_than_text(self):
        self.assertEqual(rabin_karp_search("abc", "abcd"), [])
    
    def test_exact_match(self):
        self.assertEqual(rabin_karp_search("abc", "abc"), [0])
    
    def test_multiple_occurrences(self):
        text = "abababa"
        pattern = "aba"
        expected = [0, 2, 4]
        self.assertEqual(rabin_karp_search(text, pattern), expected)
    
    def test_no_occurrences(self):
        self.assertEqual(rabin_karp_search("abc", "d"), [])
    
    def test_hash_collision(self):
        # Тест на корректную обработку коллизий хешей
        text = "abcde"
        pattern = "abc"
        self.assertEqual(rabin_karp_search(text, pattern), [0])


if __name__ == '__main__':
    unittest.main()
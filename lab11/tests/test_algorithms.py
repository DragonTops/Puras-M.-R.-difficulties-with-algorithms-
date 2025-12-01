import pytest
from src.prefix_function import prefix_function
from src.kmp_search import kmp_search
from src.z_function import z_function
from src.rabin_karp import RabinKarp

class TestPrefixFunction:
    def test_empty_string(self):
        assert prefix_function("") == []
    
    def test_single_char(self):
        assert prefix_function("a") == [0]
    
    def test_known_pattern(self):
        assert prefix_function("ababaca") == [0, 0, 1, 2, 3, 0, 1]
    
    def test_all_same_chars(self):
        assert prefix_function("aaaa") == [0, 1, 2, 3]

class TestKMP:
    def test_empty_pattern(self):
        assert kmp_search("text", "") == []
    
    def test_pattern_longer_than_text(self):
        assert kmp_search("abc", "abcd") == []
    
    def test_exact_match(self):
        assert kmp_search("abc", "abc") == [0]
    
    def test_multiple_matches(self):
        text = "abababab"
        pattern = "ab"
        assert kmp_search(text, pattern) == [0, 2, 4, 6]

class TestZFunction:
    def test_empty_string(self):
        assert z_function("") == []
    
    def test_single_char(self):
        assert z_function("a") == [0]
    
    def test_known_pattern(self):
        assert z_function("abacaba") == [0, 0, 1, 0, 3, 0, 1]
    
    def test_all_same_chars(self):
        assert z_function("aaaa") == [0, 3, 2, 1]

class TestRabinKarp:
    def setUp(self):
        self.rk = RabinKarp()
    
    def test_empty_pattern(self):
        assert self.rk.search("text", "") == []
    
    def test_pattern_longer_than_text(self):
        assert self.rk.search("abc", "abcd") == []
    
    def test_exact_match(self):
        assert self.rk.search("abc", "abc") == [0]
    
    def test_multiple_matches(self):
        text = "abababab"
        pattern = "ab"
        assert self.rk.search(text, pattern) == [0, 2, 4, 6]

if __name__ == "__main__":
    pytest.main([__file__])
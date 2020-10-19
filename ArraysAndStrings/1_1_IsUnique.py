"""
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""
import unittest


def is_unique(s):
    return len(set(s)) == len(s)


def is_unique_no_data_structure(s):
    L = len(s)

    for i in range(L):
        for j in range(i + 1, L):
            if s[i] == s[j]:
                return False

    return True


class Test(unittest.TestCase):
    def test_is_unique(self):
        s = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"
        self.assertEqual(True, is_unique(s), "Should return True if input string is unique")

        s = "abcdeabc"
        self.assertEqual(False, is_unique(s), "Should return False if input string is NOT unique")

        s = ""
        self.assertEqual(True, is_unique(s), "Should return True if input string is empty")

    def test_is_unique_no_data_structure(self):
        s = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"
        self.assertEqual(True, is_unique_no_data_structure(s), "Should return True if input string is unique")

        s = "abcdeabc"
        self.assertEqual(False, is_unique_no_data_structure(s), "Should return False if input string is NOT unique")

        s = ""
        self.assertEqual(True, is_unique_no_data_structure(s), "Should return True if input string is empty")
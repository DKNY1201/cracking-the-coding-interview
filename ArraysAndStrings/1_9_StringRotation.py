"""
String Rotation: Assume you have a method is_substring which checks if one word is a substring
of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat").
"""
import unittest


def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    # rotate string will be substring of double string
    # e.g: s1 = "google", s2 = "glegoo"
    # s = "googlegoogle", s2 is rotation of s1 if it is in s
    s = s1 * 2

    return is_substring(s2, s)

def is_substring(small_str, large_str):
    return small_str in large_str


class Test(unittest.TestCase):
    def test_string_rotation(self):
        s1 = "waterbottle"
        s2 = "erbottlewat"
        self.assertEqual(True, string_rotation(s1, s2), "Should return True if s2 is a rotation of s1")

        s1 = "maharishi"
        s2 = "harishima"
        self.assertEqual(True, string_rotation(s1, s2), "Should return True if s2 is a rotation of s1")

        s1 = "smartsheet"
        s2 = "rtsheetsma"
        self.assertEqual(True, string_rotation(s1, s2), "Should return True if s2 is a rotation of s1")

        s1 = "aaaaaaaa"
        s2 = "aaaaaaaa"
        self.assertEqual(True, string_rotation(s1, s2), "Should return True if s2 and s1 are equal")

        s1 = ""
        s2 = ""
        self.assertEqual(True, string_rotation(s1, s2), "Should return True if s2 and s1 are empty")

        s1 = "seattle"
        s2 = "ttlesae"
        self.assertEqual(False, string_rotation(s1, s2), "Should return False if s2 is NOT a rotation of s1")

        s1 = "washington"
        s2 = "newyork"
        self.assertEqual(False, string_rotation(s1, s2), "Should return False if s2 and s1 are NOT equal")
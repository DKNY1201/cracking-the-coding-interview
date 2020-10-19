"""
Given two strings, write a method to decide if one is a permutation of the other.
"""
import unittest


def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    # build char to occurrence map
    char_occur_map = {}
    for c in s1:
        if c not in char_occur_map:
            char_occur_map[c] = 0
        char_occur_map[c] += 1

    # reduce number of occurrence
    for c in s2:
        if c not in char_occur_map:
            return False
        else:
            char_occur_map[c] -= 1
            if char_occur_map[c] < 0:
                return False

    # check to see if all occurrences were reduce to zero
    for val in char_occur_map.values():
        if val != 0:
            return False

    return True


class Test(unittest.TestCase):
    def test_check_permutation(self):
        s1 = "programmingisfun"
        s2 = "funisprogramming"
        self.assertEqual(True, check_permutation(s1, s2), "Should return True if input strings are permutation")

        s1 = "thinkaboutit"
        s2 = "thinkaboutit"
        self.assertEqual(True, check_permutation(s1, s2), "Should return True if input strings are identical")

        s1 = "programmingisfun"
        s2 = "sadisprogramming"
        self.assertEqual(False, check_permutation(s1, s2), "Should return False if input strings are NOT permutation")

        s1 = "programmingisfun"
        s2 = "programming"
        self.assertEqual(False, check_permutation(s1, s2), "Should return False if input strings are not equal")

        s1 = ""
        s2 = ""
        self.assertEqual(True, check_permutation(s1, s2), "Should return True if input strings are both empty")


"""
There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a
character. Given two strings, write a function to check if they are one edit (or zero edits) away.
"""
import unittest


def one_away(s1, s2):
    if len(s1) > len(s2):
        # make sure length of s1 always less than or equal length of s2
        return one_away(s2, s1)

    if abs(len(s1) - len(s2)) > 1:
        return False

    if s1 == s2:
        return True

    i = j = 0
    diff_occurred = 0

    while i < len(s1):
        if s1[i] != s2[j]:
            if diff_occurred:
                return False

            # When diff occurs, if length of 2 strings are different then we only need move the pointer of the longer
            # string. If length of both strings are equal then we need to move both pointers.
            if len(s1) < len(s2):
                j += 1
            else:
                i += 1
                j += 1

            diff_occurred = True
        else:
            i += 1
            j += 1

    return True


class Test(unittest.TestCase):
    def test_one_away(self):
        s1 = "pale"
        s2 = "ple"
        self.assertEqual(True, one_away(s1, s2), "Should return True if 2 strings are one away (remove a character from s1)")

        s1 = "pale"
        s2 = "pales"
        self.assertEqual(True, one_away(s1, s2), "Should return True if 2 strings are one away (insert a character to s1)")

        s1 = "pale"
        s2 = "bale"
        self.assertEqual(True, one_away(s1, s2), "Should return True if 2 strings are one away (replace a character)")

        s1 = ""
        s2 = ""
        self.assertEqual(True, one_away(s1, s2), "Should return True if 2 strings are empty")

        s1 = "pale"
        s2 = "bake"
        self.assertEqual(False, one_away(s1, s2), "Should return False if 2 strings are NOT one away")

        s1 = "dog"
        s2 = "sdogs"
        self.assertEqual(False, one_away(s1, s2), "Should return False if len of 2 strings are different more than 1")

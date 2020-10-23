"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome
is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat". "atco cta". etc.)
"""
import unittest


def palindrome_permutation(s):
    # we only consider a-z and A-Z
    checker = [0] * 26

    for c in s:
        if ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z'):
            checker[ord(c.lower()) - ord('a')] += 1

    has_odd = False

    for occurrence in checker:
        if occurrence % 2 == 1:
            if has_odd:
                return False
            has_odd = True

    return True


class Test(unittest.TestCase):
    def test_palindrome_permutation(self):
        s = "Tact Coa"
        self.assertEqual(True, palindrome_permutation(s), "Should return True since s is permutation of a palindrome "
                                                          "such as 'taco cat', 'atco cta'")

        s = "bananaa"
        self.assertEqual(True, palindrome_permutation(s), "Should return True since s is permutation of a palindrome "
                                                          "like 'aanbnaa'")

        s = "Coca Coca"
        self.assertEqual(True, palindrome_permutation(s), "Should return True since s is permutation of a palindrome "
                                                          "like 'ccoaaocc'")

        s = "nogainnopain"
        self.assertEqual(False, palindrome_permutation(s), "Should return False if input is not a permutation of a palindrome")



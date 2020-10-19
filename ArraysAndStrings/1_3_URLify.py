"""
Write a method to replace all spaces in a string with '%20: You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
"""
import unittest


def URLify(url, L):
    spaces = 0

    for i in range(L):
        if url[i] == ' ':
            spaces += 1

    if L + spaces*2 != len(url):
        return ""

    url = list(url)
    l, r = L - 1, len(url) - 1

    while l >= 0:
        if url[l] != ' ':
            url[r] = url[l]
        else:
            url[r] = '0'
            r -= 1
            url[r] = '2'
            r -= 1
            url[r] = '%'

        l -= 1
        r -= 1

    return ''.join(url)


class Test(unittest.TestCase):
    def test_URLify(self):
        url = "Mr John Smith    "
        url_len = 13
        self.assertEqual("Mr%20John%20Smith", URLify(url, url_len), "Should return correct replaced url")

        url = "Mr John Smith       "
        url_len = 14
        self.assertEqual("Mr%20John%20Smith%20", URLify(url, url_len), "Should return correct replaced url")

        url = "Kevin  Tran             "
        url_len = 14
        self.assertEqual("Kevin%20%20Tran%20%20%20", URLify(url, url_len), "Should return correct replaced url")

        url = "Kevin  Tran            "
        url_len = 14
        self.assertEqual("", URLify(url, url_len), "Should return empty string if not enough space")




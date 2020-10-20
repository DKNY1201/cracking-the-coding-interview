"""
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""
import unittest


def string_compression(s):
    if len(s) == 0:
        return s

    comp_strs = []
    cur = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            comp_strs.append(cur)
            comp_strs.append(str(count))
            cur = s[i]
            count = 1

    comp_strs.append(cur)
    comp_strs.append(str(count))

    compressed_str = "".join(comp_strs)

    return compressed_str if len(compressed_str) < len(s) else s


class Test(unittest.TestCase):
    def test_string_compression(self):
        s = "aabcccccaaa"
        self.assertEqual("a2b1c5a3", string_compression(s),
                         "Should return correct string after compression")

        s = "aaaaaaaaaaaaaabbbbbbbbbbbbbbcccccaaa"
        self.assertEqual("a14b14c5a3", string_compression(s),
                         "Should return correct string after compression")

        s = "abcdef"
        self.assertEqual("abcdef", string_compression(s),
                         "Should return original string since the compression string is longer than the original")

        s = ""
        self.assertEqual("", string_compression(s), "Should empty string if input is empty")

import unittest
from solution import first_uniq_char

class TestFirstUniqChar(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(first_uniq_char("leetcode"), 0)
        self.assertEqual(first_uniq_char("loveleetcode"), 2)
        self.assertEqual(first_uniq_char("aabb"), -1)

    def test_empty_string(self):
        self.assertEqual(first_uniq_char(""), -1)

    def test_single_char(self):
        self.assertEqual(first_uniq_char("z"), 0)

if __name__ == "__main__":
    unittest.main()

import unittest
from index import bs_list


class MyTestCase(unittest.TestCase):
    def test_something(self):
        haystack = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(bs_list(haystack, 5), True)  # add assertion here


if __name__ == '__main__':
    unittest.main()

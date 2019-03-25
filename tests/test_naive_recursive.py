from unittest import TestCase

import egg_drop


class TestNaiveRecursive(TestCase):
    """
    Basic tests for the naive recursive approach. Same as for dynamic approach.

    Notes:
        All test cases are taken from the Super Egg Drop problem on Leetcode:
            https://leetcode.com/problems/super-egg-drop/

    """
    def test_case_1(self):
        res = egg_drop.naive_recursive(1, 2)
        self.assertEqual(res, 2)

    def test_case_2(self):
        res = egg_drop.naive_recursive(2, 6)
        self.assertEqual(res, 3)

    def test_case_3(self):
        res = egg_drop.naive_recursive(3, 14)
        self.assertEqual(res, 4)

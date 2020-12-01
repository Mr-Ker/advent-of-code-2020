import unittest
from day01 import Day01


class Day01Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.day01 = Day01('test/test_day01.txt', None)
        cls.day01.target_sum = 2020

    def test_multiple_of_found_sum_part1(self):
        self.assertEqual(self.day01.part1(), 514579)

    def test_multiple_of_found_sum_part2(self):
        self.assertEqual(self.day01.part2(), 241861950)

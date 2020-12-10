from test.day_test import DayTest
import sys


class Day09Test(DayTest):
    def test_part1(self):
        self.day.preamble_size = 5
        self.assertEqual(self.day.part1(), 127)

    def test_part2(self):
        self.day.preamble_size = 5
        self.assertEqual(self.day.part2(), 62)

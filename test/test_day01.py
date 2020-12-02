from test.day_test import DayTest


class Day01Test(DayTest):
    def test_multiple_of_found_sum_part1(self):
        self.assertEqual(self.day.part1(), 514579)

    def test_multiple_of_found_sum_part2(self):
        self.assertEqual(self.day.part2(), 241861950)

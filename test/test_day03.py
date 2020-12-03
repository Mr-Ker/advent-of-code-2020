from test.day_test import DayTest


class Day03Test(DayTest):
    def test_single_slope_part1(self):
        self.assertEqual(self.day.part1(), 7)

    def test_multiply_results_of_several_slopes_part2(self):
        self.assertEqual(self.day.part2(), 336)

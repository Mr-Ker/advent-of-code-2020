from test.day_test import DayTest


class Day02Test(DayTest):
    def test_password_validity_for_value_in_range_part1(self):
        self.assertEqual(self.day.part1(), 2)

    def test_password_validity_for_exact_count_part2(self):
        self.assertEqual(self.day.part2(), 1)

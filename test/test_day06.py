from test.day_test import DayTest


class Day06Test(DayTest):
    def test_count_all_distinct_answers_part1(self):
        self.assertEqual(self.day.part1(), 11)

    def test_count_all_common_answers_part2(self):
        self.assertEqual(self.day.part2(), 6)

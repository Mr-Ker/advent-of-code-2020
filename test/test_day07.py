from test.day_test import DayTest


class Day07Test(DayTest):
    def test_bags_containing_shiny_gold_part1(self):
        self.assertEqual(self.day.part1(), 4)

    def test_count_bags_contained_in_shiny_gold_part2(self):
        self.assertEqual(self.day.part2(), 32)

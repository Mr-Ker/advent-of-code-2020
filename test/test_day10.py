from test.day_test import DayTest


class Day10Test(DayTest):
    def test_part1(self):
        self.assertEqual(self.day.part1(), 220)

    def test_part2(self):
        self.assertEqual(self.day.part2(), 19208)

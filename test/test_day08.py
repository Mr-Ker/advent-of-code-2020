from test.day_test import DayTest


class Day08Test(DayTest):
    def test_accumulator_on_infinite_loop_part1(self):
        self.assertEqual(self.day.part1(), 5)

    def test_accumulator_on_corrected_program_part2(self):
        self.assertEqual(self.day.part2(), 8)

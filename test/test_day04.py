from test.day_test import DayTest


class Day04Test(DayTest):
    def test_mandatory_fields_presence_part1(self):
        self.assertEqual(self.day.part1(), 10)

    def test_passport_validity_part2(self):
        self.assertEqual(self.day.part2(), 6)

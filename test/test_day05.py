from test.day_test import DayTest


class Day05Test(DayTest):
    def test_highest_seat_id_part1(self):
        self.assertEqual(self.day.part1(), 822)

    def test_my_seat_id_part2(self):
        self.assertEqual(self.day.part2(), 821)

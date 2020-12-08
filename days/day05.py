from days.day import Day


class Day05(Day):
    def __init__(self):
        super().__init__()
        self.store_all_seat_ids()

    def seat_id(self, seat_specification):
        row = 0
        column = 0

        # No need to keep track of both limits of the range. Upper and lower
        # range value will converge to the result. Here, only lower range is
        # considered for the row and column.
        for i in range(7):
            if seat_specification[i] == 'B':
                row += 64 >> i

        for i in range(3):
            if seat_specification[i + 7] == 'R':
                column += 4 >> i

        return (row * 8 + column)

    def store_all_seat_ids(self):
        self.seat_ids = []
        for seat_specification in self.lines:
            self.seat_ids.append(self.seat_id(seat_specification))

    def part1(self):
        return max(self.seat_ids)

    def part2(self):
        # Create a list with all potential seat ids.
        potential_seat_ids = range(0, max(self.seat_ids) + 1)

        # Remove occupied seats.
        potential_seat_ids = set(potential_seat_ids) - set(self.seat_ids)

        for seat_id in potential_seat_ids:
            # The seats with IDs +1 and -1 from mine will be in occupied. This
            # means, they shouldn't be in the list of potential seats.
            if ((seat_id - 1) not in potential_seat_ids and
                    (seat_id + 1) not in potential_seat_ids):
                return seat_id

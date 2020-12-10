from days.day import Day
from days.list_helper import elements_that_sum_to, contiguous_elements_that_sum_to


class Day09(Day):
    def __init__(self):
        super().__init__()
        self.lines = [int(line) for line in self.lines]
        self.preamble_size = self.args.preamble_size

    def add_extra_args(self):
        self.parser.add_argument(
            '--preamble-size', type=int, default=25,
            help="Size of the preamble")

    def find_first_invalid_number(self):
        i = 0
        result = elements_that_sum_to(
            self.lines[: self.preamble_size],
            self.lines[self.preamble_size],
            2)

        while result and i <= len(self.lines):
            i += 1
            result = elements_that_sum_to(
                self.lines[i: self.preamble_size + i],
                self.lines[self.preamble_size + i],
                2)

        return self.lines[i+self.preamble_size]

    def part1(self):
        return self.find_first_invalid_number()

    def part2(self):
        target_sum = self.find_first_invalid_number()

        result = []
        i = 2

        while not result:
            result = contiguous_elements_that_sum_to(
                self.lines, target_sum, i)
            i += 1

        return min(result) + max(result)

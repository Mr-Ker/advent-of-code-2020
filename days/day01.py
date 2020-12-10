from days.day import Day
from days.list_helper import elements_that_sum_to, multiple_list_elements


class Day01(Day):
    def __init__(self):
        super().__init__()
        self.lines = [int(line) for line in self.lines]

        self.target_sum = self.args.target_sum

    def add_extra_args(self):
        self.parser.add_argument(
            '--target-sum', type=int, default=2020, help="Target sum to reach")

    def part1(self):
        return multiple_list_elements(
            elements_that_sum_to(self.lines, self.target_sum, 2))

    def part2(self):
        return multiple_list_elements(
            elements_that_sum_to(self.lines, self.target_sum, 3))

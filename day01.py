from days import Day
from itertools import combinations


class Day01(Day):
    def __init__(self, input_file, extra_args):
        super().__init__(input_file, extra_args)
        self.lines = [int(line) for line in self.lines]

        if 'target_sum' in self.extra_args:
            self.target_sum = int(self.extra_args['target_sum'])
        else:
            self.target_sum = 2020

    def extra_args_helper_str(self):
        extra_args_helper_text = self.__module__ + \
            ' supports the following extra arguments:'
        extra_args_helper_text += '\r\n\t target_sum=N (e.g. target_sum=2020)'
        return extra_args_helper_text

    def multiple_of_found_sum(self, number_of_elements_to_sum):
        result = 1
        for items in combinations(self.lines, number_of_elements_to_sum):
            if sum(items) == self.target_sum:
                for item in items:
                    result *= item
                break
        return result

    def part1(self):
        return self.multiple_of_found_sum(2)

    def part2(self):
        return self.multiple_of_found_sum(3)

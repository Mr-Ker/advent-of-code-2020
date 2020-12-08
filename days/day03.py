from days.day import Day


class Day03(Day):
    def __init__(self):
        super().__init__()
        self.current_position = [0, 0]
        self.target_position_x = len(self.lines) - 1
        self.parse_slope_part1()
        self.parse_slopes_part2()

    def add_extra_args(self):
        self.parser.add_argument(
            '--slope-part1', default='[3, 1]',
            help="Slope as string in the format '[right, down]'")
        self.parser.add_argument(
            '--slopes-part2', nargs="*",
            default=['[1, 1]', '[3, 1]', '[5, 1]', '[7, 1]', '[1, 2]'],
            help="Slopes in the format '[right1, down1]' '[right2, down2]' ...")

    def parse_slope(self, coordinates):
        coordinates = coordinates[1:-1].split(",")
        coordinates = [int(coordinates[0]), int(coordinates[1])]
        return coordinates

    def parse_slope_part1(self):
        self.slope_part1 = self.parse_slope(self.args.slope_part1)

    def parse_slopes_part2(self):
        self.slopes_part2 = []
        for coordinates in self.args.slopes_part2:
            self.slopes_part2.append(self.parse_slope(coordinates))

    def is_tree_present_in_current_position(self):
        current_position_square_content = self.lines[self.current_position[1]
                                                     ][self.current_position[0]]
        return current_position_square_content == '#'

    def update_position(self, slope):
        self.current_position[0] += slope[0]
        self.current_position[0] %= len(self.lines[0])
        self.current_position[1] += slope[1]

    def count_encoutered_trees_for_slope(self, slope):
        encountered_tree = 0

        if self.is_tree_present_in_current_position():
            encountered_tree += 1

        while self.current_position[1] != self.target_position_x:
            self.update_position(slope)

            if self.is_tree_present_in_current_position():
                encountered_tree += 1

        return encountered_tree

    def part1(self):
        self.current_position = [0, 0]
        return self.count_encoutered_trees_for_slope(self.slope_part1)

    def part2(self):
        result = 1

        for slope in self.slopes_part2:
            self.current_position = [0, 0]
            result *= self.count_encoutered_trees_for_slope(slope)

        return result

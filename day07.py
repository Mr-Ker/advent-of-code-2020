from day import Day
import re


class BagContent():
    def __init__(self, name):
        self.name = name
        self.contents = {}

    def add_content(self, quantity, name):
        self.contents[name] = quantity


class Day07(Day):
    def __init__(self):
        super().__init__()
        self.bags_contents = {}
        self.parse_bag_content_rules()
        self.bag = self.args.bag

    def add_extra_args(self):
        self.parser.add_argument(
            '--bag', type=str, default="shiny gold",
            help="Bag to use as input")

    def parse_bag_content_rules(self):
        pattern = re.compile(
            r"^(\w+ \w+) bags contain (.*)\.$")

        pattern_content = re.compile(r"(\d) (\w+ \w+)")

        for line in self.lines:
            match = pattern.match(line)

            if match:
                bag, contents = match.groups()
                bag_rule = BagContent(bag)
                if contents != 'no other bags':
                    contents = contents.split(", ")
                    for content in contents:
                        match_content = pattern_content.match(content)
                        if match_content:
                            quantity, bag_name = match_content.groups()
                            bag_rule.add_content(int(quantity), bag_name)

                self.bags_contents[bag] = bag_rule

    def bags_containing(self, bag):
        result = set()
        for bag_content in self.bags_contents.values():
            if bag in bag_content.contents:
                result.add(bag_content.name)
                result.update(self.bags_containing(bag_content.name))
        return result

    def count_bags(self, bag):
        result = 1
        contents = self.bags_contents[bag].contents
        for content in contents:
            result += contents[content] * self.count_bags(content)
        return result

    def part1(self):
        return len(self.bags_containing(self.bag))

    def part2(self):
        # We need to return the number of bags contained by one shiny gold bag.
        # We shouldn't count the shiny gold bag itself, hence the -1.
        return self.count_bags(self.bag) - 1

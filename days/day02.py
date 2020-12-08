from days.day import Day


class PasswordEntry():
    def __init__(self, minimum: int, maximum: int, value: str, password: str):
        self.minimum = minimum
        self.maximum = maximum
        self.value = value
        self.password = password

    def is_value_occurence_within_range(self):
        value_count = self.password.count(self.value)
        return value_count >= self.minimum and value_count <= self.maximum

    def is_value_occuring_only_once(self):
        result = 0
        if self.password[self.minimum] == self.value:
            result += 1

        if self.password[self.maximum] == self.value:
            result += 1

        return result == 1


class Day02(Day):
    def __init__(self):
        super().__init__()
        self.parse_lines()

    def parse_lines(self):
        self.entries = []
        for line in self.lines:
            minimum, line = line.split("-", 1)
            maximum, line = line.split(" ", 1)
            value, password = line.split(":")
            self.entries.append(
                PasswordEntry(
                    int(minimum),
                    int(maximum),
                    value, password))

    def part1(self):
        result = 0
        for entry in self.entries:
            if entry.is_value_occurence_within_range():
                result += 1
        return result

    def part2(self):
        result = 0
        for entry in self.entries:
            if entry.is_value_occuring_only_once():
                result += 1
        return result

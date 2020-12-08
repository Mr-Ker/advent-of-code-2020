from days.day import Day


class GroupAnswer():
    def __init__(self):
        self.answer_sets = []

    def add_answer(self, answer):
        answer_set = set()

        for letter in answer:
            answer_set.add(letter)

        self.answer_sets.append(answer_set)

    def count_distinct_answers(self):
        distinct_answers = set(self.answer_sets[0])
        for answer_set in self.answer_sets[1:]:
            distinct_answers.update(answer_set)

        return len(distinct_answers)

    def count_common_answers(self):
        common_answers = set(self.answer_sets[0])
        for answer_set in self.answer_sets[1:]:
            common_answers.intersection_update(answer_set)

        return len(common_answers)


class Day06(Day):
    def __init__(self):
        super().__init__()
        self.group_answers = []
        self.parse_group_answers()

    def parse_group_answers(self):
        group_answer = GroupAnswer()
        for line in self.lines:
            if line != "":
                group_answer.add_answer(line)
            else:
                self.group_answers.append(group_answer)
                group_answer = GroupAnswer()

        # Add the last group's answer if no new line was present at the end
        if group_answer.answer_sets != []:
            self.group_answers.append(group_answer)

    def part1(self):
        result = 0

        for group_answer in self.group_answers:
            result += group_answer.count_distinct_answers()

        return result

    def part2(self):
        result = 0

        for group_answer in self.group_answers:
            result += group_answer.count_common_answers()

        return result

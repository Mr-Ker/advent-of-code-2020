from days.day import Day
import abc


class Instruction():
    def __init__(self, value):
        self.value = value

    @abc.abstractmethod
    def run(self, instruction_index, accumlated_value):
        raise NotImplementedError


class Accumulator(Instruction):
    def __init__(self, value):
        super().__init__(value)

    def run(self, instruction_index, accumlated_value):
        return instruction_index+1, accumlated_value+self.value


class Jump(Instruction):
    def __init__(self, value):
        super().__init__(value)

    def run(self, instruction_index, accumlated_value):
        return instruction_index+self.value, accumlated_value


class Nop(Instruction):
    def __init__(self, value):
        super().__init__(value)

    def run(self, instruction_index, accumlated_value):
        return instruction_index+1, accumlated_value


class Day08(Day):
    def __init__(self):
        super().__init__()
        self.instructions = []
        self.parse_instructions()

    def parse_instructions(self):
        for line in self.lines:
            instruction, value = line.split(" ")
            if instruction == 'acc':
                self.instructions.append(Accumulator(int(value)))
            elif instruction == 'jmp':
                self.instructions.append(Jump(int(value)))
            elif instruction == 'nop':
                self.instructions.append(Nop(int(value)))
            else:
                raise ValueError("Instruction not supported")

    def run_program(self, instructions):
        executed_instruction_indexes = []
        instruction_index = 0
        accumulator = 0
        infinite_loop = True
        end_of_program = len(instructions)

        while instruction_index not in executed_instruction_indexes:
            executed_instruction_indexes.append(instruction_index)
            instruction = instructions[instruction_index]
            instruction_index, accumulator = instruction.run(
                instruction_index, accumulator)

            if instruction_index == end_of_program:
                infinite_loop = False
                break

        return infinite_loop, accumulator

    def part1(self):
        infinite_loop, accumulator = self.run_program(self.instructions)

        if not infinite_loop:
            raise ValueError("Infinite loop expected for part 1!")

        return accumulator

    def part2(self):
        for i in range(len(self.instructions)):
            temp_instructions = self.instructions.copy()
            if isinstance(self.instructions[i], Nop):
                temp_instructions[i] = Jump(self.instructions[i].value)
            elif isinstance(self.instructions[i], Jump):
                temp_instructions[i] = Nop(self.instructions[i].value)

            infinite_loop, accumulator = self.run_program(temp_instructions)

            if not infinite_loop:
                return accumulator

        # This should not happen
        return 0

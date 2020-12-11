from days.day import Day


class Day10(Day):
    def __init__(self):
        super().__init__()
        self.adapters_jolt = [int(line) for line in self.lines]
        self.adapters_jolt.sort()
        self.devices_jolt = max(self.adapters_jolt)
        self.adapters_jolt_differences = self.compute_adapters_differences()

    def compute_adapters_differences(self):
        adapters_jolt_differences = [self.adapters_jolt[0]]
        for i in range(1, len(self.adapters_jolt)):
            adapters_jolt_differences.append(
                self.adapters_jolt[i] - self.adapters_jolt[i - 1])

        # Add my own device's difference at the end of chain
        adapters_jolt_differences.append(3)

        return adapters_jolt_differences

    def compute_arrangements_number(self, chunk):
        if 2 in chunk:
            raise ValueError("Only differences of 1 are expected currently.")

        number_of_possibilites_per_chunk_length = [1, 1, 2, 4, 7]

        if len(chunk) > len(number_of_possibilites_per_chunk_length):
            raise ValueError("Only chunks of size 5 or smaller are supported.")

        return number_of_possibilites_per_chunk_length[len(chunk)]

    def part1(self):
        one_jolt_differences = self.adapters_jolt_differences.count(1)
        three_jolts_differences = self.adapters_jolt_differences.count(3)

        return one_jolt_differences * three_jolts_differences

    def part2(self):
        adapter_chunks = []
        adapter_chunk = []

        for difference in self.adapters_jolt_differences:
            if difference == 3:
                adapter_chunks.append(adapter_chunk)
                adapter_chunk = []
            else:
                adapter_chunk.append(difference)

        result = 1
        for adapter_chunk in adapter_chunks:
            result *= self.compute_arrangements_number(adapter_chunk)

        return result

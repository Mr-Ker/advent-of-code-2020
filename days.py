import abc


class Day():
    __metaclass__ = abc.ABCMeta

    def __init__(self, input_file, extra_args):
        self.input_file = open(input_file)
        self.lines = self.input_file.read().splitlines()
        self.extra_args = {}

        if extra_args is None:
            return

        if 'help' in extra_args:
            print(self.extra_args_helper_str())
            exit(0)

        for args in extra_args:
            key, value = args.split("=")
            self.extra_args[key] = value

    def part1(self):
        raise NotImplementedError

    def part2(self):
        raise NotImplementedError

    @abc.abstractmethod
    def extra_args_helper_str(self):
        return "No extra arguments supported for " + self.__module__

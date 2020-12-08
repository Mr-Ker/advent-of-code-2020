import abc
import argparse


class Day():
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description='Advent of code 2020',
            formatter_class=argparse.RawTextHelpFormatter)

        self.parser.add_argument(
            '-d', '--day',
            help='Day of advent of code to run')
        self.parser.add_argument(
            '-i', '--input', type=str, default=self.__module__.replace(".", "/")+".txt",
            help='Input file for the day\'s exercise')

        self.add_extra_args()

        self.args = self.parser.parse_args()

        self.input_file = open(self.args.input)
        self.lines = self.input_file.read().splitlines()

    @abc.abstractmethod
    def part1(self):
        raise NotImplementedError

    @abc.abstractmethod
    def part2(self):
        raise NotImplementedError

    @abc.abstractmethod
    def add_extra_args(self):
        pass

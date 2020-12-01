#!python3
import argparse

extra_args_help_str = 'Extra arguments specific for the day\'s exercise.'
extra_args_help_str += '\r\nUse [--extra-args help] to list available extra'
extra_args_help_str += ' arguments for the day.'

parser = argparse.ArgumentParser(
    description='Advent of code 2020',
    formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument(
    '-d', '--day', default='01',
    help='Day of advent of code to run')
parser.add_argument(
    '-i', '--input', type=str, default='day01.txt',
    help='Input file for the day\'s exercise')
parser.add_argument('--extra-args', nargs='*', help=extra_args_help_str)

args = parser.parse_args()

if len(args.day) == 1:
    args.day = "0" + args.day

module = __import__("day" + str(args.day))
class_ = getattr(module, "Day" + str(args.day))
day = class_(args.input, args.extra_args)

print("Result of part 1 is " + str(day.part1()))
print("Result of part 2 is " + str(day.part2()))

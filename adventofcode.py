#!python3
import sys

day = "01"

if "--day" in sys.argv:
    day = sys.argv[sys.argv.index("--day")+1]
elif "-d" in sys.argv:
    day = sys.argv[sys.argv.index("-d")+1]

if len(day) == 1:
    day = "0" + day

module = __import__("day" + str(day))
class_ = getattr(module, "Day" + str(day))
day = class_()

print("Result of part 1 is " + str(day.part1()))
print("Result of part 2 is " + str(day.part2()))

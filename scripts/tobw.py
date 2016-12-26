import fileinput
import sys
import re
from random import randint

# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv[1])

f = open(sys.argv[1], 'r')

gray_color = re.compile(r'[\'|"](\d+) (\d+) (\d+)[\'|"]')

def replace(match):
    ret = '"%s %s %s"' % (match.group(1), match.group(2), match.group(3))
    if sys.argv[2] == 'grayscale':
        val1 = val2 = val3 = (int(match.group(1)) + int(match.group(2)) + int(match.group(3))) / 3
        ret = '"%s %s %s"' % (val1, val2, val3)
    elif sys.argv[2] == 'random':
        ret = '"%s %s %s"' % (randint(1,255), randint(1,255), randint(1,255))
    elif sys.argv[2] == 'invert':
        ret = '"%s %s %s"' % (256 - int(match.group(1)), 256 - int(match.group(2)), 256 - int(match.group(3)))
    elif sys.argv[2] == 'luminance':
        val1 = val2 = val3 = (int(int(match.group(1)) * 0.3) + int(int(match.group(2)) * 0.59)
                              + int(int(match.group(3)) * 0.11))
        ret = '"%s %s %s"' % (val1, val2, val3)

    return ret

# for line in fileinput.input(inplace=False):
for line in f.readlines():
    line = gray_color.sub(replace, line)
    sys.stdout.write(line)

sys.stdout.write('\n')

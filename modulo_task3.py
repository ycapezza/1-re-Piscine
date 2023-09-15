import math
import sys

b = int(sys.argv[1])
def sumDigits(no):
    return 0 if no == 0 else int(no % 10) + sumDigits(int(no / 10))
print(sumDigits(b))
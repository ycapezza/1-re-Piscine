import math
import sys

c = float(sys.argv[1])
C = math.modf(c)
print(C[1])
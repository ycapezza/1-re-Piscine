import math
import sys

pi = 1
i = 3
x = 1
moins = True
while pi != 3.141592:
    if moins == True:
        pi -= 1/i
    else:
        pi += 1/i
    i += 2
    moins = False
    print(pi)
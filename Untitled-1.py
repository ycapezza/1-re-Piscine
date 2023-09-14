import math
import sys
# Opération 
# Task 1 :
1 + 1 
30 + 12 
777 + (-735) 
1 + 2 + 3 + 5 + 7 + 11 + 13 

#Task 2 :
82 - 42 
0 - (-42) 
2 * 21 
(-6)*(-7) 
2 + 5 * 8 
(3 + (3 * 4 - 2 * 2) * 3 - 2) * 2 - 3 

# Variables 
# Task 1 :
n = "1"
m = 1
chaine = "1"
for m in range(9):
    n = n + "1"
    chaine = chaine + "+" + n
print(chaine)

# Task 2 :
a = pow(17, 1024)
# print(a)

# Modulo
# Task 1 :
result = 42/4
result2 = 42//4
result3 = 42%4
print(result, result2, result3)

# Task 2 :
"""message = "Entrez un nombre :"
nb = int(input(message))
if nb%2 == 0:
    print("Le nombre est pair")
elif nb%2 == 1:
    print("Le nombre est impair")"""

# Task 3 :
"""b = int(sys.argv[1])
def sumDigits(no):
    return 0 if no == 0 else int(no % 10) + sumDigits(int(no / 10))
print(sumDigits(b))"""

# Task 4 :
"""c = float(sys.argv[1])
C = math.modf(c)
print(C[1])"""

# Task 5 :
"""d = float(sys.argv[1])
D = math.modf(d)
print(D)"""

# Archimedes constant and more
# Task 1 :
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
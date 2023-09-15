import math
import sys

message = "Entrez un nombre :"
nb = int(input(message))
if nb%2 == 0:
    print("Le nombre est pair")
elif nb%2 == 1:
    print("Le nombre est impair")
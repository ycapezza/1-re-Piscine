# si l'élément courant de la liste est pair : le divisier pas 2
# si l'élément est inpair : le multiplier par 2
var = [x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]]

print(var)
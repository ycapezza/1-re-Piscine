first_name = [" Jackie ", " Bruce ", " Arnold ", " Sylvester "]
last_name = [" Stallone ", " Schwarzenegger ", " Willis ", " Chan "]
# zip : crée des tuples avec pour éléments first_name et last_name
# la liste last_name est reverse : [:: -1]
# pour chaque tuples on aura : 0 = (0: "Jackie", 1: "Chan")
magic = [* zip( first_name , last_name [:: -1]) ]
# exemple : retourne le tuple qui à pour index 0
print ( magic [0])
print ( magic [3])
# exemple : retourne le deuxième élément du tuple qui à pour index 1
print ( magic [1][0])
print ( magic [0][1])
print ( magic [2])
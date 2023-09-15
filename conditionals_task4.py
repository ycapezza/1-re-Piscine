d = input("Entrer un nombre entier : ")
other_cases = True
if int(d) == 42:
    print("OK")
    other_cases = False

if int(d) <= 21:
    print("OK")
    other_cases = False

if int(d) % 2 == 0:
    print("OK")
    other_cases = False

if int(d) / 2 < 21:
    print("OK")
    other_cases = False

if int(d) % 2 != 0 and int(d) >= 45:
    print("OK")
    other_cases = False

if other_cases == True:
    print("You got wrong my poor friend!")

def A(unString, unInt):
    nb = 0
    for i in range(len(unString)):
        if unString[i].islower() == True:
            nb += 1
    if nb >= unInt:
        resultat = True
    else:
        resultat = False
    return resultat

print(A("sSSs", 3))

def B(unString, unInt):
    nb = 0
    for i in range(len(unString)):
        if unString[i].isupper() == True:
            nb += 1
    if nb >= unInt:
        resultat = True
    else:
        resultat = False
    return resultat

print(B("SSs", 1))

def C(unString, unInt):
    if len(unString) >= unInt:
        resultat = True
    else:
        resultat = False
    return resultat

print(C("bonjour", 7))

def D(unString, unInt):
    s = '[@_!#$%^&*()<>?/\|}{~:]'
    nb = 0
    for i in range(len(unString)):
        if unString[i] in s:
            nb += 1
    if nb >= unInt:
        resultat = True
    else:
        resultat = False
    return resultat

print(D("Bonj$@#r", 4))

def E(unString, unInt):
    nb = 0
    for i in range(len(unString)):
        if unString[i].isdigit() == True:
            nb += 1
    if nb >= unInt:
        resultat = True
    else:
        resultat = False
    return resultat

print(E("B455njour", 4))
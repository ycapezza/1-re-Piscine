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

def C(unString, unInt):
    if len(unString) >= unInt:
        resultat = True
    else:
        resultat = False
    return resultat

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


def check_password(contains, unInt, password):
    resultat = False
    erreur = ""
    if contains == "lower":
        if A(password, unInt) == True:
            resultat = True
        else:
            erreur += "Votre mot de pass doit contenir au moin " + str(unInt) + " lower !!!"
    else:
        if contains == "upper":
            if B(password, unInt) == True:
                resultat = True
            else:
                erreur += "Votre mot de pass doit contenir au moin " + str(unInt) + " upper !!!"
        else:
            if contains == "caractère":
                if C(password, unInt):
                    resultat = True
                else:
                    erreur += "Votre mot de pass doit contenir au moin " + str(unInt) + " caractères !!!"
            else:
                if contains == "special":
                    if D(password, unInt) == True:
                        resultat == True
                    else:
                        erreur += "Votre mot de passe doit contenir au moin " + str(unInt) + " caractères spéciaux !!!"
                else:
                    if contains == "number":
                        if E(password, unInt) == True:
                            resultat = True
                        else:
                            erreur += "Votre mot de pass doit contenir au moin " + str(unInt) + " chiffre(s) !!!"
    print(erreur)
    return resultat


resultat = check_password("lower", 4, "mysecretpassword") and check_password("special", 2, "mysecretpassword")

print(resultat)
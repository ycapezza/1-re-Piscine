names = ["Arnold", "Bruce", "Silvester"]
a = input("Entrer votre nom : ")
compteur = 0
for i in range(len(names)):
    if names[i] == a:
        print("Welcome in")
    else:
        compteur += 1

if compteur == 3:
    print("Get lost !")
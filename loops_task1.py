e = input("Entrer une chaine de caractère : ")
E =""
for i in range(len(e)):
    E += e[i] + e[i]
print(E)
key = 3
message = input("Entrer une chaine de caractère : ")
cryptage = ""
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(message)):
    letter = message[i]
    if alphabet.find(letter) != -1:
        cryptage += alphabet[alphabet.rfind(letter) + key]
print(cryptage)

decryptage = ""
for i in range(len(cryptage)):
    letter = cryptage[i]
    if alphabet.find(letter) != -1:
        decryptage += alphabet[alphabet.rfind(letter) - key]
print(decryptage)
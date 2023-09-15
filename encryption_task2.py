message2 = input("Entrer une chaine de caractère : ")
cle = "cle"
alphabet = "abcdefghijklmnopqrstuvwxyz"
code = ""
for i in range(0, len(message2)):
    letter2 = message2[i]
    if i >= len(cle):
        letterCLE = cle[i - len(cle)]
    else:
        letterCLE = cle[i]
    res = alphabet.rfind(letter2) + alphabet.rfind(letterCLE)
    code += alphabet[res]
#    print(res)
    res = 0
print(code)

newMessage = ""
for i2 in range(0, len(code)):
    letter2 = code[i2]
    if i2 >= len(cle):
        letterCLE = cle[i2 - len(cle)]
    else:
        letterCLE = cle[i2]
    res = alphabet.rfind(letter2) - alphabet.rfind(letterCLE)
    if res < 0:
        res += 26
    newMessage += alphabet[res]
#    print(res)
    res = 0
print(newMessage)
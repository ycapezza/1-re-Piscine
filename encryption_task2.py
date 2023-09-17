message2 = input("Entrer une chaine de caractère : ")
cle = "cle"
alphabet = "abcdefghijklmnopqrstuvwxyz"
code = ""
iCLE = 0
for i in range(0, len(message2)):
    letter2 = message2[i]
    if iCLE >= len(cle):
        iCLE = 0
    letterCLE = cle[iCLE]
    res = alphabet.rfind(letter2) + alphabet.rfind(letterCLE)
    if res > 25:
        res = res - 26
    code += alphabet[res]
#    print(res)
    res = 0
print(code)

newMessage = ""
for i2 in range(0, len(code)):
    letter2 = code[i2]
    if iCLE >= len(cle):
        iCLE = 0
    letterCLE = cle[iCLE]
    res = alphabet.rfind(letter2) - alphabet.rfind(letterCLE)
    if res < 0:
        res += 26
    newMessage += alphabet[res]
#    print(res)
    res = 0
print(newMessage)
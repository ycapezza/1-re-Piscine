import string

def isPalindrome(mot):
    newMot = mot.translate(str.maketrans("", "", string.punctuation)).replace(" ", "")
    if newMot == newMot[::-1]:
        print("Le mot est une palindrome")
    else:
        print("Le mot n'est pas un palindrome")
    print(newMot)
isPalindrome(" bateau.")
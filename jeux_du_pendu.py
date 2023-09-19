from random import choice
 
def random_word(myfile):
    with open(myfile, 'r') as f:
        word_list = f.read().splitlines()
        random_w = choice(word_list)
     
    return random_w

word = random_word("dictionnaires.txt")
print(word)

hiddenWord = "_" * len(word)
print(hiddenWord)

nbPoints = 0
while hiddenWord != word:
    letter = input("Saisissez une lettre : ")
    letter = letter.upper()
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                newHidden = list(hiddenWord)
                newHidden[i] = letter
                hiddenWord = "".join(newHidden)
    else:
        print("La lettre ne fait pas partie du mot")
        nbPoints += 1
    print((hiddenWord if word[-1] == letter else hiddenWord[:-1]) + " / " + str(nbPoints) + (" point" if nbPoints <= 1 else " points"))
    if nbPoints == 10:
        print("Vous avez perdu !!!")
        break

if hiddenWord == word:
    print("Vous avez gagner !!!")
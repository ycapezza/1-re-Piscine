sentence = input("Entrer une phrase : ")
x = sentence.split()
i = 0
Word = [x[0]]
for i in range(len(x) - 1):
    word = x[i]
    if word.find(".") != -1 or word.find("?") != -1 or word.find("!") != -1: 
        Word.append(x[i + 1]) 
    ++i
#print(x)
newSentence = ' '.join(map(str, Word)) + "."
#print(Word)
print(newSentence)
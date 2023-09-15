myList = [1, 2, 3, 4, 5]
newList = []
for i in range(len(myList)):
    if i == 1:
        pass
    else:
        newList.append(myList[i])
print(newList)
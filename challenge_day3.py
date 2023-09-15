import random
import time

myList = []

startingTime = time.time()
for i in range(999999):
    myList.append(random.randint(1, 9))

duration = time.time() - startingTime
print(duration)
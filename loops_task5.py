n = input("Entrer un nombre entier : ")
# 14
n_nbr = int(n)
last = n_nbr // 2
# last = 7
multiple = ""
print(n_nbr)
for i in range(2, last + 1):
    j = 2
    while j < n_nbr:
        if j % i == 0:
            multiple += str(j) + " "
        print(j)
        j = j + 1
        print(j)
    multiple += "\n"
    ++i 
print("Multiple = \n" + multiple)

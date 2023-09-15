my_first_list = [4, 5, 6]
my_second_list = [1, 2, 3]
# rajoute les elements de la seconde liste à la fin de la première liste
my_first_list.extend(my_second_list)

print(my_first_list)

my_first_list = [7, 8, 9]
my_second_list = [4, 5, 6]
# rajoute les elements de la seconde liste à la fin de la première liste
my_first_list = [* my_first_list , * my_second_list ]

print(my_first_list)
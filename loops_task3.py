i = -30
other_conds =True
for i in range(31):
    if i == 0:
        pass
    else:
        if 3 % i == 0:
            print("Fizz")
            other_conds = False

        if 5 % i == 0:
            print("Buzz")
            other_conds = False
        
        if 3 % i == 0 and 5 % i == 0:
            print("FizzBuzz")
            other_conds = False

        if other_conds == True:
            print("The integer itself")
def bread ():
    print (" <////////// > ")
def lettuce ():
    print (" ~~~~~~~~~~~~ ")
def tomato ():
    print ("O O O O O O")
def ham ():
    print (" ============ ")

def make_sandwiches(numbers):
    if numbers > 0:
        while numbers != 0:
            bread(), lettuce(), tomato(), ham(), ham(), bread() 
            numbers -= 1
    else:
        print("Veuillez rentrez un nombre valide")

make_sandwiches(2)
# crée une fonction f(x) dont x est un paramètre type int
def f(x):
    return 2 * x + 1
# crée la fonction g()
def g():
    return 7
# affecte le résultat de la fonction f(x) pour x = 2 dans une varriable y
y = f(2)
print (y)
# affecte le résultat de la fonction f(x) + g() pour x = 5 dans une varriable y
y = f(5) + g()
print (y)
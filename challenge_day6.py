def computes_power(number, power):
    res = number
    for i in range(power - 1):
        res *= number
    return res

print(computes_power(42, 84))
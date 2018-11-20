#see central binomial coefficient

def fact(n):
    product = 1
    for i in range(1, n + 1):
        product = product * i
    return product

n = 20
print(fact(2 * n) / (fact(n) * fact(n)))
#Problem 4: Implement a function product, to compute product of a list of numbers.

def product(x):
    product = 1
    for i in x:
        product *= i
    return product


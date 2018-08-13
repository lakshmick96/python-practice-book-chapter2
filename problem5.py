#Problem 5: Write a function factorial to compute factorial of a number. 
#Can you use the product function defined in the previous example to compute factorial?

def product(x):
    product = 1
    for i in x:
        product *= i
    return product


def factorial(y):
    x = []
    for i in range(1, y+1):
        x.append(i)
    return product(x)
        
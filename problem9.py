#Problem 9: Write a function cumulative_product to compute cumulative product of a list of numbers.

def cumulative_product(x):
    y = []
    product = x[0]
    y.append(product)
    for i in range(1, len(x)):
        product *= x[i]
        y.append(product)
    return y


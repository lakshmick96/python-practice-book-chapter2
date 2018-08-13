#Problem 2: Python has a built-in function sum to find sum of all elements of a list.
# Provide an implementation for sum.
#sum([1, 2, 3])
#6


def sum(x):
    total = 0
    for i in x:
        total += i
    return total

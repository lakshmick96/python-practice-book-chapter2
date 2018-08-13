#Problem 25: Python provides a built-in function map that applies a function to each element of a list. 
#Provide an implementation for map using list comprehensions.

def square(x):
    return x*x

def map(func, n):
    l = []
    for i in n:
        y = func(i)
        l.append(y)
    return l
print(map(square, range(5)))


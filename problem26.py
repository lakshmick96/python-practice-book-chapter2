#Problem 26: Python provides a built-in function filter(f, a) 
#that returns items of the list a for which f(item) returns true. 
#Provide an implementation for filter using list comprehensions.

def even(x):
    return x % 2 == 0

def filter(f, a):
    l = []
    for i in a:
        if f(i):
            l.append(i)
    return l

print(filter(even, range(10)))
            
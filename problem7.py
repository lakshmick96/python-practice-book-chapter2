#Problem 7: Python has built-in functions min and max to compute minimum and maximum of a given list. 
#Provide an implementation for these functions. 
#What happens when you call your min and max functions with a list of strings?

def min(x):
    y = x[0]
    for i in x:
        if i <= y:
            y = i
    return y

def max(x):
    y = x[0]
    for i in x:
        if i >= y:
            y = i
    return y



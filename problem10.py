#Problem 10: Write a function unique to find all the unique elements of a list.

def unique(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y
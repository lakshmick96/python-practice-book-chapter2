#Problem 24: Provide an implementation for zip function using list comprehensions.

def zip(x, y):
    i = 0
    zip = []
    for a in x:
        b = y[i]
        z = (a, b)
        i += 1
        zip.append(z)
    return zip
        


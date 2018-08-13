#Problem 29: Write a function array to create an 2-dimensional array.
#The function should take both dimensions as arguments.
#Value of each element can be initialized to None:

def array(i, j):
    a = []
    for m in range(i):
        b = []
        for n in range(j):
            b.append('None')
        a.append(b)
    return a


            
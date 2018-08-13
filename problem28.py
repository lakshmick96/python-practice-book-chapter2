#Problem 28: Write a function enumerate that takes a list
#and returns a list of tuples containing (index,item) for each item in the list.


def enumerate(x):
    l = []
    for i in range(len(x)):
        a = i , x[i]
        l.append(a)
    return l

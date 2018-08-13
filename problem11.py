#Write a function dups to find all duplicates in the list.

def unique(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y

def dups(x):
    z = []
    for i in x:
        count = 0
        for j in x:
            if i == j:
                count += 1
        if count > 1:
            z.append(i)
    return unique(z)


            
                
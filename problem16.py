#Problem 16: Write a function extsort to sort a list of files based on extension.

def extsort(a):
    b = []
    c = []
    e = []
    f = []
    for i in a:
        x = i.split('.')
        b.append(x)
    for i in b:
        y = i[::-1]       
        c.append(y)
    d = sorted(c)
    for i in d:
        z = i[::-1]       
        e.append(z)
    for i in e:
        x = '.'.join(i)
        f.append(x)
    return f



    




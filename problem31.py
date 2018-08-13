#Problem 31: Generalize the above implementation of csv parser to support any delimiter and comments.


def parser(filename, x, y):
    a = open(filename).readlines()
    c = []
    for line in a:
        if line.startswith(y) == False:
                           c.append(line)
    b = []
    for i in c:
        d = i.strip()
        b.append(d)
    e = []
    for i in b:
        d = i.split(x)
        e.append(d)
    return(e)
    
    

    

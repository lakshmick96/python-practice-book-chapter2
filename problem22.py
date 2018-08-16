#Problem 22: The above wrap program is not so nice because it is breaking the line at middle of any word.
#Can you write a new program wordwrap.py that works like wrap.py,but breaks the line only at the word boundaries?

def wordwrap(filename, n):
    x = open(filename).readlines()
    for i in x:
        b = i.split()
        while len(b) != 0:
            length = 0
            a = []
            c = []
            for j in range(len(b)):
                length +=  len(b[j])
                if length <= n:
                    a.append(b[j])
                    length += 1
                else:
                    c.append(b[j])
            print(' '.join(a))
            b = c
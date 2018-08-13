#Problem 22: The above wrap program is not so nice because it is breaking the line at middle of any word.
#Can you write a new program wordwrap.py that works like wrap.py,but breaks the line only at the word boundaries?

def wordwrap(filename, n):
    x = open(filename).readlines()
    for i in x:
        length = 0
        a = []
        b = []
        for j in range(len(i.split())):
            length +=  len(i.split()[j]) 
            if length <= n:
                a.append(i.split()[j])
                length += 1
            else:
                b.append(i.split()[j])
                length += 1
        print(' '.join(a))
        print(' '.join(b))
        
            
        

            
#Problem 18: Write a program to print each line of a file in reverse order.

x = open(filename).readlines()
z =[]
for i in x:
    y = i.split()
    y = y[::-1]
    z.append(y)
for i in z:
    print(' '.join(i))
    
    

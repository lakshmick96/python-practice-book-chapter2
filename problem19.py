#Problem 19: Implement unix commands head and tail.
#The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.

def head(filename):
    y = open(filename).readlines()
    for i in range(10):
        print(y[i])
    
head(filename)

def tail(filename):
    y = open(filename).readlines()
    for i in range(len(y)-10, len(y)):
        print(y[i])
        
tail(filename)

#Problem 20: Implement unix command grep. 
#The grep command takes a string and a file as arguments and 
#prints all lines in the file which contain the specified string.

def grep(filename, string):
    x = open('head.txt').readlines()
    for i in x:
        if string in i:
            print(i)

    


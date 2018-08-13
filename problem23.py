#23. Write a program center_align.py to center align all lines in the given file.


def center_align(filename):
    x = open(filename).readlines()
    maxlen = 0
    for i in x:
        length = len(i)
        if length > maxlen:
            maxlen = length
    for i in x:
        start = (maxlen - len(i))//2
        print(' '*start + i)
        

